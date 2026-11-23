# -*- coding: utf-8 -*-
"""Genera los archivos de lectura de corrido:
   - 02 Materia/Unidad N — …/00 Unidad N completa (lectura de corrido).md
   - 02 Materia/00 Materia completa (las 10 unidades en un archivo).md
Re-ejecutar después de editar cualquier subtema. Uso: python3 tools/unir_unidades.py
"""
import re, os, glob

V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT = os.path.join(V, "02 Materia")

def strip_fm(s):
    if s.startswith("---"):
        p = s.split("---", 2)
        if len(p) >= 3: return p[2].lstrip("\n")
    return s

def demote(body, levels):
    out = []
    for ln in body.split("\n"):
        m = re.match(r"^(#{1,6}) (.*)$", ln)
        out.append("#" * min(6, len(m.group(1)) + levels) + " " + m.group(2) if m else ln)
    return "\n".join(out)

def sub_doc(f, pref, nivel_sub):
    s = strip_fm(open(f, encoding="utf-8").read())
    s = re.sub(r"^# .*\n", "", s, count=1)                     # sacar el H1 del subtema
    s = s.replace("](../../../assets/", f"]({pref}assets/")    # rutas de imágenes relativas al archivo nuevo
    return demote(s, nivel_sub - 1).strip("\n")

def mil(n): return f"{n:,}".replace(",", ".")

def unidades():
    us = []
    for d in sorted(glob.glob(MAT + "/Unidad *"), key=lambda x: int(re.search(r"Unidad (\d+)", x).group(1))):
        n = int(re.search(r"Unidad (\d+)", d).group(1))
        nombre = re.sub(r"^Unidad \d+ — ", "", os.path.basename(d))
        temas = []
        for td in glob.glob(d + "/Tema *"):
            mt = re.match(r"Tema (\d+\.\d+) (.+)$", os.path.basename(td))
            subs = []
            for f in glob.glob(td + "/*.md"):
                m = re.match(r"^(\d+\.\d+\.\d+) (.+)\.md$", os.path.basename(f))
                if m: subs.append((m.group(1), m.group(2), f))
            subs.sort(key=lambda t: [int(x) for x in t[0].split(".")])
            if subs: temas.append((mt.group(1), mt.group(2), subs))
        temas.sort(key=lambda t: [int(x) for x in t[0].split(".")])
        us.append(dict(n=n, nombre=nombre, dir=d, temas=temas))
    return us

def stats(subs): return sum(len(open(f, encoding="utf-8").read().split()) for _, _, f in subs)

US = unidades()
for u in US:
    subs_all = [s for _, _, ss in u["temas"] for s in ss]; w = stats(subs_all)
    o = ["---", "tipo: unidad-completa", f"unidad: {u['n']}", "---", "",
         f"# Unidad {u['n']} — {u['nombre']}", "",
         "> [!abstract] Qué es este archivo",
         f"> **La Unidad {u['n']} completa en un solo archivo**: los **{len(subs_all)} subtemas** pegados uno detrás de otro,",
         "> con todo su contenido: definiciones, tablas, diagramas, ejemplos resueltos, figuras del libro y errores",
         f"> típicos. Son **{mil(w)} palabras** y **{len(u['temas'])} temas**. Está pensado para **leer de corrido** y para",
         "> **imprimir**: no hace falta abrir ninguna otra nota.",
         ">",
         f"> - **Repaso rápido** (una página): [[00 Síntesis — Unidad {u['n']}]].",
         f"> - **Buscar un punto**: el índice de abajo o el de la unidad, [[00 Unidad {u['n']} — temas y subtemas]].",
         "> - Cada subtema conserva su número (`1.4.1`), así coincide con el índice y con las preguntas del final.",
         "> - **Todo junto, las 10 unidades**: [[00 Materia completa (las 10 unidades en un archivo)]].",
         ">", "> *Archivo generado con `tools/unir_unidades.py`: no editarlo a mano, editar el subtema y regenerar.*", "",
         "## Contenido", ""]
    for cod, nombre, subs in u["temas"]:
        o.append(f"**{cod} {nombre}**")
        o += [f"- [[#{sc} {sn}]]" for sc, sn, _ in subs]
        o.append("")
    o += ["---", ""]
    for cod, nombre, subs in u["temas"]:
        o += [f"## {cod} {nombre}", ""]
        for sc, sn, f in subs:
            o += [f"### {sc} {sn}", "", sub_doc(f, "../../", 3), ""]
    o += ["---", "", "## Al terminar la unidad",
          f"- Una pasada rápida: [[00 Síntesis — Unidad {u['n']}]].",
          f"- Los subtemas por separado: [[00 Unidad {u['n']} — temas y subtemas]].",
          "- Seguir de corrido: [[00 Materia completa (las 10 unidades en un archivo)]].",
          "- Practicar: [[Banco de preguntas del final]] · [[Autoevaluación]] · [[Prácticas resueltas]].", ""]
    dst = f"{u['dir']}/00 Unidad {u['n']} completa (lectura de corrido).md"
    open(dst, "w", encoding="utf-8").write("\n".join(o))
    print(f"U{u['n']:>2}: {len(subs_all):>2} subtemas · {mil(w):>7} palabras · {os.path.getsize(dst)/1024:>5.0f} KB")

o = ["---", "tipo: materia-completa", "---", "",
     "# Materia completa — Arquitectura del Computador (UCASAL)", "",
     "> [!abstract] Qué es este archivo",
     "> **Las 10 unidades en un solo archivo**, con los **107 subtemas** pegados en orden: es la materia entera para",
     "> **leer de corrido** o imprimir. Cada subtema trae su definición, sus tablas, su diagrama propio, un ejemplo",
     "> resuelto, el error típico y la figura del libro.",
     ">",
     "> - **Si estás repasando**: no leas todo, usá el índice de abajo o el [[Banco de preguntas del final]].",
     "> - **Si es la primera lectura**: leé unidad por unidad; cada una termina con su cierre.",
     "> - **Si querés una unidad sola**: [[00 Índice de la materia (las 10 unidades)]] tiene el archivo «Unidad N completa».",
     "> - Los números (`3.2.1`, `5.5.2`…) son los mismos del índice y del modelo de final.",
     ">", "> *Archivo generado con `tools/unir_unidades.py`: no editarlo a mano, editar el subtema y regenerar.*", "",
     "## Contenido", ""]
tot_w = 0; tot_s = 0
for u in US:
    subs_all = [s for _, _, ss in u["temas"] for s in ss]; w = stats(subs_all); tot_w += w; tot_s += len(subs_all)
    o.append(f"**Unidad {u['n']} — {u['nombre']}** · {len(subs_all)} subtemas")
    for cod, nombre, subs in u["temas"]:
        o.append(f"- {cod} {nombre}: " + " · ".join(f"[[#{sc} {sn}]]" for sc, sn, _ in subs))
    o.append("")
o += ["---", ""]
for u in US:
    subs_all = [s for _, _, ss in u["temas"] for s in ss]
    o += [f"## Unidad {u['n']} — {u['nombre']}", "",
          f"> [!info] Unidad {u['n']}",
          f"> {len(subs_all)} subtemas · {mil(stats(subs_all))} palabras ·",
          f"> síntesis de una página: [[00 Síntesis — Unidad {u['n']}]] · archivo de la unidad: [[00 Unidad {u['n']} completa (lectura de corrido)]]", ""]
    for cod, nombre, subs in u["temas"]:
        o += [f"### {cod} {nombre}", ""]
        for sc, sn, f in subs:
            o += [f"#### {sc} {sn}", "", sub_doc(f, "../", 4), ""]
o += ["---", "", "## Después de leer todo",
      "- **Repasar el día antes**: [[04 Resumen integrador de la materia]].",
      "- **Practicar**: [[Banco de preguntas del final]] · [[Autoevaluación]] · [[Prácticas resueltas]].",
      "- **El final**: [[00 Matriz del final — las 3 tandas]] · [[Guion de respuestas — preguntas principales]].",
      "- **Las palabras**: [[Glosario]].", ""]
dst = MAT + "/00 Materia completa (las 10 unidades en un archivo).md"
open(dst, "w", encoding="utf-8").write("\n".join(o))
print(f"TOTAL: {tot_s} subtemas · {mil(tot_w)} palabras · {os.path.getsize(dst)/1024:.0f} KB")
