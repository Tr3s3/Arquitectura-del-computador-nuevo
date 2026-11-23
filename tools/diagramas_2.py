#!/usr/bin/env python3
"""
Diagramas de la segunda tanda (cobertura de subtemas que no tenían gráfico).
Usa el mismo API que diagramas.py.
    python3 diagramas_2.py            # todos
    python3 diagramas_2.py a b c      # sólo los que se nombren (sin .svg)
"""
import sys
from diagramas import Svg, ACCENT, RED, MONO, STROKE


# ══════════════════════════ UNIDAD 1 ══════════════════════════
def d_compuertas_nand_nor_xor():
    s = Svg(960, 400, "NAND, NOR, XOR y XNOR: símbolo, ecuación y tabla")
    specs = [
        ("NAND", "Y = (A · B)'", ["A B | Y", "0 0 | 1", "0 1 | 1", "1 0 | 1", "1 1 | 0"],
         "AND negada: sale 0 sólo con todo 1"),
        ("NOR", "Y = (A + B)'", ["A B | Y", "0 0 | 1", "0 1 | 0", "1 0 | 0", "1 1 | 0"],
         "OR negada: sale 1 sólo con todo 0"),
        ("XOR", "Y = A ⊕ B", ["A B | Y", "0 0 | 0", "0 1 | 1", "1 0 | 1", "1 1 | 0"],
         "1 si son distintos (paridad impar)"),
        ("XNOR", "Y = (A ⊕ B)'", ["A B | Y", "0 0 | 1", "0 1 | 0", "1 0 | 0", "1 1 | 1"],
         "1 si son iguales (comparador)"),
    ]
    for k, (nom, eq, tabla, nota) in enumerate(specs):
        x = 24 + k * 235
        s.raw(f'<rect x="{x}" y="44" width="222" height="286" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
        s.text(x + 12, 66, nom, size=13, weight="700", color=ACCENT)
        s.gate(nom, x + 52, 78, ["A", "B"], "Y", w=64, h=46, stub=26)
        s.text(x + 12, 152, eq, size=11.5, weight="700", family=MONO, color="#0f766e")
        for i, r in enumerate(tabla):
            s.text(x + 12, 178 + i * 18, r, size=10.2, weight="700" if i == 0 else "400",
                   family=MONO if i else None)
        s.text(x + 12, 292, nota, size=9.4, color="#4b5563")
    s.text(24, 356, "Las cuatro son de 2 entradas y una salida. NAND y NOR son universales (con ellas se arma cualquier función);", size=10.2)
    s.text(24, 376, "XOR y XNOR son imprescindibles para sumar (S = A⊕B⊕Cin) y para comparar si dos palabras son iguales.", size=10.2, color="#4b5563")
    s.save("compuertas_nand_nor_xor.svg")


def d_nand_universal():
    s = Svg(940, 430, "NAND como compuerta universal: NOT, AND, OR y XOR armados sólo con NAND")
    # 1 NOT
    s.text(30, 52, "1 · NOT con NAND", size=11, weight="700")
    s.gate("NAND", 60, 66, ["A", "A"], "A'", w=66, h=46, stub=28)
    s.text(30, 140, "Uniendo las dos entradas:", size=9.6, color="#4b5563")
    s.text(30, 156, "(A·A)' = A' ⇒ inversor.", size=9.6, color="#4b5563")
    # 2 AND
    s.text(330, 52, "2 · AND = dos NAND", size=11, weight="700")
    s.gate("NAND", 348, 66, ["A", "B"], "N1", w=58, h=46, stub=20)
    s.gate("NAND", 496, 66, ["N1", "N1"], "A·B", w=56, h=46, stub=12)
    s.text(330, 140, "La primera da (A·B)' y la segunda", size=9.6, color="#4b5563")
    s.text(330, 156, "lo invierte: A·B.", size=9.6, color="#4b5563")
    # 3 OR
    s.text(660, 52, "3 · OR = NAND de negados", size=11, weight="700")
    s.gate("NAND", 700, 66, ["A'", "B'"], "A + B", w=64, h=46, stub=24)
    s.text(660, 140, "DeMorgan: (A'·B')' = A + B.", size=9.6, color="#4b5563")
    s.text(660, 156, "Necesita dos inversores.", size=9.6, color="#4b5563")
    # 4 XOR
    s.raw('<rect x="24" y="186" width="892" height="228" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 212, "4 · XOR con 4 NAND (el circuito que se pregunta)", size=11, weight="700")
    s.gate("NAND", 60, 260, ["A", "B"], "N1", w=64, h=46, stub=24)
    s.gate("NAND", 250, 232, ["A", "N1"], "N2", w=62, h=46, stub=24)
    s.gate("NAND", 250, 312, ["N1", "B"], "N3", w=62, h=46, stub=24)
    s.gate("NAND", 440, 272, ["N2", "N3"], "A ⊕ B", w=66, h=48, stub=22)
    s.text(612, 254, "N1 = (A·B)'", size=10.4, family=MONO, color="#7c2d12")
    s.text(612, 276, "N2 = (A·N1)' = A' + A·B", size=10.4, family=MONO, color="#7c2d12")
    s.text(612, 298, "N3 = (N1·B)' = A·B' + B'", size=10.4, family=MONO, color="#7c2d12")
    s.text(612, 320, "salida = (N2·N3)' = A·B' + A'·B = A ⊕ B", size=10.4, family=MONO, weight="700", color="#0f766e")
    s.text(40, 372, "Las entradas N1, N2 y N3 son nombres de señales: no hace falta dibujar cada cable, basta con escribir el nombre.", size=9.8, color="#4b5563")
    s.text(40, 392, "Un XOR cuesta 4 compuertas (4 NAND o 4 NOR): ése es el argumento de 'universal' — un solo tipo de chip arma todo.", size=9.8, color="#4b5563")
    s.save("nand_universal.svg")

def d_demorgan_circuitos():
    s = Svg(940, 420, "DeMorgan dibujado:  (A·B)' = A' + B'   y   (A+B)' = A'·B'")
    # ---- primera ley
    s.raw('<rect x="24" y="40" width="892" height="170" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 64, "Primera ley: NAND = OR de los negados", size=11, weight="700")
    s.gate("NAND", 60, 84, ["A", "B"], "(A·B)'", w=70, h=48, stub=26)
    s.text(216, 114, "≡", size=20, weight="700", color=ACCENT)
    s.gate("NOT", 252, 78, ["A"], "", w=44, h=36, stub=16, isize=10)
    s.gate("NOT", 252, 128, ["B"], "", w=44, h=36, stub=16, isize=10)
    s.gate("OR", 366, 92, ["A'", "B'"], "A' + B'", w=74, h=50, stub=20)
    s.text(520, 96, "A B | (A·B)' | A' + B'", size=9.8, family=MONO, weight="700")
    for i, (a, b) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
        nand = 0 if (a and b) else 1
        orn = (0 if a else 1) or (0 if b else 1)
        s.text(520, 114 + i * 16, f" {a} {b} |    {nand}    |    {int(orn)}", size=9.8, family=MONO)
    s.text(680, 150, "Las dos columnas son iguales:", size=9.6, color="#4b5563")
    s.text(680, 166, "misma tabla, mismas compuertas.", size=9.6, color="#4b5563")
    # ---- segunda ley
    s.raw('<rect x="24" y="224" width="892" height="150" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 248, "Segunda ley: NOR = AND de los negados", size=11, weight="700")
    s.gate("NOR", 60, 266, ["A", "B"], "(A+B)'", w=70, h=48, stub=26)
    s.text(216, 296, "≡", size=20, weight="700", color=ACCENT)
    s.gate("NOT", 252, 260, ["A"], "", w=44, h=36, stub=16, isize=10)
    s.gate("NOT", 252, 310, ["B"], "", w=44, h=36, stub=16, isize=10)
    s.gate("AND", 366, 274, ["A'", "B'"], "A' · B'", w=74, h=50, stub=20)
    s.text(520, 278, "A B | (A+B)' | A' · B'", size=9.8, family=MONO, weight="700")
    for i, (a, b) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
        nor = 0 if (a or b) else 1
        andn = (0 if a else 1) and (0 if b else 1)
        s.text(520, 296 + i * 16, f" {a} {b} |    {nor}    |    {int(andn)}", size=9.8, family=MONO)
    s.text(24, 396, "Regla para simplificar sin equivocarse: al negar cambia AND↔OR y se niega cada término (también los literales sueltos).", size=10.2, color="#7c2d12")
    s.save("demorgan_circuitos.svg")

def d_simplificacion_compuertas():
    s = Svg(940, 420, "Simplificar es sacar compuertas: la misma función con menos hardware")
    s.text(24, 52, "Sin simplificar:  Y = A'·B·C + A·B·C + A·B·C'", size=11.5, weight="700", family=MONO)
    for k, (lab, ins) in enumerate([("p1", ["A'", "B", "C"]), ("p2", ["A", "B", "C"]), ("p3", ["A", "B", "C'"])]):
        s.gate("AND", 50 + k * 165, 72, ins, lab, w=64, h=56, stub=18, isize=10)
    s.gate("OR", 560, 84, ["", "", ""], "Y", w=74, h=76, stub=22, isize=10)
    s.text(680, 104, "p1 = A'BC   p2 = ABC   p3 = ABC'", size=10, family=MONO, color="#7c2d12")
    s.text(680, 128, "3 AND de 3 entradas + 1 OR de 3 + 2 NOT", size=9.6, color=RED)
    s.text(680, 146, "⇒ 14 compuertas", size=9.6, weight="700", color=RED)
    s.text(24, 200, "Simplificada:  Y = B·C + A·B", size=11.5, weight="700", family=MONO)
    s.gate("AND", 100, 232, ["B", "C"], "B·C", w=64, h=48, stub=22)
    s.gate("AND", 100, 306, ["A", "B"], "A·B", w=64, h=48, stub=22)
    s.gate("OR", 320, 254, ["", ""], "Y", w=74, h=64, stub=22)
    s.text(460, 240, "Y = B·C + A·B", size=12, weight="700", family=MONO, color="#0f766e")
    s.text(460, 264, "3 compuertas de 2 entradas ⇒ 1 circuito integrado", size=9.8, color="#15803d")
    s.text(460, 288, "La función es la MISMA: la tabla de verdad no cambia.", size=9.8, color="#4b5563")
    s.text(460, 312, "Chequeo: A=1,B=1 ⇒ Y=1 · A=0,B=1,C=1 ⇒ Y=1 · A=1,B=0 ⇒ Y=0.", size=9.6, color="#4b5563")
    s.text(24, 384, "Simplificar no cambia qué hace el circuito: cambia su costo (compuertas, retardos, consumo y tamaño del chip).", size=10.2)
    s.text(24, 406, "El Karnaugh es el método sistemático para llegar a esta versión; la simplificación analítica usa postulados y DeMorgan.", size=10.2, color="#4b5563")
    s.save("simplificacion_compuertas.svg")

def d_mintterminos_canonica():
    s = Svg(940, 430, "De la tabla de verdad al circuito canónico (suma de mintérminos)")
    s.text(30, 54, "Tabla de verdad", size=11, weight="700")
    filas = ["A B C | Y", "0 0 0 | 0", "0 0 1 | 1", "0 1 0 | 1", "0 1 1 | 0",
             "1 0 0 | 0", "1 0 1 | 1", "1 1 0 | 0", "1 1 1 | 1"]
    for i, r in enumerate(filas):
        s.text(30, 78 + i * 17, r, size=10, family=MONO, weight="700" if i == 0 else "400")
    s.text(160, 95, "m1 = A'·B'·C", size=10, family=MONO, color=RED)
    s.text(160, 112, "m2 = A'·B·C'", size=10, family=MONO, color=RED)
    s.text(160, 146, "m5 = A·B'·C", size=10, family=MONO, color=RED)
    s.text(160, 180, "m7 = A·B·C", size=10, family=MONO, color=RED)
    s.text(30, 232, "Y = Σm(1, 2, 5, 7)", size=12, weight="700", family=MONO, color="#7c2d12")
    s.text(30, 258, "Cada 1 de la salida es un mintérmino:", size=9.6, color="#4b5563")
    s.text(30, 274, "un AND con TODAS las variables", size=9.6, color="#4b5563")
    s.text(30, 290, "(la que vale 0 va negada).", size=9.6, color="#4b5563")
    s.text(30, 316, "Cada 0 es un maxtérmino (una OR).", size=9.6, color="#4b5563")
    s.raw('<rect x="404" y="44" width="512" height="330" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(420, 66, "Circuito canónico: 4 AND de 3 entradas + 1 OR de 4", size=10.6, weight="700")
    for k, (lab, a, b, c) in enumerate([("m1", "A'", "B'", "C"), ("m2", "A'", "B", "C'"),
                                        ("m5", "A", "B'", "C"), ("m7", "A", "B", "C")]):
        s.gate("AND", 424, 86 + k * 62, [a, b, c], lab, w=60, h=50, stub=16, isize=9.4)
    s.gate("OR", 600, 110, ["", "", "", ""], "Y", w=70, h=104, stub=20, isize=9.4)
    s.text(700, 128, "Dos niveles:", size=10.2, weight="700")
    s.text(700, 148, "AND – OR", size=10.4, weight="700", color=ACCENT)
    s.text(700, 176, "SOP = suma de", size=9.4, color="#4b5563")
    s.text(700, 192, "productos (Σm).", size=9.4, color="#4b5563")
    s.text(700, 218, "POS = producto", size=9.4, color="#4b5563")
    s.text(700, 234, "de sumas (ΠM).", size=9.4, color="#4b5563")
    s.text(700, 262, "Las entradas del OR", size=9.4, color="#4b5563")
    s.text(700, 278, "son las salidas de", size=9.4, color="#4b5563")
    s.text(700, 294, "los AND (m1…m7).", size=9.4, color="#4b5563")
    s.text(420, 348, "Es el punto de partida: nunca falla, pero gasta mucho (por eso se simplifica con Karnaugh).", size=9.6, color="#7c2d12")
    s.text(30, 392, "El índice del mintérmino es el número binario de las entradas: A=0,B=1,C=0 ⇒ 010 ⇒ m2.", size=10.2)
    s.text(30, 412, "Para 3 variables hay 8 mintérminos (m0…m7); para 4 variables, dieciséis (m0…m15).", size=10.2, color="#4b5563")
    s.save("mintterminos_canonica.svg")

def d_karnaugh_dontcare():
    s = Svg(900, 400, "Karnaugh de 4 variables con condiciones 'no importa' (don't care)")
    # mapa 4x4
    x0, y0, cw, ch = 120, 92, 92, 56
    cols = ["00", "01", "11", "10"]
    rows = ["00", "01", "11", "10"]
    s.text(x0 + cw * 2 - 30, y0 - 46, "AB", size=10.5, weight="700")
    s.text(x0 - 54, y0 + ch * 2 + 6, "CD", size=10.5, weight="700")
    for j, c in enumerate(cols):
        s.text(x0 + j * cw + cw / 2, y0 - 14, c, size=10.5, anchor="middle", weight="700")
    for i, r in enumerate(rows):
        s.text(x0 - 22, y0 + i * ch + ch / 2 + 4, r, size=10.5, anchor="middle", weight="700")
    vals = [["1", "1", "X", "0"],
            ["0", "X", "1", "1"],
            ["0", "0", "1", "1"],
            ["X", "0", "0", "0"]]
    for i in range(4):
        for j in range(4):
            x, y = x0 + j * cw, y0 + i * ch
            v = vals[i][j]
            fill = "#dcfce7" if v == "1" else ("#fef3c7" if v == "X" else "#ffffff")
            s.raw(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{fill}" stroke="{STROKE}" stroke-width="1.3"/>')
            s.text(x + cw / 2, y + ch / 2 + 6, v, size=15, anchor="middle", weight="700")
    # grupo 1: columna 11 y 10, filas 01 y 11 (cuatro 1)
    s.raw(f'<rect x="{x0+cw*2+4}" y="{y0+ch+6}" width="{cw*2-8}" height="{ch*2-12}" rx="18" fill="none" stroke="{ACCENT}" stroke-width="2.6"/>')
    # grupo 2: fila 00, columnas 00 y 01
    s.raw(f'<rect x="{x0+6}" y="{y0+6}" width="{cw*2-12}" height="{ch-12}" rx="16" fill="none" stroke="{RED}" stroke-width="2.6"/>')
    s.text(560, 104, "grupo azul (4 unos): B · C", size=11, weight="700", color=ACCENT)
    s.text(560, 128, "cuatro unos adyacentes ⇒ B·C", size=9.4, color="#4b5563")
    s.text(560, 168, "grupo rojo (2 unos): A' · C'", size=11, weight="700", color=RED)
    s.text(560, 192, "dos unos adyacentes ⇒ A'·C'", size=9.4, color="#4b5563")
    s.text(560, 232, "Y = B·C + A'·C'", size=12.5, weight="700", family=MONO, color="#0f766e")
    s.text(560, 256, "Sin usar los X: Y = B·C + A'·C'·D' … más términos", size=9.4, color="#4b5563")
    s.raw('<rect x="24" y="330" width="852" height="52" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 352, "Reglas del don't care: X se puede usar como 1 (si agranda un grupo) o como 0 (si no conviene) — nunca es obligatorio.", size=10)
    s.text(40, 372, "Grupos de 1, 2, 4, 8 (potencias de 2) · lo más grandes posible · pueden cruzar bordes · todos los 1 deben quedar cubiertos.", size=10, color="#4b5563")
    s.save("karnaugh_dontcare.svg")


def d_sumador_n_bits():
    s = Svg(950, 420, "Sumador de n bits en cascada, la resta A + B' + 1 y la bandera V")
    s.text(28, 52, "Sumador de 4 bits (acarreo en cascada): el Cout de cada etapa es el Cin de la siguiente", size=10.6, weight="700")
    for k in range(4):
        x = 40 + k * 205
        s.box(x, 70, 150, 96, "", "", fill="#dbeafe")
        s.text(x + 75, 92, f"SUMADOR", size=9.4, anchor="middle", color="#4b5563")
        s.text(x + 75, 106, f"completo {k}", size=9.4, anchor="middle", color="#4b5563")
        s.text(x + 14, 134, f"A{k}  B{k}", size=10.5, weight="700", family=MONO)
        s.text(x + 14, 152, f"Cin", size=9.6, family=MONO, color="#4b5563")
        s.text(x + 150 - 14, 134, f"S{k}", size=10.5, anchor="end", weight="700", family=MONO, color=ACCENT)
        s.text(x + 150 - 14, 152, f"Cout", size=9.6, anchor="end", family=MONO, color=RED)
        if k < 3:
            s.arrow(x + 150, 148, x + 200, 148, color=RED)
    s.arrow(34, 148, 36, 148)
    s.text(14, 136, "C0", size=9.6, family=MONO, color="#4b5563")
    s.arrow(40 + 3 * 205 + 150, 148, 40 + 3 * 205 + 196, 148, color=RED)
    s.text(40 + 3 * 205 + 198, 152, "C4", size=9.6, family=MONO, color=RED)
    s.text(28, 196, "C4 = acarreo de salida (bandera C).  Con 4 sumadores: 4 bits, retardo ≈ 4 × 2 compuertas de acarreo.", size=9.8, color="#4b5563")
    s.raw('<rect x="24" y="216" width="902" height="128" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 240, "La resta como suma:  A − B = A + B' + 1   (complemento a 2)", size=10.8, weight="700", family=MONO)
    s.text(40, 262, "B' = complemento bit a bit (4 inversores)   ·   el +1 entra como C0 = 1   ·   se usa el mismo sumador", size=9.8, color="#4b5563")
    s.text(40, 284, "Ejemplo: 9 − 5 = 1001 + 1010 + 1 = 1001 + 1011 = 10100 ⇒ se descarta C4 ⇒ 0100 = +4 ✓", size=10, family=MONO, color="#7c2d12")
    s.text(40, 306, "9 − 12 = 1001 + 0011 + 1 = 1001 + 0100 = 1101 = −3 (en complemento a 2) ✓   ·  el resultado negativo se lee así", size=10, family=MONO, color="#7c2d12")
    s.text(40, 330, "V (desborde) = C3 ⊕ C4: se calcula con el acarreo que ENTRA al bit de signo y el que SALE de él — nunca restando los signos.", size=9.8, color=RED)
    s.text(28, 374, "n bits en cascada: el retardo crece con n; por eso existe el acarreo anticipado (G y P), que lo calcula en paralelo.", size=10.2)
    s.text(28, 396, "Cada etapa hace S = A⊕B⊕Cin y Cout = A·B + Cin·(A⊕B). Con el mismo bloque de n etapas se suman enteros de n bits.", size=10.2, color="#4b5563")
    s.save("sumador_n_bits.svg")


# ══════════════════════════ UNIDAD 2 ══════════════════════════
def d_flipflop_d_t_tiempos():
    s = Svg(920, 410, "Flip-flop D y flip-flop T: ecuación, tabla y formas de onda")
    # D
    s.raw('<rect x="24" y="42" width="424" height="300" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 66, "Flip-flop D (dato)", size=11.5, weight="700", color=ACCENT)
    s.raw('<rect x="56" y="84" width="120" height="80" rx="6" fill="#ffffff" stroke="#1f2937" stroke-width="1.8"/>')
    s.text(116, 106, "D", size=12, weight="700", anchor="middle")
    s.line(40, 130, 56, 130); s.text(44, 124, "D", size=10, weight="700")
    s.raw('<path d="M56,140 l10,6 l-10,6" fill="none" stroke="#1f2937" stroke-width="1.3"/>')
    s.text(46, 160, "C", size=9.5, weight="700")
    s.line(176, 112, 196, 112); s.text(200, 116, "Q", size=11, weight="700")
    s.line(176, 140, 196, 140); s.text(200, 144, "Q'", size=10)
    s.text(40, 192, "Q(t+1) = D", size=12, weight="700", family=MONO, color="#0f766e")
    s.text(40, 216, "D C | Q(t+1)", size=10, family=MONO, weight="700")
    s.text(40, 234, "0 ↑ |   0", size=10, family=MONO)
    s.text(40, 250, "1 ↑ |   1", size=10, family=MONO)
    s.text(40, 266, "x 0 |   Q (mantiene)", size=10, family=MONO)
    s.text(216, 216, "Es el único que NO tiene", size=9.6, color="#4b5563")
    s.text(216, 232, "estado prohibido: la salida", size=9.6, color="#4b5563")
    s.text(216, 248, "copia la entrada en el flanco.", size=9.6, color="#4b5563")
    s.text(40, 300, "Aplicaciones: registro, memoria, D = J = K'… es el biestable de la cátedra.", size=9.6, color="#4b5563")
    # T
    s.raw('<rect x="470" y="42" width="426" height="300" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(486, 66, "Flip-flop T (toggle)", size=11.5, weight="700", color=ACCENT)
    s.raw('<rect x="502" y="84" width="120" height="80" rx="6" fill="#ffffff" stroke="#1f2937" stroke-width="1.8"/>')
    s.text(562, 106, "T", size=12, weight="700", anchor="middle")
    s.line(486, 130, 502, 130); s.text(490, 124, "T", size=10, weight="700")
    s.raw('<path d="M502,140 l10,6 l-10,6" fill="none" stroke="#1f2937" stroke-width="1.3"/>')
    s.text(492, 160, "C", size=9.5, weight="700")
    s.line(622, 112, 642, 112); s.text(646, 116, "Q", size=11, weight="700")
    s.line(622, 140, 642, 140); s.text(646, 144, "Q'", size=10)
    s.text(486, 192, "Q(t+1) = T ⊕ Q", size=12, weight="700", family=MONO, color="#0f766e")
    s.text(486, 216, "T C | Q(t+1)", size=10, family=MONO, weight="700")
    s.text(486, 234, "0 ↑ | Q (mantiene)", size=10, family=MONO)
    s.text(486, 250, "1 ↑ | Q' (conmuta)", size=10, family=MONO)
    s.text(660, 216, "Con T = 1 siempre:", size=9.6, color="#4b5563")
    s.text(660, 232, "divide la frecuencia", size=9.6, color="#4b5563")
    s.text(660, 248, "del reloj a la mitad.", size=9.6, color="#4b5563")
    s.text(486, 300, "Aplicaciones: contadores (T = 1 en la primera etapa) y divisores de frecuencia.", size=9.6, color="#4b5563")
    s.text(24, 372, "Los dos son disparados por flanco: Q cambia sólo en el instante del pulso de reloj, no mientras el reloj está en 1.", size=10.2)
    s.text(24, 392, "D = 'dato' (se usa para almacenar) · T = 'toggle' (se usa para contar). Con D se arma un registro; con T, un contador.", size=10.2, color="#4b5563")
    s.save("flipflop_d_t_tiempos.svg")


def d_flipflop_jk_ecuaciones():
    s = Svg(900, 400, "Flip-flop J-K: tabla, ecuación característica y conversión a D y a T")
    s.raw('<rect x="24" y="42" width="380" height="300" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 66, "J-K: el que resuelve el estado prohibido", size=11, weight="700")
    s.raw('<rect x="70" y="86" width="130" height="96" rx="6" fill="#ffffff" stroke="#1f2937" stroke-width="1.8"/>')
    s.text(135, 116, "J-K", size=13, weight="700", anchor="middle")
    s.line(52, 108, 70, 108); s.text(56, 102, "J", size=10.5, weight="700")
    s.line(52, 146, 70, 146); s.text(56, 162, "K", size=10.5, weight="700")
    s.raw('<path d="M70,152 l10,6 l-10,6" fill="none" stroke="#1f2937" stroke-width="1.3"/>')
    s.text(60, 172, "C", size=9.5, weight="700")
    s.line(200, 112, 220, 112); s.text(224, 116, "Q", size=11, weight="700")
    s.line(200, 156, 220, 156); s.text(224, 160, "Q'", size=10)
    s.text(40, 216, "J C K | Q(t+1)", size=10, family=MONO, weight="700")
    for i, t in enumerate(["0 ↑ 0 | Q   (mantiene)", "1 ↑ 0 | 1   (set)", "0 ↑ 1 | 0   (reset)", "1 ↑ 1 | Q'  (conmuta)"]):
        s.text(40, 236 + i * 17, t, size=10, family=MONO)
    s.text(40, 318, "Con J = K = 1 ya no hay prohibido: conmuta.", size=9.6, color="#4b5563")
    # ecuación + conversiones
    s.raw('<rect x="426" y="42" width="450" height="300" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(442, 66, "Ecuación característica", size=11, weight="700")
    s.text(442, 92, "Q(t+1) = J·Q' + K'·Q", size=13, weight="700", family=MONO, color="#0f766e")
    s.text(442, 116, "Se deduce de la tabla: mantiene con 00, pone con 10,", size=9.6, color="#4b5563")
    s.text(442, 132, "borra con 01 y conmuta con 11.", size=9.6, color="#4b5563")
    s.text(442, 164, "Tabla de excitación (para diseñar):", size=10.4, weight="700")
    s.text(442, 184, "Q → Q(t+1) | J K", size=10, family=MONO, weight="700")
    s.text(442, 202, "0 → 0    | 0 x", size=10, family=MONO)
    s.text(442, 218, "0 → 1    | 1 x", size=10, family=MONO)
    s.text(442, 234, "1 → 0    | x 1", size=10, family=MONO)
    s.text(442, 250, "1 → 1    | x 0", size=10, family=MONO)
    s.text(600, 184, "J-K → D:  J = D,  K = D'", size=10.4, family=MONO, color="#7c2d12")
    s.text(600, 202, "J-K → T:  J = K = T", size=10.4, family=MONO, color="#7c2d12")
    s.text(600, 226, "Chequeo con D: J·Q' + K'·Q", size=9.6, color="#4b5563")
    s.text(600, 242, "= D·Q' + D·Q = D ✓", size=9.6, color="#4b5563", family=MONO)
    s.text(442, 288, "Un J-K con J = K = T se comporta como T; con J = D y K = D',", size=9.6, color="#4b5563")
    s.text(442, 304, "como D. Por eso el J-K es el biestable 'general'.", size=9.6, color="#4b5563")
    s.text(24, 372, "El J-K es el único que aprovecha el caso 1-1 en vez de prohibirlo: en ese caso la salida conmuta.", size=10.2)
    s.save("flipflop_jk_ecuaciones.svg")


def d_registros_pipo_siso():
    s = Svg(920, 420, "Registro PIPO (paralelo) y registro SISO (desplazamiento)")
    s.text(24, 50, "PIPO: Parallel In – Parallel Out · los n bits entran y salen a la vez", size=10.8, weight="700")
    for k in range(4):
        x = 70 + k * 150
        s.raw(f'<rect x="{x}" y="100" width="90" height="70" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.7"/>')
        s.text(x + 45, 138, f"FF{k}", size=11, weight="700", anchor="middle")
        s.arrow(x + 45, 82, x + 45, 98)
        s.text(x + 45, 76, f"D{k}", size=9.6, anchor="middle", weight="700")
        s.line(x + 90, 126, x + 132, 126); s.text(x + 136, 130, f"Q{k}", size=9.6, weight="700", color=ACCENT)
    s.line(70, 190, 550, 190, color=RED, w=1.8)
    s.text(556, 194, "CLK (común a todos)", size=9.6, color=RED)
    s.text(24, 222, "En un solo pulso los 4 bits se cargan o se leen juntos: es la memoria de trabajo más rápida (un registro).", size=9.8, color="#4b5563")
    s.text(24, 242, "SISO: Serial In – Serial Out · el dato entra por un extremo y sale por el otro, un bit por pulso", size=10.8, weight="700")
    for k in range(4):
        x = 70 + k * 150
        s.raw(f'<rect x="{x}" y="272" width="90" height="70" rx="5" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.7"/>')
        s.text(x + 45, 312, f"FF{k}", size=11, weight="700", anchor="middle")
        if k:
            s.arrow(x - 60, 306, x - 2, 306)
    s.arrow(8, 306, 68, 306)
    s.text(8, 296, "entrada", size=8.8, weight="700", color=RED)
    s.text(8, 324, "serie", size=8.8, weight="700", color=RED)
    s.line(700, 306, 742, 306); s.text(746, 310, "salida serie", size=9.4, weight="700", color=ACCENT)
    s.line(70, 362, 550, 362, color=RED, w=1.8); s.text(556, 366, "CLK (común)", size=9.6, color=RED)
    s.text(24, 392, "Cada pulso corre un bit: el dato tarda n pulsos en atravesar el registro (lento, pero con 2 cables en vez de n).", size=9.8, color="#4b5563")
    s.text(24, 412, "Con la salida del último FF realimentada a la entrada se arma un registro circular (rotación).", size=9.8, color="#4b5563")
    s.save("registros_pipo_siso.svg")
def d_registros_sipo_piso():
    s = Svg(920, 420, "Registro SIPO (serie → paralelo) y PISO (paralelo → serie)")
    s.text(24, 50, "SIPO: entra bit a bit, sale todo junto — el receptor de un enlace serie", size=10.8, weight="700")
    for k in range(4):
        x = 70 + k * 150
        s.raw(f'<rect x="{x}" y="80" width="88" height="64" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.7"/>')
        s.text(x + 44, 116, f"FF{k}", size=10.5, weight="700", anchor="middle")
        s.arrow(x + 44, 146, x + 44, 166)
        s.text(x + 44, 182, f"Q{k}", size=9.6, anchor="middle", weight="700", color=ACCENT)
        if k:
            s.arrow(x - 60, 110, x - 2, 110)
    s.arrow(8, 110, 68, 110)
    s.text(8, 100, "entrada", size=8.8, weight="700", color=RED)
    s.text(8, 128, "serie", size=8.8, weight="700", color=RED)
    s.text(24, 206, "Después de 4 pulsos los 4 bits están en paralelo: eso hace la UART cuando recibe un byte.", size=9.8, color="#4b5563")
    s.text(24, 232, "PISO: entra todo junto, sale bit a bit — el transmisor", size=10.8, weight="700")
    for k in range(4):
        x = 70 + k * 150
        s.raw(f'<rect x="{x}" y="286" width="88" height="64" rx="5" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.7"/>')
        s.text(x + 44, 322, f"FF{k}", size=10.5, weight="700", anchor="middle")
        s.arrow(x + 44, 268, x + 44, 284)
        s.text(x + 44, 262, f"D{k}", size=9.2, anchor="middle", weight="700")
        if k:
            s.arrow(x - 60, 316, x - 2, 316)
    s.line(700, 316, 742, 316); s.text(746, 320, "salida serie", size=9.4, weight="700", color=ACCENT)
    s.text(24, 374, "Primero se carga el byte (LOAD en paralelo) y después se desplaza: un bit por pulso hacia la salida.", size=9.8, color="#4b5563")
    s.raw('<rect x="24" y="382" width="872" height="30" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 402, "Para qué sirven: convertir entre el mundo paralelo (bus de datos) y el serie (un cable). Son la base de las UART del tema 10.4.", size=9.8)
    s.save("registros_sipo_piso.svg")
def d_contadores_modulo():
    s = Svg(920, 400, "Contadores: binario de 3 bits (módulo 8) y contador de módulo 6")
    s.text(24, 50, "Contador binario de 3 bits con flip-flops T en cascada", size=10.8, weight="700")
    for k in range(3):
        x = 60 + k * 165
        s.raw(f'<rect x="{x}" y="72" width="96" height="80" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.7"/>')
        s.text(x + 48, 106, "T", size=12, weight="700", anchor="middle")
        s.text(x + 12, 130, "T = 1", size=9, color="#4b5563")
        s.line(x + 96, 96, x + 128, 96); s.text(x + 132, 100, f"Q{k}", size=9.6, weight="700", color=ACCENT)
        if k < 2:
            s.arrow(x + 40, 166, x + 128, 166)
            s.text(x + 40, 182, "Q → reloj del siguiente", size=8.4, color=RED)
        s.line(x - 16, 130, x, 130)
        if k == 0:
            s.text(x - 20, 126, "CLK", size=9, anchor="end", color=RED)
    s.text(600, 96, "Cuenta:  000 → 001 → 010 → 011", size=9.8, family=MONO)
    s.text(600, 116, "→ 100 → 101 → 110 → 111 → 000", size=9.8, family=MONO)
    s.text(600, 140, "Módulo 8 = 2³ (tres flip-flops)", size=9.6, color="#4b5563")
    s.text(24, 206, "Cada flip-flop divide la frecuencia a la mitad: Q0 = f/2, Q1 = f/4, Q2 = f/8.", size=9.8, color="#4b5563")
    s.text(24, 240, "Contador de módulo 6: se resetea cuando llega a 110 (=6) — así cuenta 0…5", size=10.8, weight="700")
    s.raw(f'<rect x="60" y="256" width="130" height="70" rx="5" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.7"/>')
    s.text(125, 284, "contador", size=10, anchor="middle", color="#4b5563")
    s.text(125, 302, "0 a 5", size=10, anchor="middle", weight="700")
    s.gate("NAND", 250, 268, ["Q2", "Q1"], "", w=64, h=44, stub=22, isize=9.6)
    s.arrow(340, 290, 388, 290)
    s.text(392, 276, "Q2·Q1 = 1 ⟺ cuenta = 110 = 6 ⇒ el NAND manda CLEAR y vuelve a 000.", size=9.6, color="#4b5563")
    s.text(392, 296, "Así se arma cualquier módulo N: se detecta el estado N y se borra.", size=9.6, color="#4b5563")
    s.text(392, 316, "Para módulo 10 (décadas): NAND(Q3, Q1) detecta 1010.", size=9.6, color="#7c2d12")
    s.text(24, 356, "Fórmula: n flip-flops dan como máximo módulo 2ⁿ. Para módulo N se necesitan n ≥ log₂N y un circuito de reset.", size=10.2)
    s.text(24, 378, "Síncrono = todos los FF con el mismo reloj · asíncrono = la salida de uno es el reloj del siguiente (más simple, más lento).", size=9.8, color="#4b5563")
    s.save("contadores_modulo.svg")
def d_celda_memoria():
    s = Svg(920, 410, "La celda de memoria: SRAM (6 transistores) y DRAM (1 transistor + 1 capacitor)")
    s.text(24, 50, "SRAM: biestable de 2 inversores cruzados — guarda mientras haya alimentación", size=10.8, weight="700")
    s.raw(f'<rect x="70" y="72" width="150" height="96" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.6"/>')
    s.gate("NOT", 110, 100, None, None, w=70, h=40)
    s.raw(f'<rect x="300" y="72" width="150" height="96" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.6"/>')
    s.gate("NOT", 340, 100, None, None, w=70, h=40)
    s.arrow(222, 104, 298, 104); s.text(258, 96, "Q", size=10, weight="700", anchor="middle")
    s.arrow(298, 136, 222, 136); s.text(258, 152, "Q'", size=10, weight="700", anchor="middle")
    s.text(250, 188, "realimentación cruzada = 1 bit estable", size=9.4, color="#4b5563", anchor="middle")
    s.text(24, 214, "Para leer/escribir se agregan 2 transistores de acceso que conectan la celda a las líneas de bit (BL y BL').", size=9.6, color="#4b5563")
    s.text(24, 232, "Total: 6 transistores · no necesita refresco · rápida (ns) · ocupa mucho ⇒ se usa en la caché.", size=9.6, color="#4b5563")
    s.text(24, 266, "DRAM: un transistor de acceso + un capacitor — guarda como carga eléctrica", size=10.8, weight="700")
    s.raw(f'<rect x="430" y="286" width="80" height="46" rx="4" fill="#ffffff" stroke="{STROKE}" stroke-width="1.6"/>')
    s.text(470, 314, "MOS", size=10, anchor="middle", weight="700")
    s.line(430, 300, 400, 300); s.text(396, 304, "palabra (fila)", size=9, anchor="end", color="#4b5563")
    s.line(470, 332, 470, 352)
    s.line(452, 352, 488, 352); s.line(452, 362, 488, 362)
    s.text(496, 360, "capacitor C", size=9, color="#4b5563")
    s.text(540, 290, "El transistor conecta el capacitor a la línea de bit cuando la fila está activa.", size=9.4, color="#4b5563")
    s.text(540, 308, "1 bit = 1 transistor ⇒ altísima densidad, pero la carga se ESCAPA.", size=9.4, color="#4b5563")
    s.text(540, 326, "Por eso hay que REFRESCAR cada celda cada ~64 ms: leer y reescribir.", size=9.4, color=RED)
    s.text(540, 344, "La lectura es destructiva: descarga el capacitor y hay que reescribirlo.", size=9.4, color="#4b5563")
    s.text(24, 386, "Celda = unidad mínima que guarda 1 bit. La matriz las ordena en filas (palabra) y columnas (bit); el decodificador de fila elige la palabra.", size=9.8)
    s.text(24, 404, "SRAM = rápida y cara (caché) · DRAM = densa y barata, con refresco (memoria principal).", size=9.8, color="#4b5563")
    s.save("celda_memoria.svg")
def d_sram_dram_refresco():
    s = Svg(920, 400, "SRAM vs DRAM, y el ciclo de refresco de la DRAM")
    s.text(24, 52, "Refresco: cada fila se reescribe antes de que el capacitor pierda la carga", size=11, weight="700")
    for i in range(8):
        x = 40 + i * 100
        s.raw(f'<rect x="{x}" y="74" width="86" height="46" rx="4" fill="{"#dcfce7" if i % 2 == 0 else "#e0e7ff"}" stroke="{STROKE}" stroke-width="1.3"/>')
        s.text(x + 43, 102, f"fila {i}", size=9.6, anchor="middle")
    s.text(24, 146, "Se refresca una fila por vez, en ronda (refresco distribuido) o todas juntas (refresco en ráfaga).", size=9.8, color="#4b5563")
    s.text(24, 164, "Mientras el controlador refresca, la memoria NO atiende al procesador ⇒ hay una pérdida de ancho de banda (~1-5 %).", size=9.8, color="#4b5563")
    s.text(24, 200, "Comparación", size=11, weight="700")
    s.text(40, 224, "SRAM", size=10.5, weight="700", color=ACCENT)
    s.text(40, 244, "6 transistores por bit", size=9.8)
    s.text(40, 262, "no necesita refresco", size=9.8)
    s.text(40, 280, "1-10 ns, muy rápida", size=9.8)
    s.text(40, 298, "cara por bit ⇒ caché chica", size=9.8)
    s.text(40, 322, "volátil (pierde al apagar)", size=9.8, color="#4b5563")
    s.text(230, 224, "DRAM", size=10.5, weight="700", color=RED)
    s.text(230, 244, "1 transistor + 1 capacitor", size=9.8)
    s.text(230, 262, "refresco cada ~64 ms", size=9.8)
    s.text(230, 280, "50-100 ns (con fila abierta)", size=9.8)
    s.text(230, 298, "barata por bit ⇒ GB de RAM", size=9.8)
    s.text(230, 322, "volátil (pierde al apagar)", size=9.8, color="#4b5563")
    s.raw('<rect x="430" y="196" width="466" height="120" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(446, 218, "Otros tipos que se nombran", size=10.4, weight="700")
    s.text(446, 240, "SDRAM: sincrónica, trabaja con el reloj del bus.", size=9.4, color="#4b5563")
    s.text(446, 258, "DDR: transfiere en los dos flancos ⇒ el doble por ciclo.", size=9.4, color="#4b5563")
    s.text(446, 276, "RDRAM, VRAM (video, doble puerto), caché L1/L2 en SRAM.", size=9.4, color="#4b5563")
    s.text(446, 296, "Memoria ROM/Flash: no volátil, se ve en 2.4.", size=9.4, color="#4b5563")
    s.text(24, 352, "Las dos son volátiles: al cortar la alimentación se pierde el contenido. Lo no volátil (ROM, Flash, disco) guarda sin energía.", size=10.2)
    s.text(24, 374, "Regla: mientras más rápida, más cara por bit y más chica ⇒ la jerarquía (registros → caché → RAM → disco) es una consecuencia del costo.", size=10.2, color="#4b5563")
    s.save("sram_dram_refresco.svg")


def d_rom_decodificador_or():
    s = Svg(900, 400, "ROM = decodificador de direcciones + matriz OR de datos")
    s.text(24, 52, "Ejemplo: ROM de 4 palabras × 3 bits (direcciones de 2 bits)", size=10.8, weight="700")
    # decodificador
    s.box(50, 90, 110, 110, "", "", fill="#dbeafe")
    s.text(105, 116, "DECODIF.", size=9.6, anchor="middle", weight="700")
    s.text(105, 132, "2 → 4", size=9.4, anchor="middle", color="#4b5563")
    s.line(30, 120, 50, 120); s.text(24, 116, "A1", size=9.6, anchor="end", family=MONO)
    s.line(30, 160, 50, 160); s.text(24, 164, "A0", size=9.6, anchor="end", family=MONO)
    for i in range(4):
        y = 104 + i * 26
        s.line(160, y, 210, y)
        s.text(214, y + 4, f"m{i}", size=9.4, family=MONO, color=ACCENT)
    # matriz OR
    for j in range(3):
        s.raw(f'<rect x="{330}" y="{96 + j * 66}" width="150" height="52" rx="5" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.6"/>')
        s.text(405, 126 + j * 66, f"OR {j}", size=10, anchor="middle", weight="700")
        s.line(480, 122 + j * 66, 520, 122 + j * 66)
        s.text(524, 126 + j * 66, f"D{j}", size=9.8, weight="700", color=ACCENT)
    s.text(560, 110, "Cada línea de palabra (m_i) se conecta", size=9.6, color="#4b5563")
    s.text(560, 128, "a las OR que deben dar 1 en esa fila.", size=9.6, color="#4b5563")
    s.text(560, 152, "Contenido grabado (ejemplo):", size=9.6, weight="700")
    s.text(560, 172, "m0 → 1 0 1", size=9.6, family=MONO)
    s.text(560, 188, "m1 → 0 1 1", size=9.6, family=MONO)
    s.text(560, 204, "m2 → 1 1 0", size=9.6, family=MONO)
    s.text(560, 220, "m3 → 0 0 1", size=9.6, family=MONO)
    s.text(560, 248, "Cambiar el contenido = cambiar", size=9.6, color="#4b5563")
    s.text(560, 264, "las conexiones de la matriz.", size=9.6, color="#4b5563")
    s.raw('<rect x="24" y="286" width="852" height="96" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 308, "Por qué 'decodificador + OR': la dirección elige UNA fila (minterm) y la matriz OR dice qué bits de salida se activan en esa fila.", size=9.8)
    s.text(40, 330, "Tamaño: n bits de dirección ⇒ 2ⁿ palabras × m bits de datos. Ejemplo: 4×3 = 12 celdas; una ROM de 1 K×8 tiene 1024 × 8 = 8192 celdas.", size=9.8, family=MONO, color="#7c2d12")
    s.text(40, 352, "Es un circuito combinacional: sin reloj. Cualquier tabla de verdad se puede fabricar como ROM sin simplificar nada.", size=9.8, color="#4b5563")
    s.text(40, 370, "Se usa en decodificadores de instrucciones, tablas de senos, microcódigo (unidad 6) y arranque del sistema (BIOS).", size=9.6, color="#4b5563")
    s.save("rom_decodificador_or.svg")


def d_prom_flash_celda():
    s = Svg(900, 390, "De la ROM grabada a la Flash: qué se puede cambiar y cuántas veces")
    filas = [("Máscara (ROM)", "grabada en fábrica", "no se puede", "0", "grandes volúmenes"),
             ("PROM", "fusible que se quema", "una sola vez", "1", "prototipos viejos"),
             ("EPROM", "celda flotante + luz UV", "con UV, ~100 veces", "100", "borrado lento"),
             ("EEPROM", "celda flotante eléctrica", "byte a byte, 10⁵-10⁶", "1 000 000", "configuración"),
             ("Flash", "celda flotante por bloques", "por bloques, 10⁴-10⁵", "100 000", "SSD, USB, BIOS")]
    x0, y0 = 30, 60
    cols = [(x0, 180), (210, 210), (430, 180), (620, 90), (720, 150)]
    s.text(cols[0][0], y0, "Tipo", size=10.4, weight="700")
    s.text(cols[1][0], y0, "Cómo guarda el bit", size=10.4, weight="700")
    s.text(cols[2][0], y0, "Cómo se borra", size=10.4, weight="700")
    s.text(cols[3][0], y0, "Ciclos", size=10.4, weight="700")
    s.text(cols[4][0], y0, "Uso típico", size=10.4, weight="700")
    for i, (a, b, c, d, e) in enumerate(filas):
        y = y0 + 30 + i * 40
        if i % 2 == 0:
            s.raw(f'<rect x="{x0-8}" y="{y-18}" width="856" height="34" rx="4" fill="#f8fafc"/>')
        s.text(cols[0][0], y, a, size=10, weight="700")
        s.text(cols[1][0], y, b, size=9.6)
        s.text(cols[2][0], y, c, size=9.6)
        s.text(cols[3][0], y, d, size=9.6, family=MONO)
        s.text(cols[4][0], y, e, size=9.6, color="#4b5563")
    # celda flotante
    s.raw('<rect x="30" y="266" width="852" height="106" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(46, 288, "La celda flotante (la clave de la EPROM/EEPROM/Flash):", size=10.4, weight="700")
    s.text(46, 310, "Un transistor MOS con una 'isla' de silicio sin conexión (compuerta flotante). Si se le inyectan electrones, cambia su tensión umbral:", size=9.6)
    s.text(46, 328, "con carga NO conduce (bit 0) y sin carga SÍ conduce (bit 1). La carga queda atrapada aunque se corte la alimentación ⇒ NO volátil.", size=9.6, color="#7c2d12")
    s.text(46, 350, "Borrar = sacar los electrones (UV en la EPROM, campo eléctrico en la EEPROM/Flash). Por eso el borrado desgasta: cada ciclo daña el óxido.", size=9.6, color="#4b5563")
    s.text(30, 400 - 8, "Flash = EEPROM organizada en bloques: se borra un bloque entero y se escribe página por página (eso explica el SSD del tema 10.4).", size=9.6, color="#4b5563")
    s.save("prom_flash_celda.svg")


def d_amat_cache():
    s = Svg(920, 400, "AMAT: el tiempo promedio de acceso con acierto, fallo y dos niveles")
    s.text(24, 52, "AMAT = tiempo de acierto + (tasa de fallos × penalidad de fallo)", size=12, weight="700", family=MONO, color="#0f766e")
    s.text(24, 84, "Una sola caché:  acierto 1 ciclo, 5 % de fallos, penalidad 100 ciclos", size=10.4, weight="700")
    s.raw('<rect x="40" y="100" width="120" height="34" rx="4" fill="#dcfce7" stroke="'+STROKE+'" stroke-width="1.3"/>')
    s.text(100, 122, "acierto 1", size=9.6, anchor="middle")
    s.raw('<rect x="170" y="100" width="330" height="34" rx="4" fill="#fecaca" stroke="'+STROKE+'" stroke-width="1.3"/>')
    s.text(335, 122, "5 % de 100 ciclos = 5 ciclos promedio", size=9.6, anchor="middle")
    s.text(520, 122, "⇒ AMAT = 1 + 0,05×100 = 6 ciclos (16,7× mejor que ir siempre a RAM)", size=10, color="#7c2d12")
    s.text(24, 166, "Dos niveles: L1 (1 ciclo, 5 % falla) → L2 (10 ciclos, de esos fallos el 20 % va a RAM de 100 ciclos)", size=10.4, weight="700")
    s.raw('<rect x="40" y="182" width="120" height="34" rx="4" fill="#dcfce7" stroke="'+STROKE+'" stroke-width="1.3"/>')
    s.text(100, 204, "L1: 1", size=9.6, anchor="middle")
    s.raw('<rect x="170" y="182" width="180" height="34" rx="4" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.3"/>')
    s.text(260, 204, "L2: 10", size=9.6, anchor="middle")
    s.raw('<rect x="360" y="182" width="200" height="34" rx="4" fill="#fecaca" stroke="'+STROKE+'" stroke-width="1.3"/>')
    s.text(460, 204, "RAM: 20 % × 100 = 20", size=9.6, anchor="middle")
    s.text(580, 192, "AMAT = 1 + 0,05 × (10 + 0,2×100)", size=10, family=MONO, color="#7c2d12")
    s.text(580, 212, "= 1 + 0,05 × 30 = 2,5 ciclos", size=10, family=MONO, weight="700", color="#7c2d12")
    s.text(24, 250, "Por qué el segundo nivel ayuda tanto: absorbe la mayoría de los fallos de L1 y evita pagar los 100 ciclos de la RAM.", size=9.8, color="#4b5563")
    s.raw('<rect x="24" y="270" width="872" height="112" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 292, "Lo que cambia el resultado, en orden de impacto:", size=10.4, weight="700")
    s.text(40, 314, "1 · la tasa de fallos (localidad del programa) · 2 · la penalidad (ancho de banda de la RAM) · 3 · el tiempo de acierto.", size=9.8)
    s.text(40, 334, "Mejorar la tasa de fallos de 5 % a 2 % con penalidad 100: AMAT = 1 + 2 = 3 ciclos (¡la mitad!).", size=9.8, color="#15803d")
    s.text(40, 354, "Duplicar la caché suele bajar la tasa; subir la asociatividad también; el tamaño del bloque tiene un óptimo (más bloque = más localidad, pero más penalidad).", size=9.6, color="#4b5563")
    s.text(40, 372, "CPI con caché: CPI = CPI_ideal + (fallos por instrucción × penalidad). Con 2 % y 100 ⇒ +2 al CPI.", size=9.6, color="#7c2d12")
    s.text(24, 400 - 6, "AMAT = Average Memory Access Time: es el número que se usa para comparar dos jerarquías en el final.", size=9.8, color="#4b5563")
    s.save("amat_cache.svg")


def d_memoria_virtual_tlb():
    s = Svg(920, 410, "Memoria virtual: dirección virtual → tabla de páginas → dirección física (y el TLB)")
    s.text(24, 52, "La CPU genera una dirección VIRTUAL; la MMU la traduce a FÍSICA usando la tabla de páginas", size=10.8, weight="700")
    s.box(40, 76, 150, 60, "CPU", "dir. virtual", fill="#dbeafe")
    s.box(230, 76, 130, 60, "MMU", "traduce", fill="#fef3c7")
    s.box(400, 76, 170, 60, "RAM", "dir. física", fill="#e0e7ff")
    s.arrow(190, 106, 226, 106); s.arrow(360, 106, 396, 106)
    s.box(230, 176, 130, 50, "TLB", "caché de la tabla", fill="#dcfce7")
    s.arrow(295, 140, 295, 172)
    s.text(410, 194, "TLB acierto ⇒ 1 ciclo; fallo ⇒ leer la tabla en RAM (1-2 accesos: 100+ ciclos).", size=9.6, color="#4b5563")
    s.text(410, 214, "Es exactamente 'caché de la caché de la traducción'.", size=9.6, color="#4b5563")
    # dirección partida
    s.text(24, 258, "La dirección se parte en dos campos:", size=10.4, weight="700")
    s.raw('<rect x="40" y="272" width="150" height="40" rx="3" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.4"/>')
    s.text(115, 297, "nº de página", size=9.8, anchor="middle", weight="700")
    s.raw('<rect x="190" y="272" width="120" height="40" rx="3" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.4"/>')
    s.text(250, 297, "desplazamiento", size=9.8, anchor="middle", weight="700")
    s.text(330, 288, "El desplazamiento NO se traduce: pasa tal cual.", size=9.6, color="#4b5563")
    s.text(330, 306, "Sólo se traduce el número de página.", size=9.6, color="#4b5563")
    s.text(24, 344, "Fallo de página: la página no está en RAM ⇒ el SO la trae del disco (13 ms de un HDD) ⇒ por eso se elige una víctima y se escribe si está sucia.", size=9.8, color=RED)
    s.text(24, 364, "Qué resuelve: dar a cada proceso un espacio de direcciones propio y aislado, permitir programas más grandes que la RAM y compartir páginas.", size=9.8, color="#4b5563")
    s.text(24, 384, "Se apoya en la misma idea de la caché: localidad + traducción guardada + política de reemplazo. El 'disco lento' del tema 10.4 es la razón de existir.", size=9.8, color="#4b5563")
    s.save("memoria_virtual_tlb.svg")


def d_memoria_asociativa_cam():
    s = Svg(900, 390, "Memoria asociativa (CAM): buscar por CONTENIDO, no por dirección")
    s.text(24, 52, "RAM normal: se da la dirección y devuelve el dato · CAM: se da el dato y devuelve la dirección (y si está)", size=10.6, weight="700")
    s.box(50, 80, 180, 66, "RAM", "dirección → dato", fill="#e0e7ff")
    s.box(300, 80, 200, 66, "CAM", "contenido → coincidencia", fill="#dcfce7")
    s.text(530, 96, "La CAM compara la entrada contra TODAS las", size=9.6, color="#4b5563")
    s.text(530, 114, "palabras a la vez (comparadores en paralelo)", size=9.6, color="#4b5563")
    s.text(530, 132, "y marca cuáles coinciden.", size=9.6, color="#4b5563")
    s.text(24, 186, "Dónde aparece en la materia", size=11, weight="700")
    s.text(40, 210, "· TLB: la traducción de páginas se busca por contenido (nº de página virtual).", size=9.8)
    s.text(40, 230, "· Caché totalmente asociativa: el bloque se busca por etiqueta en todos los marcos.", size=9.8)
    s.text(40, 250, "· Tablas de ruteo, colas de instrucciones, detección de dependencias en un superscalar.", size=9.8)
    s.text(40, 274, "Costo: una celda CAM ocupa ~6-10 transistores y consume mucho ⇒ se usa en memorias CHICAS y muy consultadas.", size=9.8, color=RED)
    s.raw('<rect x="24" y="296" width="852" height="80" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 318, "Memoria auxiliar (el último nivel): disco, SSD, cinta. Es la que alimenta a la RAM cuando hay fallo de página.", size=9.8)
    s.text(40, 338, "Registros → caché → RAM → memoria auxiliar: cada nivel es ~10-1000 veces más grande y más lento que el anterior.", size=9.8, color="#4b5563")
    s.text(40, 358, "Por eso la CAM vive arriba (TLB, caché) y el disco abajo: velocidad contra capacidad.", size=9.8, color="#4b5563")
    s.text(24, 396 - 4, "Asociativa = comparación en paralelo. Es la única memoria que responde 'no está' en un solo ciclo.", size=9.8, color="#4b5563")
    s.save("memoria_asociativa_cam.svg")


def d_bits_direccion():
    s = Svg(920, 400, "Bits de dirección = log₂ de celdas, y cómo se expande un banco de memoria")
    s.text(24, 52, "Si hay N celdas, hacen falta n = log₂ N líneas de dirección", size=12, weight="700", family=MONO, color="#0f766e")
    for i, (n, txt) in enumerate([("8", "256 celdas"), ("10", "1 K"), ("12", "4 096 (la BLUE)"), ("16", "64 K"), ("20", "1 M")]):
        x = 40 + i * 175
        s.raw(f'<rect x="{x}" y="74" width="160" height="62" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 80, 98, f"{n} líneas", size=11.5, anchor="middle", weight="700")
        s.text(x + 80, 120, txt, size=9.6, anchor="middle", color="#4b5563")
    s.text(24, 164, "2¹² = 4 096 ⇒ 12 líneas (la BLUE). 2¹⁶ = 65 536 ⇒ 16 líneas. Cada línea nueva duplica la memoria.", size=9.8, color="#4b5563")
    s.text(24, 200, "Expansión: para una memoria más grande que el chip se combinan chips con un decodificador de selección", size=10.6, weight="700")
    s.box(50, 222, 140, 64, "8 K × 8", "chip 0", fill="#dcfce7")
    s.box(50, 296, 140, 64, "8 K × 8", "chip 1", fill="#dcfce7")
    s.box(230, 222, 140, 64, "8 K × 8", "chip 2", fill="#dcfce7")
    s.box(230, 296, 140, 64, "8 K × 8", "chip 3", fill="#dcfce7")
    s.text(400, 240, "Con 4 chips de 8 K×8 y 15 líneas (2¹⁵ = 32 K) se arma 32 K×8:", size=9.8)
    s.text(400, 260, "A0-A12 van a TODOS los chips (dirección dentro del chip);", size=9.8, color="#4b5563")
    s.text(400, 278, "A13-A14 entran al decodificador 2→4 que activa CS de un solo chip.", size=9.8, color="#4b5563")
    s.text(400, 298, "CS = chip select: sin CS el chip queda en alta impedancia.", size=9.8, color="#4b5563")
    s.text(400, 320, "Para más ancho (16 bits) se ponen dos bancos en paralelo con el mismo CS.", size=9.8, color="#4b5563")
    s.text(24, 380, "Regla de examen: primero contar celdas, después sacar log₂ para las líneas, y al final decidir cuántas van al decodificador de chips.", size=10.2)
    s.save("bits_direccion.svg")


def d_codop_vs_direccion():
    s = Svg(920, 400, "Reparto de la instrucción: CodOp vs campo de dirección")
    s.text(24, 52, "Una instrucción con n bits: el CodOp dice QUÉ se hace y la dirección dice DÓNDE", size=11, weight="700")
    s.raw('<rect x="40" y="74" width="200" height="46" rx="3" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(140, 103, "CodOp (k bits)", size=11.5, anchor="middle", weight="700")
    s.raw('<rect x="240" y="74" width="300" height="46" rx="3" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(390, 103, "Campo de dirección (d bits)", size=11.5, anchor="middle", weight="700")
    s.text(560, 92, "k + d = largo de la instrucción", size=10, family=MONO,
           color="#7c2d12")
    s.text(540, 112, "Ejemplo BLUE: 16 bits = 4 (CodOp) + 12 (dirección) ⇒ 16 opcodes y 4 096 direcciones.", size=8.8, color="#4b5563")
    s.text(24, 152, "Cuántas direcciones entran:  d = log₂ (número de celdas de memoria)", size=10.6, weight="700", family=MONO, color="#0f766e")
    s.text(24, 172, "Cuántos opcodes entran:      k = log₂ (número de operaciones distintas)  ⇒ k = 4 da 16; k = 5 da 32; k = 3 da 8.", size=10.6, weight="700", family=MONO, color="#0f766e")
    s.text(24, 206, "El compromiso (el cálculo que se toma)", size=10.8, weight="700")
    s.text(40, 230, "Memoria de 1 K celdas ⇒ d = 10 bits. Instrucción de 16 bits ⇒ k = 16 − 10 = 6 ⇒ 64 opcodes distintos.", size=9.8, family=MONO)
    s.text(40, 250, "Memoria de 4 K ⇒ d = 12 ⇒ k = 4 ⇒ 16 opcodes.", size=9.8, family=MONO)
    s.text(40, 270, "Memoria de 64 K ⇒ d = 16 ⇒ k = 0 ⇒ NO entra ningún opcode: hay que alargar la instrucción.", size=9.8, family=MONO, color=RED)
    s.raw('<rect x="24" y="290" width="872" height="92" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 312, "Cómo lo resuelven las máquinas reales: formatos múltiples (la BLUE tiene 4), campos implícitos y varias palabras por instrucción.", size=9.8)
    s.text(40, 332, "Si la dirección no entra completa se usa un registro: la instrucción trae el número de registro (pocos bits) y el registro guarda la dirección.", size=9.8, color="#4b5563")
    s.text(40, 352, "Los bits de modo de direccionamiento salen del mismo presupuesto: cada modo que se agrega quita un bit al opcode o a la dirección.", size=9.8, color="#4b5563")
    s.text(40, 370, "Regla: el campo de dirección debe poder nombrar TODA la memoria; el opcode debe nombrar TODAS las operaciones. Si no entran las dos, cambia el formato.", size=9.8, color="#7c2d12")
    s.text(24, 404 - 6, "En la BLUE: 4096 celdas ⇒ 12 bits de dirección; con instrucciones de 16 bits quedan 4 para el opcode (16 octales) — ver 4.2.2 y 5.2.", size=9.8, color="#4b5563")
    s.save("codop_vs_direccion.svg")


# ══════════════════════════ UNIDAD 3 ══════════════════════════
def d_microoperaciones_bus():
    s = Svg(920, 400, "Bus único y microoperaciones: una transferencia por pulso")
    s.line(60, 300, 860, 300, w=3, color=ACCENT)
    for i, n in enumerate(["R0", "R1", "R2", "R3", "ALU"]):
        x = 90 + i * 150
        s.raw(f'<rect x="{x}" y="150" width="100" height="56" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.6"/>')
        s.text(x + 50, 184, n, size=12, weight="700", anchor="middle")
        s.arrow(x + 50, 206, x + 50, 296)
        s.text(x + 56, 250, "out", size=8.6, color=RED)
        s.arrow(x + 30, 296, x + 30, 210)
        s.text(x + 6, 250, "in", size=8.6, color="#15803d")
    s.text(60, 330, "Cada registro tiene un buffer de 3 estados a la salida (sólo uno habla a la vez) y una entrada que se carga con el pulso.", size=9.8, color="#4b5563")
    s.text(24, 52, "La microoperación R1 ← R2 se hace en UN pulso:", size=11, weight="700")
    s.text(24, 78, "1 · la UC activa la salida de R2 (R2out) ⇒ R2 pone su contenido en el bus;", size=9.8)
    s.text(24, 98, "2 · la UC activa la carga de R1 (R1in) ⇒ en el flanco del pulso R1 copia el bus.", size=9.8)
    s.text(24, 118, "Todo lo demás queda en alta impedancia: el bus es compartido y sólo un dueño por vez.", size=9.8, color="#4b5563")
    s.raw('<rect x="24" y="352" width="872" height="40" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 372, "Notación RTL:  R1 ← R2   ·   R3 ← R1 + R2   ·   R0 ← 0   ·   PC ← PC + 1   (la flecha indica destino, el ← es la operación)", size=9.6, family=MONO)
    s.text(40, 388, "Toda instrucción es una secuencia de microoperaciones: buscar (MAR←PC), ejecutar (R1←R2) y actualizar (PC←PC+1).", size=9.4, color="#4b5563")
    s.save("microoperaciones_bus.svg")


def d_buffer_tres_estados():
    s = Svg(900, 400, "Buffer de 3 estados: la compuerta que permite compartir un bus")
    s.text(24, 52, "Símbolo y tabla", size=11, weight="700")
    s.poly([(80, 90), (80, 166), (170, 128)], close=True, fill="#dbeafe", color=STROKE, w=1.8)
    s.line(48, 108, 80, 108); s.text(44, 112, "D", size=10.5, anchor="end", weight="700")
    s.line(48, 148, 80, 148); s.text(44, 152, "EN", size=10.5, anchor="end", weight="700")
    s.line(170, 128, 210, 128); s.text(214, 132, "Y", size=10.5, weight="700", color=ACCENT)
    s.text(24, 210, "EN D | Y", size=10, family=MONO, weight="700")
    s.text(24, 228, "0  x | Z (alta impedancia)", size=10, family=MONO, color=RED)
    s.text(24, 244, "1  0 | 0", size=10, family=MONO)
    s.text(24, 260, "1  1 | 1", size=10, family=MONO)
    s.text(24, 288, "Con EN = 0 la salida queda 'desconectada':", size=9.6, color="#4b5563")
    s.text(24, 304, "no empuja ni 0 ni 1, no carga el bus.", size=9.6, color="#4b5563")
    s.text(24, 330, "Ése es el tercer estado: 0, 1 y Z (alta impedancia).", size=9.6, weight="700", color="#7c2d12")
    # por qué
    s.raw('<rect x="360" y="86" width="516" height="288" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(376, 110, "Por qué es imprescindible: el bus es un solo cable para muchos", size=10.6, weight="700")
    s.line(400, 176, 850, 176, w=3, color=ACCENT)
    for i, n in enumerate(["R0", "R1", "R2"]):
        x = 420 + i * 150
        s.raw(f'<rect x="{x}" y="128" width="90" height="36" rx="4" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 45, 152, n, size=10, weight="700", anchor="middle")
        s.arrow(x + 45, 166, x + 45, 174)
    s.text(400, 204, "Si dos registros hablaran a la vez, uno forzaría 1 y el otro 0 ⇒ cortocircuito.", size=9.6, color=RED)
    s.text(400, 226, "Con buffers de 3 estados, la UC habilita UNO solo por pulso: el resto queda en Z.", size=9.6, color="#4b5563")
    s.text(400, 258, "Dónde más aparece: salidas de memoria y periféricos, bus de datos bidireccional,", size=9.6, color="#4b5563")
    s.text(400, 276, "y el 'chip select' (CS) de cualquier integrado.", size=9.6, color="#4b5563")
    s.text(400, 306, "En la BLUE: cada registro tiene su buffer y la UC abre el que corresponde", size=9.6, color="#4b5563")
    s.text(400, 324, "en cada uno de los 8 pulsos (ver la instrucción LDA).", size=9.6, color="#4b5563")
    s.text(400, 352, "Se dice 'tres estados' porque la salida puede ser 0, 1 o alta impedancia: no es un 0 ni un 1,", size=9.4, color="#4b5563")
    s.text(400, 368, "es una desconexión eléctrica.", size=9.4, color="#4b5563")
    s.save("buffer_tres_estados.svg")


def d_alu_estructura():
    s = Svg(920, 400, "La ALU: entradas, selección de operación, salidas G/P y flags")
    s.text(24, 52, "Bloque combinacional: la operación la elige la Unidad de Control", size=10.8, weight="700")
    s.raw('<rect x="300" y="80" width="300" height="150" rx="6" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="2"/>')
    s.text(450, 128, "ALU", size=20, weight="700", anchor="middle")
    s.text(450, 156, "suma · resta · AND · OR · XOR", size=9.4, anchor="middle", color="#4b5563")
    s.text(450, 174, "desplazamientos · complemento", size=9.4, anchor="middle", color="#4b5563")
    s.text(450, 202, "3-5 bits de selección", size=9, anchor="middle", color=RED)
    s.line(180, 110, 300, 110); s.text(176, 114, "A (n bits)", size=10, anchor="end", weight="700")
    s.line(180, 170, 300, 170); s.text(176, 174, "B (n bits)", size=10, anchor="end", weight="700")
    s.line(180, 226, 300, 226); s.text(176, 230, "sel (de la UC)", size=9.6, anchor="end", weight="700", color=RED)
    s.line(600, 120, 700, 120); s.text(704, 124, "resultado F", size=10, weight="700", color=ACCENT)
    s.line(600, 200, 700, 200); s.text(704, 204, "Cout / G / P", size=9.6, weight="700", color="#0f766e")
    s.text(24, 262, "Cómo se controla", size=11, weight="700")
    s.text(40, 286, "La UC manda un código de operación (3-5 bits) a un decodificador interno.", size=9.8)
    s.text(40, 306, "Con multiplexores se elige qué resultado sale: cada operación es un bloque y el MUX selecciona uno.", size=9.8)
    s.text(40, 326, "El mismo bloque de suma sirve para restar (B' + 1) y para comparar (restando y mirando Z).", size=9.8, color="#4b5563")
    s.raw('<rect x="600" y="262" width="296" height="106" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(616, 284, "Señales de la cátedra", size=10.2, weight="700")
    s.text(616, 304, "· G = A·B  (genera acarreo)", size=9.4, family=MONO)
    s.text(616, 322, "· P = A⊕B  (propaga acarreo)", size=9.4, family=MONO)
    s.text(616, 340, "· F: resultado   ·   Cout: acarreo", size=9.4, family=MONO)
    s.text(616, 358, "· flags: Z, C, V, N (ver 3.2.2)", size=9.4, family=MONO)
    s.text(24, 384, "La ALU es combinacional (sin reloj): el resultado está apenas cambian las entradas; lo que lo 'guarda' es el registro de destino.", size=10.2)
    s.save("alu_estructura.svg")


def d_flags_alu():
    s = Svg(920, 400, "De la operación a las banderas: Z, C, V y N")
    s.text(24, 52, "Cada bandera es un biestable que se carga al final de la operación", size=10.6, weight="700")
    filas = [("Z (cero)", "Z = 1 si F = 000…0", "NOR de todos los bits de F", "para comparar: si Z=1, A = B"),
             ("C (acarreo)", "C = Cout del bit más significativo", "el acarreo que sale del último sumador", "en la suma/resta y en los desplazamientos"),
             ("V (desborde)", "V = C_entrada_al_signo ⊕ C_salida_del_signo", "siempre con DOS acarreos, nunca con los signos", "sólo tiene sentido en aritmética con signo"),
             ("N (negativo)", "N = bit más significativo de F", "un simple cable", "copia el signo del resultado")]
    y = 82
    for nom, defi, como, uso in filas:
        s.raw(f'<rect x="24" y="{y-22}" width="872" height="66" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
        s.text(40, y - 2, nom, size=11, weight="700", color=ACCENT)
        s.text(40, y + 18, defi, size=9.4, family=MONO, color="#7c2d12")
        s.text(330, y - 2, como, size=9.4, color="#4b5563")
        s.text(330, y + 18, uso, size=9.4, color="#4b5563")
        y += 74
    s.text(24, 384, "Las banderas se miran después: la UC decide un salto condicional (JZ, JN, JC) leyendo Z, N y C.", size=10.2)
    s.save("flags_alu.svg")


def d_registros_cpu_mar():
    s = Svg(920, 410, "Los registros de la CPU y su papel en el ciclo de instrucción")
    s.box(340, 60, 240, 60, "", "", fill="#dbeafe")
    s.text(460, 84, "UNIDAD DE CONTROL", size=10.4, anchor="middle", weight="700")
    s.text(460, 104, "decodifica el IR y genera señales", size=9, anchor="middle", color="#4b5563")
    s.box(60, 60, 200, 60, "PC", "dir. de la próxima", fill="#dcfce7")
    s.box(60, 160, 200, 60, "MAR", "dirección al bus", fill="#dcfce7")
    s.box(60, 260, 200, 60, "MBR", "dato que entra/sale", fill="#dcfce7")
    s.box(660, 60, 210, 60, "IR", "instrucción en curso", fill="#fef3c7")
    s.box(660, 160, 210, 60, "AC", "acumulador", fill="#fef3c7")
    s.box(660, 260, 210, 60, "SP / índice", "pila y direccionamiento", fill="#fef3c7")
    s.arrow(260, 90, 336, 90); s.arrow(584, 90, 656, 90)
    s.arrow(160, 122, 160, 156, color=RED)
    s.arrow(160, 222, 160, 256, color=RED)
    s.text(168, 146, "PC → MAR", size=8.6, color=RED)
    s.text(168, 246, "MBR → memoria", size=8.6, color=RED)
    s.arrow(656, 190, 584, 190); s.text(600, 182, "IR → UC", size=8.6, color=RED)
    s.line(260, 290, 660, 290, w=2, color=ACCENT); s.text(400, 306, "bus interno", size=8.6, color=ACCENT)
    s.text(24, 350, "PC apunta a la próxima instrucción · MAR lleva la dirección a memoria · MBR recibe el dato · IR guarda la instrucción que se decodifica", size=9.8)
    s.text(24, 372, "AC es el registro de trabajo de la ALU · SP guarda la pila (llamadas, interrupciones) · los de índice y base calculan direcciones", size=9.8, color="#4b5563")
    s.text(24, 394, "Por qué se llaman así: MAR = Memory Address Register, MBR = Memory Buffer Register, IR = Instruction Register, PC = Program Counter.", size=9.8, color="#4b5563")
    s.save("registros_cpu_mar.svg")


# ══════════════════════════ UNIDAD 4 ══════════════════════════
def d_ias_estructura():
    s = Svg(920, 410, "La máquina IAS: el primer computador con programa almacenado")
    s.box(50, 70, 210, 90, "", "", fill="#dbeafe")
    s.text(66, 96, "UNIDAD DE CONTROL", size=9.6, weight="700")
    s.text(66, 116, "ejecuta el ciclo", size=9, color="#4b5563")
    s.text(66, 134, "búsqueda → ejecución", size=9, color="#4b5563")
    s.box(50, 200, 210, 120, "", "", fill="#dcfce7")
    s.text(66, 224, "UNIDAD ARITMÉTICA", size=9.6, weight="700")
    s.text(66, 246, "AC (acumulador)", size=9.2, family=MONO)
    s.text(66, 266, "MQ (cociente)", size=9.2, family=MONO)
    s.text(66, 288, "suma, resta,", size=9, color="#4b5563")
    s.text(66, 306, "multiplicación, división", size=9, color="#4b5563")
    s.box(330, 70, 250, 250, "", "", fill="#f8fafc")
    s.text(346, 94, "MEMORIA PRINCIPAL", size=9.8, weight="700")
    s.text(346, 114, "1 000 palabras de 40 bits", size=9.2, color="#4b5563")
    s.text(346, 138, "cada palabra: 20 bits de", size=9, color="#4b5563")
    s.text(346, 154, "izquierda + 20 de derecha", size=9, color="#4b5563")
    s.raw('<rect x="346" y="170" width="218" height="26" rx="3" fill="#ffffff" stroke="#94a3b8"/>')
    s.text(455, 188, "0 0 0 … 0  0 0 … 0", size=9, anchor="middle", family=MONO, color="#4b5563")
    s.raw('<rect x="346" y="200" width="218" height="26" rx="3" fill="#ffffff" stroke="#94a3b8"/>')
    s.text(455, 218, "1 0 0 … 1  0 1 … 1", size=9, anchor="middle", family=MONO, color="#4b5563")
    s.text(455, 246, "instrucciones y datos", size=9, anchor="middle", color=RED)
    s.text(455, 262, "en la MISMA memoria", size=9, anchor="middle", color=RED)
    s.box(650, 130, 240, 130, "", "", fill="#fef3c7")
    s.text(666, 154, "REGISTROS", size=9.6, weight="700")
    s.text(666, 176, "IR: instrucción en curso", size=9, family=MONO)
    s.text(666, 196, "IBR: operando derecho", size=9, family=MONO)
    s.text(666, 216, "PC: próxima instrucción", size=9, family=MONO)
    s.text(666, 236, "MAR: dirección de memoria", size=9, family=MONO)
    s.text(666, 252, "MBR: dato leído/escrito", size=9, family=MONO)
    s.arrow(260, 115, 328, 115); s.arrow(260, 260, 328, 220)
    s.arrow(580, 160, 648, 170); s.arrow(648, 210, 580, 200)
    s.text(24, 350, "La idea central (1946): las instrucciones se guardan en la MISMA memoria que los datos ⇒ el programa se puede cargar, cambiar y hasta tratar como dato.", size=9.8)
    s.text(24, 372, "Eso es el modelo von Neumann (unidad 7.4). El IAS ya tenía la estructura que se repite en toda la materia: UC + ALU + memoria + registros.", size=9.8, color="#4b5563")
    s.text(24, 394, "Direccionamiento: 10 bits para 1 000 palabras; el bit de la izquierda dice si la palabra es una instrucción (0) o un dato (1).", size=9.8, color="#4b5563")
    s.save("ias_estructura.svg")


def d_blue_opcodes():
    s = Svg(920, 420, "Los 16 códigos de operación de la BLUE (4 bits, en octal)")
    datos = [("0", "HLT", "alta (detiene)"), ("1", "ADD", "AC ← AC + M[D]"), ("2", "SUB", "AC ← AC − M[D]"),
             ("3", "STA", "M[D] ← AC"), ("4", "LDA", "AC ← M[D]"), ("5", "INP", "AC ← periférico"),
             ("6", "OUT", "periférico ← AC"), ("7", "SKF", "salta si bandera"),
             ("10", "JMP", "PC ← D"), ("11", "JMA", "salto si AC<0"), ("12", "JSR", "salto a subrutina"),
             ("13", "RET", "vuelve de subrutina"), ("14", "SRJ", "salto y retorno"),
             ("15", "RAL", "rota AC a la izquierda"), ("16", "CSA", "cambia signo"), ("17", "NOP", "no opera")]
    for k, (code, mne, desc) in enumerate(datos):
        x = 30 + (k % 4) * 222
        y = 60 + (k // 4) * 82
        s.raw(f'<rect x="{x}" y="{y}" width="206" height="68" rx="5" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.5"/>')
        s.text(x + 12, y + 26, code, size=13, weight="700", family=MONO, color=ACCENT)
        s.text(x + 44, y + 26, mne, size=12, weight="700")
        s.text(x + 12, y + 52, desc, size=8.8, color="#4b5563")
    s.text(30, 400, "En octal se escribe con un dígito (0-7 con 3 bits) — la BLUE usa 4 bits de opcode, así que los códigos van de 0 a 17 octal (0 a 15 decimal).", size=9.6, color="#4b5563")
    s.text(30, 416, "Grupos de ciclo: HLT, NOP, RAL, CSA, SRJ, JMP y JMA son de 1 ciclo (8 pulsos); LDA/STA/ADD/SUB de 2; indexada e indirecta, más.", size=9.6, color="#7c2d12")
    s.save("blue_opcodes.svg")


def d_blue_programa_ram():
    s = Svg(920, 410, "Un programa en la memoria de la BLUE: instrucciones y datos mezclados")
    s.text(24, 52, "Programa: sumar los números de las posiciones 10, 11 y 12 y guardar el total en 13", size=10.6, weight="700")
    prog = [("0", "LDA 10", "AC ← M[10]"), ("1", "ADD 11", "AC ← AC + M[11]"), ("2", "ADD 12", "AC ← AC + M[12]"),
            ("3", "STA 13", "M[13] ← AC"), ("4", "HLT", "detiene la máquina")]
    for i, (dirx, ins, com) in enumerate(prog):
        y = 80 + i * 34
        s.raw(f'<rect x="40" y="{y}" width="70" height="28" rx="3" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(75, y + 19, dirx, size=10, anchor="middle", family=MONO, weight="700")
        s.raw(f'<rect x="110" y="{y}" width="120" height="28" rx="3" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(170, y + 19, ins, size=10, anchor="middle", family=MONO, weight="700")
        s.text(242, y + 19, com, size=9.4, family=MONO, color="#4b5563")
    for i, (dirx, val) in enumerate([("10", "5"), ("11", "7"), ("12", "9"), ("13", "—")]):
        y = 80 + i * 34
        s.raw(f'<rect x="440" y="{y}" width="70" height="28" rx="3" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(475, y + 19, dirx, size=10, anchor="middle", family="monospace", weight="700")
        s.raw(f'<rect x="510" y="{y}" width="80" height="28" rx="3" fill="#ffffff" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(550, y + 19, val, size=10, anchor="middle", family="monospace")
    s.text(440, 236, "datos", size=9.4, color="#7c2d12")
    s.text(620, 92, "Primero se carga el programa en memoria (a mano, con", size=9.6, color="#4b5563")
    s.text(620, 110, "las llaves o un cargador) y después se pone PC = 0.", size=9.6, color="#4b5563")
    s.text(620, 140, "Ejecución: 5 → 12 → 21 ⇒ M[13] = 21.", size=9.8, weight="700", color="#15803d")
    s.text(620, 168, "Cada instrucción ocupa UNA celda de 16 bits:", size=9.6, color="#4b5563")
    s.text(620, 186, "4 bits de opcode + 4 de dirección (+12 sin usar", size=9.6, color="#4b5563")
    s.text(620, 204, "o para formatos extendidos).", size=9.6, color="#4b5563")
    s.raw('<rect x="24" y="280" width="872" height="112" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 302, "Lo importante: el programa ES dato. La misma memoria guarda instrucciones en las celdas 0-4 y datos en 10-13.", size=9.8, color="#7c2d12")
    s.text(40, 324, "Por eso el PC puede apuntar a cualquier celda y por eso un error de direccionamiento puede terminar 'ejecutando datos'.", size=9.8, color="#4b5563")
    s.text(40, 346, "Si el programa se equivoca y sigue de largo, la BLUE ejecuta lo que haya después (no hay protección de memoria).", size=9.8, color="#4b5563")
    s.text(40, 368, "Costos: LDA y ADD son de 2 ciclos (16 pulsos); HLT, de 1 ciclo (8 pulsos). Contar pulsos = sumar por instrucción.", size=9.8, color="#4b5563")
    s.save("blue_programa_ram.svg")


def d_busqueda_pulsos():
    s = Svg(920, 400, "El ciclo de búsqueda: los 8 pulsos de CP1 a CP8")
    pulsos = [("CP1", "MAR ← PC", "la dirección de la instrucción va al bus"),
              ("CP2", "PC ← PC + 1", "se apunta a la siguiente"),
              ("CP3", "MBR ← M[MAR], Read", "llega la instrucción"),
              ("CP4", "IR ← MBR", "queda en el registro de instrucción"),
              ("CP5", "UC decodifica", "el opcode elige la secuencia"),
              ("CP6", "— (nada)", "pulso de decodificación"),
              ("CP7", "— (nada)", "pulso de decodificación"),
              ("CP8", "estado ← E", "pasa a ejecución (o interrupción)")]
    for k, (cp, acc, com) in enumerate(pulsos):
        y = 62 + k * 34
        s.raw(f'<rect x="40" y="{y}" width="66" height="28" rx="3" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.3"/>')
        s.text(73, y + 19, cp, size=9.6, anchor="middle", weight="700", color=ACCENT)
        s.raw(f'<rect x="106" y="{y}" width="230" height="28" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.1"/>')
        s.text(116, y + 19, acc, size=9.6, family=MONO, weight="700")
        s.text(350, y + 19, com, size=9.4, color="#4b5563")
    s.raw('<rect x="620" y="62" width="276" height="248" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(636, 84, "Reglas del ciclo", size=10.4, weight="700")
    s.text(636, 106, "· 8 pulsos = 1 ciclo de máquina.", size=9.2)
    s.text(636, 124, "· Un pulso dura 125 ns si el reloj", size=9.2, color="#4b5563")
    s.text(636, 142, "  es de 1 MHz.", size=9.2, color="#4b5563")
    s.text(636, 164, "· Toda instrucción empieza con", size=9.2, color="#4b5563")
    s.text(636, 182, "  este mismo ciclo de búsqueda.", size=9.2, color="#4b5563")
    s.text(636, 204, "· La interrupción se acepta en CP8.", size=9.2, color=RED)
    s.text(636, 226, "· En CP8 el estado pasa de F a E:", size=9.2, color="#4b5563")
    s.text(636, 244, "  búsqueda (F) → ejecución (E) →", size=9.2, color="#4b5563")
    s.text(636, 262, "  interrupción (I).", size=9.2, color="#4b5563")
    s.text(636, 288, "Los pulsos 5-7 se usan para decodificar", size=9.2, color="#4b5563")
    s.text(636, 304, "sin tocar el bus.", size=9.2, color="#4b5563")
    s.text(24, 356, "Ciclo de reloj (1 pulso) ⊂ ciclo de máquina (8 pulsos) ⊂ ciclo de instrucción (búsqueda + 1 o más ciclos de ejecución).", size=10.2)
    s.text(24, 378, "Por eso la instrucción más corta dura 8 pulsos = 1 µs, y por eso el tiempo de un programa se cuenta en pulsos.", size=10.2, color="#4b5563")
    s.save("busqueda_pulsos.svg")


def d_estado_pulso_1_16():
    s = Svg(920, 410, "estado · pulso · instrucción: la lógica que genera las señales de control")
    s.text(24, 52, "Las señales de control se activan por la combinación de tres cosas", size=10.8, weight="700")
    s.box(60, 80, 130, 44, "ESTADO", "F / E / I", fill="#dbeafe")
    s.box(60, 146, 130, 44, "PULSO", "CP1 … CP8", fill="#dcfce7")
    s.box(60, 212, 130, 44, "INSTRUCCIÓN", "opcode (4 bits)", fill="#fef3c7")
    s.box(280, 130, 180, 90, "", "", fill="#f8fafc")
    s.text(370, 158, "DECODIFICADOR", size=9.6, anchor="middle", weight="700")
    s.text(370, 176, "1 de 16", size=9.4, anchor="middle", color="#4b5563")
    s.text(370, 198, "y compuertas AND", size=9.2, anchor="middle", color="#4b5563")
    s.arrow(192, 102, 278, 140)
    s.arrow(192, 168, 278, 168)
    s.arrow(192, 234, 278, 196)
    for i, lab in enumerate(["MAR ← PC", "PC ← PC+1", "IR ← MBR", "Read", "Write", "AC ← ALU"]):
        y = 90 + i * 34
        s.arrow(462, 168, 540, y + 4)
        s.text(548, y + 8, lab, size=9.4, family=MONO)
    s.text(700, 96, "Cada señal es un producto:", size=9.8, weight="700")
    s.text(700, 118, "salida = F·CP1·LDA", size=9.6, family=MONO, color="#7c2d12")
    s.text(700, 138, "⇒ MAR←PC sólo en CP1, en", size=9.2, color="#4b5563")
    s.text(700, 154, "búsqueda, con LDA.", size=9.2, color="#4b5563")
    s.text(700, 180, "El decodificador 1 de 16 convierte", size=9.2, color="#4b5563")
    s.text(700, 196, "los 4 bits del opcode en una línea", size=9.2, color="#4b5563")
    s.text(700, 212, "activa (una por instrucción).", size=9.2, color="#4b5563")
    s.raw('<rect x="24" y="286" width="872" height="106" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 308, "Con 3 bits de estado (F, E, I), 3 bits de pulso (CP1-CP8) y 4 de opcode: 10 variables ⇒ la UC es una función combinacional enorme.", size=9.8)
    s.text(40, 330, "Por eso se usan dos soluciones: control cableado (compuertas y PLA, rápido pero rígido) o microprogramado (memoria de control, flexible). Ver unidad 6.", size=9.8, color="#4b5563")
    s.text(40, 352, "El estado F/E/I se guarda en 2 biestables; el pulso lo da un contador de 3 bits que cuenta 1…8 con el reloj.", size=9.8, color="#4b5563")
    s.text(40, 374, "Regla de la cátedra: toda señal se escribe como estado·pulso·instrucción — así aparece en las tablas de microoperaciones.", size=9.8, color="#7c2d12")
    s.text(24, 410 - 4, "El decodificador 1 de 16 es el mismo circuito de la unidad 1 (2⁴ = 16 salidas), aplicado al campo CodOp.", size=9.8, color="#4b5563")
    s.save("estado_pulso_1_16.svg")

# ══════════════════════════ UNIDAD 5 ══════════════════════════
def d_instruccion_partes():
    s = Svg(920, 400, "La instrucción: código de operación + operandos")
    s.text(24, 52, "Qué debe contestar una instrucción", size=10.8, weight="700")
    s.text(40, 76, "1 · QUÉ se hace  ⇒ código de operación (opcode / CodOp)", size=9.8)
    s.text(40, 96, "2 · CON QUÉ se hace  ⇒ uno o más operandos (registro, memoria, inmediato)", size=9.8)
    s.text(40, 116, "3 · CÓMO se busca el operando ⇒ modo de direccionamiento", size=9.8)
    s.raw('<rect x="40" y="140" width="140" height="46" rx="3" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(110, 168, "CodOp", size=11.5, anchor="middle", weight="700")
    s.raw('<rect x="180" y="140" width="120" height="46" rx="3" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(240, 168, "modo", size=11.5, anchor="middle", weight="700")
    s.raw('<rect x="300" y="140" width="160" height="46" rx="3" fill="#dcfce7" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(380, 168, "operando / dirección", size=10.5, anchor="middle", weight="700")
    s.text(490, 158, "Una instrucción de máquina, campo por campo.", size=9.4, color="#4b5563")
    s.text(490, 176, "El largo total lo fija el formato (1, 2 o más palabras).", size=9.4, color="#4b5563")
    s.text(24, 216, "Clasificación por número de operandos (lo que se pregunta de memoria)", size=10.8, weight="700")
    for i, (n, d) in enumerate([("3 direcciones", "A ← B + C  (una instrucción, más bits)"),
                                ("2 direcciones", "A ← A + B  (destruye A)"),
                                ("1 dirección", "AC ← AC + M[D]  (acumulador: la BLUE)"),
                                ("0 direcciones", "pila: push, push, add  (todo implícito)")]):
        x = 40 + i * 220
        s.raw(f'<rect x="{x}" y="242" width="206" height="66" rx="5" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
        s.text(x + 12, 264, n, size=10.2, weight="700", color=ACCENT)
        s.text(x + 12, 288, d, size=8.8, color="#4b5563")
    s.text(24, 336, "Menos direcciones ⇒ instrucciones más cortas y más simples (bueno para RISC), pero más instrucciones para lo mismo.", size=9.8, color="#7c2d12")
    s.text(24, 358, "En la BLUE: 16 bits = 4 de opcode + 12 de dirección ⇒ 1 dirección (acumulador), 16 opcodes y 4 096 celdas direccionables.", size=9.8)
    s.text(24, 380, "Una instrucción NO dice el valor: dice DÓNDE está el valor. Esa diferencia es todo el tema de los modos de direccionamiento (5.3).", size=9.8, color="#4b5563")
    s.save("instruccion_partes.svg")


def d_clasificacion_instrucciones():
    s = Svg(920, 400, "Clasificación de las instrucciones de un repertorio")
    s.box(340, 52, 240, 46, "INSTRUCCIONES", "", fill="#dbeafe")
    grupos = [("Transferencia de datos", "LOAD · STORE · MOV · INP/OUT", "mueven datos, no los cambian"),
              ("Aritméticas", "ADD · SUB · MUL · DIV · INC · DEC", "operan con números"),
              ("Lógicas y de bits", "AND · OR · XOR · NOT · SHIFT · ROT", "bit a bit"),
              ("Control de flujo", "JMP · JZ · CALL · RET · HLT", "cambian el PC"),
              ("Entrada/salida", "IN · OUT · INP · OUT (BLUE)", "hablan con periféricos"),
              ("De control del sistema", "NOP · flags · interrupciones (EI/DI)", "gobiernan la máquina")]
    for k, (nom, ej, que) in enumerate(grupos):
        x = 40 + (k % 3) * 290
        y = 140 + (k // 3) * 110
        s.raw(f'<rect x="{x}" y="{y}" width="270" height="92" rx="5" fill="#f8fafc" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 12, y + 24, nom, size=10.4, weight="700", color=ACCENT)
        s.text(x + 12, y + 48, ej, size=8.8, family=MONO, color="#7c2d12")
        s.text(x + 12, y + 70, que, size=8.8, color="#4b5563")
    s.text(24, 380, "Lo que cambia el flujo (saltos, llamadas, retornos) es lo que rompe el pipeline: ver 7.1.2 (conflicto de control).", size=10.2)
    s.save("clasificacion_instrucciones.svg")


def d_ea_calculo():
    s = Svg(920, 410, "Dirección efectiva: qué se suma y cuántos accesos a memoria cuesta")
    s.text(24, 52, "EA = lo que hay que calcular para saber DÓNDE está el operando", size=11, weight="700")
    filas = [("Inmediato", "el operando es el dato", "EA = —", "0"),
             ("Directo (absoluto)", "la instrucción trae la dirección", "EA = D", "1"),
             ("Indirecto", "la instrucción trae la dirección de la dirección", "EA = M[D]", "2"),
             ("Por registro", "el operando está en un registro", "EA = R", "0"),
             ("Indexado", "dirección base + índice", "EA = D + R", "1"),
             ("Base + desplazamiento", "posición del registro + desplazamiento", "EA = R + d", "1"),
             ("Relativo al PC", "posición actual + desplazamiento", "EA = PC + d", "1"),
             ("Pila (implícito)", "el SP ya dice dónde", "EA = SP", "1")]
    y0 = 82
    s.text(40, y0, "Modo", size=10, weight="700")
    s.text(230, y0, "Qué hace", size=10, weight="700")
    s.text(620, y0, "Fórmula", size=10, weight="700")
    s.text(800, y0, "Accesos", size=10, weight="700")
    for i, (m, d, f, a) in enumerate(filas):
        y = y0 + 26 + i * 28
        if i % 2 == 0:
            s.raw(f'<rect x="32" y="{y-18}" width="862" height="26" rx="3" fill="#f8fafc"/>')
        s.text(40, y, m, size=9.6, weight="700")
        s.text(230, y, d, size=9.4, color="#4b5563")
        s.text(620, y, f, size=9.6, family=MONO, color="#7c2d12")
        s.text(808, y, a, size=9.6, family=MONO, weight="700", color=ACCENT)
    s.text(24, 350, "Costo = accesos a memoria para traer el operando (más 1 para la búsqueda de la instrucción). El indirecto es el más caro: 2 o 3 accesos.", size=9.8, color="#7c2d12")
    s.text(24, 372, "El indexado es el que hace posible recorrer un vector: cambia el índice, no la instrucción (es el bucle FOR del hardware). ¡Por eso la BLUE indexada tiene 24 pulsos!", size=9.8)
    s.text(24, 394, "Regla: más modos = más flexibilidad y menos instrucciones, pero más bits de modo y más ciclos de cálculo de dirección.", size=9.8, color="#4b5563")
    s.save("ea_calculo.svg")


def d_rif_rid_rb():
    s = Svg(920, 400, "La BLUE indexada: RIF, RID y RB más el modificador de 2 bits")
    s.text(24, 52, "Tres registros que la BLUE original no tenía", size=10.8, weight="700")
    s.box(50, 80, 190, 60, "RIF", "índice · incrementa solo", fill="#dbeafe")
    s.box(50, 160, 190, 60, "RID", "puntero de pila · apila/desapila", fill="#dbeafe")
    s.box(50, 240, 190, 60, "RB", "base · desplaza el bloque", fill="#dbeafe")
    s.text(270, 108, "se usa con el modo indexado: EA = D + RIF (y RIF sube o baja)", size=9.2, color="#4b5563")
    s.text(270, 188, "SP ⇒ permite anidar interrupciones y subrutinas", size=9.2, color="#4b5563")
    s.text(270, 268, "se suma a la dirección para mover un programa en memoria", size=9.2, color="#4b5563")
    s.raw('<rect x="50" y="322" width="190" height="46" rx="4" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.4"/>')
    s.text(145, 350, "modificador (2 bits)", size=9.6, anchor="middle", weight="700")
    s.text(270, 338, "00 sin índice · 01 incrementa · 10 decrementa · 11 usa puntero (o RB)", size=9.2, color="#7c2d12")
    s.text(270, 356, "Son 4 combinaciones porque el campo tiene 2 bits ⇒ 2² = 4.", size=9.2, color="#4b5563")
    s.raw('<rect x="640" y="80" width="256" height="130" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(656, 102, "Por qué 24 pulsos", size=10.4, weight="700")
    s.text(656, 124, "8 pulsos de búsqueda", size=9.2)
    s.text(656, 142, "+ 8 de ejecución", size=9.2)
    s.text(656, 160, "+ 8 de la indexación (calcular", size=9.2, color="#4b5563")
    s.text(656, 176, "  EA = D + RIF y actualizar RIF)", size=9.2, color="#4b5563")
    s.text(656, 196, "= 24 pulsos = 3 µs", size=9.4, weight="700", color="#7c2d12")
    s.text(24, 384, "La BLUE original (unidad 4) no tiene estos registros: la indexada los agrega para recorrer vectores y usar pila. Eso agrega pulsos a la instrucción.", size=9.8)
    s.save("rif_rid_rb.svg")


def d_irq_logica():
    s = Svg(920, 400, "La lógica de la interrupción: IRQ · SI · CP8")
    s.text(24, 52, "El periférico pide, la CPU decide y sólo acepta al final de la instrucción", size=10.8, weight="700")
    for i in range(3):
        y = 90 + i * 44
        s.raw(f'<rect x="60" y="{y}" width="120" height="32" rx="4" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.3"/>')
        s.text(120, y + 21, f"bandera {i}", size=9.6, anchor="middle")
        s.line(180, y + 16, 250, y + 16)
    s.gate("OR", 250, 100, ["b0", "b1", "b2"], "IRQ", w=70, h=70, stub=26, isize=9.4)
    s.gate("AND", 420, 108, ["IRQ", "SI", "CP8"], "aceptar", w=80, h=70, stub=30, isize=9.4)
    s.text(60, 228, "IRQ = OR de todas las banderas: un solo cable hacia la CPU.", size=9.4, color="#4b5563")
    s.text(60, 246, "Se acepta sólo si SI = 1 (habilitado) y CP8 = 1 (fin de la instrucción).", size=9.4, color="#4b5563")
    s.raw('<rect x="600" y="90" width="296" height="120" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(616, 112, "Si falta una, no pasa nada", size=10.2, weight="700")
    s.text(616, 134, "IRQ = 0 ⇒ no hay pedido.", size=9.2)
    s.text(616, 152, "SI = 0 ⇒ el pedido queda PENDIENTE", size=9.2, color="#4b5563")
    s.text(616, 168, "  (máscara: se posterga, no se borra).", size=9.2, color="#4b5563")
    s.text(616, 186, "CP8 = 0 ⇒ hay que esperar al final.", size=9.2, color=RED)
    s.text(616, 202, "  Nunca se corta una instrucción.", size=9.2, color=RED)
    s.text(24, 268, "La secuencia completa (los 8 pulsos del ciclo de interrupción)", size=10.8, weight="700")
    pulsos = [("CP1", "SI ← 0", "no anidar sin control"), ("CP2", "PC al MBR", "se guarda la vuelta"),
              ("CP3", "M[0] ← PC", "posición 0 = dirección de retorno"), ("CP4", "PC ← 1", "la rutina empieza en 1"),
              ("CP5-CP7", "—", "la rutina ya corre"), ("CP8", "I ← 0", "termina el reconocimiento")]
    for i, (cp, acc, com) in enumerate(pulsos):
        y = 282 + (i % 3) * 30
        x = 40 + (i // 3) * 440
        s.raw(f'<rect x="{x}" y="{y}" width="60" height="26" rx="3" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(x + 30, y + 18, cp, size=8.8, anchor="middle", weight="700", color=ACCENT)
        s.text(x + 68, y + 18, acc, size=9.2, family=MONO, weight="700")
        s.text(x + 190, y + 18, com, size=8.6, color="#4b5563")
    s.text(24, 392, "Con RTI se recupera el PC de la posición 0 y se vuelve a poner SI = 1: el programa no se entera de nada.", size=9.6, color="#4b5563")
    s.save("irq_logica.svg")


def d_pila_rti():
    s = Svg(920, 410, "La pila: guardar y recuperar el contexto sin pisar nada")
    s.text(24, 52, "Pila LIFO: el último que entra es el primero que sale (SP apunta al tope)", size=10.8, weight="700")
    for i in range(6):
        y = 80 + i * 34
        s.raw(f'<rect x="70" y="{y}" width="150" height="30" rx="3" fill="{"#dbeafe" if i < 3 else "#f8fafc"}" stroke="{STROKE}" stroke-width="1.2"/>')
        if i < 3:
            s.text(145, y + 20, ["ret 3", "ret 2", "ret 1"][i], size=9.4, anchor="middle", family=MONO)
    s.arrow(30, 176, 66, 176, color=ACCENT)
    s.text(26, 180, "SP", size=9.4, anchor="end", color=ACCENT)
    s.text(240, 100, "Al llamar (SRJ / CALL / interrupción):", size=9.6, weight="700")
    s.text(240, 120, "SP ← SP − 1 y luego M[SP] ← PC", size=9.4, family=MONO, color="#7c2d12")
    s.text(240, 148, "Al volver (RET / RTI):", size=9.6, weight="700")
    s.text(240, 168, "PC ← M[SP] y luego SP ← SP + 1", size=9.4, family=MONO, color="#7c2d12")
    s.text(240, 196, "La pila crece hacia abajo en casi todas las máquinas.", size=9.4, color="#4b5563")
    s.text(24, 264, "Anidamiento: una interrupción dentro de otra", size=10.8, weight="700")
    s.raw('<rect x="40" y="282" width="860" height="76" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(56, 304, "programa → IRQ1 (apila PC) → rutina 1 → IRQ2 (apila PC de la rutina 1) → rutina 2 → RTI (vuelve a la rutina 1) → RTI (vuelve al programa)", size=9.6)
    s.text(56, 324, "Sin pila: la segunda interrupción PISA la dirección de retorno de la primera y el primer RTI vuelve a cualquier lado (el programa 'salta al vacío').", size=9.6, color=RED)
    s.text(56, 344, "Por eso el SP es obligatorio: es lo que hace que la interrupción sea transparente aun con anidamiento.", size=9.6, color="#4b5563")
    s.text(24, 384, "En la BLUE de la cátedra la interrupción usa una posición fija (M[0]) en vez de pila; con SP se puede anidar. En el 8086 la pila va con SS:SP.", size=9.8)
    s.save("pila_rti.svg")


def d_biu_eu_cola():
    s = Svg(920, 400, "El 8086: BIU y EU trabajando en paralelo con la cola de instrucciones")
    s.box(50, 70, 300, 120, "", "", fill="#dbeafe")
    s.text(66, 96, "BIU (unidad de interfaz con el bus)", size=9.8, weight="700")
    s.text(66, 118, "calcula direcciones físicas", size=9, color="#4b5563")
    s.text(66, 136, "CS:IP · DS · SS:SP · ES", size=9, family=MONO, color="#4b5563")
    s.text(66, 158, "busca instrucciones ADELANTÁNDOSE", size=9, color=RED)
    s.text(66, 176, "y las apila en la cola", size=9, color=RED)
    s.box(50, 240, 300, 100, "", "", fill="#dcfce7")
    s.text(66, 266, "EU (unidad de ejecución)", size=9.8, weight="700")
    s.text(66, 288, "decodifica y ejecuta", size=9, color="#4b5563")
    s.text(66, 306, "ALU, flags, registros AX/BX/CX/DX", size=9, family=MONO, color="#4b5563")
    s.text(66, 324, "NO toca el bus de memoria", size=9, color="#15803d")
    s.raw('<rect x="440" y="96" width="300" height="46" rx="4" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(590, 116, "COLA DE 6 BYTES", size=10, anchor="middle", weight="700")
    s.text(590, 134, "FIFO: la BIU llena, la EU vacía", size=8.8, anchor="middle", color="#4b5563")
    s.arrow(350, 120, 436, 120); s.text(360, 112, "instrucciones", size=8.6, color=RED)
    s.arrow(440, 202, 352, 244)
    s.text(358, 268, "la EU lee de la cola (no del bus)", size=8.6, color="#15803d")
    s.box(790, 96, 110, 46, "MEMORIA", "", fill="#e0e7ff")
    s.arrow(744, 120, 786, 120)
    s.arrow(786, 134, 744, 134)
    s.text(24, 366, "Es el primer pipeline comercial: mientras la EU ejecuta una instrucción, la BIU ya trajo las siguientes. Si la EU salta, la cola se descarta (penalidad).", size=9.8)
    s.text(24, 388, "Segmentación: dir. física = segmento × 16 + desplazamiento (20 bits = 1 MB con registros de 16 bits). Ver 5.6.1 y la señal BREQ del tema de buses.", size=9.8, color="#4b5563")
    s.save("biu_eu_cola.svg")


# ══════════════════════════ UNIDAD 6 ══════════════════════════
def d_micropc_flujo():
    s = Svg(920, 400, "Microprogramado: la microinstrucción y el secuenciamiento del microPC")
    s.text(24, 52, "Cada microinstrucción es una palabra partida en campos", size=10.8, weight="700")
    campos = [("señales de control", "abre buffers y carga registros", 320, "#dbeafe"),
              ("salto", "qué hacer con el microPC", 150, "#fef3c7"),
              ("dirección", "a dónde ir si salta", 150, "#dcfce7"),
              ("condición", "qué mirar para saltar", 180, "#fce7f3")]
    x = 40
    for nom, d, w, col in campos:
        s.raw(f'<rect x="{x}" y="80" width="{w}" height="52" rx="3" fill="{col}" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + w / 2, 102, nom, size=9.2, anchor="middle", weight="700")
        s.text(x + w / 2, 120, d, size=8, anchor="middle", color="#4b5563")
        x += w
    s.text(24, 168, "Secuenciamiento: de dónde sale la próxima microdirección", size=10.8, weight="700")
    s.box(60, 190, 220, 56, "microPC", "contador de microdirección", fill="#dcfce7")
    s.box(340, 190, 200, 56, "MEMORIA DE CONTROL", "ROM de microcódigo", fill="#dbeafe")
    s.box(600, 190, 190, 56, "REGISTRO", "de microinstrucción", fill="#fef3c7")
    s.arrow(280, 218, 336, 218); s.arrow(540, 218, 596, 218)
    s.arrow(695, 246, 695, 290)
    s.text(700, 276, "sus campos vuelven al microPC", size=8.8, color="#4b5563")
    s.arrow(695, 292, 170, 292); s.arrow(170, 292, 170, 250)
    s.text(190, 312, "1 · incrementar  2 · saltar  3 · salto condicional  4 · mapear el opcode", size=9, family=MONO, color="#7c2d12")
    s.raw('<rect x="24" y="322" width="872" height="66" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 344, "Mapeo: al empezar una instrucción, el opcode se pone en el microPC (o en un registro de mapeo) ⇒ cada instrucción tiene su microprograma.", size=9.6)
    s.text(40, 364, "Ventaja: cambiar el repertorio = cambiar el contenido de la ROM, sin tocar cables. Desventaja: más lento (una lectura de ROM por microinstrucción).", size=9.6, color="#4b5563")
    s.save("micropc_flujo.svg")


def d_cableada_vs_micro():
    s = Svg(920, 400, "Control cableado vs control microprogramado, lado a lado")
    s.raw('<rect x="24" y="46" width="424" height="230" rx="6" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.4"/>')
    s.text(40, 70, "CABLEADA (hardwired)", size=11.5, weight="700", color=ACCENT)
    s.text(40, 96, "Compuertas y biestables fijos.", size=9.6)
    s.text(40, 118, "· velocidad: máxima (sin leer memoria)", size=9.6, color="#15803d")
    s.text(40, 140, "· costo: crece con la complejidad", size=9.6, color="#7c2d12")
    s.text(40, 162, "· cambiar el repertorio = rediseñar", size=9.6, color=RED)
    s.text(40, 184, "· difícil de depurar y de corregir", size=9.6, color="#4b5563")
    s.text(40, 206, "· se usa en RISC, con repertorio chico", size=9.6)
    s.text(40, 232, "La UC cableada es una función combinacional:", size=9.2, color="#4b5563")
    s.text(40, 250, "señal = f(estado, pulso, opcode).", size=9.2, family=MONO, color="#7c2d12")
    s.raw('<rect x="472" y="46" width="424" height="230" rx="6" fill="#dcfce7" stroke="#86efac" stroke-width="1.4"/>')
    s.text(488, 70, "MICROPROGRAMADA", size=11.5, weight="700", color="#15803d")
    s.text(488, 96, "Una ROM con microinstrucciones.", size=9.6)
    s.text(488, 118, "· velocidad: menor (1 lectura por paso)", size=9.6, color="#7c2d12")
    s.text(488, 140, "· costo: fijo (la ROM)", size=9.6, color="#15803d")
    s.text(488, 162, "· cambiar el repertorio = reprogramar", size=9.6, color="#15803d")
    s.text(488, 184, "· fácil de corregir y de emular", size=9.6, color="#15803d")
    s.text(488, 206, "· se usa en CISC y en máquinas complejas", size=9.6)
    s.text(488, 232, "Cada microinstrucción es una palabra de la ROM:", size=9.2, color="#4b5563")
    s.text(488, 250, "señales + control del microPC.", size=9.2, family=MONO, color="#7c2d12")
    s.raw('<rect x="24" y="292" width="872" height="96" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 314, "Cómo decidir: si el repertorio es simple y fijo (RISC) ⇒ cableada; si es grande, irregular o tiene que poder corregirse (CISC) ⇒ microprogramada.", size=9.6)
    s.text(40, 336, "En la práctica se combinan: el 8086 tiene microcódigo para las instrucciones complejas y lógica cableada para las simples.", size=9.6, color="#4b5563")
    s.text(40, 358, "Dato de la cátedra: la ROM de control del 8088 es de 504 palabras × 21 bits ⇒ 10 584 bits de microcódigo.", size=9.6, color="#7c2d12")
    s.text(24, 404 - 4, "Es el mismo compromiso de CISC vs RISC (unidad 7.3): complejo en el hardware o complejo en el microcódigo.", size=9.8, color="#4b5563")
    s.save("cableada_vs_micro.svg")


def d_rom_control_8088():
    s = Svg(920, 400, "La ROM de control del 8088: 504 palabras de 21 bits")
    s.text(24, 52, "504 microinstrucciones × 21 bits = 10 584 bits de microcódigo", size=11, weight="700", family=MONO, color="#0f766e")
    s.raw('<rect x="60" y="86" width="230" height="150" rx="5" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.6"/>')
    s.text(175, 112, "ROM DE CONTROL", size=10.4, anchor="middle", weight="700")
    s.text(175, 134, "504 × 21", size=11, anchor="middle", family=MONO)
    s.text(175, 158, "cada palabra = 1 microinstrucción", size=8.8, anchor="middle", color="#4b5563")
    s.text(175, 180, "9 bits de dirección (2⁹ = 512 ≥ 504)", size=8.8, anchor="middle", color="#7c2d12")
    s.text(175, 202, "21 bits de salida", size=8.8, anchor="middle", color="#7c2d12")
    s.arrow(290, 120, 350, 120); s.text(296, 112, "microdirección", size=8.6, color="#4b5563")
    s.box(350, 96, 150, 56, "microPC", "9 bits", fill="#dcfce7")
    s.arrow(500, 124, 560, 124)
    s.box(560, 96, 170, 56, "registro de microinstrucción", "", fill="#fef3c7", size=9.4)
    s.arrow(690, 152, 780, 190)
    s.text(700, 210, "señales de control a toda la máquina", size=8.8, color="#4b5563")
    s.raw('<rect x="24" y="252" width="872" height="112" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 274, "Qué se pregunta de este dato", size=10.4, weight="700")
    s.text(40, 296, "1 · Cuántas microinstrucciones entran: 2^bits_de_dirección ≥ 504 ⇒ 9 bits (512).", size=9.6)
    s.text(40, 316, "2 · Tamaño total del microcódigo: 504 × 21 = 10 584 bits ≈ 1,3 KB.", size=9.6, family=MONO, color="#7c2d12")
    s.text(40, 336, "3 · Para qué sirven los 21 bits: señales de control internas + control del secuenciamiento (condición, salto, próxima dirección).", size=9.6, color="#4b5563")
    s.text(40, 356, "Es el ejemplo real que cierra la unidad: una máquina CISC resuelve sus instrucciones complejas leyendo microcódigo, paso por paso.", size=9.4, color="#4b5563")
    s.text(24, 388, "Comparación: en la BLUE cada instrucción son 8 o 16 pulsos fijos de hardware; en el 8088 cada instrucción es un microprograma de varias microinstrucciones.", size=9.8, color="#4b5563")
    s.save("rom_control_8088.svg")

# ══════════════════════════ UNIDAD 7 ══════════════════════════
def d_speedup_limites():
    s = Svg(920, 400, "Speedup: tiende a k y nunca lo alcanza")
    s.text(24, 52, "S(n) = k·n / (k + n − 1)  →  k   cuando n → ∞", size=11.5, weight="700", family=MONO, color="#0f766e")
    # gráfico de barras: speedup con k=5
    x0, y0 = 60, 250
    s.line(x0 - 10, y0, x0 + 380, y0, w=1.4)
    s.line(x0 - 10, y0, x0 - 10, 84, w=1.4)
    s.text(x0 - 16, 88, "5", size=9, anchor="end")
    s.text(x0 - 16, y0 + 4, "0", size=9, anchor="end")
    s.line(x0 - 6, 90, x0 + 380, 90, w=1, color=RED, dash="4,3")
    s.text(96, 80, "techo = k = 5", size=8.8, color=RED)
    for i, (n, sp) in enumerate([(3, 2.14), (5, 3.13), (10, 3.57), (25, 4.17), (100, 4.81), (1000, 4.98)]):
        h = sp / 5 * 160
        x = x0 + 10 + i * 60
        s.raw(f'<rect x="{x}" y="{y0-h}" width="40" height="{h}" rx="2" fill="#dbeafe" stroke="{ACCENT}" stroke-width="1.2"/>')
        s.text(x + 20, y0 - h - 6, f"{sp:.2f}", size=8.6, anchor="middle", color="#7c2d12")
        s.text(x + 20, y0 + 16, str(n), size=8.8, anchor="middle")
    s.text(x0 + 120, y0 + 34, "n (instrucciones)", size=9, color="#4b5563")
    s.text(24, 300, "Con k = 5 etapas: S(3) = 2,14 · S(100) = 4,81 · S(1000) = 4,98. Nunca llega a 5.", size=9.8)
    s.text(24, 320, "Por qué: hay que llenar el pipeline (k − 1 ciclos) y ese costo se reparte entre n instrucciones.", size=9.8, color="#4b5563")
    s.raw('<rect x="470" y="70" width="426" height="180" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(486, 92, "Ejemplo con penalidades (el del final)", size=10.4, weight="700")
    s.text(486, 114, "5 etapas · 100 instrucciones · 20 load-use · 15 saltos", size=9.2, color="#4b5563")
    s.text(486, 138, "serie:        5 × 100 = 500 ciclos", size=9.4, family=MONO)
    s.text(486, 158, "ideal:        5 + 99 = 104 ciclos", size=9.4, family=MONO, color="#15803d")
    s.text(486, 178, "+ 20 stalls = 124      ⇒ S = 4,03", size=9.4, family=MONO, color="#7c2d12")
    s.text(486, 198, "+ 15 por saltos = 139  ⇒ S = 3,60", size=9.4, family=MONO, color=RED)
    s.text(486, 218, "CPI = 139/100 = 1,39   (ideal 1,00)", size=9.4, family=MONO, color=RED)
    s.text(486, 240, "La diferencia entre 5 y 3,60 es lo que 'cuesta' la realidad.", size=9.2, color="#4b5563")
    s.text(24, 356, "Qué se pregunta: ciclos ideales, ciclos reales, speedup ideal y real, CPI. Y siempre el techo: no se puede superar k.", size=10.2)
    s.text(24, 378, "Truco para no equivocarse: la penalidad se SUMA a los ciclos, aparte del k + (n − 1). Nunca se resta ni se promedia.", size=9.8, color="#7c2d12")
    s.save("speedup_limites.svg")


def d_anchura_superscalar_smt():
    s = Svg(920, 400, "Más ancho, más hilos, más núcleos: cuatro formas de ir más rápido")
    s.text(24, 52, "1 · Escalar", size=9.8, weight="700")
    for i in range(3):
        x = 190 + i * 52
        s.raw(f'<rect x="{x}" y="44" width="44" height="18" rx="2" fill="#dbeafe" stroke="{STROKE}" stroke-width="1"/>')
    s.text(360, 58, "1 instrucción por ciclo", size=8.8, color="#4b5563")
    s.text(24, 100, "2 · Superscalar", size=9.8, weight="700")
    for row in range(4):
        for i in range(3):
            x = 190 + i * 52
            y = 86 + row * 22
            s.raw(f'<rect x="{x}" y="{y}" width="44" height="18" rx="2" fill="#dcfce7" stroke="{STROKE}" stroke-width="1"/>')
    s.text(360, 100, "4 vías ⇒ CPI ideal 0,25", size=8.4, color="#15803d")
    s.text(24, 190, "3 · SMT", size=9.8, weight="700")
    for row in range(2):
        for i in range(3):
            x = 190 + i * 52
            y = 176 + row * 22
            s.raw(f'<rect x="{x}" y="{y}" width="44" height="18" rx="2" fill="{"#fef3c7" if row == 0 else "#fce7f3"}" stroke="{STROKE}" stroke-width="1"/>')
    s.text(360, 196, "2 hilos: llena huecos de memoria", size=8.4, color="#7c2d12")
    s.text(24, 262, "4 · Multicore", size=9.8, weight="700")
    for c in range(4):
        x = 190 + c * 56
        s.raw(f'<rect x="{x}" y="248" width="50" height="46" rx="3" fill="#e0e7ff" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(x + 25, 276, f"CPU{c}", size=8.2, anchor="middle")
    s.text(430, 276, "n núcleos, cada uno con su L1/L2", size=8.6, color="#4b5563")
    s.raw('<rect x="620" y="44" width="276" height="250" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(636, 66, "Los números del ejemplo", size=10.4, weight="700")
    s.text(636, 90, "4 núcleos × 2 vías × 2 hilos", size=9.2, color="#4b5563")
    s.text(636, 110, "= 16 instrucciones por ciclo", size=9.6, weight="700", color=ACCENT)
    s.text(636, 132, "a 3 GHz ⇒ 48·10⁹ instr/s teóricas", size=9.4, family=MONO, color="#7c2d12")
    s.text(636, 156, "En la práctica: la mitad o menos.", size=9.2, color=RED)
    s.text(636, 182, "Por qué no se cumple:", size=9.2, weight="700")
    s.text(636, 200, "· dependencias entre instrucciones", size=8.8, color="#4b5563")
    s.text(636, 216, "· fallos de caché y de predicción", size=8.8, color="#4b5563")
    s.text(636, 232, "· leyes de Amdahl y de rendimientos", size=8.8, color="#4b5563")
    s.text(636, 246, "  decrecientes", size=8.8, color="#4b5563")
    s.text(636, 266, "· coherencia de caché entre núcleos", size=8.8, color="#4b5563")
    s.text(24, 330, "Superpipeline (más etapas) ataca la FRECUENCIA; superscalar, la ANCHURA; SMT, los HUECOS; multicore, el PARALELISMO de programa.", size=9.8)
    s.text(24, 352, "Cada técnica tiene un costo: más etapas ⇒ más penalidad por salto; más vías ⇒ más hardware y más lógica de detección de dependencias.", size=9.8, color="#4b5563")
    s.text(24, 374, "De ahí el techo real: 4 núcleos × 4 vías no dan 16× porque el programa no tiene tanto paralelismo disponible (ver Amdahl en 8.4.1).", size=9.8, color="#7c2d12")
    s.save("anchura_superscalar_smt.svg")


def d_prediccion_saltos():
    s = Svg(920, 400, "Predicción de saltos: adivinar para no frenar el pipeline")
    s.text(24, 52, "Por qué hace falta: cuando llega un salto, la etapa de búsqueda no sabe qué traer", size=10.4, weight="700")
    # predictor de 2 bits
    s.text(24, 92, "Predictor dinámico de 2 bits (máquina de estados)", size=10.4, weight="700")
    estados = [("00", "no tomar\n(seguro)"), ("01", "casi no\ntomar"), ("10", "casi\ntomar"), ("11", "tomar\n(seguro)")]
    coords = [(70, 130), (230, 130), (390, 130), (550, 130)]
    for (et, nom), (x, y) in zip(estados, coords):
        s.raw(f'<rect x="{x}" y="{y}" width="140" height="56" rx="6" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.5"/>')
        s.text(x + 70, y + 24, et, size=11, anchor="middle", weight="700", family=MONO, color=ACCENT)
        s.text(x + 70, y + 44, nom.replace("\n", " "), size=8.4, anchor="middle", color="#4b5563")
    s.arrow(210, 150, 228, 150); s.arrow(370, 150, 388, 150); s.arrow(530, 150, 548, 150)
    s.text(160, 200, "tomó", size=8.4, color="#15803d")
    s.text(320, 200, "tomó", size=8.4, color="#15803d")
    s.text(470, 200, "tomó", size=8.4, color="#15803d")
    s.arrow(228, 180, 210, 180); s.arrow(388, 180, 370, 180); s.arrow(548, 180, 530, 180)
    s.text(160, 196, "", size=8)
    s.text(300, 232, "no tomó (vuelve)", size=8.6, color=RED)
    s.text(60, 252, "Hacen falta DOS errores seguidos para cambiar de opinión: así los lazos no engañan al predictor.", size=8.8, color="#4b5563")
    s.raw('<rect x="700" y="84" width="196" height="180" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(716, 106, "Acierto típico", size=10.2, weight="700")
    s.text(716, 128, "estático: 50-70 %", size=9)
    s.text(716, 146, "dinámico 2 bits: 85-90 %", size=9)
    s.text(716, 164, "con historial: 95 %+", size=9, color="#15803d")
    s.text(716, 188, "BTB: guarda la dirección", size=8.6, color="#4b5563")
    s.text(716, 204, "del salto ya tomado", size=8.6, color="#4b5563")
    s.text(716, 228, "Retorno (RET/RTI):", size=8.6, color="#4b5563")
    s.text(716, 244, "pila de direcciones", size=8.6, color="#4b5563")
    s.text(24, 274, "El costo de equivocarse (el cálculo del final)", size=10.4, weight="700")
    s.raw('<rect x="24" y="288" width="872" height="96" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 310, "1 000 instrucciones · 200 saltos (20 %) · penalidad 5 ciclos", size=9.6)
    s.text(40, 332, "90 % de acierto ⇒ 20 fallos × 5 = 100 ciclos ⇒ CPI = 1,10      ·      95 % ⇒ 10 × 5 = 50 ciclos ⇒ CPI = 1,05", size=9.6, family=MONO, color="#7c2d12")
    s.text(40, 354, "Subir el acierto 5 puntos recorta la MITAD de la pérdida: por eso los predictores son tan caros y tan importantes.", size=9.6, color="#15803d")
    s.text(40, 374, "Un salto mal predicho descarta las instrucciones que ya entraron al pipeline: no es gratis aunque el salto 'era lógico'.", size=9.6, color="#4b5563")
    s.text(24, 396, "Complementos: delay slot (MIPS: la instrucción siguiente se ejecuta siempre) y saltos retardados por el compilador.", size=9.6, color="#4b5563")
    s.save("prediccion_saltos.svg")


def d_load_store_risc():
    s = Svg(920, 400, "Por qué RISC es load/store y cableado: la cadena que lo explica todo")
    s.text(24, 52, "La cadena causal (la respuesta del final)", size=10.8, weight="700")
    pasos = [("instrucciones\nsimples", "pocas y\nuniformes"), ("control\ncableado", "sin microcódigo"),
             ("1 ciclo por\ninstrucción", "CPI ≈ 1"), ("pipeline\nnatural", "etapas parejas"),
             ("load/store", "la memoria sólo en\n2 instrucciones")]
    for i, (a, b) in enumerate(pasos):
        x = 30 + i * 172
        s.raw(f'<rect x="{x}" y="78" width="150" height="76" rx="6" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.5"/>')
        for k, ln in enumerate(a.split("\n")):
            s.text(x + 75, 102 + k * 15, ln, size=9.2, anchor="middle", weight="700")
        for k, ln in enumerate(b.split("\n")):
            s.text(x + 75, 132 + k * 13, ln, size=8.2, anchor="middle", color="#4b5563")
        if i < 4:
            s.arrow(x + 152, 116, x + 168, 116)
    s.text(24, 190, "Qué significa load/store en la práctica", size=10.6, weight="700")
    s.text(40, 214, "RISC:  a = b + c  ⇒  LOAD R1,b  ·  LOAD R2,c  ·  ADD R3,R1,R2  ·  STORE a,R3   (4 instrucciones)", size=9.6, family=MONO)
    s.text(40, 236, "CISC:  a = b + c  ⇒  ADD [a],[b],[c]                                            (1 instrucción, varios ciclos)", size=9.6, family=MONO)
    s.text(40, 262, "Ventaja del load/store: todas las operaciones son entre registros ⇒ duración pareja ⇒ el pipeline no se traba esperando memoria.", size=9.6, color="#15803d")
    s.text(40, 282, "Costo: más instrucciones y más registros (se necesitan 32 o más para no estar yendo y viniendo a memoria).", size=9.6, color="#7c2d12")
    s.raw('<rect x="24" y="300" width="872" height="84" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 322, "El número que cierra el argumento: vector de 100 elementos ⇒ CISC 500 instrucciones × CPI 3 = 1 500 ciclos contra RISC 800 × 1,1 = 880.", size=9.6)
    s.text(40, 344, "RISC gana 1,7× con 60 % más instrucciones: importa el CPI, no la cantidad de instrucciones.", size=9.6, color="#7c2d12")
    s.text(40, 366, "Y por eso la UC cableada (unidad 6) va con RISC: si cada instrucción es simple, no hace falta microcódigo para resolverla.", size=9.6, color="#4b5563")
    s.save("load_store_risc.svg")


# ══════════════════════════ UNIDAD 8 ══════════════════════════
def d_encadenamiento():
    s = Svg(920, 400, "Encadenamiento (chaining) en el pipeline aritmético")
    s.text(24, 52, "Sin encadenamiento: cada operación espera el resultado completo de la anterior", size=10.2, weight="700")
    for i in range(6):
        x = 60 + i * 130
        s.raw(f'<rect x="{x}" y="72" width="110" height="26" rx="3" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(x + 55, 90, f"suma {i+1}", size=8.8, anchor="middle")
    s.text(24, 118, "cada suma ocupa 4 ciclos de la etapa de suma ⇒ 6 sumas = 24 ciclos", size=9.4, color=RED)
    s.text(24, 152, "Con encadenamiento: el resultado parcial se pasa a la etapa siguiente sin esperar", size=10.2, weight="700")
    for i in range(6):
        x = 60 + (i % 3) * 120
        y = 172 + (i // 3) * 26
        s.raw(f'<rect x="{x}" y="{y}" width="110" height="20" rx="3" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(x + 55, y + 14, f"suma {i+1}", size=8.4, anchor="middle")
    s.text(24, 250, "los resultados se pasan de etapa en etapa: se solapan varias sumas a la vez", size=9.2, color="#15803d")
    s.raw('<rect x="470" y="160" width="426" height="112" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(486, 182, "El cálculo", size=10.2, weight="700")
    s.text(486, 204, "k etapas de suma de t ciclos, n operaciones:", size=9, color="#4b5563")
    s.text(486, 224, "T = k·t + (n − 1)·t      S = k·n / (k + n − 1)", size=9.4, family=MONO, color="#7c2d12")
    s.text(486, 246, "Con k = 4, t = 1, n = 100 ⇒ T = 103, S = 3,88", size=9.2, family=MONO)
    s.text(24, 300, "Diferencia con el pipeline de instrucciones: ahí se solapan INSTRUCCIONES; acá se solapan ETAPAS de una misma operación vectorial.", size=9.8)
    s.text(24, 322, "Es lo que hace un procesador vectorial: una instrucción de suma procesa 64 elementos, y el encadenamiento aprovecha la etapa libre.", size=9.8, color="#4b5563")
    s.text(24, 344, "Limitación: sólo sirve si las operaciones son independientes y la etapa es segmentable (suma sí, división casi no).", size=9.8, color="#7c2d12")
    s.text(24, 366, "Sin encadenamiento el resultado del vector tarda n × latencia; con encadenamiento, n + k − 1 pasos.", size=9.8, color="#4b5563")
    s.save("encadenamiento.svg")


def d_simd_registros():
    s = Svg(920, 400, "SIMD: una instrucción, varios datos")
    s.text(24, 52, "Un registro ancho se parte en lanes: se opera con todos a la vez", size=10.4, weight="700")
    s.text(24, 80, "Registro de 32 bits partido en 4 lanes de 8 bits", size=9.4, color="#4b5563")
    for i in range(4):
        x = 60 + i * 100
        s.raw(f'<rect x="{x}" y="94" width="94" height="34" rx="3" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 47, 116, f"a{i}", size=10, anchor="middle", family=MONO)
    s.text(470, 108, "+   (UNA instrucción ADD)", size=9.6, weight="700", color=ACCENT)
    for i in range(4):
        x = 60 + i * 100
        s.raw(f'<rect x="{x}" y="140" width="94" height="34" rx="3" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 47, 162, f"b{i}", size=10, anchor="middle", family=MONO)
    for i in range(4):
        x = 60 + i * 100
        s.raw(f'<rect x="{x}" y="200" width="94" height="34" rx="3" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 47, 222, f"a{i}+b{i}", size=9.2, anchor="middle", family=MONO)
        s.arrow(x + 47, 176, x + 47, 196)
    s.text(480, 214, "4 sumas en el tiempo de 1 ⇒ 4× de rendimiento", size=9.6, color="#15803d")
    s.text(480, 232, "sin tocar la frecuencia ni el repertorio", size=9.2, color="#4b5563")
    s.raw('<rect x="24" y="256" width="872" height="128" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 278, "Dónde se usa y qué límites tiene", size=10.4, weight="700")
    s.text(40, 300, "SSE/AVX (x86): registros de 128-512 bits · NEON (ARM) · vectoriales de 64 lanes en GPUs.", size=9.6)
    s.text(40, 320, "GPU: miles de lanes simples (SIMT) contra pocos lanes anchos de la CPU; el mismo programa sobre datos distintos.", size=9.6, color="#4b5563")
    s.text(40, 340, "Límite 1: el programa tiene que tener datos paralelos (multiplicar matrices sí; un cálculo en cadena no).", size=9.6, color="#7c2d12")
    s.text(40, 360, "Límite 2: hay que EMPAQUETAR y DESEMPAQUETAR los datos (si vienen de a uno, se pierde lo ganado). Límite 3: las máscaras/condicionales.", size=9.6, color="#7c2d12")
    s.save("simd_registros.svg")


def d_matriz_simd():
    s = Svg(920, 400, "Multiplicación de matrices con SIMD: el ejemplo clásico de paralelismo de datos")
    s.text(24, 52, "C = A × B: cada elemento de C es un producto escalar (fila de A · columna de B)", size=10.4, weight="700")
    # A
    s.text(40, 84, "A (fila i)", size=9.2, weight="700")
    for j in range(3):
        s.raw(f'<rect x="{60 + j*54}" y="92" width="50" height="30" rx="2" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(85 + j * 54, 112, f"a{j}", size=9, anchor="middle", family=MONO)
    # B
    s.text(280, 84, "B (columna j)", size=9.2, weight="700")
    for j in range(3):
        s.raw(f'<rect x="300" y="{92 + j*34}" width="50" height="30" rx="2" fill="#fef3c7" stroke="{STROKE}" stroke-width="1.2"/>')
        s.text(325, 112 + j * 34, f"b{j}", size=9, anchor="middle", family=MONO)
    s.text(400, 130, "producto escalar: multiplicar y acumular", size=9.2, color="#4b5563")
    s.text(400, 150, "⇒ con SIMD se multiplican los 3 pares a la vez", size=9.2, color="#15803d")
    s.text(400, 170, "⇒ 1 instrucción vectorial en vez de 3 (o 8, o 16)", size=9.2, color="#15803d")
    s.raw('<rect x="24" y="196" width="872" height="88" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 218, "Cómo se paraleliza en la práctica", size=10.4, weight="700")
    s.text(40, 240, "1 · por elementos de C: cada lane calcula un C[i][j] distinto (mismo patrón, datos distintos ⇒ SIMD/SIMT perfecto).", size=9.4)
    s.text(40, 258, "2 · por bloques (tiling): se traen submatrices que entran en caché y se reutilizan ⇒ menos accesos a memoria.", size=9.4, color="#4b5563")
    s.text(40, 276, "3 · con varios núcleos: se reparten filas de C (memoria compartida o paso de mensajes).", size=9.4, color="#4b5563")
    s.text(24, 310, "Costo: para un N×N hay N³ multiplicaciones, pero sólo N² resultados ⇒ mucha operación por cada dato (por eso la GPU gana: tiene miles de lanes).", size=9.6)
    s.text(24, 332, "Ejemplo de cuenta: matriz de 100×100 ⇒ 1 000 000 de multiplicaciones. Con 4 lanes SIMD ⇒ 250 000 ciclos de multiplicación (ideal).", size=9.6, family=MONO, color="#7c2d12")
    s.text(24, 354, "Y eso sin contar los accesos a memoria: si los datos no están en caché, el cuello de botella deja de ser la ALU y pasa a ser la memoria.", size=9.6, color="#4b5563")
    s.text(24, 376, "Es el mismo argumento del tema 2.5 (localidad) llevado al paralelismo: primero los datos, después las operaciones.", size=9.6, color="#4b5563")
    s.save("matriz_simd.svg")


def d_conflictos_banco():
    s = Svg(920, 400, "Memoria entrelazada: dirección módulo bancos y conflictos de banco")
    s.text(24, 52, "Cuatro bancos: dirección módulo 4 decide el banco", size=10.4, weight="700")
    for i in range(4):
        x = 60 + i * 200
        s.raw(f'<rect x="{x}" y="76" width="180" height="60" rx="4" fill="#dbeafe" stroke="{STROKE}" stroke-width="1.4"/>')
        s.text(x + 90, 100, f"BANCO {i}", size=10, anchor="middle", weight="700")
        s.text(x + 90, 120, f"direcciones ≡ {i} (mod 4)", size=8.4, anchor="middle", color="#4b5563")
    s.text(24, 166, "Sin conflicto: direcciones 0, 1, 2, 3 ⇒ un elemento por banco ⇒ los 4 en un ciclo", size=9.8, color="#15803d")
    for i in range(4):
        x = 60 + i * 200
        s.raw(f'<rect x="{x}" y="182" width="180" height="28" rx="3" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.1"/>')
        s.text(x + 90, 201, f"dir {i}", size=9, anchor="middle", family=MONO)
    s.text(24, 236, "Con conflicto: 0, 4, 8, 12 ⇒ todos caen en el banco 0 ⇒ se atienden de a uno (4 ciclos)", size=9.8, color=RED)
    for i, d in enumerate([0, 4, 8, 12]):
        x = 60 + i * 88
        s.raw(f'<rect x="{x}" y="252" width="80" height="28" rx="3" fill="#fecaca" stroke="{STROKE}" stroke-width="1.1"/>')
        s.text(x + 40, 271, f"dir {d}", size=8.6, anchor="middle", family=MONO)
    s.arrow(420, 266, 470, 266)
    s.raw('<rect x="474" y="252" width="90" height="28" rx="3" fill="#fecaca" stroke="{STROKE}" stroke-width="1.2"/>')
    s.text(519, 271, "banco 0 ×4", size=8.6, anchor="middle")
    s.text(580, 264, "⇒ 4 ciclos en vez de 1 (cuatro veces más lento)", size=9.4, color=RED)
    s.text(580, 282, "Pasa con matrices accedidas por columnas: stride = tamaño de la fila.", size=9.2, color="#4b5563")
    s.raw('<rect x="24" y="300" width="872" height="84" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 322, "Ancho de banda con b bancos de w bytes: B = (b × w) / t_ciclo. Cuatro bancos de 8 B cada 10 ns ⇒ 3,2 GB/s.", size=9.6, family=MONO)
    s.text(40, 344, "Solución al conflicto: elegir el stride coprimo con el número de bancos, o rellenar filas (padding) para que no coincidan.", size=9.6, color="#4b5563")
    s.text(40, 364, "Es la misma idea del tema 7.4: varios caminos en paralelo para que no haya que esperar turno. Y alimenta al pipeline aritmético del 8.1.", size=9.6, color="#4b5563")
    s.save("conflictos_banco.svg")


def d_amdahl_grafico():
    s = Svg(920, 400, "Ley de Amdahl y coherencia de caché en multiprocesadores")
    s.text(24, 52, "S = 1 / ((1 − p) + p/N)   —  p: fracción paralelizable, N: procesadores", size=11, weight="700", family=MONO, color="#0f766e")
    x0, y0 = 60, 250
    s.line(x0, y0, x0 + 360, y0, w=1.4); s.line(x0, y0, x0, 90, w=1.4)
    s.text(x0 - 14, 94, "8×", size=8.6, anchor="end"); s.text(x0 - 14, y0 + 4, "0", size=8.6, anchor="end")
    for i in range(1, 9):
        y = y0 - i * 20
        s.line(x0 - 4, y, x0, y, w=1)
    for p, col, lab in [(0.95, ACCENT, "p = 95 %"), (0.90, "#0f766e", "p = 90 %"), (0.50, RED, "p = 50 %")]:
        pts = []
        for k in range(1, 17):
            n = k
            sp = 1 / ((1 - p) + p / n)
            pts.append((x0 + (n - 1) * 22, y0 - sp * 20))
        s.poly(pts, color=col, w=2)
        s.text(x0 + 350, pts[-1][1] - 6, lab, size=8.6, anchor="end", color=col)
    s.text(x0 + 150, y0 + 22, "N procesadores (1 a 16)", size=8.8, color="#4b5563")
    s.text(24, 268, "Con p = 90 % el techo es S = 10 aunque haya infinitas CPUs; con p = 50 %, el techo es 2.", size=9.2, color="#7c2d12")
    s.raw('<rect x="470" y="70" width="426" height="180" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(486, 92, "Coherencia de caché", size=10.4, weight="700")
    s.text(486, 114, "Cada núcleo tiene su L1: si dos escriben la misma", size=9, color="#4b5563")
    s.text(486, 130, "variable, uno ve datos viejos.", size=9, color="#4b5563")
    s.text(486, 152, "Protocolos: MESI (Modified, Exclusive, Shared,", size=9)
    s.text(486, 168, "Invalid), snooping en el bus o directorio.", size=9)
    s.text(486, 190, "Costo: invalidar y refrescar líneas ⇒ el", size=9, color="#4b5563")
    s.text(486, 206, "paralelismo real nunca es N×.", size=9, color="#4b5563")
    s.text(486, 230, "Amdahl + coherencia = por qué 64 núcleos no dan 64×.", size=9, weight="700", color="#7c2d12")
    s.text(24, 292, "Ejemplo: p = 90 % con N = 4 ⇒ S = 1/(0,1 + 0,225) = 3,08 (no 4). Con N = 16 ⇒ 5,93. Con N = ∞ ⇒ 10.", size=9.6, family=MONO)
    s.text(24, 314, "La parte secuencial (1 − p) es la que manda: si es el 10 %, ningún número de núcleos pasa de 10×.", size=9.8, color="#7c2d12")
    s.text(24, 336, "Multicore (memoria compartida) vs cluster (memoria distribuida, paso de mensajes): más núcleos y más barato, pero comunicar cuesta.", size=9.8)
    s.text(24, 358, "Y siempre: más núcleos = más consumo y más calor ⇒ por eso la industria también sube vías y frecuencia (tema 7.2).", size=9.8, color="#4b5563")
    s.text(24, 380, "Este es el techo que explica por qué el paralelismo no reemplaza al pipeline: atacan cosas distintas.", size=9.8, color="#4b5563")
    s.save("amdahl_grafico.svg")


def d_multiusuario_escalabilidad():
    s = Svg(920, 400, "Monousuario vs multiusuario: qué cambia al conectar varias máquinas")
    s.raw('<rect x="24" y="46" width="424" height="216" rx="6" fill="#dbeafe" stroke="#93c5fd" stroke-width="1.4"/>')
    s.text(40, 70, "MONOUSUARIO (multicore / multihilo)", size=10.8, weight="700", color=ACCENT)
    s.text(40, 96, "· un sistema operativo, una memoria", size=9.4)
    s.text(40, 118, "· los núcleos comparten la RAM", size=9.4)
    s.text(40, 140, "· comunican por variables y caché", size=9.4)
    s.text(40, 162, "· coherencia por hardware (MESI)", size=9.4)
    s.text(40, 184, "· límite: el ancho de banda de la memoria", size=9.4, color="#7c2d12")
    s.text(40, 206, "· ejemplo: laptop de 8 núcleos", size=9.4, color="#4b5563")
    s.text(40, 232, "Escala a decenas de núcleos.", size=9.4, weight="700")
    s.raw('<rect x="472" y="46" width="424" height="216" rx="6" fill="#dcfce7" stroke="#86efac" stroke-width="1.4"/>')
    s.text(488, 70, "MULTIUSUARIO (cluster / distribuido)", size=10.8, weight="700", color="#15803d")
    s.text(488, 96, "· muchas máquinas, cada una con su SO", size=9.4)
    s.text(488, 118, "· NO comparten memoria: mensajes", size=9.4)
    s.text(488, 140, "· comunican por red (latencia de µs-ms)", size=9.4)
    s.text(488, 162, "· tolera fallas de una máquina", size=9.4)
    s.text(488, 184, "· límite: la red y el balance de carga", size=9.4, color="#7c2d12")
    s.text(488, 206, "· ejemplo: servidores de un banco", size=9.4, color="#4b5563")
    s.text(488, 232, "Escala a miles de máquinas.", size=9.4, weight="700")
    s.raw('<rect x="24" y="280" width="872" height="104" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 302, "Lo que hay que decir en el final", size=10.4, weight="700")
    s.text(40, 324, "Mismo objetivo (más rendimiento), distinto mecanismo: memoria compartida = rápido y con techo; paso de mensajes = escala mucho y cuesta coordinar.", size=9.4)
    s.text(40, 344, "La ley de Amdahl vale para los dos: la parte secuencial y la comunicación ponen el techo. Un cluster no arregla un programa poco paralelo.", size=9.4, color="#4b5563")
    s.text(40, 364, "Vocabulario: SISD/SIMD/MISD/MIMD (Flynn, 8.2.2) · UMA vs NUMA · granularidad gruesa (procesos) vs fina (hilos).", size=9.4, color="#4b5563")
    s.text(24, 400 - 4, "En la máquina de la cátedra no hay nada de esto: es un solo procesador. Por eso la unidad 8 es 'concepto + cuenta', no circuito.", size=9.6, color="#4b5563")
    s.save("multiusuario_escalabilidad.svg")

# ══════════════════════════ UNIDAD 9 ══════════════════════════
def d_complemento2_rango():
    s = Svg(920, 400, "Complemento a 2: rango, acarreo (C) y desborde (V)")
    s.text(24, 52, "Con n bits: los enteros que entran son de −2ⁿ⁻¹ a +2ⁿ⁻¹ − 1", size=10.8, weight="700")
    s.text(24, 76, "4 bits: 1000 = −8  ·  1111 = −1  ·  0000 = 0  ·  0111 = +7   ⇒ 16 valores en total", size=9.6, family=MONO, color="#7c2d12")
    for i in range(16):
        x = 40 + i * 55
        val = i - 16 if i >= 8 else i
        col = "#dbeafe" if i < 8 else "#fef3c7"
        s.raw(f'<rect x="{x}" y="92" width="50" height="40" rx="3" fill="{col}" stroke="{STROKE}" stroke-width="1.1"/>')
        s.text(x + 25, 110, format(i, "04b"), size=7.6, anchor="middle", family=MONO)
        s.text(x + 25, 124, f"{val:+d}", size=9, anchor="middle", weight="700")
    s.text(24, 156, "Por qué es asimétrico: hay un solo cero (0000) y el 1000 no tiene positivo ⇒ el rango negativo tiene un valor más.", size=9.6, color="#4b5563")
    s.text(24, 190, "Las dos banderas NO son lo mismo (el error clásico)", size=10.8, weight="700")
    s.raw('<rect x="24" y="204" width="440" height="120" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 226, "C (acarreo) = C_out del último bit", size=9.8, weight="700", color=ACCENT)
    s.text(40, 248, "Indica que el resultado se salió de n bits", size=9.2, color="#4b5563")
    s.text(40, 268, "tratándolos como SIN signo.", size=9.2, color="#4b5563")
    s.text(40, 292, "9 + 8 = 17 ⇒ 1 0001: C = 1 (y el bit que", size=9.2, family=MONO)
    s.text(40, 308, "queda es 0001).", size=9.2, family=MONO)
    s.raw('<rect x="480" y="204" width="416" height="120" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(496, 226, "V (desborde) = C_entrada ⊕ C_salida del signo", size=9.8, weight="700", color=RED)
    s.text(496, 248, "Indica que el resultado no entra con SIGNO:", size=9.2, color="#4b5563")
    s.text(496, 268, "dos positivos dieron negativo (o al revés).", size=9.2, color="#4b5563")
    s.text(496, 292, "+7 + 1 = 1000 = −8 ⇒ V = 1 (¡y C = 0!)", size=9.2, family=MONO)
    s.text(496, 308, "−8 − 1 = 0111 = +7 ⇒ V = 1", size=9.2, family=MONO)
    s.text(24, 348, "Cómo se detecta V sin mirar los acarreos: si los dos operandos tienen el MISMO signo y el resultado tiene otro, hay desborde.", size=9.6)
    s.text(24, 370, "La resta se hace con A + B' + 1: el +1 entra como C0, y el C final se INVIERTE al leerlo como 'hubo préstamo'.", size=9.6, color="#4b5563")
    s.text(24, 392, "Regla de oro: C se lee en aritmética sin signo; V, en aritmética con signo. Nunca se mezclan.", size=9.6, color="#7c2d12")
    s.save("complemento2_rango.svg")


def d_multiplicacion_registros():
    s = Svg(920, 410, "Multiplicación sin signo: sumar y desplazar (13 × 11 = 143)")
    s.text(24, 52, "Tres registros: M (multiplicando), Q (multiplicador), A (acumulador)", size=10.6, weight="700")
    s.box(60, 78, 130, 44, "M", "multiplicando", fill="#dbeafe")
    s.text(200, 104, "= 1101 (13)", size=9.6, family=MONO, color="#7c2d12")
    s.box(60, 134, 130, 44, "Q", "multiplicador", fill="#dcfce7")
    s.text(200, 160, "= 1011 (11)", size=9.6, family=MONO, color="#7c2d12")
    s.box(60, 190, 130, 44, "A", "acumulador", fill="#fef3c7")
    s.text(200, 216, "= 0000", size=9.6, family=MONO, color="#7c2d12")
    s.text(24, 262, "Regla en cada paso: si Q0 = 1 ⇒ A ← A + M. Después, desplazar a la derecha el par (A,Q).", size=9.8, weight="700")
    s.text(24, 282, "Se repite n veces (n = número de bits). El producto queda en A:Q.", size=9.6, color="#4b5563")
    filas = [("inicio", "0000", "1011", "—"), ("1", "0110", "1101", "Q0=1 ⇒ A+M"),
             ("2", "1001", "1110", "Q0=1 ⇒ A+M"), ("3", "0100", "1111", "Q0=0 ⇒ no suma"),
             ("4", "1000", "1111", "Q0=1 ⇒ A+M")]
    s.text(470, 84, "paso", size=9.4, family=MONO, weight="700")
    s.text(540, 84, "A", size=9.4, family=MONO, weight="700")
    s.text(610, 84, "Q", size=9.4, family=MONO, weight="700")
    s.text(680, 84, "qué pasó", size=9.4, family=MONO, weight="700")
    for i, (p, a, q, com) in enumerate(filas):
        y = 106 + i * 22
        col = "#15803d" if p == "inicio" else STROKE
        s.text(470, y, p, size=9.4, family=MONO, color=col)
        s.text(540, y, a, size=9.4, family=MONO, color=col)
        s.text(610, y, q, size=9.4, family=MONO, color=col)
        s.text(680, y, com, size=9.4, family=MONO, color=col)
    s.raw(f'<rect x="460" y="204" width="440" height="32" rx="4" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.3"/>')
    s.text(470, 226, "producto = A:Q = 1000 1111 = 143  ✓ (13 × 11)", size=10, family=MONO, weight="700", color="#0f766e")
    s.raw('<rect x="24" y="300" width="872" height="92" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 322, "Por qué funciona: 13 × 11 = 13 × (8 + 2 + 1) = 13×8 + 13×2 + 13×1 ⇒ multiplicar es sumar copias desplazadas.", size=9.6)
    s.text(40, 344, "El desplazamiento a la derecha del par (A,Q) equivale a multiplicar por 2 el registro y desplazar la coma del producto.", size=9.6, color="#4b5563")
    s.text(40, 364, "Costo: n sumas de n bits + n desplazamientos ⇒ O(n²) para un producto de 2n bits. El arreglo multiplicador (9.2.3) lo hace en un solo paso combinacional.", size=9.6, color="#4b5563")
    s.text(24, 408 - 2, "Con signo: se toma el valor absoluto, se multiplica así y se pone el signo del resultado (regla de los signos). Booth evita el paso de los valores absolutos.", size=9.4, color="#7c2d12")
    s.save("multiplicacion_registros.svg")


def d_booth_traza():
    s = Svg(920, 410, "Algoritmo de Booth: multiplicar con signo sin separar los signos")
    s.text(24, 52, "La idea: mirar el par (Q0, Q−1) y decidir sin mirar los signos", size=10.6, weight="700")
    tabla = [("0 0", "nada", "los bits son iguales: no hay que sumar"), ("0 1", "A ← A + M", "empieza una tira de unos"),
             ("1 0", "A ← A − M", "termina una tira de unos"), ("1 1", "nada", "los bits son iguales")]
    s.text(40, 84, "Q0 Q−1", size=9.4, family=MONO, weight="700")
    s.text(130, 84, "acción", size=9.4, family=MONO, weight="700")
    s.text(250, 84, "cuándo", size=9.4, family=MONO, weight="700")
    for i, (par, acc, cuan) in enumerate(tabla):
        y = 106 + i * 22
        col = "#7c2d12" if acc != "nada" else "#4b5563"
        s.text(40, y, par, size=9.4, family=MONO, color=col)
        s.text(130, y, acc, size=9.4, family=MONO, color=col)
        s.text(250, y, cuan, size=9.4, family=MONO, color=col)
    s.text(40, 206, "Después de cada paso se desplaza a la DERECHA el conjunto (A, Q, Q−1) con extensión de signo.", size=9.4, color="#4b5563")
    s.text(470, 84, "Ejemplo: (−5) × 3 = −15", size=10.2, weight="700")
    filas = [("inicio", "0000", "0011", "0", "—"),
             ("1", "0010", "1001", "1", "par 10 ⇒ A − M"),
             ("2", "0001", "0100", "1", "par 11 ⇒ nada"),
             ("3", "1110", "0010", "0", "par 01 ⇒ A + M"),
             ("4", "1111", "0001", "0", "par 00 ⇒ nada")]
    for lab, x in [("paso", 470), ("A", 530), ("Q", 600), ("Q−1", 665), ("acción", 720)]:
        s.text(x, 108, lab, size=9.2, family=MONO, weight="700")
    for i, (p, a, q, qm, acc) in enumerate(filas):
        y = 130 + i * 22
        col = "#15803d" if p == "inicio" else STROKE
        s.text(470, y, p, size=9.2, family=MONO, color=col)
        s.text(530, y, a, size=9.2, family=MONO, color=col)
        s.text(600, y, q, size=9.2, family=MONO, color=col)
        s.text(665, y, qm, size=9.2, family=MONO, color=col)
        s.text(720, y, acc, size=9.2, family=MONO, color=col)
    s.raw(f'<rect x="460" y="238" width="440" height="32" rx="4" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.3"/>')
    s.text(470, 260, "A:Q = 1111 0001 = −15 en complemento a 2  ✓", size=10, family=MONO, weight="700", color="#0f766e")
    s.raw('<rect x="24" y="292" width="872" height="100" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 314, "Ventaja: no hay que separar signos ni tomar valores absolutos; se opera directamente en complemento a 2 y el desplazamiento es aritmético.", size=9.6)
    s.text(40, 336, "Cuándo suma y cuándo no: sólo actúa en los cambios de bit (01 y 10). Una tira de unos se resuelve con UNA suma o UNA resta en vez de varias.", size=9.6, color="#4b5563")
    s.text(40, 356, "M = 1011 = −5 · −M = 0101 (se obtiene invirtiendo y sumando 1) · el resultado se lee con signo en A:Q.", size=9.6, family=MONO, color="#7c2d12")
    s.text(40, 378, "Es el algoritmo que se pregunta con traza: hay que mostrar en cada fila el par, la acción, A, Q y Q−1.", size=9.6, color="#4b5563")
    s.save("booth_traza.svg")


def d_division_restauracion():
    s = Svg(920, 410, "División con restauración: 7 ÷ 3 (cociente 2, resto 1)")
    s.text(24, 52, "Registros: M (divisor), Q (dividendo → luego cociente), A (resto parcial)", size=10.4, weight="700")
    s.box(60, 78, 130, 40, "M", "divisor = 0011", fill="#dbeafe")
    s.box(60, 128, 130, 40, "Q", "dividendo = 0111", fill="#dcfce7")
    s.box(60, 178, 130, 40, "A", "resto = 0000", fill="#fef3c7")
    s.text(24, 256, "Cada vuelta: desplazar (A,Q) a la izquierda · A ← A − M · si A < 0, restaurar (A ← A + M) y Q0 = 0; si no, Q0 = 1", size=9.4, weight="700")
    filas = [("1", "0000", "1110", "A−M = −3 ⇒ restaura, Q0=0"),
             ("2", "0001", "1100", "A−M = −2 ⇒ restaura, Q0=0"),
             ("3", "0000", "1001", "A−M = 0 ⇒ Q0=1"),
             ("4", "0001", "0010", "A−M = −2 ⇒ restaura, Q0=0")]
    for lab, x in [("paso", 470), ("A", 530), ("Q", 600), ("qué pasó", 660)]:
        s.text(x, 84, lab, size=9.2, family=MONO, weight="700")
    for i, (p, a, q, com) in enumerate(filas):
        y = 106 + i * 22
        s.text(470, y, p, size=9.2, family=MONO)
        s.text(530, y, a, size=9.2, family=MONO)
        s.text(600, y, q, size=9.2, family=MONO)
        s.text(660, y, com, size=9.2, family=MONO)
    s.raw(f'<rect x="460" y="196" width="440" height="32" rx="4" fill="#dcfce7" stroke="{STROKE}" stroke-width="1.3"/>')
    s.text(470, 218, "cociente Q = 0010 = 2 · resto A = 0001 = 1  ✓", size=9.8, family=MONO, weight="700", color="#0f766e")
    s.text(470, 246, "Comprobación: 7 = 2 × 3 + 1", size=9.4, color="#4b5563")
    s.raw('<rect x="24" y="272" width="872" height="116" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 294, "Restauración: si la resta dio negativo, se DES HACE la resta (se vuelve a sumar M). Es simple, pero pierde un tiempo.", size=9.6)
    s.text(40, 316, "No restauración: no se deshace; si A < 0, en la vuelta siguiente se SUMA M en vez de restar. Mismo resultado, menos operaciones.", size=9.6, color="#4b5563")
    s.text(40, 338, "Por qué se desplaza el par (A,Q): el resto parcial 'baja' el bit siguiente del dividendo, igual que en la división a mano.", size=9.6, color="#4b5563")
    s.text(40, 360, "Costo: n vueltas para n bits (cada una, una resta y un desplazamiento); el cociente queda en Q y el resto en A.", size=9.6, color="#4b5563")
    s.text(24, 408 - 4, "Trampa de examen: A tiene n bits y el cociente n bits ⇒ el cociente puede no entrar (sobreflujo) cuando el divisor es muy chico.", size=9.4, color="#7c2d12")
    s.save("division_restauracion.svg")


def d_division_signo():
    s = Svg(920, 390, "División con signo y sobreflujo")
    s.text(24, 52, "Regla de los signos: el signo del cociente es XOR de los signos; el resto tiene el signo del dividendo", size=10.4, weight="700")
    casos = [("+ / +", "positivo", "resto positivo", "#dcfce7"), ("− / +", "negativo", "resto negativo", "#fef3c7"),
             ("+ / −", "negativo", "resto positivo", "#fef3c7"), ("− / −", "positivo", "resto negativo", "#dbeafe")]
    for i, (caso, coc, res, col) in enumerate(casos):
        x = 40 + i * 215
        s.raw(f'<rect x="{x}" y="76" width="200" height="76" rx="5" fill="{col}" stroke="{STROKE}" stroke-width="1.3"/>')
        s.text(x + 100, 100, caso, size=12, anchor="middle", weight="700", family=MONO)
        s.text(x + 100, 122, f"cociente {coc}", size=9.2, anchor="middle")
        s.text(x + 100, 140, res, size=9, anchor="middle", color="#4b5563")
    s.text(24, 180, "Cómo se hace en la práctica", size=10.6, weight="700")
    s.text(40, 202, "1 · tomar valores absolutos y dividir sin signo (como en 9.3.1).", size=9.6)
    s.text(40, 222, "2 · aplicar el XOR de los signos al cociente y el signo del dividendo al resto.", size=9.6)
    s.text(40, 242, "3 · el resto SIEMPRE cumple: dividendo = cociente × divisor + resto (con su signo).", size=9.6, color="#7c2d12")
    s.raw('<rect x="24" y="262" width="872" height="106" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 284, "Sobreflujo (overflow) de la división: pasa cuando el cociente no entra en n bits, es decir cuando |dividendo| ≥ |divisor| × 2ⁿ⁻¹.", size=9.6, color=RED)
    s.text(40, 306, "Ejemplo con 4 bits: 8 ÷ 1 = 8, pero el máximo positivo representable es +7 ⇒ desborde. Se detecta ANTES, comparando los bits altos.", size=9.6, family=MONO, color="#7c2d12")
    s.text(40, 328, "División por cero: no se puede representar ⇒ la CPU dispara una excepción (interrupción interna, tema 10.2).", size=9.6, color="#4b5563")
    s.text(40, 350, "Y el caso −8 ÷ −1 = +8 tampoco entra en 4 bits: es el único sobreflujo que hay que memorizar.", size=9.6, color="#4b5563")
    s.text(24, 384 - 2, "El resto con signo es la diferencia con la división entera de la matemática: −7 ÷ 3 da cociente −2 y resto −1 (no resto +2).", size=9.4, color="#4b5563")
    s.save("division_signo.svg")


def d_punto_flotante_normalizacion():
    s = Svg(920, 400, "Punto flotante: signo, exponente y mantissa — y por qué hay que normalizar")
    s.text(24, 52, "Formato: (−1)^S × 1.M × 2^(E − exceso)", size=12, weight="700", family=MONO, color="#0f766e")
    s.raw('<rect x="60" y="80" width="80" height="44" rx="3" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(100, 108, "S", size=12, anchor="middle", weight="700")
    s.raw('<rect x="140" y="80" width="200" height="44" rx="3" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(240, 108, "E (exponente)", size=10.5, anchor="middle", weight="700")
    s.raw('<rect x="340" y="80" width="300" height="44" rx="3" fill="#dcfce7" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(490, 108, "M (mantissa / fracción)", size=10.5, anchor="middle", weight="700")
    s.text(660, 96, "Exceso 127 en simple:", size=9.2, color="#4b5563")
    s.text(660, 112, "así se comparan como enteros.", size=9.2, color="#4b5563")
    s.text(24, 156, "Normalizar = dejar la mantissa como 1,xxx (un solo 1 antes de la coma) y acomodar el exponente", size=10.4, weight="700")
    s.text(40, 182, "Ejemplo: 1011,01  ⇒  1,01101 × 2³", size=10, family=MONO, color="#7c2d12")
    s.text(40, 204, "Se corrió la coma 3 lugares a la izquierda ⇒ el exponente sube 3.", size=9.4, color="#4b5563")
    s.text(40, 226, "Ejemplo: 0,00101 ⇒ 1,01 × 2⁻³", size=10, family=MONO, color="#7c2d12")
    s.text(40, 248, "Se corrió la coma 3 lugares a la derecha ⇒ el exponente baja 3.", size=9.4, color="#4b5563")
    s.text(40, 276, "Cero y desnormalizados: E = 0 ⇒ sin el 1 implícito (números muy chicos).", size=9.4, color="#4b5563")
    s.raw('<rect x="500" y="170" width="396" height="106" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(516, 192, "Las operaciones, en orden", size=10.4, weight="700")
    s.text(516, 214, "1 · alinear exponentes (el menor se corre)", size=9.2)
    s.text(516, 232, "2 · sumar/restar mantissas", size=9.2)
    s.text(516, 250, "3 · normalizar y redondear", size=9.2)
    s.text(516, 268, "4 · revisar sobreflujo / subflujo del exponente", size=9.2, color="#7c2d12")
    s.text(24, 318, "Por qué punto flotante y no coma fija: con 32 bits, la coma fija llega a ~2·10⁹ y no puede con 10⁻²⁰ ni con 10³⁰; el flotante cubre ambos a costa de precisión.", size=9.6)
    s.text(24, 340, "El costo: no todos los números se representan exactos (0,1 no es exacto en binario) ⇒ los errores de redondeo se acumulan al sumar muchas veces números muy distintos.", size=9.6, color="#4b5563")
    s.text(24, 362, "En la máquina de la cátedra (BLUE) no hay punto flotante: se hace por software o con la FPU del 8087 en el 8086/8088.", size=9.6, color="#4b5563")
    s.text(24, 384, "Y siempre: normalizar primero ⇒ más precisión con la misma cantidad de bits (la mantissa no desperdicia ceros a la izquierda).", size=9.6, color="#7c2d12")
    s.save("punto_flotante_normalizacion.svg")


def d_ieee754_campos():
    s = Svg(920, 400, "IEEE 754: los campos del formato simple y del doble")
    s.text(24, 52, "Simple (32 bits): 1 + 8 + 23 · exceso 127", size=10.8, weight="700")
    s.raw('<rect x="60" y="70" width="50" height="40" rx="3" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(85, 96, "S", size=11, anchor="middle", weight="700")
    s.text(85, 126, "1", size=8.6, anchor="middle", color="#4b5563")
    s.raw('<rect x="110" y="70" width="150" height="40" rx="3" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(185, 96, "exponente", size=10, anchor="middle", weight="700")
    s.text(185, 126, "8 bits (0-255)", size=8.6, anchor="middle", color="#4b5563")
    s.raw('<rect x="260" y="70" width="400" height="40" rx="3" fill="#dcfce7" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(460, 96, "mantissa (fracción)", size=10, anchor="middle", weight="700")
    s.text(460, 126, "23 bits", size=8.6, anchor="middle", color="#4b5563")
    s.text(24, 156, "Doble (64 bits): 1 + 11 + 52 · exceso 1023 · 15-17 dígitos decimales", size=10.8, weight="700")
    s.raw('<rect x="60" y="172" width="40" height="40" rx="3" fill="#dbeafe" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(80, 198, "S", size=11, anchor="middle", weight="700")
    s.raw('<rect x="100" y="172" width="190" height="40" rx="3" fill="#fef3c7" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(195, 198, "exponente (11)", size=10, anchor="middle", weight="700")
    s.raw('<rect x="290" y="172" width="500" height="40" rx="3" fill="#dcfce7" stroke="'+STROKE+'" stroke-width="1.5"/>')
    s.text(540, 198, "mantissa (52 bits)", size=10, anchor="middle", weight="700")
    # ejemplo
    s.raw('<rect x="24" y="232" width="872" height="132" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 254, "Ejemplo resuelto: decodificar  0 10000010 01000000000000000000000", size=10.4, weight="700")
    s.text(40, 276, "S = 0 ⇒ positivo · E = 10000010 = 130 ⇒ 130 − 127 = 3 · M = 01000… ⇒ 1,01 (el 1 es implícito)", size=9.4, family=MONO)
    s.text(40, 296, "valor = +1,01₂ × 2³ = 1,25 × 8 = 10,0  ⇒  0x41200000 es el 10,0 en simple precisión", size=9.4, family=MONO, color="#0f766e")
    s.text(40, 322, "Al revés (10,0 a binario): 10 = 1010 = 1,010 × 2³ ⇒ S=0, E=3+127=130=10000010, M=0100… ⇒ 0 10000010 0100…", size=9.4, family=MONO)
    s.text(40, 346, "Casos especiales: E = 0 y M = 0 ⇒ ±0 · E = 255 y M = 0 ⇒ ±∞ · E = 255 y M ≠ 0 ⇒ NaN (no es un número) · E = 0 con M ≠ 0 ⇒ desnormalizado.", size=9.2, color="#7c2d12")
    s.text(24, 384, "Rangos del simple: ≈ 1,2·10⁻³⁸ a 3,4·10³⁸, con 7 dígitos significativos. Por eso 0,1 + 0,2 no da exactamente 0,3.", size=9.6, color="#4b5563")
    s.save("ieee754_campos.svg")


def d_bcd_correccion():
    s = Svg(920, 400, "Suma BCD: por qué hay que sumar 6 y cuándo")
    s.text(24, 52, "BCD: cada dígito decimal ocupa 4 bits (0-9). Sumar en binario no alcanza.", size=10.6, weight="700")
    s.text(24, 84, "Caso 1 · sin corrección:  12 + 34 = 46", size=10.2, weight="700", color="#15803d")
    s.text(40, 108, "0001 0010  (12)", size=9.8, family=MONO)
    s.text(40, 126, "+ 0011 0100  (34)", size=9.8, family=MONO)
    s.text(40, 148, "= 0100 0110  ⇒ 4 y 6: los dos dígitos son ≤ 9 ⇒ 46  ✓", size=9.8, family=MONO, color="#15803d")
    s.text(24, 186, "Caso 2 · hace falta corrección:  27 + 35 = 62", size=10.2, weight="700", color=RED)
    s.text(40, 210, "0010 0111  (27)", size=9.8, family=MONO)
    s.text(40, 228, "+ 0011 0101  (35)", size=9.8, family=MONO)
    s.text(40, 250, "= 0101 1100   ⇒ las unidades dan 1100 = 12 > 9  ✗ no es un dígito BCD", size=9.8, family=MONO, color=RED)
    s.text(40, 272, "+      0110   ⇒ sumar 6 a ese dígito", size=9.8, family=MONO, color="#7c2d12")
    s.text(40, 294, "= 0110 0010   ⇒ 6 y 2  ⇒ 62  ✓  (el acarreo pasa al dígito siguiente)", size=9.8, family=MONO, color="#15803d")
    s.raw('<rect x="560" y="76" width="336" height="230" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(576, 98, "La regla", size=10.4, weight="700")
    s.text(576, 122, "Después de sumar cada dígito BCD:", size=9.2)
    s.text(576, 144, "si el resultado es > 9  ó  hubo", size=9.2, color="#7c2d12")
    s.text(576, 160, "acarreo ⇒ sumar 0110 (6).", size=9.2, color="#7c2d12")
    s.text(576, 186, "Por qué 6: hay 6 combinaciones", size=9.2, color="#4b5563")
    s.text(576, 202, "binarias (1010 a 1111) que no son", size=9.2, color="#4b5563")
    s.text(576, 218, "dígitos decimales ⇒ hay que saltarlas.", size=9.2, color="#4b5563")
    s.text(576, 244, "Y por qué sigue sirviendo: el acarreo", size=9.2, color="#4b5563")
    s.text(576, 260, "que se genera ES la decena que hay", size=9.2, color="#4b5563")
    s.text(576, 276, "que pasar al dígito siguiente.", size=9.2, color="#4b5563")
    s.text(24, 330, "Es la corrección que hace la instrucción DAA (decimal adjust) del 8086: el programador suma en binario y la CPU corrige.", size=9.6)
    s.text(24, 352, "Resta BCD: se resta 6 (o se suma 1010) cuando hay préstamo; el razonamiento es el mismo con acarreo invertido.", size=9.6, color="#4b5563")
    s.text(24, 374, "Para qué se usa: calculadoras, relojes, contadores de display, cualquier cosa que tenga que mostrar decimales exactos (el punto flotante no garantiza el dígito).", size=9.6, color="#4b5563")
    s.text(24, 396, "Costo: 4 bits por dígito ⇒ se desperdicia el 37,5 % de las combinaciones (6 de 16).", size=9.6, color="#7c2d12")
    s.save("bcd_correccion.svg")


# ══════════════════════════ UNIDAD 10 ══════════════════════════
def d_handshake_tiempos():
    s = Svg(920, 380, "Handshake asíncrono: STB y ACK, paso a paso")
    s.text(24, 52, "Sin handshake la transferencia se pisa; con handshake cada parte sabe cuándo actuar", size=10.2, weight="700")
    # líneas
    for i, (nom, y) in enumerate([("DATO", 96), ("STB", 140), ("ACK", 184)]):
        s.text(30, y + 4, nom, size=9.6, weight="700", color=ACCENT)
        s.line(90, y, 860, y, w=1, color="#cbd5e1")
    # dato válido
    s.line(200, 96, 200, 76, w=1.6); s.line(200, 76, 480, 76, w=1.6); s.line(480, 76, 480, 96, w=1.6)
    s.text(300, 70, "dato válido en las líneas", size=8.8, color="#7c2d12")
    # STB pulso
    s.wire([(90, 140), (200, 140)]); s.wire([(200, 140), (200, 120)])
    s.wire([(200, 120), (420, 120)]); s.wire([(420, 120), (420, 140)]); s.wire([(420, 140), (860, 140)])
    s.text(210, 112, "STB = 1 (el dato está puesto)", size=8.8, color="#7c2d12")
    # ACK pulso
    s.wire([(90, 184), (330, 184)]); s.wire([(330, 184), (330, 164)])
    s.wire([(330, 164), (560, 164)]); s.wire([(560, 164), (560, 184)]); s.wire([(560, 184), (860, 184)])
    s.text(340, 158, "ACK = 1 (lo tomé)", size=8.8, color="#15803d")
    s.text(24, 226, "Secuencia: 1 · el periférico pone el dato  →  2 · pone STB  →  3 · el receptor toma el dato y contesta ACK  →  4 · se bajan las dos señales", size=9.6)
    s.text(24, 248, "Recién cuando STB volvió a 0 se puede poner el dato siguiente: eso es lo que evita perder o repetir datos.", size=9.6, color="#4b5563")
    s.raw('<rect x="24" y="266" width="872" height="98" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 288, "Por qué es asíncrono: no hay reloj común; cada parte espera la señal de la otra. Sirve para periféricos de cualquier velocidad.", size=9.4)
    s.text(40, 308, "Costo: dos líneas más y más tiempo por transferencia (hay que esperar el ida y vuelta). Por eso los buses rápidos son sincrónicos.", size=9.4, color="#4b5563")
    s.text(40, 328, "En la BLUE es más simple: la línea R (ready) hace de 'listo' y la instrucción INP espera ahí mismo (polling dentro de la instrucción).", size=9.4, color="#7c2d12")
    s.text(40, 348, "Las tres señales del handshake (STB, ACK, BUSY) son las mismas en Centronics, en el 8255 y en cualquier interfaz paralela.", size=9.4, color="#4b5563")
    s.save("handshake_tiempos.svg")


def d_vector_prioridad():
    s = Svg(920, 400, "Prioridad de interrupciones: encadenado de ACK y tabla de vectores")
    s.text(24, 52, "Encadenado de ACK (daisy chain): el más cercano a la CPU gana", size=10.6, weight="700")
    s.box(40, 80, 110, 54, "CPU", "", fill="#dbeafe")
    for i in range(4):
        x = 210 + i * 170
        s.box(x, 80, 140, 54, f"disp. {i}", f"prioridad {i+1}", fill="#dcfce7")
        s.arrow(x - 26, 100, x - 4, 100, color=ACCENT)
    s.text(210, 154, "ACK recorre la cadena: el primero que pidió se la queda y no la pasa.", size=9.4, color="#4b5563")
    s.text(40, 176, "Alternativa: controlador de prioridades (8259) con 8 entradas, máscara por bit y vector programable.", size=9.4, color="#4b5563")
    s.text(24, 214, "Tabla de vectores del 8086: 256 entradas de 4 bytes en 00000H–003FFH", size=10.6, weight="700")
    for i in range(4):
        y = 232 + i * 24
        s.raw(f'<rect x="40" y="{y}" width="120" height="20" rx="2" fill="#fef3c7" stroke="{STROKE}" stroke-width="1"/>')
        s.text(100, y + 14, f"IRQ{i} → INT 0{i+8}H", size=8.6, anchor="middle", family=MONO)
        s.raw(f'<rect x="200" y="{y}" width="150" height="20" rx="2" fill="#dcfce7" stroke="{STROKE}" stroke-width="1"/>')
        s.text(275, y + 14, f"entrada {i+8}H × 4 = {i*4+32:02X}H", size=8.6, anchor="middle", family=MONO)
        s.text(360, y + 14, "→ IP + CS de la rutina", size=8.6, color="#4b5563")
    s.text(40, 336, "IRQ0 = timer (INT 08H) · IRQ1 = teclado (INT 09H) · NMI = INT 02H (no enmascarable) · IRQ5 ⇒ 0DH × 4 = 34H", size=9.2, family=MONO, color="#7c2d12")
    s.raw('<rect x="24" y="352" width="872" height="42" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 372, "Ventaja de vectorizar: un solo salto indirecto en vez de preguntar bandera por bandera (con 8 dispositivos, hasta 8 consultas).", size=9.4)
    s.text(40, 388, "Y la prioridad deja de depender del orden del programa: la fija el hardware (posición en la cadena o programación del 8259).", size=9.4, color="#4b5563")
    s.save("vector_prioridad.svg")


def d_serie_paralelo_skew():
    s = Svg(920, 380, "Serie vs paralelo: el desfasaje (skew) que mató al paralelo")
    s.text(24, 52, "En paralelo, cada línea llega a su tiempo: con períodos cortos, se mezclan dos envíos", size=10.4, weight="700")
    # paralelo con skew
    for i in range(4):
        y = 84 + i * 26
        s.text(30, y + 4, f"D{i}", size=9.2, weight="700", family=MONO)
        s.line(60, y, 380, y, w=1, color="#cbd5e1")
        x0 = 100 + i * 22
        s.raw(f'<rect x="{x0}" y="{y-8}" width="90" height="14" rx="2" fill="#dbeafe" stroke="{ACCENT}" stroke-width="1"/>')
        s.text(390, y + 4, f"llega +{i*0.5:.1f} ns", size=8.2, color=RED if i else "#4b5563")
    s.text(60, 200, "Se pisan: no se puede leer la palabra sin esperar al más lento.", size=9.2, color=RED)
    s.text(24, 232, "En serie, un solo carril: no hay desfasaje y la frecuencia puede subir mucho", size=10.4, weight="700")
    s.line(60, 268, 380, 268, w=1, color="#cbd5e1")
    for k in range(8):
        x = 100 + k * 32
        s.raw(f'<rect x="{x}" y="258" width="26" height="14" rx="2" fill="{"#dcfce7" if k % 2 == 0 else "#fef3c7"}" stroke="{STROKE}" stroke-width="1"/>')
        s.text(x + 13, 269, "1" if k % 2 == 0 else "0", size=7.6, anchor="middle", family=MONO)
    s.text(60, 292, "bits uno detrás del otro, con el reloj embebido en la propia señal (o diferencial: dos cables con la señal invertida).", size=9.2, color="#15803d")
    s.raw('<rect x="470" y="76" width="426" height="180" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(486, 98, "Las cuentas que se preguntan", size=10.4, weight="700")
    s.text(486, 120, "Centronics (paralelo): ~150 kB/s", size=9)
    s.text(486, 138, "RS-232: 115 200 bps ÷ 10 ≈ 11,5 kB/s", size=9, family=MONO)
    s.text(486, 156, "USB 2.0: 480 Mb/s = 60 MB/s", size=9, family=MONO)
    s.text(486, 174, "SATA 6 Gb/s × 8/10 ÷ 8 = 600 MB/s", size=9, family=MONO, color="#7c2d12")
    s.text(486, 192, "PCIe 4.0 x4: ≈ 7,9 GB/s", size=9, family=MONO)
    s.text(486, 216, "100 MB: USB 2.0 ⇒ 1,67 s · SATA ⇒ 0,17 s", size=9, color="#4b5563")
    s.text(486, 234, "RS-232 ⇒ ≈ 2,4 horas", size=9, color="#4b5563")
    s.raw('<rect x="24" y="272" width="872" height="94" rx="6" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1.2"/>')
    s.text(40, 294, "Conclusión para el final: 'serie' no es 'lento'. El paralelo perdió por el skew y por el costo de pines; el serie gana frecuencia y llega más lejos.", size=9.6)
    s.text(40, 316, "El paralelo sigue vivo donde las distancias son cortas: dentro del chip y en el bus de memoria (64-512 bits).", size=9.6, color="#4b5563")
    s.text(40, 338, "Al pasar de bits/s a MB/s: dividir por 8 y descontar el codificado (8b/10b ⇒ ×0,8). Olvidar eso es el error más común en esta pregunta.", size=9.6, color="#7c2d12")
    s.text(40, 358, "Y siempre: el cuello real puede ser el disco (100 MB/s) antes que el enlace (600 MB/s) ⇒ mirar la cadena completa.", size=9.6, color="#4b5563")
    s.save("serie_paralelo_skew.svg")

# ══════════════════════════ UNIDAD 1 (extra) ══════════════════════════
def d_dualidad_teoremas():
    s = Svg(920, 400, "Postulados y dualidad: cada identidad tiene su gemela con AND↔OR y 0↔1")
    s.text(24, 52, "La regla de dualidad: se cambia AND por OR, se cambia 0 por 1, y la identidad sigue valiendo", size=10.6, weight="700")
    filas = [("A + 0 = A", "A · 1 = A", "neutro"), ("A + 1 = 1", "A · 0 = 0", "dominante"),
             ("A + A = A", "A · A = A", "idempotencia"), ("A + A' = 1", "A · A' = 0", "complemento"),
             ("(A')' = A", "(A')' = A", "involución"),
             ("A + A·B = A", "A · (A + B) = A", "absorción"),
             ("A + A'·B = A + B", "A · (A' + B) = A·B", "absorción 2"),
             ("A + B = B + A", "A · B = B · A", "conmutativa"),
             ("A+(B+C) = (A+B)+C", "A·(B·C) = (A·B)·C", "asociativa"),
             ("A·(B+C) = A·B + A·C", "A+(B·C) = (A+B)·(A+C)", "distributiva"),
             ("(A·B)' = A' + B'", "(A+B)' = A'·B'", "DeMorgan")]
    s.text(40, 82, "con OR", size=9.6, weight="700", color=ACCENT)
    s.text(320, 82, "su dual con AND", size=9.6, weight="700", color="#0f766e")
    s.text(640, 82, "nombre", size=9.6, weight="700")
    for i, (a, b, n) in enumerate(filas):
        y = 106 + i * 24
        if i % 2 == 0:
            s.raw(f'<rect x="32" y="{y-16}" width="856" height="22" rx="3" fill="#f8fafc"/>')
        s.text(40, y, a, size=9.6, family=MONO)
        s.text(320, y, b, size=9.6, family=MONO, color="#0f766e")
        s.text(640, y, n, size=9.2, color="#4b5563")
    s.text(760, 106, "Y en compuertas:", size=9.2, weight="700")
    s.text(760, 126, "AND ↔ OR", size=9.2, family=MONO, color="#7c2d12")
    s.text(760, 146, "0 ↔ 1", size=9.2, family=MONO, color="#7c2d12")
    s.text(760, 166, "NAND ↔ NOR", size=9.2, family=MONO, color="#7c2d12")
    s.raw('<rect x="24" y="380" width="872" height="14" rx="4" fill="#f8fafc" stroke="#e5e7eb" stroke-width="1"/>')
    s.text(40, 392, "Para qué sirve: demostrar una identidad y usar la dual sin volver a probarla · y simplificar cambiando de forma (SOP ↔ POS).", size=9)
    s.save("dualidad_teoremas.svg")

# ══════════════════════════ CÓDIGOS Y ERRORES (Fase 12) ══════════════════════════
def d_codigos_ponderados():
    s = Svg(920, 430, "Códigos binarios: el mismo 5 se escribe distinto en cada código")
    s.text(24, 52, "Ponderados (cada bit vale un peso) y no ponderados (una regla, sin pesos)", size=10.6, weight="700")
    cols = [("dec", 40), ("natural  8-4-2-1", 110), ("AIKEN  2-4-2-1", 300), ("Exceso 3  (n + 3)", 510), ("BCD empaq. (2 díg. / byte)", 700)]
    for tit, x in cols:
        s.text(x, 82, tit, size=9.6, weight="700", color=ACCENT)
    filas = [
        ("0", "0000", "0000", "0011", ""),
        ("1", "0001", "0001", "0100", ""),
        ("2", "0010", "0010", "0101", ""),
        ("3", "0011", "0011", "0110", ""),
        ("4", "0100", "0100", "0111", ""),
        ("5", "0101", "1011", "1000", ""),
        ("6", "0110", "1100", "1001", ""),
        ("7", "0111", "1101", "1010", ""),
        ("8", "1000", "1110", "1011", "27 = 0010 0111"),
        ("9", "1001", "1111", "1100", "62 = 0110 0010"),
    ]
    for i, (d, nat, aik, exc, bcd) in enumerate(filas):
        y = 106 + i * 22
        if i % 2 == 0:
            s.raw(f'<rect x="32" y="{y-15}" width="856" height="21" rx="3" fill="#f8fafc"/>')
        s.text(40, y, d, size=9.6, family=MONO, weight="700")
        s.text(110, y, nat, size=9.6, family=MONO)
        s.text(300, y, aik, size=9.6, family=MONO, color="#0f766e" if d in ("5","6","7","8","9") else STROKE)
        s.text(510, y, exc, size=9.6, family=MONO)
        if bcd:
            s.text(700, y, bcd, size=9.4, family=MONO, color="#7c2d12")
    s.line(20, 340, 900, 340, w=1, color="#d1d5db")
    s.text(24, 358, "Natural: pesos 8-4-2-1 · AIKEN: 2-4-2-1 (el 5 es 1011: 4+0+1) · Exceso 3: al binario puro se le suma 3 (autocomplementario)", size=9.2, color="#4b5563")
    s.text(24, 374, "BCD empaquetado: un dígito decimal por nible, dos por byte · BCD desempaquetado: un dígito por byte (el otro nible en 0)", size=9.2, color="#4b5563")
    s.note(24, 396, ["Para qué sirve el exceso 3: el complemento a 9 se obtiene invirtiendo los bits, y no tiene la combinación 0000",
                     "(un cable roto no parece un 0). Por eso se usa en transmisión."], size=9.2)
    s.save("codigos_ponderados.svg")

def d_codigos_continuos():
    s = Svg(920, 430, "Códigos continuos y cíclicos: cambia un solo bit entre números seguidos")
    s.text(24, 52, "Continuo = combinaciones consecutivas adyacentes · cíclico = además la última es adyacente a la primera", size=10.4, weight="700")
    # Gray
    s.text(30, 86, "Gray (reflejado): 2, 3 y 4 bits", size=9.8, weight="700", color=ACCENT)
    g2 = ["00","01","11","10"]; g3 = ["000","001","011","010","110","111","101","100"]
    g4 = ["0000","0001","0011","0010","0110","0111","0101","0100","1100","1101","1111","1110","1010","1011","1001","1000"]
    for i, v in enumerate(g2):
        x = 40 + i * 52
        s.box(x, 100, 46, 24, v, size=9.4)
    for i, v in enumerate(g3):
        x = 40 + i * 46
        s.box(x, 146, 42, 24, v, size=9.2)
    for i, v in enumerate(g4):
        x = 40 + (i % 8) * 46
        y = 192 + (i // 8) * 34
        s.box(x, y, 42, 26, v, size=9.2)
    s.text(300, 118, "el 3 (010) y el 4 (110) difieren en 1 bit", size=9, color=RED)
    s.text(430, 210, "16 combinaciones, un bit por paso,", size=9, color="#4b5563")
    s.text(430, 226, "y del 1111 se vuelve a 1000 sin saltos.", size=9, color="#4b5563")
    # Johnson
    s.text(30, 306, "Johnson (5 bits): 10 combinaciones, cíclico", size=9.8, weight="700", color="#0f766e")
    j = ["00000","00001","00011","00111","01111","11111","11110","11100","11000","10000"]
    for i, v in enumerate(j):
        x = 40 + (i % 5) * 86
        y = 320 + (i // 5) * 34
        s.box(x, y, 80, 26, v, size=9.2, fill="#ecfdf5")
    s.note(520, 322, ["Dónde aparecen: el Gray en codificadores y en convertidores",
                      "rápidos (un solo bit cambia ⇒ menos error). El Johnson se arma",
                      "con un registro de desplazamiento realimentado y da 2n estados",
                      "con n biestables (10 con 5 bits)."], size=9)
    s.save("codigos_continuos.svg")

def d_deteccion_errores():
    s = Svg(920, 470, "Detección y corrección de errores: paridad, Hamming, LRC y CRC")
    s.text(24, 52, "Se agregan bits redundantes: sirven para DETECTAR (paridad, LRC, CRC) o para CORREGIR (Hamming)", size=10.4, weight="700")
    # paridad
    s.text(30, 86, "1. Paridad", size=9.8, weight="700", color=ACCENT)
    s.box(30, 96, 400, 78, "", fill="#f8fafc")
    s.text(40, 116, "dato  1 0 1 1 0 0 1 0   →  tres unos ⇒ impar", size=9.2, family=MONO)
    s.text(40, 134, "paridad PAR  ⇒ P = 1  (queda 4 unos: par)", size=9.2, family=MONO, color="#0f766e")
    s.text(40, 152, "paridad IMPAR ⇒ P = 0  (queda 3 unos: impar)", size=9.2, family=MONO, color="#0f766e")
    s.text(40, 168, "Detecta 1 bit mal; con 2 bits mal no ve nada.", size=8.8, color="#4b5563")
    # Hamming
    s.text(470, 86, "2. Hamming: los bits de control van en las potencias de 2", size=9.8, weight="700", color="#0f766e")
    pos = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    tipo = ["P1","P2","D1","P4","D2","D3","D4","P8","D5","D6","D7","D8"]
    for i, (p, t) in enumerate(zip(pos, tipo)):
        x = 470 + i * 33
        ctrl = t.startswith("P")
        s.box(x, 100, 30, 26, t, fill="#fef3c7" if ctrl else "#ecfdf5", size=8.8)
        s.text(x + 15, 140, p, size=8.4, anchor="middle", color="#4b5563")
    s.text(470, 160, "P1 cubre 1,3,5,7,9,11 · P2 cubre 2,3,6,7,10,11 · P4 cubre 4,5,6,7,12 · P8 cubre 8..12", size=8.8, family=MONO, color="#7c2d12")
    s.text(470, 176, "El patrón de fallas da la posición del bit con error (síndrome): 101 = 5 ⇒ se invierte el bit 5.", size=8.8, color="#4b5563")
    s.text(470, 192, "Cuesta log₂(n)+1 bits extra: con 8 de datos, 4 de control (12,8).", size=8.8, color="#4b5563")
    # LRC
    s.text(30, 224, "3. LRC (bloque)", size=9.8, weight="700", color=ACCENT)
    s.text(30, 242, "Se suman los bytes en hexadecimal y se toma el complemento a 2:", size=9.2)
    s.text(40, 262, "01 + 08 + 00 + 00 + 61 + 62 = CC  →  C2 = 34", size=9.2, family=MONO, color="#0f766e")
    s.text(30, 280, "El receptor suma todo (datos + LRC): si el total no da 00, hubo error.", size=8.8, color="#4b5563")
    # CRC
    s.text(470, 224, "4. CRC (polinomio)", size=9.8, weight="700", color="#0f766e")
    s.text(470, 242, "El bloque es un polinomio D(X); se lo divide por G(X) y se", size=9.2)
    s.text(470, 258, "agrega el RESTO. En el receptor, el resto debe dar 0.", size=9.2)
    s.text(470, 276, "CRC-8 = X⁸+X⁵+X⁴+1   ·   CRC-16 = X¹⁶+X¹⁵+X²+1", size=9, family=MONO, color="#7c2d12")
    s.note(30, 306, ["Regla de oro para el final: paridad, LRC y CRC DETECTAN (no saben dónde está el error).",
                     "Hamming DETECTA y CORRIGE un bit, porque el síndrome dice la posición."], size=9)
    s.text(24, 366, "En el 8088 y en las PC: la paridad se usaba en los módulos de memoria (9 bits por byte), y el CRC en discos, redes y ZIP.", size=9, color="#4b5563")
    s.text(24, 384, "Hamming se usa en memorias con ECC: 72 bits por línea = 64 de datos + 8 de control.", size=9, color="#4b5563")
    s.save("deteccion_errores.svg")

TODAS_U2 = [d_flipflop_d_t_tiempos, d_flipflop_jk_ecuaciones, d_registros_pipo_siso, d_registros_sipo_piso,
            d_contadores_modulo, d_celda_memoria, d_sram_dram_refresco, d_rom_decodificador_or,
            d_prom_flash_celda, d_amat_cache, d_memoria_virtual_tlb, d_memoria_asociativa_cam,
            d_bits_direccion, d_codop_vs_direccion,
            d_microoperaciones_bus, d_buffer_tres_estados, d_alu_estructura, d_flags_alu, d_registros_cpu_mar,
            d_ias_estructura, d_blue_opcodes, d_blue_programa_ram, d_busqueda_pulsos, d_estado_pulso_1_16,
            d_instruccion_partes, d_clasificacion_instrucciones, d_ea_calculo, d_rif_rid_rb, d_irq_logica, d_pila_rti,
            d_biu_eu_cola, d_micropc_flujo, d_cableada_vs_micro, d_rom_control_8088,
            d_speedup_limites, d_anchura_superscalar_smt, d_prediccion_saltos, d_load_store_risc,
            d_encadenamiento, d_simd_registros, d_matriz_simd, d_conflictos_banco, d_amdahl_grafico,
            d_multiusuario_escalabilidad,
            d_complemento2_rango, d_multiplicacion_registros, d_booth_traza, d_division_restauracion,
            d_division_signo, d_punto_flotante_normalizacion, d_ieee754_campos, d_bcd_correccion,
            d_handshake_tiempos, d_vector_prioridad, d_serie_paralelo_skew, d_dualidad_teoremas, d_codigos_ponderados, d_codigos_continuos, d_deteccion_errores]

TODAS = [d_compuertas_nand_nor_xor, d_nand_universal, d_demorgan_circuitos, d_simplificacion_compuertas,
         d_mintterminos_canonica, d_karnaugh_dontcare, d_sumador_n_bits] + TODAS_U2

if __name__ == "__main__":
    pedidos = sys.argv[1:]
    for f in TODAS:
        if pedidos and f.__name__[2:] not in pedidos:
            continue
        f()
