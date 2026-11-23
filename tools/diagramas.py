#!/usr/bin/env python3
"""
Generador de diagramas SVG para la bóveda de Arquitectura de Computadoras (UCASAL).
Versión 2: ruteo planificado, compuertas con pines etiquetados.
Salida: ../assets/*.svg
"""
import os, math

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
os.makedirs(OUT, exist_ok=True)

STROKE = "#1f2937"
FILL = "#ffffff"
ACCENT = "#1d4ed8"
RED = "#b91c1c"
FONT = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
MONO = "Consolas, 'Courier New', monospace"


class Svg:
    def __init__(self, w, h, title=None):
        self.w, self.h = w, h
        self.parts = []
        if title:
            self.text(20, 26, title, size=15, weight="700")

    def raw(self, s): self.parts.append(s)

    def line(self, x1, y1, x2, y2, w=1.6, color=STROKE, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.raw(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>')

    def wire(self, pts, w=1.6, color=STROKE, dash=None):
        for i in range(len(pts) - 1):
            self.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], w=w, color=color, dash=dash)

    def poly(self, pts, w=1.6, color=STROKE, fill="none", close=False):
        p = " ".join(f"{x},{y}" for x, y in pts)
        tag = "polygon" if close else "polyline"
        self.raw(f'<{tag} points="{p}" fill="{fill}" stroke="{color}" stroke-width="{w}" stroke-linejoin="round"/>')

    def arrow(self, x1, y1, x2, y2, w=1.6, color=STROKE, size=9):
        ang = math.atan2(y2 - y1, x2 - x1)
        self.line(x1, y1, x2, y2, w=w, color=color)
        for s in (+1, -1):
            a = ang + s * math.radians(24)
            self.line(x2, y2, x2 - size * math.cos(a), y2 - size * math.sin(a), w=w, color=color)

    def arrowpath(self, pts, w=1.6, color=STROKE):
        """Flecha por segmentos: la cabeza va en el último punto."""
        for i in range(len(pts) - 2):
            self.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], w=w, color=color)
        self.arrow(pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1], w=w, color=color)

    def box(self, x, y, w, h, label="", sub="", fill=FILL, r=6, size=13, weight="600",
            color=STROKE, subcolor="#4b5563"):
        self.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
                 f'fill="{fill}" stroke="{color}" stroke-width="1.7"/>')
        if label and sub:
            self.text(x + w / 2, y + h / 2 - 3, label, size=size, weight=weight, anchor="middle")
            self.text(x + w / 2, y + h / 2 + 14, sub, size=size - 3.5, weight="400",
                      anchor="middle", color=subcolor)
        elif label:
            self.text(x + w / 2, y + h / 2 + size * 0.35, label, size=size, weight=weight, anchor="middle")

    def text(self, x, y, s, size=12, weight="400", anchor="start", color=STROKE,
             family=None, style=""):
        family = family or FONT
        st = f' font-style="{style}"' if style else ""
        s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
        self.raw(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
                 f'font-weight="{weight}" text-anchor="{anchor}" fill="{color}"{st}>{s}</text>')

    def dot(self, x, y, r=3.4, color=STROKE):
        self.raw(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')

    def note(self, x, y, lines, size=10.5, color="#4b5563", lh=15):
        for i, l in enumerate(lines):
            self.text(x, y + i * lh, l, size=size, color=color)

    # ---------------- compuertas ----------------
    def _body(self, kind, x, y, w, h, color=STROKE):
        """Dibuja el cuerpo; devuelve (x_in_pin, x_out_pin)."""
        r = h / 2
        if kind in ("AND", "NAND"):
            self.raw(f'<path d="M{x},{y} L{x + w - r},{y} A{r},{r} 0 0 1 {x + w - r},{y + h} '
                     f'L{x},{y + h} Z" fill="{FILL}" stroke="{color}" stroke-width="1.7"/>')
            xin, xout = x, x + w
        elif kind in ("OR", "NOR", "XOR", "XNOR"):
            d = (f'M{x},{y} C{x + w*0.26},{y} {x + w*0.74},{y + h*0.1} {x + w},{y + h/2} '
                 f'C{x + w*0.74},{y + h*0.9} {x + w*0.26},{y + h} {x},{y + h} '
                 f'C{x + w*0.18},{y + h*0.66} {x + w*0.18},{y + h*0.34} {x},{y} Z')
            self.raw(f'<path d="{d}" fill="{FILL}" stroke="{color}" stroke-width="1.7"/>')
            if kind in ("XOR", "XNOR"):
                self.raw(f'<path d="M{x-9},{y} C{x + w*0.09},{y + h*0.34} {x + w*0.09},{y + h*0.66} '
                         f'{x-9},{y + h}" fill="none" stroke="{color}" stroke-width="1.7"/>')
            xin, xout = x + 8, x + w
        else:  # NOT
            self.poly([(x, y), (x, y + h), (x + w - 8, y + h / 2)], close=True, fill=FILL, color=color)
            self.raw(f'<circle cx="{x + w - 3}" cy="{y + h/2}" r="5" fill="{FILL}" stroke="{color}" stroke-width="1.7"/>')
            xin, xout = x, x + w + 2
        if kind in ("NAND", "NOR", "XNOR"):
            self.raw(f'<circle cx="{xout + 5}" cy="{y + h/2}" r="5" fill="{FILL}" stroke="{color}" stroke-width="1.7"/>')
            xout += 10
        return xin, xout

    def gate(self, kind, x, y, ins=None, out=None, w=62, h=44, stub=22, tag=None,
             tagpos="in", isize=11):
        """Compuerta con pines etiquetados (estilo didáctico, sin cables largos)."""
        xin, xout = self._body(kind, x, y, w, h)
        n = max(1, len(ins or []))
        if ins:
            for i, lab in enumerate(ins):
                yy = y + h * (i + 1) / (n + 1)
                self.line(xin - stub, yy, xin, yy)
                self.text(xin - stub - 5, yy + 4, lab, size=isize, anchor="end", weight="600")
        if out:
            yy = y + h / 2
            self.line(xout, yy, xout + stub, yy)
            self.text(xout + stub + 5, yy + 4, out, size=isize, weight="700", color=ACCENT)
        if tag:
            self.text(x + w * 0.5, y + h / 2 + 4, tag, size=9.5, weight="700",
                      anchor="middle", color="#64748b")
        return {"xin": xin, "xout": xout, "mid": y + h / 2,
                "in_y": [y + h * (i + 1) / (n + 1) for i in range(n)]}

    def save(self, name):
        body = "\n  ".join(self.parts)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
               f'viewBox="0 0 {self.w} {self.h}">\n  <rect width="100%" height="100%" fill="#ffffff"/>\n'
               f'  {body}\n</svg>\n')
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("ok:", name)


# =====================================================================
def d_semisumador():
    s = Svg(520, 250, "Semisumador (half adder):  S = A⊕B   ·   C = A·B")
    # XOR
    x1 = s.gate("XOR", 150, 62, ["A", "B"], "S = A ⊕ B", w=70, h=52)
    a1 = s.gate("AND", 150, 165, ["A", "B"], "C = A · B", w=70, h=52)
    s.text(40, 60, "Suma sin acarreo de entrada: c = 0", size=10.5, color="#4b5563")
    s.text(40, 78, "Sólo sirve para el bit menos significativo (LSB).", size=10.5, color="#4b5563")
    s.note(40, 200, ["A, B: bits a sumar.", "S: bit de suma.  C: acarreo de salida (carry)."], size=10)
    s.save("semisumador.svg")


def d_sumador_completo():
    s = Svg(780, 360, "Sumador completo (full adder):  S = A⊕B⊕Cin   ·   Cout = A·B + Cin·(A⊕B)")
    s.gate("XOR", 170, 55, ["A", "B"], "S1", w=70, h=52, stub=30)
    s.gate("AND", 170, 150, ["A", "B"], "A·B", w=70, h=52, stub=30)
    s.gate("XOR", 420, 55, ["S1", "Cin"], "S", w=70, h=52, stub=30)
    s.gate("AND", 420, 150, ["S1", "Cin"], "S1·Cin", w=70, h=52, stub=30)
    s.gate("OR", 640, 95, ["A·B", "S1·Cin"], "Cout", w=76, h=70, stub=28)
    # llaves de agrupación (A y B alimentan a las dos primeras compuertas)
    s.line(88, 70, 88, 165, w=1.1, color="#94a3b8")
    s.line(88, 70, 100, 70, w=1.1, color="#94a3b8")
    s.line(88, 165, 100, 165, w=1.1, color="#94a3b8")
    s.text(84, 122, "A y B", size=9, anchor="end", color="#64748b")
    s.text(84, 138, "van a X1 y A1", size=9, anchor="end", color="#64748b")
    s.line(370, 70, 390, 70, w=1.2, color="#94a3b8")
    s.line(370, 165, 390, 165, w=1.2, color="#94a3b8")
    s.line(390, 70, 390, 165, w=1.2, color="#94a3b8")
    s.note(34, 275, [
        "S1 = A⊕B es la señal intermedia: se calcula una sola vez y se reutiliza en X2 y en A2 (es el 'acarreo generado').",
        "Cout = A·B + Cin·(A⊕B): el acarreo sale si A y B son 1, o si el acarreo de entrada encuentra una suma parcial en 1.",
        "Sumando n bits: se encadenan n sumadores completos y el Cout de cada uno se conecta al Cin del siguiente (acarreo en cascada).",
        "Tabla de verdad: S = 1 sólo con un número impar de unos en A, B y Cin;  Cout = 1 cuando hay dos o tres unos.",
    ], size=10.5, lh=20)
    s.save("sumador_completo.svg")


def d_decodificador_2x4():
    s = Svg(700, 400, "Decodificador 2 a 4 (activo por nivel alto)")
    s.gate("NOT", 90, 55, ["A1"], "A1'", w=54, h=44, stub=26)
    s.gate("NOT", 90, 115, ["A0"], "A0'", w=54, h=44, stub=26)
    ys = [55, 135, 215, 315]
    outs = ["Y0 = A1'·A0'", "Y1 = A1'·A0", "Y2 = A1·A0'", "Y3 = A1·A0"]
    pins = [["A1'", "A0'"], ["A1'", "A0"], ["A1", "A0'"], ["A1", "A0"]]
    for y, o, p in zip(ys, outs, pins):
        s.gate("AND", 330, y, p, o, w=64, h=52, stub=34)
    s.note(90, 210, ["Los complementos A1' y A0'", "salen de dos inversores.",
                     "Cada salida Yi es un mintérmino:", "Yi = 1 sólo para una", "combinación de entrada."], size=10)
    s.text(20, 385, "Uso típico: seleccionar una de 8 palabras de memoria (3→8) o habilitar un registro.", size=10.5, color="#4b5563")
    s.save("decodificador_2x4.svg")


def d_decodificador_3x8():
    s = Svg(780, 470, "Decodificador 3 a 8 (bloque tipo 74LS138) y su tabla de verdad")
    s.box(130, 55, 150, 160, "DEC 3→8", "3 entradas · 8 salidas", fill="#f8fafc")
    for i, y in enumerate([85, 115, 145]):
        s.line(50, y, 130, y); s.text(44, y + 4, f"A{2 - i}", size=12, weight="700", anchor="end")
    s.line(50, 185, 130, 185); s.text(44, 189, "EN", size=11.5, weight="700", anchor="end")
    for i, y in enumerate(range(72, 210, 17)):
        s.line(280, y, 320, y)
        s.text(326, y + 4, f"Y{i}", size=11.5, weight="600", color=ACCENT)
    # tabla de verdad
    tx, ty = 400, 50
    s.raw(f'<rect x="{tx}" y="{ty}" width="350" height="215" rx="6" fill="#f8fafc" stroke="#1f2937" stroke-width="1.3"/>')
    s.text(tx + 175, ty + 20, "A2 A1 A0  →  salida activa (=1)", size=10.5, anchor="middle", weight="700")
    for i in range(8):
        bits = f"{i:03b}"
        s.text(tx + 175, ty + 44 + i * 22, f"{bits[0]}  {bits[1]}  {bits[2]}   →   Y{i} = 1   (las demás en 0)",
               size=10.5, anchor="middle", family=MONO, weight="600", color="#0f766e")
    s.note(30, 300, [
        "· Cada salida Yi es un mintérmino: vale 1 sólo para la combinación de entrada que le corresponde.",
        "· EN (enable) = 0 deshabilita el C.I.: todas las salidas quedan inactivas. Por eso se pueden combinar dos",
        "   decodificadores 3→8 y armar uno 4→16 (se usa el bit más significativo como EN de cada uno).",
        "· En las memorias, el decodificador es el que 'elige' la fila o palabra que se va a leer o escribir.",
        "· Organización 2D: el decodificador de fila y el de columna seleccionan la celda dentro de la matriz.",
    ], size=10.5, lh=19)
    s.save("decodificador_3x8.svg")


def d_mux_4x1():
    s = Svg(720, 380, "Multiplexor 4 a 1:  Z = S1'·S0'·D0 + S1'·S0·D1 + S1·S0'·D2 + S1·S0·D3")
    ys = [50, 115, 180, 245]
    pins = [["D0", "S1'", "S0'"], ["D1", "S1'", "S0"], ["D2", "S1", "S0'"], ["D3", "S1", "S0"]]
    s.gate("OR", 480, 50, ["t0", "t1", "t2", "t3"], "Z", w=76, h=250, stub=30)
    for i, (y, p) in enumerate(zip(ys, pins)):
        s.gate("AND", 300, y, p, f"t{i}", w=66, h=56, stub=34)
    s.note(40, 330, [
        "El selector (S1 S0) habilita UN solo AND por vez; por lo tanto sólo ese dato llega a la OR y sale por Z.",
        "Es un selector de datos: conmuta 4 entradas a 1 salida. Es la base del manejo de un bus compartido.",
    ], size=10.5)
    s.save("mux_4x1.svg")


def d_demux_1x4():
    s = Svg(680, 400, "Demultiplexor 1 a 4: el dato D se dirige a la salida seleccionada por S1 S0")
    ys = [60, 130, 200, 270]
    pins = [["D", "S1'", "S0'"], ["D", "S1'", "S0"], ["D", "S1", "S0'"], ["D", "S1", "S0"]]
    for y, p, i in zip(ys, pins, range(4)):
        s.gate("AND", 300, y, p, f"Y{i}", w=66, h=56, stub=34)
    s.note(40, 350, [
        "Las 4 salidas están en 0 salvo la seleccionada, que toma el valor de D.",
        "Es el camino inverso al MUX: 1 línea → N líneas (reparto de datos / direccionamiento).",
    ], size=10.5)
    s.save("demux_1x4.svg")


def d_estructura_basica():
    s = Svg(760, 470, "Estructura básica de un computador (Von Neumann): unidades y buses")
    # CPU
    s.raw('<rect x="40" y="45" width="330" height="150" rx="8" fill="#ffffff" stroke="#1f2937" stroke-width="2"/>')
    s.text(52, 66, "CPU", size=14, weight="700", color=ACCENT)
    s.box(55, 76, 145, 52, "UNIDAD DE CONTROL", "", fill="#eef2ff", size=10.5)
    s.box(215, 76, 140, 52, "ALU", "aritmética y lógica", fill="#eef2ff", size=12)
    s.box(55, 138, 300, 44, "REGISTROS", "PC · IR · MAR · MBR · AC", fill="#eef2ff", size=11)
    # Memoria
    s.box(430, 45, 290, 150, "MEMORIA PRINCIPAL", "RAM / ROM — instrucciones + datos", fill="#e0e7ff")
    # Bus
    s.raw('<rect x="40" y="228" width="680" height="40" rx="6" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.9"/>')
    s.text(380, 243, "BUS DEL SISTEMA", size=13, weight="700", anchor="middle", color="#1e3a8a")
    s.text(380, 259, "bus de datos  ·  bus de direcciones  ·  bus de control", size=10.5,
           anchor="middle", color="#1e3a8a")
    # E/S
    s.box(40, 330, 330, 90, "UNIDAD DE ENTRADA / SALIDA", "interfaces y controladores de periféricos", fill="#f8fafc")
    s.box(430, 330, 290, 90, "PERIFÉRICOS", "teclado · monitor · disco · impresora", fill="#f8fafc")
    # conexiones
    s.arrow(205, 195, 205, 228); s.arrow(205, 268, 205, 330)
    s.arrow(575, 195, 575, 228); s.arrow(575, 268, 575, 330)
    s.note(40, 450, ["Von Neumann: un único bus y una única memoria para instrucciones y datos (cuello de botella de von Neumann)."], size=10.5)
    s.save("estructura_basica.svg")


def d_ram_8x3():
    s = Svg(800, 580, "Memoria RAM 8 × 3: 8 palabras de 3 bits (3 biestables por palabra)")
    s.raw('<rect x="60" y="52" width="600" height="350" rx="10" fill="#f8fafc" stroke="#1f2937" stroke-width="1.8"/>')
    s.text(74, 72, "C.I. RAM 8×3", size=12.5, weight="700", color=ACCENT)
    s.box(110, 95, 92, 62, "DEC 3→8", fill="#ffffff", size=11)
    for i, y in enumerate([108, 124, 140]):
        s.line(50, y, 110, y); s.text(44, y + 4, f"A{2 - i}", size=11, weight="700", anchor="end")
    s.text(20, 172, "dirección", size=9.5, color="#4b5563")
    s.line(202, 126, 226, 126)
    s.line(226, 88, 226, 350)
    for i in range(8):
        cy = 88 + i * 36
        s.line(226, cy, 250, cy); s.dot(226, cy)
        s.text(238, cy - 7, f"{i:03b}", size=8, anchor="middle", color="#64748b", family=MONO)
        for cx in (250, 300, 350):
            s.raw(f'<rect x="{cx}" y="{cy - 13}" width="42" height="26" rx="3" fill="#e0e7ff" stroke="#1f2937" stroke-width="1.2"/>')
            s.text(cx + 21, cy + 4, "FF-D", size=8.5, anchor="middle", weight="600")
        s.line(392, cy, 470, cy)
        s.text(436, cy - 6, "3", size=8, color="#1d4ed8")
    # bus de datos
    s.raw('<rect x="470" y="72" width="26" height="316" rx="4" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="1.4"/>')
    for i in range(8):
        cy = 88 + i * 36
        s.dot(470, cy)
    s.arrow(496, 230, 560, 230)
    s.text(566, 226, "datos (3 bits)", size=10, weight="600", color=ACCENT)
    s.text(566, 240, "D2 D1 D0  →  bus", size=9.5, color="#4b5563")
    # control debajo del C.I.
    s.box(410, 425, 145, 44, "R/W'", "1 = lee · 0 = escribe", fill="#ffffff", size=11)
    s.box(580, 425, 110, 44, "CS", "chip select", fill="#ffffff", size=11)
    s.arrow(482, 425, 482, 402)
    s.arrow(635, 425, 635, 402)
    s.note(30, 500, [
        "Capacidad = 8 palabras × 3 bits = 24 bits.   Direcciones: 000 … 111 (3 bits ⇒ 2³ = 8 posiciones).",
        "Cada palabra es un registro de 3 biestables D que comparten la MISMA línea de selección (la salida del decodificador):",
        "por eso la palabra entera se lee o se escribe en un solo acceso de memoria.",
        "Escritura: se ponen dirección + dato en los buses y R/W' = 0 (el flanco guarda el dato en los 3 FF).  Lectura: dirección + R/W' = 1.",
    ], size=10.5, lh=19)
    s.save("ram_8x3.svg")


def d_jerarquia():
    s = Svg(700, 420, "Jerarquía de memorias: velocidad, capacidad y costo por bit")
    levels = [("Registros de la CPU", "~1 ns", "≈ cientos de bytes", "#dbeafe"),
              ("Caché L1", "~1–2 ns", "decenas de KB", "#c7ddfc"),
              ("Caché L2 / L3", "~5–15 ns", "MB", "#b5d0fa"),
              ("Memoria principal (RAM)", "~50–100 ns", "GB", "#a3c3f7"),
              ("Memoria secundaria (SSD/disco)", "~0,1 ms", "TB", "#d7e0ea"),
              ("Cinta magnética / respaldo", "segundos", "TB", "#e5eaf0")]
    y = 50
    for i, (n, t, c, col) in enumerate(levels):
        w = 260 + i * 58
        x = 350 - w / 2 + 60
        s.raw(f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="5" fill="{col}" stroke="#1f2937" stroke-width="1.4"/>')
        s.text(x + w / 2, y + 19, n, size=11.5, weight="600", anchor="middle")
        s.text(x + w / 2, y + 34, f"{t} · {c}", size=9.5, anchor="middle", color="#4b5563")
        y += 52
    s.text(20, 90, "más rápida", size=11, weight="700", color=ACCENT)
    s.text(20, 160, "más cara por bit", size=10, color=ACCENT)
    s.arrow(50, 100, 50, 205)
    s.text(20, 330, "más lenta", size=11, weight="700", color=RED)
    s.text(20, 348, "más barata por bit", size=10, color=RED)
    s.arrow(50, 320, 50, 240)
    s.text(690, y + 10, "Localidad: la CPU usa pocas instrucciones y datos muchas veces ⇒ lo chico y rápido arriba rinde.", size=9.5, anchor="end", color="#4b5563")
    s.save("jerarquia_memorias.svg")


def d_flipflops():
    s = Svg(820, 480, "Biestables: S-R, D, J-K y T (símbolo, tabla de estados y ecuación)")
    specs = [
        ("S-R", ["S  C  R", "0 ↑ 0  →  Q (mantiene)", "1 ↑ 0  →  Q = 1  (set)", "0 ↑ 1  →  Q = 0  (reset)", "1 ↑ 1  →  estado prohibido"],
         ["S", "R"], "Q(t+1) = S + R'·Q"),
        ("D", ["D  C", "0 ↑  →  Q = 0", "1 ↑  →  Q = 1", "Q sigue a D (dato)", "sin flanco: mantiene"],
         ["D"], "Q(t+1) = D"),
        ("J-K", ["J  C  K", "0 ↑ 0  →  mantiene", "1 ↑ 0  →  Q = 1", "0 ↑ 1  →  Q = 0", "1 ↑ 1  →  conmuta (toggle)"],
         ["J", "K"], "Q(t+1) = J·Q' + K'·Q"),
        ("T", ["T  C", "0 ↑  →  mantiene", "1 ↑  →  conmuta", "Q(t+1) = T ⊕ Q", "divisor de frecuencia"],
         ["T"], "Q(t+1) = T ⊕ Q"),
    ]
    for k, (name, rows, pins, eq) in enumerate(specs):
        x = 25 + k * 196
        w, y0 = 145, 55
        s.raw(f'<rect x="{x}" y="{y0}" width="{w}" height="95" rx="6" fill="#f8fafc" stroke="#1f2937" stroke-width="1.8"/>')
        s.text(x + w / 2, y0 + 18, name, size=13.5, weight="700", anchor="middle", color=ACCENT)
        # salidas Q y Q' (derecha)
        s.line(x + w, y0 + 30, x + w + 13, y0 + 30)
        s.text(x + w + 17, y0 + 34, "Q", size=10.5, weight="700")
        s.line(x + w, y0 + 63, x + w + 13, y0 + 63)
        s.text(x + w + 17, y0 + 67, "Q'", size=10, weight="600")
        # entradas (izquierda)
        if len(pins) == 1:
            s.line(x - 13, y0 + 33, x, y0 + 33); s.text(x + 9, y0 + 37, pins[0], size=10.5, weight="700")
        else:
            s.line(x - 13, y0 + 25, x, y0 + 25); s.text(x + 9, y0 + 29, pins[0], size=10.5, weight="700")
            s.line(x - 13, y0 + 57, x, y0 + 57); s.text(x + 9, y0 + 61, pins[1], size=10.5, weight="700")
        # reloj
        s.line(x - 13, y0 + 81, x + 12, y0 + 81)
        s.raw(f'<path d="M{x + 12},{y0 + 75} l9,6 l-9,6" fill="none" stroke="#1f2937" stroke-width="1.3"/>')
        s.text(x + 24, y0 + 85, "C", size=10, weight="700")
        for i, r in enumerate(rows):
            s.text(x, 178 + i * 19, r, size=10, weight="700" if i == 0 else "400")
        s.text(x, 288, eq, size=10.5, weight="700", color="#0f766e")
    s.note(30, 335, [
        "↑ = flanco activo (normalmente de subida). Los biestables de la cátedra son disparados por flanco:",
        "Q sólo puede cambiar en el instante del pulso de reloj (los cambios asincrónicos se ven como basura).",
        "Entradas asincrónicas PRESET (Q = 1) y CLEAR (Q = 0) actúan sin esperar el reloj: se usan para",
        "inicializar registros y contadores al encender la máquina (RESET del sistema).",
        "Poniendo n biestables en paralelo con el mismo reloj y la misma línea de LOAD se arma un registro de n bits;",
        "con la salida Q' realimentada a la entrada D se obtiene un divisor de frecuencia (T = 1).",
    ], size=10.5, lh=19)
    s.save("flipflops.svg")


def d_pipeline():
    s = Svg(760, 400, "Pipeline de instrucciones de 4 segmentos: solapamiento (paralelismo temporal)")
    cols = ["#fde68a", "#bfdbfe", "#a7f3d0", "#fecaca"]
    segs = ["BI", "DE", "OP", "EJ"]
    for i, (n, c) in enumerate(zip(segs, cols)):
        x = 90 + i * 62
        s.raw(f'<rect x="{x}" y="50" width="56" height="24" rx="3" fill="{c}" stroke="#1f2937" stroke-width="1.1"/>')
        s.text(x + 28, 66, n, size=10, anchor="middle", weight="700")
    s.text(90 + 4 * 62 + 10, 66, "BI = búsqueda · DE = decodificación · OP = operandos · EJ = ejecución",
           size=10, color="#4b5563")
    for row in range(5):
        y = 95 + row * 40
        s.text(45, y + 20, f"I{row+1}", size=12, weight="700", anchor="middle")
        for seg in range(4):
            t = row + seg
            if t < 10:
                x = 90 + t * 62
                s.raw(f'<rect x="{x}" y="{y}" width="56" height="30" rx="3" fill="{cols[seg]}" stroke="#1f2937" stroke-width="1.1"/>')
                s.text(x + 28, y + 19, segs[seg], size=10, anchor="middle", weight="600")
    s.line(90, 330, 690, 330)
    for t in range(10):
        x = 90 + t * 62
        s.line(x, 326, x, 334)
        s.text(x, 348, f"t{t+1}", size=9.5, anchor="middle", color="#4b5563")
    s.note(30, 380, ["Sin pipeline: 4 ciclos por instrucción (1 instrucción cada 4 t). Con pipeline lleno: 1 instrucción por ciclo."], size=10.5)
    s.save("pipeline.svg")


def d_formatos():
    s = Svg(780, 400, "Los cuatro formatos clásicos de instrucción")
    fmt = [("4 direcciones", ["OP", "A1", "A2", "A3", "A4"], "A1 ← A2 OP A3 ;  salto a A4", "instrucción más larga, menos instrucciones"),
           ("3 direcciones", ["OP", "A1", "A2", "A3"], "A1 ← A2 OP A3", "equilibrado; base de máquinas RISC"),
           ("2 direcciones", ["OP", "A1", "A2"], "A1 ← A1 OP A2   (se destruye A1)", "típico de CISC / x86"),
           ("1 dirección", ["OP", "A1"], "AC ← AC OP A1   (acumulador implícito)", "corta, pero más instrucciones por programa")]
    for i, (name, fields, op, note) in enumerate(fmt):
        y = 55 + i * 82
        s.text(24, y + 26, name, size=12.5, weight="700")
        x = 150
        colors = ["#fecaca", "#dbeafe", "#dbeafe", "#bfdbfe", "#e0e7ff"]
        for j, f in enumerate(fields):
            w = 52 if j == 0 else 66
            s.raw(f'<rect x="{x}" y="{y + 6}" width="{w}" height="30" rx="3" fill="{colors[j % len(colors)]}" stroke="#1f2937" stroke-width="1.3"/>')
            s.text(x + w / 2, y + 26, f, size=10.5, anchor="middle", weight="600")
            x += w
        s.text(x + 14, y + 26, op, size=10.5, weight="600", color=ACCENT)
        s.text(150, y + 52, note, size=9.5, color="#4b5563")
    s.note(24, 380, ["Menos direcciones ⇒ instrucción más corta, pero se necesitan más instrucciones para el mismo trabajo.",
                     "La cantidad de direcciones también define en qué registro queda el resultado (A1 o el AC)."], size=10.5)
    s.save("formatos_instruccion.svg")


def d_modos():
    s = Svg(800, 600, "Los siete modos de direccionamiento: cómo se construye la dirección efectiva (EA)")
    items = [("1. Inmediato", "OP  dato", "EA = —   el operando viaja dentro de la instrucción", "0 accesos", "LDI 5"),
             ("2. Directo / absoluto", "OP  D", "EA = D", "1 acceso", "LDA 25h"),
             ("3. Indirecto", "OP  D", "EA = M[D]   en la celda hay una dirección", "2 accesos", "LDA @25h"),
             ("4. De registro", "OP  R", "EA = R   el operando está en un registro", "0 accesos", "ADD RIF"),
             ("5. Registro indirecto", "OP  R", "EA = R   el registro guarda la dirección", "1 acceso", "LDA (RIF)"),
             ("6. Desplazamiento / indexado", "OP  D + X", "EA = D + X   con X = RIF o RID", "1 acceso", "LDA 25h,RIF"),
             ("7. De pila (stack)", "OP", "el operando está en el tope de la pila (LIFO)", "1 acceso", "PUSH / POP")]
    for i, (name, form, expl, acc, ej) in enumerate(items):
        y = 44 + i * 66
        s.raw(f'<rect x="20" y="{y}" width="760" height="56" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
        s.text(32, y + 24, name, size=12, weight="700")
        s.text(250, y + 24, form, size=11, family=MONO, weight="600", color="#0f766e")
        s.text(32, y + 44, expl, size=10.5, color="#374151")
        s.text(585, y + 24, acc, size=10.5, family=MONO, color="#b91c1c")
        s.text(585, y + 44, ej, size=10.5, family=MONO, color="#7c2d12")
    s.note(20, 528, ["EA (effective address) = dirección final que se pone en el MAR para ir a memoria.",
                     "Indexado = directo + un sumador de direcciones: la dirección de la instrucción se suma al registro",
                     "índice en el momento del acceso ⇒ permite recorrer arreglos y tablas con un mismo código.",
                     "Regla para distinguirlos: contar los accesos a memoria que hacen falta para tener el dato."], size=10.5)
    s.save("modos_direccionamiento.svg")



def d_lda24():
    """Línea de tiempo de la LDA indexada: 3 ciclos de máquina = 24 pulsos."""
    rows = [
        ("CICLO 1 · BÚSQUEDA", [
            ("1", "PC→MAR\nZ\nMEMR"), ("2", "+1→Y"), ("3", "espera"),
            ("4", "SUMA→PC"), ("5", "MBR\nstrobe"), ("6", "MBR→IR"), ("7", "decod."),
            ("8", "E→STATE")]),
        ("CICLO 2 · EJECUCIÓN 1\n(traer dirección y calcular EA)", [
            ("9", "PC→MAR\nZ\nMEMR"), ("10", "+1→Y"), ("11", "espera"),
            ("12", "SUMA→PC"), ("13", "RID→X"), ("14", "MBR→W"), ("15", "Σ suma"),
            ("16", "sigue E")]),
        ("CICLO 3 · EJECUCIÓN 2\n(ir al operando)", [
            ("17", "Σ→MAR\nMEMR"), ("18", "espera"), ("19", "espera"),
            ("20", "espera"), ("21", "espera"), ("22", "MBR→A"), ("23", "-"),
            ("24", "F→STATE")]),
    ]
    s = Svg(1250, 615, "LDA 3, X en la BLUE indexada: 3 ciclos de máquina de 8 pulsos = 24 pulsos")
    y0 = 60
    cw, ch, gap, lx = 108, 96, 10, 250
    for r, (label, cells) in enumerate(rows):
        y = y0 + r * (ch + 34)
        # etiqueta de la fila
        s.raw(f'<rect x="16" y="{y}" width="{lx-30}" height="{ch}" rx="7" fill="#eef2ff" stroke="{ACCENT}" stroke-width="1.3"/>')
        parts = label.split("\n")
        s.text(16 + (lx - 30) / 2, y + (ch / 2) - (len(parts) - 1) * 9, parts[0], size=11.5,
               weight="700", anchor="middle", color="#1e3a8a")
        for i, extra in enumerate(parts[1:]):
            s.text(16 + (lx - 30) / 2, y + (ch / 2) + 10 + i * 13, extra, size=9,
                   anchor="middle", color="#3730a3")
        for c, (num, act) in enumerate(cells):
            x = lx + c * (cw + gap)
            key = num in ("1", "4", "6", "13", "14", "17", "22", "24")
            fill = "#fef9c3" if key else "#f8fafc"
            stroke = "#ca8a04" if key else "#e5e7eb"
            s.raw(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>')
            s.text(x + 8, y + 17, "CP" + num, size=10.5, weight="700", color="#7c2d12", family=MONO)
            for i, ln in enumerate(act.split("\n")):
                s.text(x + 8, y + 34 + i * 13, ln, size=9.2, family=MONO, color="#111827")
        # numeración global
        s.text(lx - 8, y - 6, "" if r else "", size=9)
    ty = y0 + 3 * (ch + 34) + 6
    s.note(lx, ty, [
        "Amarillo = los pulsos que hay que saber nombrar en el oral: CP1/CP6 de la búsqueda (traer la instrucción),",
        "CP13/CP14 de ejecución 1 (cargar el índice en X y el campo de dirección en W) y CP17/CP22 de ejecución 2",
        "(direccionar el operando y cargarlo en el acumulador).",
    ], size=10)
    s.note(lx, ty + 56, [
        "Hay 3 accesos a memoria: búsqueda (trae la 1. palabra), ejecución 1 (trae la 2. palabra = campo de dirección)",
        "y ejecución 2 (trae el operando). Por eso 24 pulsos y no 16: la instrucción ocupa 2 palabras.",
    ], size=10)
    s.note(lx, ty + 100, [
        "LDA 0, X (directo): 24 pulsos, en CP13 se carga 0 en X.     LDA 1, X (indirecto): 32 pulsos (un ciclo más).",
        "LDA 2, X (RIF): 24 pulsos, en CP13 se carga RIF.             LDA 3, X (RID): 24 pulsos, en CP13 se carga RID.",
    ], size=10)
    s.save("lda24_pulsos.svg")


def d_blue_flujo():
    s = Svg(800, 560, "BLUE: registros y flujo de información (dato y direcciones)")
    # memoria
    s.box(560, 45, 200, 90, "MEMORIA", "4096 palabras × 16 bits", fill="#e0e7ff")
    # registros arriba del bus
    regs = [("PC", 45), ("MAR", 190), ("MBR", 335), ("IR", 480)]
    for n, x in regs:
        s.box(x, 165, 110, 48, n, fill="#ffffff", size=13)
    # bus
    s.raw('<rect x="45" y="255" width="715" height="40" rx="6" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.9"/>')
    s.text(400, 270, "BUS DEL SISTEMA", size=13, weight="700", anchor="middle", color="#1e3a8a")
    s.text(400, 286, "datos (16 bits)  ·  direcciones (12 bits)  ·  control (MEMR, MEMW, READ, WRITE)",
           size=10, anchor="middle", color="#1e3a8a")
    # conexiones registro-bus (doble flecha)
    for n, x in regs:
        cx = x + 55
        s.arrow(cx - 6, 213, cx - 6, 255, color="#334155")
        s.arrow(cx + 6, 255, cx + 6, 213, color="#334155")
    # PC -> MAR  y  MBR -> IR
    s.arrow(155, 189, 190, 189, color=RED)
    s.text(172, 180, "PC→MAR", size=8.5, anchor="middle", color=RED)
    s.arrow(445, 189, 480, 189, color=RED)
    s.text(462, 180, "MBR→IR", size=8.5, anchor="middle", color=RED)
    # memoria <-> bus
    s.arrow(640, 135, 640, 255, color="#1d4ed8")
    s.text(648, 200, "dirección ↑ / dato ↓", size=9.5, color="#1d4ed8")
    # abajo: AC, ALU, UC
    s.box(45, 345, 110, 48, "AC", fill="#ffffff", size=13)
    s.box(190, 340, 150, 58, "ALU", "opera con AC", fill="#eef2ff")
    s.box(400, 340, 175, 58, "UNIDAD DE CONTROL", "genera las señales", fill="#eef2ff", size=11)
    for cx in (100, 265):
        s.arrow(cx - 6, 345, cx - 6, 295, color="#334155")
        s.arrow(cx + 6, 295, cx + 6, 345, color="#334155")
    s.arrow(400, 369, 340, 369, color="#334155")
    # leyenda
    s.note(45, 440, [
        "1) PC → MAR: la dirección de la instrucción.             2) MAR → memoria: bus de direcciones (12 bits ⇒ 4096 posiciones).",
        "3) memoria → MBR: el dato leído viaja por el bus de datos (16 bits).      4) MBR → IR: la instrucción queda en el IR.",
        "5) IR(opcode) → UC: la UC decodifica y genera las señales del ciclo de ejecución.      6) AC: operando implícito de la ALU.",
        "El bus es el único camino entre registros: nunca hay dos transferencias al mismo tiempo ⇒ cada microoperación usa 1 pulso.",
    ], size=10.5, lh=22)
    s.save("blue_flujo.svg")


def d_ciclo_maquina():
    s = Svg(780, 340, "Ciclo de máquina: búsqueda (fetch) + ejecución (execute)")
    s.raw('<rect x="30" y="60" width="320" height="170" rx="8" fill="#dbeafe" stroke="#1d4ed8" stroke-width="1.8"/>')
    s.text(190, 85, "CICLO DE BÚSQUEDA", size=13, weight="700", anchor="middle", color="#1e3a8a")
    p1 = ["1. MAR ← PC", "2. MEMR = 1  (leer memoria)", "3. MBR ← M[MAR]  ;  PC ← PC + 1",
          "4. IR ← MBR", "5. decodificar opcode  ;  STATE ← E"]
    for i, p in enumerate(p1):
        s.text(50, 112 + i * 22, p, size=10.5)
    s.raw('<rect x="430" y="60" width="320" height="170" rx="8" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>')
    s.text(590, 85, "CICLO DE EJECUCIÓN", size=13, weight="700", anchor="middle", color="#14532d")
    p2 = ["6. leer operandos según el modo", "7. operar (ALU / registro / memoria)",
          "8. escribir el resultado", "9. actualizar PC si es salto", "10. STATE ← F   (vuelve a buscar)"]
    for i, p in enumerate(p2):
        s.text(450, 112 + i * 22, p, size=10.5)
    s.arrow(350, 145, 430, 145)
    s.raw('<path d="M590,230 C590,285 190,285 190,230" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="7 5"/>')
    s.arrow(190, 245, 190, 231, color="#7c3aed")
    s.note(30, 320, ["Mientras RUN = 1 el ciclo se repite instrucción por instrucción; los flip-flops STATE (F/E) y CLOCK (pulsos) lo sincronizan."], size=10.5)
    s.save("ciclo_maquina.svg")


def d_cache():
    s = Svg(780, 470, "Formas de mapear la memoria principal en la caché y partición de la dirección")
    cols = [("Mapeo directo", ["cada bloque tiene UN único lugar", "línea = (nº de bloque) mod (nº líneas)",
                               "+ simple, barato, rápido de buscar", "− conflictos (thrashing) frecuentes"], 25, "#dbeafe"),
            ("Asociativo total", ["cualquier bloque, cualquier línea", "se compara con TODAS las etiquetas",
                                  "+ máxima flexibilidad, menos fallos", "− comparadores caros (mem. asociativa)"], 275, "#dcfce7"),
            ("Asociativo por conjuntos", ["el bloque va a UN conjunto fijo", "y dentro del conjunto, a cualquier vía",
                                          "+ el compromiso real (L1/L2/L3)", "− necesita política de reemplazo"], 525, "#fef3c7")]
    for name, lines, x, col in cols:
        s.raw(f'<rect x="{x}" y="50" width="230" height="180" rx="8" fill="{col}" stroke="#1f2937" stroke-width="1.5"/>')
        s.text(x + 115, 76, name, size=11.5, weight="700", anchor="middle")
        for i, l in enumerate(lines):
            s.text(x + 14, 108 + i * 32, l, size=9.8)
    s.text(25, 275, "La dirección se parte así para buscar en caché:", size=11, weight="700", color="#334155")
    y = 295
    segs = [("ETIQUETA (tag)", 170, "#fecaca"), ("Nº de línea / conjunto", 190, "#bfdbfe"),
            ("desplazamiento (palabra/byte)", 210, "#bbf7d0")]
    x = 40
    for name, w, col in segs:
        s.raw(f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="4" fill="{col}" stroke="#1f2937" stroke-width="1.4"/>')
        s.text(x + w / 2, y + 22, name, size=9.8, anchor="middle", weight="600")
        x += w
    s.note(40, 370, [
        "Comparación de etiqueta → acierto (hit) o fallo (miss). Si falla, se trae el bloque entero de la memoria principal",
        "y se reemplaza uno de los residentes (FIFO, LRU, aleatorio). Escritura: write-through (escribe siempre) o",
        "write-back (escribe en caché y marca el bit 'dirty' hasta que el bloque sale). La inicialización del caché la hace",
        "el hardware: arranca 'vacía' (todos los bits de validez en 0) y cada línea se valida cuando se carga.",
    ], size=10.5, lh=19)
    s.save("cache_mapeos.svg")


def d_cisc_risc():
    s = Svg(780, 520, "CISC vs RISC: largo de la instrucción, quién hace el trabajo y por qué el pipeline")
    GREEN = "#15803d"

    # ---- encabezados
    s.raw(f'<rect x="40" y="46" width="330" height="46" rx="6" fill="#fee2e2" stroke="#1f2937" stroke-width="1.7"/>')
    s.text(205, 66, "CISC  (x86, 8086, VAX)", size=14, weight="700", anchor="middle")
    s.text(205, 83, "pocas instrucciones, cada una hace mucho", size=10.5, anchor="middle", color="#4b5563")

    s.raw(f'<rect x="410" y="46" width="330" height="46" rx="6" fill="#dbeafe" stroke="#1f2937" stroke-width="1.7"/>')
    s.text(575, 66, "RISC  (ARM, MIPS, RISC-V)", size=14, weight="700", anchor="middle")
    s.text(575, 83, "muchas instrucciones, cada una hace poco", size=10.5, anchor="middle", color="#4b5563")

    # ---- barra de instrucción variable (CISC)
    s.text(40, 122, "Una instrucción puede medir de 1 a 6 bytes:", size=10.5, color="#4b5563")
    campos_c = [(40, 56, "opc"), (96, 78, "mod"), (174, 116, "desplazamiento"), (290, 50, "dato")]
    for x, w, lab in campos_c:
        s.raw(f'<rect x="{x}" y="130" width="{w}" height="34" rx="3" fill="#fef3c7" stroke="#1f2937" stroke-width="1.4"/>')
        s.text(x + w / 2, 152, lab, size=9.2, weight="600", anchor="middle")
    s.text(348, 152, "← 4 bytes", size=9.5, color="#4b5563")
    campos_c2 = [(40, 56, "opc"), (96, 62, "reg")]
    for x, w, lab in campos_c2:
        s.raw(f'<rect x="{x}" y="170" width="{w}" height="34" rx="3" fill="#fef3c7" stroke="#1f2937" stroke-width="1.4"/>')
        s.text(x + w / 2, 192, lab, size=9.2, weight="600", anchor="middle")
    s.text(166, 192, "← 2 bytes  ⇒ largo VARIABLE", size=9.5, color=RED, weight="600")
    s.text(40, 226, "ADD [BX+SI+4], AX   →  memoria + memoria en UNA instrucción",
           size=10, family=MONO, color=ACCENT)

    # ---- barra de instrucción fija (RISC)
    s.text(410, 122, "Todas las instrucciones miden lo mismo:", size=10.5, color="#4b5563")
    campos_r = [(410, "Op"), (470, "rs1"), (530, "rs2"), (590, "rd"), (650, "funct")]
    for x, lab in campos_r:
        s.raw(f'<rect x="{x}" y="130" width="60" height="34" rx="3" fill="#bfdbfe" stroke="#1f2937" stroke-width="1.4"/>')
        s.text(x + 30, 152, lab, size=9.6, weight="600", anchor="middle")
    s.raw('<rect x="410" y="170" width="300" height="34" rx="3" fill="#eff6ff" stroke="#1f2937" '
          'stroke-width="1.4" stroke-dasharray="4 3"/>')
    for x, lab in campos_r:
        s.raw(f'<rect x="{x}" y="170" width="60" height="34" rx="3" fill="#bfdbfe" stroke="#1f2937" stroke-width="1.4"/>')
        s.text(x + 30, 192, lab, size=9.6, weight="600", anchor="middle")
    s.text(716, 152, "4 bytes", size=9.5, color="#4b5563")
    s.text(410, 226, "LW + ADD + SW  →  tres instrucciones simples",
           size=10, family=MONO, color=ACCENT)

    # ---- lista comparativa
    s.line(40, 246, 740, 246, w=1.2, color="#cbd5e1")
    izq = [
        ("+", "densidad de código alta (programa chico)", GREEN),
        ("+", "compatibilidad: el repertorio crece sin romper", GREEN),
        ("+", "menos búsquedas de instrucción", GREEN),
        ("-", "largo variable ⇒ pipeline difícil", RED),
        ("-", "UC microprogramada ⇒ más lento por microorden", RED),
        ("-", "hardware complejo y difícil de verificar", RED),
        ("→", "se ejecuta traduciendo a micro-operaciones", "#4b5563"),
    ]
    der = [
        ("+", "un ciclo por instrucción ⇒ pipeline eficiente", GREEN),
        ("+", "UC cableada: pocos modos y todos registro", GREEN),
        ("+", "muchos registros, acceso a memoria sólo load/store", GREEN),
        ("+", "menos consumo y hardware regular y escalable", GREEN),
        ("-", "más instrucciones: el programa ocupa más", RED),
        ("-", "depende del compilador para optimizar", RED),
        ("→", "control cableado, sin memoria de control", "#4b5563"),
    ]
    for i, (sym, txt, col) in enumerate(izq):
        y = 274 + i * 25
        s.text(44, y, sym, size=13, weight="700", color=col)
        s.text(60, y, txt, size=10.4, color="#1f2937")
    for i, (sym, txt, col) in enumerate(der):
        y = 274 + i * 25
        s.text(414, y, sym, size=13, weight="700", color=col)
        s.text(430, y, txt, size=10.4, color="#1f2937")

    s.line(40, 466, 740, 466, w=1.2, color="#cbd5e1")
    s.note(40, 484, [
        "Hoy son híbridos: el x86 (CISC) traduce cada instrucción a micro-operaciones simples y las ejecuta con un núcleo tipo RISC",
        "⇒ CISC por fuera, RISC por dentro. Lo que decide no es \"cuál es mejor\" sino el compromiso: código compacto vs pipeline.",
    ], size=10.4, lh=16)
    s.save("cisc_risc.svg")


def d_hazards():
    s = Svg(780, 405, "Los tres conflictos del pipeline (hazards) y cómo se resuelven")
    filas = [
        ("1 · DATOS (RAW)", "ADD  R1, R2, R3", "necesita R1", "SUB  R4, R1, R5",
         ["FORWARDING: adelantar el resultado de la ALU",
          "por un camino lateral, sin esperar a que se",
          "escriba el registro. Si no alcanza: STALL o NOP."]),
        ("2 · CONTROL (saltos)", "JZ  fin", "¿cuál sigue?", "¿I3 o la del salto?",
         ["No se sabe qué instrucción sigue hasta resolver",
          "el salto ⇒ PREDICCIÓN por historial. Si falla,",
          "se descarta lo que estaba en vuelo (burbuja)."]),
        ("3 · ESTRUCTURAL", "I1 busca instrucción", "misma memoria", "I2 lee el dato",
         ["Dos etapas quieren el mismo recurso ⇒ separar",
          "CACHÉ DE INSTRUCCIONES (I) y DE DATOS (D):",
          "por eso L1 está partida (Harvard por dentro)."]),
    ]
    y = 52
    for titulo, t1, medio, t2, sol in filas:
        s.text(40, y + 12, titulo, size=12, weight="700", color=RED)
        s.box(40, y + 24, 176, 38, label=t1, size=10.4, fill="#f8fafc", weight="600")
        s.box(252, y + 24, 176, 38, label=t2, size=10.4, fill="#f8fafc", weight="600")
        s.arrow(220, y + 43, 246, y + 43, w=1.8, color=RED)
        s.text(233, y + 16, medio, size=9.4, anchor="middle", color=RED)
        for k, linea in enumerate(sol):
            s.text(452, y + 32 + k * 15, linea, size=9.9, color="#1f2937")
        s.line(40, y + 80, 740, y + 80, w=1, color="#e2e8f0")
        y += 98
    s.note(40, 356, [
        "Regla de oro para el oral: el pipeline NO acelera una instrucción, acelera el ritmo. Y cada conflicto que se resuelve",
        "cuesta hardware: comparadores y caminos de forwarding (datos), predictores (control) y memorias separadas (estructural).",
        "Sin conflictos, con k etapas el speedup tiende a k.",
    ], size=10.3, lh=17)
    s.save("pipeline_hazards.svg")


def d_compuertas():
    s = Svg(830, 560, "Las siete compuertas lógicas: símbolo, función y tabla de verdad")
    items = [
        ("AND",  "AND",  "Y = A · B"),
        ("OR",   "OR",   "Y = A + B"),
        ("NOT",  "NOT",  "Y = A'"),
        ("NAND", "NAND", "Y = (A·B)'"),
        ("NOR",  "NOR",  "Y = (A+B)'"),
        ("XOR",  "XOR",  "Y = A ⊕ B"),
        ("XNOR", "XNOR", "Y = (A ⊕ B)'"),
    ]
    for i, (kind, name, form) in enumerate(items):
        col, row = i % 4, i // 4
        x = 45 + col * 195
        y = 62 + row * 135
        s.text(x + 34, y - 6, name, size=12.5, weight="700", anchor="middle")
        ins = ["A"] if kind == "NOT" else ["A", "B"]
        g = s.gate(kind, x, y, ins=ins, out="Y", w=68, h=46, stub=16)
        s.text(x + 88, y + 74, form, size=11, family=MONO, color=ACCENT)
    # ---- tabla global
    y0 = 330
    s.line(35, y0, 795, y0, w=1.2, color="#cbd5e1")
    heads = ["A", "B", "AND", "OR", "NAND", "NOR", "XOR", "XNOR", "NOT(A)"]
    xs = [60, 105, 175, 245, 322, 395, 468, 543, 640]
    for x, h in zip(xs, heads):
        s.text(x, y0 + 26, h, size=11, weight="700", anchor="middle")
    cols = {
        "AND": [0, 0, 0, 1], "OR": [0, 1, 1, 1], "NAND": [1, 1, 1, 0],
        "NOR": [1, 0, 0, 0], "XOR": [0, 1, 1, 0], "XNOR": [1, 0, 0, 1], "NOT(A)": [1, 1, 0, 0],
    }
    filas = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for r, (a, b) in enumerate(filas):
        yy = y0 + 52 + r * 26
        s.text(xs[0], yy, str(a), size=11.5, anchor="middle")
        s.text(xs[1], yy, str(b), size=11.5, anchor="middle")
        for x, h in zip(xs[2:], heads[2:]):
            v = str(cols[h][r])
            s.text(x, yy, v, size=11.5, anchor="middle",
                   weight="700" if v == "1" else "400", color=ACCENT if v == "1" else "#374151")
    s.line(35, y0 + 40, 795, y0 + 40, w=1, color="#cbd5e1")
    s.note(35, 486, [
        "NAND y NOR son universales: con cualquiera de ellas sola se arma cualquier función.",
        "XOR = paridad (1 con un número impar de unos) · XNOR = igualdad (A = B).",
    ], size=10.5, lh=16)
    s.save("compuertas.svg")


def d_codificador_8x3():
    s = Svg(790, 400, "Codificador 8 a 3: una compuerta OR por cada bit de salida")
    s.gate("OR", 430, 70, ins=["E4", "E5", "E6", "E7"], out="A2  (bit 2)", w=76, h=54, stub=30)
    s.gate("OR", 430, 165, ins=["E2", "E3", "E6", "E7"], out="A1  (bit 1)", w=76, h=54, stub=30)
    s.gate("OR", 430, 260, ins=["E1", "E3", "E5", "E7"], out="A0  (bit 0)", w=76, h=54, stub=30)
    s.note(40, 90, [
        "Cada salida es la OR de las entradas",
        "cuyo NÚMERO tiene ese bit en 1:",
        "",
        "  E5 = 101₂  ⇒  aporta a A2 y a A0",
        "",
        "Sólo una entrada debe estar activa;",
        "si hay dos, la salida es la OR de los",
        "códigos (basura) ⇒ hace falta el",
        "codificador CON PRIORIDAD.",
    ], size=10.6, lh=17)
    s.note(40, 330, [
        "Circuito: 3 compuertas OR de 4 entradas. No lleva AND ni inversores.",
    ], size=10.8, lh=17, color="#1f2937")
    s.save("codificador_8x3.svg")


def d_karnaugh_3var():
    s = Svg(700, 400, "Mapa de Karnaugh de 3 variables: F = Σm(1,3,5,7)")
    x0, y0, w, h = 150, 90, 90, 64
    cols = ["00", "01", "11", "10"]
    s.text(x0 + 2 * w, y0 - 34, "BC", size=11.5, weight="700", anchor="middle", color="#4b5563")
    for j, c in enumerate(cols):
        s.text(x0 + j * w + w / 2, y0 - 12, c, size=11.5, weight="700", anchor="middle")
    vals = {("0", "00"): 0, ("0", "01"): 1, ("0", "11"): 1, ("0", "10"): 0,
            ("1", "00"): 0, ("1", "01"): 1, ("1", "11"): 1, ("1", "10"): 0}
    for i, a in enumerate(["0", "1"]):
        s.text(x0 - 34, y0 + i * h + h / 2 + 5, "A=" + a, size=11.5, weight="700", anchor="middle")
        for j, c in enumerate(cols):
            v = vals[(a, c)]
            fill = "#dbeafe" if v == 1 else "#ffffff"
            s.raw(f'<rect x="{x0 + j * w}" y="{y0 + i * h}" width="{w}" height="{h}" '
                  f'fill="{fill}" stroke="#1f2937" stroke-width="1.5"/>')
            s.text(x0 + j * w + w / 2, y0 + i * h + h / 2 + 6, str(v), size=13,
                   weight="700" if v == 1 else "400", anchor="middle",
                   color=ACCENT if v == 1 else "#6b7280")
    # grupo: columnas 01 y 11, las dos filas  (recuadro rojo)
    s.raw(f'<rect x="{x0 + 1 * w + 4}" y="{y0 + 4}" width="{2 * w - 8}" height="{2 * h - 8}" '
          f'fill="none" stroke="{RED}" stroke-width="2.6" rx="4"/>')
    s.note(x0 + w * 4 + 26, y0 + 60, [
        "Grupo de 4:",
        "",
        "• A cambia  ⇒ desaparece",
        "• B cambia  ⇒ desaparece",
        "• C = 1 siempre ⇒ queda",
        "",
        "F = C",
    ], size=11.2, lh=18, color="#1f2937")
    s.note(40, 300, [
        "Las columnas van en código GRAY (00, 01, 11, 10): así dos casilleros vecinos difieren en UNA sola variable,",
        "y agruparlos equivale a aplicar A·B + A·B' = A. Un grupo de 2 elimina 1 variable; de 4, elimina 2; de 8, elimina 3.",
    ], size=10.4, lh=16)
    s.save("karnaugh_3var.svg")



def d_uc_cableada():
    """UC cableada: entradas (opcode, estado, reloj) -> AND -> OR -> senales."""
    s = Svg(920, 490, "Unidad de control cableada: las AND eligen, las OR juntan")
    s.box(20, 52, 168, 52, "IR 15..12", "opcode de 4 bits")
    s.box(20, 122, 168, 52, "1 → 16", "una línea por instrucción", fill="#dbeafe")
    s.box(20, 192, 168, 52, "FF STATE · RUN · TRA", "F/E · corriendo · E/S")
    s.box(20, 262, 168, 52, "reloj maestro", "CP1 … CP8")
    # colector
    s.wire([(188, 78), (216, 78), (216, 288), (188, 288)])
    for y in (78, 148, 218, 288):
        s.dot(216, y)
    s.arrow(216, 183, 250, 183)
    s.box(250, 148, 190, 70, "compuertas AND", "una por señal", fill="#fef3c7")
    s.arrow(440, 183, 474, 183)
    s.box(474, 148, 156, 70, "compuertas OR", "las que dan el mismo efecto", fill="#dcfce7")
    s.arrow(630, 183, 664, 183)
    s.box(664, 132, 236, 102, "señales de control", "Send X · Load Y · Read / Write", fill="#ffffff")
    s.note(680, 214, ["(a los registros, la ALU, la memoria)"], size=9.5, lh=13)

    # ejemplo de expansion
    s.raw(f'<rect x="20" y="330" width="880" height="142" rx="8" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(34, 352, "Por dentro: cada AND dice «en este estado, en este pulso, con esta instrucción», y la OR junta las que producen la misma señal", size=10.6, weight="600")
    filas = [("F · CP1", "Send PC, Load MAR"),
             ("E · CP2 · ARITH", "Send A, Load Z"),
             ("E · CP6 · LDA", "Send MBR, Load A")]
    for k, (a, b) in enumerate(filas):
        y = 384 + k * 26
        s.text(44, y, a, size=10.2, family=MONO, color="#7c2d12")
        s.text(250, y, "→", size=11, color="#1f2937")
        s.text(274, y, b, size=10.2, family=MONO, color=ACCENT)
    s.text(640, 392, "ARITH = ADD + XOR + AND + IOR", size=10.2, family=MONO, color="#4b5563")
    s.text(640, 416, "REF  = LDA + STA + ARITH", size=10.2, family=MONO, color="#4b5563")
    s.text(640, 440, "MBR_in = F·CP5 + E·CP5·REF", size=10.2, family=MONO, color=RED)
    s.text(34, 456, "La UC cableada es un combinacional gigante: tabla de verdad → función → compuertas.", size=10.2, color="#4b5563")
    s.save("uc_cableada.svg")


def d_uc_microprogramada():
    """UC microprogramada: opcode -> PLA -> microMAR -> ROM de control -> senales + secuenciador."""
    s = Svg(920, 430, "Unidad de control microprogramada: el opcode elige una dirección de la memoria de control")
    s.box(20, 70, 130, 56, "IR 15..12", "opcode")
    s.box(190, 70, 130, 56, "PLA", "opcode → dirección", fill="#dbeafe")
    s.box(360, 70, 130, 56, "microMAR", "apunta a la μ-instr.", fill="#e0e7ff")
    s.box(530, 58, 190, 84, "ROM de control", "504 × 21 bits (8088)", fill="#fef3c7")
    s.box(530, 230, 190, 64, "Registro de control", "21 bits = las señales", fill="#dcfce7")
    s.box(760, 58, 140, 84, "señales", "Send / Load / R-W")
    s.box(360, 230, 130, 64, "secuenciador", "μPC + SR / μ-pila", fill="#fde68a")
    s.box(190, 230, 130, 64, "condición", "flag · R · opcode")
    s.arrow(150, 98, 190, 98)
    s.arrow(320, 98, 360, 98)
    s.arrow(490, 98, 530, 98)
    s.arrow(720, 100, 760, 100)
    s.arrow(625, 142, 625, 230)
    s.arrow(530, 262, 490, 262)
    s.arrow(360, 262, 320, 262)
    s.arrowpath([(255, 230), (255, 162), (330, 162), (330, 130)])
    s.arrow(425, 230, 425, 128)
    s.text(436, 200, "próxima dirección", size=9.5, color="#4b5563")
    s.text(436, 214, "(μPC ← …)", size=9.5, family=MONO, color="#4b5563")
    s.note(20, 330, [
        "El opcode NO enciende compuertas: elige (por la PLA) la dirección inicial de su microprograma en la ROM.",
        "Cada pulso se lee una microinstrucción; sus bits SON las señales de control de ese pulso.",
        "El secuenciador decide la próxima dirección: +1 (secuencia), la del SR (retorno) o la de un salto condicional.",
        "Microinstrucción del 8088: fuente 5 · destino 5 · tipo 3 · ALU 4 · registro 3 · condición 1 = 21 bits.",
    ], size=10.4, lh=17)
    s.save("uc_microprogramada.svg")


def d_pipeline_aritmetico():
    """Pipeline aritmetico de 4 etapas con suma de vectores."""
    s = Svg(920, 430, "Pipeline aritmético: 4 etapas, un elemento de vector por ciclo")
    etapas = [("E1", "alineación", "de exponentes"), ("E2", "suma", "de mantisas"),
              ("E3", "normalización", "del resultado"), ("E4", "redondeo", "y escritura")]
    x = 40
    for i, (n, t, sub) in enumerate(etapas):
        s.box(x, 60, 180, 64, n + " · " + t, sub, fill=["#dbeafe", "#e0e7ff", "#dcfce7", "#fef3c7"][i])
        if i < 3:
            s.arrow(x + 180, 92, x + 210, 92)
        x += 210
    s.text(40, 152, "Cada etapa tiene su propio hardware: la suma C[i] = A[i] + B[i] puede entrar cuando la anterior ya avanzó.", size=10.4, color="#4b5563")
    # escalera
    s.text(40, 186, "Diagrama en escalera (n = 5 elementos del vector)", size=11.5, weight="700")
    x0, y0, w, h = 60, 200, 74, 26
    cols = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"]
    for j, c in enumerate(cols):
        s.text(x0 + j * w + w / 2, y0 - 6, c, size=9.5, anchor="middle", color="#4b5563")
        s.raw(f'<rect x="{x0 + j * w}" y="{y0}" width="{w}" height="{4 * h}" fill="none" stroke="#e5e7eb" stroke-width="1"/>')
    for k in range(5):
        for e in range(4):
            cx = x0 + (k + e) * w
            cy = y0 + e * h
            fill = ["#dbeafe", "#e0e7ff", "#dcfce7", "#fef3c7"][e]
            s.raw(f'<rect x="{cx + 3}" y="{cy + 3}" width="{w - 6}" height="{h - 6}" rx="3" fill="{fill}" stroke="#1f2937" stroke-width="1.1"/>')
            s.text(cx + w / 2, cy + h / 2 + 4, f"c{k+1} E{e+1}", size=8.6, anchor="middle")
    s.text(x0, y0 + 4 * h + 18, "El primer resultado sale en el ciclo 4; desde ahí, uno por ciclo ⇒ 4 + (5 − 1) = 8 ciclos para 5 elementos (en serie serían 20).", size=10.4, color="#4b5563")
    s.raw(f'<rect x="40" y="356" width="840" height="54" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(56, 378, "sin pipeline: k · n     ·     con pipeline: k + (n − 1)     ·     speedup = k·n / (k + n − 1) → k", size=11, family=MONO, weight="600", color="#7c2d12")
    s.text(56, 398, "La latencia de UNA operación no baja (sigue siendo 4 ciclos). Lo que sube es el rendimiento: elementos por unidad de tiempo.", size=10.2, color="#4b5563")
    s.save("pipeline_aritmetico.svg")


def d_memoria_entrelazada():
    """Memoria entrelazada: direcciones consecutivas en bancos distintos."""
    s = Svg(900, 420, "Memoria entrelazada: las direcciones consecutivas caen en bancos distintos")
    s.box(30, 70, 150, 50, "dirección", "d = 0, 1, 2, …", fill="#e0e7ff")
    s.text(30, 150, "d mod 4 ⇒ banco", size=10.2, family=MONO, color="#4b5563")
    bx = [240, 400, 560, 720]
    for b in range(4):
        s.box(bx[b], 60, 140, 46, f"banco {b}", "su propio bus", fill="#dbeafe")
    for d in range(12):
        b = d % 4
        y = 130 + (d // 4) * 34
        s.raw(f'<rect x="{bx[b] + 10}" y="{y}" width="120" height="26" rx="3" fill="#f8fafc" stroke="#1f2937" stroke-width="1"/>')
        s.text(bx[b] + 70, y + 17, f"dir {d}", size=9.6, anchor="middle", family=MONO)
    s.wire([(180, 95), (215, 95), (215, 40), (790, 40)])
    for cx in (310, 470, 630, 790):
        s.arrow(cx, 40, cx, 58)
    s.text(222, 300, "un acceso por banco, en el MISMO ciclo", size=10.2, color=ACCENT, weight="600")
    s.raw(f'<rect x="30" y="330" width="840" height="72" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(46, 352, "Sin entrelazar: 4 palabras en serie = 4 × t.   Entrelazada: las 4 salen a la vez = 1 × t  ⇒  4× ancho de banda.", size=10.6, weight="600")
    s.text(46, 374, "ancho de banda = (nº de bancos × bytes por palabra) / tiempo de ciclo     ·     ej.: 4 bancos × 8 B / 10 ns = 3,2 GB/s", size=10.4, family=MONO, color="#7c2d12")
    s.text(46, 392, "Ojo: si el paso (stride) es múltiplo del nº de bancos, todas las direcciones caen en el mismo banco ⇒ conflicto y no hay ganancia.", size=10.2, color="#b91c1c")
    s.save("memoria_entrelazada.svg")


def d_flynn():
    """Clasificacion de Flynn en 2x2."""
    s = Svg(840, 420, "Clasificación de Flynn: cuántos flujos de instrucciones y cuántos de datos")
    s.text(200, 62, "1 instrucción", size=11, weight="700", anchor="middle", color=ACCENT)
    s.text(520, 62, "muchas instrucciones", size=11, weight="700", anchor="middle", color=ACCENT)
    s.text(96, 190, "1 dato", size=11, weight="700", anchor="middle", color=ACCENT)
    s.text(96, 330, "muchos", size=11, weight="700", anchor="middle", color=ACCENT)
    celdas = [(200, 80, "SISD", "CPU escalar · BLUE", "#dbeafe"),
              (520, 80, "MISD", "casi no existe (tolerancia a fallas)", "#f3f4f6"),
              (200, 230, "SIMD", "vectorial · GPU · SSE/AVX", "#dcfce7"),
              (520, 230, "MIMD", "multicore · clústeres", "#fef3c7")]
    for x, y, t, sub, col in celdas:
        s.box(x, y, 250, 110, t, sub, fill=col)
    s.note(200, 372, ["La unidad 8 vive en la fila de abajo: SIMD (paralelismo de datos) y MIMD (varios flujos).",
                      "El pipeline de la unidad 7 no aparece en Flynn: es paralelismo temporal DENTRO de un flujo SISD."], size=10.3, lh=17)
    s.save("flynn.svg")


def d_sumador_cla():
    """Acarreo anticipado: G y P, y el retardo frente al ripple carry."""
    s = Svg(920, 470, "Acarreo anticipado: G = A·B, P = A⊕B, C(i+1) = G + P·C(i)")
    s.text(40, 58, "Del acarreo en cadena al acarreo anticipado", size=12.5, weight="700")
    # ripple
    s.text(40, 86, "RIPPLE CARRY: el acarreo atraviesa 4 etapas", size=10.6, weight="600", color="#b91c1c")
    for k in range(4):
        x = 40 + k * 200
        s.box(x, 96, 150, 56, f"FA {k}", "espera el acarreo", fill="#fee2e2")
        if k < 3:
            s.arrow(x + 150, 124, x + 190, 124)
            s.text(x + 170, 116, "C", size=8.5, anchor="middle", color="#b91c1c")
    s.text(40, 172, "retardo total ≈ 4 × (retardo del FA) = 8 niveles de compuerta", size=10, color="#4b5563")
    # cla
    s.text(40, 208, "ACARREO ANTICIPADO: todos los acarreos se calculan a la vez", size=10.6, weight="600", color="#15803d")
    s.box(40, 220, 200, 92, "G(i) = A(i) · B(i)", "genera acarreo", fill="#dcfce7")
    s.box(280, 220, 200, 92, "P(i) = A(i) ⊕ B(i)", "propaga acarreo", fill="#dcfce7")
    s.box(520, 220, 360, 92, "C(i+1) = G(i) + P(i) · C(i)", "con 2 niveles por acarreo", fill="#fef3c7")
    s.arrow(240, 266, 280, 266)
    s.arrow(480, 266, 520, 266)
    # ecuaciones
    s.raw(f'<rect x="40" y="330" width="840" height="122" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(56, 352, "Desarrollo para 4 bits (C0 = acarreo de entrada):", size=10.4, weight="600")
    s.text(56, 374, "C1 = G0 + P0·C0", size=10.6, family=MONO)
    s.text(56, 394, "C2 = G1 + P1·G0 + P1·P0·C0", size=10.6, family=MONO)
    s.text(56, 414, "C3 = G2 + P2·G1 + P2·P1·G0 + P2·P1·P0·C0", size=10.6, family=MONO)
    s.text(56, 434, "C4 = G3 + P3·G2 + P3·P2·G1 + P3·P2·P1·G0 + P3·P2·P1·P0·C0", size=10.6, family=MONO, color=RED)
    s.text(600, 374, "Suma: S(i) = P(i) ⊕ C(i)", size=10.4, family=MONO, color=ACCENT)
    s.text(600, 398, "Cascada en bloques de 4:", size=10.4, weight="600")
    s.text(600, 418, "cada bloque calcula su G* y P*", size=10.2, color="#4b5563")
    s.text(600, 436, "y se pasa el acarreo de grupo", size=10.2, color="#4b5563")
    s.save("sumador_acarreo_anticipado.svg")


def d_arreglo_multiplicador():
    """Multiplicador de arreglo: productos parciales sumados en una matriz de FA."""
    s = Svg(860, 470, "Multiplicador de arreglo: n² celdas suman todos los productos parciales a la vez")
    s.text(40, 58, "4 × 4: cada fila es un producto parcial; cada celda es un sumador completo", size=11, weight="600")
    x0, y0, w, h = 130, 90, 130, 52
    etiquetas = ["PP0 = M·b0", "PP1 = M·b1", "PP2 = M·b2", "PP3 = M·b3"]
    for k in range(4):
        y = y0 + k * (h + 14)
        s.text(40, y + 30, etiquetas[k], size=9.8, family=MONO, color="#7c2d12")
        for j in range(4):
            x = x0 + j * w
            s.raw(f'<rect x="{x}" y="{y}" width="{w - 10}" height="{h}" rx="4" fill="#dbeafe" stroke="#1f2937" stroke-width="1.3"/>')
            s.text(x + (w - 10) / 2, y + 22, f"a{k}{j}", size=9.4, anchor="middle", family=MONO)
            s.text(x + (w - 10) / 2, y + 38, "+", size=11, anchor="middle", weight="700", color="#15803d")
    s.raw(f'<rect x="40" y="356" width="780" height="94" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(56, 376, "Cada 'a' es un sumador completo (o un sumador con acarreo guardado: carry-save).", size=10.2, color="#374151")
    s.text(56, 398, "Ventaja: es COMBINACIONAL — el producto aparece en el retardo de la matriz (≈ 2n niveles), sin reloj ni ciclos.", size=10.4, weight="600")
    s.text(56, 420, "Costo: n² celdas (un multiplicador de 32 × 32 pide 1024 sumadores) y muchísimos transistores.", size=10.4, color="#4b5563")
    s.text(56, 440, "Alternativa secuencial: sumas y desplazamientos ⇒ n ciclos de reloj, pero con un solo sumador.", size=10.4, color="#4b5563")
    s.save("arreglo_multiplicador.svg")


if __name__ == "__main__":
    d_semisumador()
    d_sumador_completo()
    d_decodificador_2x4()
    d_decodificador_3x8()
    d_mux_4x1()
    d_demux_1x4()
    d_estructura_basica()
    d_ram_8x3()
    d_jerarquia()
    d_flipflops()
    d_pipeline()
    d_formatos()
    d_modos()
    d_lda24()
    d_blue_flujo()
    d_ciclo_maquina()
    d_cache()
    d_cisc_risc()
    d_hazards()
    d_compuertas()
    d_codificador_8x3()
    d_karnaugh_3var()
    d_uc_cableada()
    d_uc_microprogramada()
    d_pipeline_aritmetico()
    d_memoria_entrelazada()
    d_flynn()
    d_sumador_cla()
    d_arreglo_multiplicador()
