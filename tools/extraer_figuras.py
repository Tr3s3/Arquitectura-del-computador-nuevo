"""Extrae figuras de un PDF (escaneado o vectorial) a partir de sus epígrafes.

Idea: la página se parte en BLOQUES verticales de contenido (filas con tinta separadas por
franjas blancas). El bloque que empieza con "Fig. N.N" / "Figura N.N" es el epígrafe; la
figura es el bloque inmediatamente encima, siempre que ese bloque no sea texto corrido.
"""
import pymupdf as fitz, numpy as np, re, os, json, sys

NUM = re.compile(r"^(\d+)[\.\-](\d+)$")
LAB = re.compile(r"^(fig\.?|figura|figure)$", re.I)

def bloques(pagina, dpi=200):
    pix = pagina.get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
    ink = (a < 170).sum(axis=1)
    sc = dpi / 72.0
    out, start = [], None
    for y, v in enumerate(ink):
        if v >= 3 and start is None:
            start = y
        elif v < 3 and start is not None:
            if y - start >= 4:
                out.append([start, y])
            start = None
    if start is not None:
        out.append([start, len(ink)])
    # unir bloques separados por menos de 8 px (interlineado dentro de un párrafo)
    unidos = []
    for b in out:
        if unidos and b[0] - unidos[-1][1] < 8:
            unidos[-1][1] = b[1]
        else:
            unidos.append(b)
    return a, unidos, sc

def cobertura_texto(pagina, y0pt, y1pt, x0pt, x1pt):
    """fracción de ancho cubierta por líneas OCR dentro de la franja (para detectar texto corrido)."""
    anchos = []
    for b in pagina.get_text("dict")["blocks"]:
        if b["type"]: continue
        for l in b["lines"]:
            lx0, ly0, lx1, ly1 = l["bbox"]
            if ly1 < y0pt - 1 or ly0 > y1pt + 1: continue
            anchos.append(min(lx1, x1pt) - max(lx0, x0pt))
    if not anchos: return 0.0, 0
    return sum(anchos) / max(1e-6, (x1pt - x0pt)), len(anchos)

def extraer(pdf, outdir, dpi=200, min_h=45, prefijo="", solo_paginas=None):
    os.makedirs(outdir, exist_ok=True)
    d = fitz.open(pdf)
    figs, vistos = [], set()
    for pno in range(len(d)):
        if solo_paginas and (pno + 1) not in solo_paginas: continue
        p = d[pno]
        a, bs, sc = bloques(p, dpi)
        if not bs: continue
        # bloque -> palabras
        for bi, (by0, by1) in enumerate(bs):
            y0pt, y1pt = by0 / sc, by1 / sc
            ws = [w for w in p.get_text("words") if w[1] >= y0pt - 2 and w[3] <= y1pt + 2]
            if not ws: continue
            ws.sort(key=lambda w: (w[6], w[0]))
            prim = ws[0][4].strip(".,;:()[]")
            if not LAB.match(prim): continue
            num = ws[1][4].strip(".,;:)]") if len(ws) > 1 else ""
            if not NUM.match(num): continue
            fig = f"{NUM.match(num).group(1)}.{NUM.match(num).group(2)}"
            if fig in vistos: continue
            epi = " ".join(w[4] for w in ws)[:150]
            if bi == 0: continue            # no hay nada arriba
            ty0, ty1 = bs[bi - 1]
            if ty1 > by0 + 2 and bi - 1 == bi: continue
            h = ty1 - ty0
            if h < min_h: continue
            reg = a[ty0:ty1, :]
            nz = np.where((reg < 170).sum(axis=0) > 0)[0]
            if len(nz) == 0: continue
            x0 = int(max(0, nz[0] - 12)); x1 = int(min(a.shape[1], nz[-1] + 14))
            cob, nl = cobertura_texto(p, ty0 / sc, ty1 / sc, x0 / sc, x1 / sc)
            # ¿hay dibujo vectorial o imagen en la franja? entonces es figura aunque tenga texto
            franja = fitz.Rect(x0 / sc, ty0 / sc, x1 / sc, ty1 / sc)
            dib = sum(1 for dr in p.get_drawings() if dr["rect"].intersects(franja))
            imgs = sum(1 for im in p.get_image_info() if fitz.Rect(im["bbox"]).intersects(franja))
            if dib < 3 and imgs == 0 and cob > 0.62 and nl >= 3:
                continue
            clip = fitz.Rect(x0 / sc, ty0 / sc, x1 / sc, ty1 / sc)
            hp = d[pno].get_pixmap(clip=clip, dpi=200, colorspace=fitz.csRGB)
            if hp.height < min_h or hp.width < 50: continue
            nombre = f"{prefijo}f{fig.replace('.', '_')}__p{pno+1:03d}.png"
            hp.save(os.path.join(outdir, nombre))
            vistos.add(fig)
            figs.append(dict(archivo=nombre, fig=fig, pagina=pno + 1, epigrafe=epi,
                             w=hp.width, h=hp.height))
    return figs

if __name__ == "__main__":
    pdf, out = sys.argv[1], sys.argv[2]
    pre = sys.argv[3] if len(sys.argv) > 3 else ""
    figs = extraer(pdf, out, prefijo=pre)
    json.dump(figs, open(os.path.join(out, f"index{pre and '_' + pre.rstrip('_') or ''}.json"), "w"),
              ensure_ascii=False, indent=1)
    print("figuras:", len(figs))
