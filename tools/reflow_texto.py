# -*- coding: utf-8 -*-
"""Reflow del texto de las notas: un párrafo = una línea lógica.

Problema que arregla: las notas se escribieron cortadas a mano a ~110 caracteres, con el corte a mitad de
oración. En cualquier visor que respete los saltos de línea (Obsidian con «Strict line breaks», la vista previa
de GitHub o de Arena) esos cortes aparecen como saltos de párrafo donde la oración no terminó.

Qué hace, en una pasada sobre cada .md:
  1. Une las líneas de continuación de un párrafo, de un ítem de lista o de una cita/callout, con un espacio.
  2. Deja una línea en blanco antes de un título, una tabla, un callout, un bloque de código o una regla `---`,
     y después de una tabla (si no la había): sin eso la tabla o el callout pueden no renderizarse.
  3. Colapsa las líneas en blanco repetidas.
No toca: el frontmatter YAML, el interior de los bloques de código, las filas de tabla, los encabezados ni el
contenido de una línea que termina en dos espacios o en `\\` (esas son saltos de línea intencionales).

Uso:
  python3 tools/reflow_texto.py --check    # sólo informa qué cambiaría
  python3 tools/reflow_texto.py            # aplica
"""
import os, re, sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Dibujo de cajas: no se toca (son diagramas en texto). Ojo: las flechas → ↑ ↓ NO van acá, porque en estas
# notas se usan como separador de todos los párrafos («definición → dibujo → desarrollo»).
BOX = set("─│┌┐└┘├┤┬┴┼━┃╔╗╚╝║═╠╣╦╩╬")


def fence_marker(line):
    """¿La línea abre/cierra un bloque cercado? Vale también dentro de una cita (`> ``` !`)."""
    s = re.sub(r"^[\s>]*", "", line)
    for m in ("```", "~~~"):
        if s.startswith(m) and s.count(m) == 1:
            return True
    return False


def cls(line):
    """Clasifica una línea por su función en el markdown."""
    s = line.strip()
    if not s:
        return "blank"
    if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
        return "hr"
    if re.match(r"^#{1,6} ", s):
        return "head"
    if s.startswith("```") or s.startswith("~~~"):
        return "fence"
    if s.startswith("|"):
        return "table"
    if re.match(r"^> ?\[!", s):
        return "callout"
    if re.match(r"^>\s*$", s):
        return "qblank"
    if re.match(r"^>\s*\|", s):
        return "qtable"          # tabla dentro de un callout: cada fila es su propia línea
    if re.match(r"^>\s*#{1,6} ", s):
        return "qhead"
    if re.match(r"^>\s*([-*+]|\d+[.)])\s", s):
        return "qlist"
    if s.startswith(">"):
        return "quote"
    if re.match(r"^([-*+]|\d+[.)])\s", s):
        return "list"
    if re.match(r"^\s+([-*+]|\d+[.)])\s", line):
        return "sublist"
    if re.match(r"^\s{1,3}\S", line):
        return "cont"          # continuación de un ítem de lista
    if re.match(r"^\s{4,}\S", line):
        return "indented"      # bloque indentado / arte: se deja como está
    return "plain"


def hard_break(line):
    return line.endswith("  ") or line.rstrip().endswith("\\")


def mergeable(prev_kind, prev, cur_kind, cur):
    """¿La línea actual es continuación de la anterior?"""
    if hard_break(prev):
        return False
    if any(c in BOX for c in prev) or any(c in BOX for c in cur):
        return False
    if prev_kind == "plain" and cur_kind in ("plain", "cont"):
        return True
    if prev_kind in ("list", "qlist", "quote") and cur_kind in ("plain", "cont"):
        return True
    if prev_kind == "quote" and cur_kind == "quote":
        return True
    return False


def join(prev, cur, prev_kind, cur_kind):
    if prev_kind == "quote":            # conservar el "> " del principio
        body = cur.strip()
        body = re.sub(r"^>\s?", "", body)
        return prev.rstrip() + " " + body
    return prev.rstrip() + " " + cur.strip()


def fence_blocks(text):
    """Bloques cercados, ignorando el prefijo de cita, para verificar que no se tocaron."""
    plano = re.sub(r"(?m)^\s*>\s?", "", text)
    return re.findall(r"(?:```|~~~).*?(?:```|~~~)", plano, flags=re.S)


def reflow(text):
    lines = text.split("\n")
    out = []            # líneas finales
    kinds = []          # tipo de cada línea final
    i = 0
    n = len(lines)

    # frontmatter intacto
    if n and lines[0].strip() == "---":
        j = 1
        while j < n and lines[j].strip() != "---":
            j += 1
        if j < n:
            out.extend(lines[: j + 1])
            kinds.extend(["fm"] * (j + 1))
            i = j + 1

    infence = False
    while i < n:
        line = lines[i]
        k = cls(line)

        if fence_marker(line):
            out.append(line)
            kinds.append("fence")
            infence = not infence
            i += 1
            continue
        if infence:
            out.append(line)
            kinds.append("fence")
            i += 1
            continue

        # ¿se une con la línea anterior?
        if out and mergeable(kinds[-1], out[-1], k, line):
            out[-1] = join(out[-1], line, kinds[-1], k)
            i += 1
            continue

        # dos callouts pegados con un ">" en el medio: sin línea en blanco el segundo se pierde
        if k == "qblank":
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and re.match(r"^> ?\[!", lines[j].strip()):
                out.append("")
                kinds.append("blank")
                i += 1
                continue

        # normalización de líneas en blanco alrededor de bloques (sólo a nivel superior)
        if out:
            pk = kinds[-1]
            prev_block = pk in ("head", "table", "callout", "fence", "hr", "list", "plain", "indented")
            if k in ("head", "table", "callout", "fence", "hr", "list") and prev_block:
                same = (k == "table" and pk == "table")
                if not same:
                    out.append("")
                    kinds.append("blank")
            elif pk == "table" and k not in ("table", "blank"):
                out.append("")
                kinds.append("blank")

        # colapsar blancos repetidos
        if k == "blank" and kinds and kinds[-1] == "blank":
            i += 1
            continue

        out.append(line)
        kinds.append(k)
        i += 1

    # sin blancos al principio ni al final; un solo \n final
    while out and out[0].strip() == "":
        out.pop(0); kinds.pop(0)
    while out and out[-1].strip() == "":
        out.pop(); kinds.pop()
    res = "\n".join(out) + "\n"
    if fence_blocks(res) != fence_blocks(text):       # red de seguridad: no se escribe nada
        raise ValueError("los bloques de código cambiarían")
    return res


def walk():
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in (".git", ".obsidian")]
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(root, f)


def main():
    check = "--check" in sys.argv
    changed = []
    for p in walk():
        orig = open(p, encoding="utf-8").read()
        try:
            new = reflow(orig)
        except ValueError as e:
            print("SALTADO (bloques de código):", os.path.relpath(p, VAULT), "→", e)
            continue
        if new != orig:
            changed.append((os.path.relpath(p, VAULT),
                            orig.count("\n") - new.count("\n"),
                            len(new) - len(orig)))
            if not check:
                open(p, "w", encoding="utf-8").write(new)
    print(("REVISIÓN: " if check else "REESCRITOS: ") + str(len(changed)) + " archivos")
    for c in changed[:15]:
        print("   %-70s %+5d líneas  %+6d bytes" % (c[0][:70], -c[1], c[2]))
    if len(changed) > 15:
        print("   … y %d más" % (len(changed) - 15))


if __name__ == "__main__":
    main()
