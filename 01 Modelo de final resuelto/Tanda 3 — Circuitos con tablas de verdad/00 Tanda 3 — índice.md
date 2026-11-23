---
tipo: indice
prioridad: maxima
---
# Tanda 3 — Circuitos con tablas de verdad (peso 12, la más pesada)

> [!warning] El orden obligatorio de cada ítem
> **1) tabla de verdad → 2) función → 3) simplificación (Karnaugh si se pide) → 4) circuito dibujado.**
> Si falta el circuito o la función, la tabla sola **no alcanza**. Se rinde **dibujando**.

| # | Ítem de la matriz | Carpeta | Archivos que corresponden |
|---|---|---|---|
| 3.0 | **Herramientas de la tanda** | `3.0 Herramientas (Karnaugh y compuertas)/` | [[Mintérminos y maxtérminos]] (Karnaugh paso a paso) · [[Compuertas lógicas]] (símbolos y tablas) |
| 3.1 | **Decodificadores** | `3.1 Decodificadores/` | [[Decodificador]] |
| 3.2 | **Codificadores** | `3.2 Codificadores/` | [[Codificador]] |
| 3.3 | **Multiplexores** | `3.3 Multiplexores/` | [[Multiplexor]] |
| 3.4 | **Demultiplexores** | `3.4 Demultiplexores/` | [[Demultiplexor]] |
| 3.5 | **Cómo pasar de un flip-flop RS a JK** | `3.5 De flip-flop RS a JK (Karnaugh)/` | [[Conversión entre biestables (RS, JK, D, T)]] |
| 3.6 | **Flip-flop tipo D, T y RS** | `3.6 Flip-flops D, T y RS/` | [[Flip-Flops SR, D, JK y T]] |
| 3.7 | **Álgebra de Boole, leyes y DeMorgan** | `3.7 Álgebra de Boole y DeMorgan/` | [[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] |
| 3.8 | **Sumadores** | `3.8 Sumadores/` | [[Semisumador]] · [[Sumador completo]] |
| 3.9 | **El RI y 3 ejemplos de instrucciones** | `3.9 El RI y 3 ejemplos de instrucciones/` | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] |

---

## El orden en que conviene estudiarla

1. **3.7 Boole y DeMorgan** — el idioma con el que se escribe todo lo demás.
2. **3.0 Karnaugh y compuertas** — cómo se simplifica y cómo se dibuja.
3. **3.1 a 3.4** los cuatro bloques combinacionales (van juntos, se preguntan juntos).
4. **3.6 Flip-flops** — ecuaciones características con su mapa.
5. **3.5 RS → JK** — la conversión con tabla de excitación y dos mapas.
6. **3.8 Sumadores** — el circuito aritmético (y su versión de 4 bits).
7. **3.9 El RI y los 3 ejemplos** — la parte "de máquina" de esta tanda.

---

## Qué hay que poder dibujar de cada ítem

| Ítem | Tabla | Función | Circuito |
|---|---|---|---|
| Decodificador 2→4 | 4 filas, un 1 por fila | `Y0 = A1'A0'` … `Y3 = A1A0` | 2 NOT + 4 AND |
| Codificador 8→3 | 8 filas, una entrada activa | `A2 = E4+E5+E6+E7` … | 3 OR de 4 entradas |
| Multiplexor 4→1 | 4 filas de selección | `Y = S1'S0'I0 + …` | 4 AND de 3 + 1 OR |
| Demultiplexor 1→4 | `D` por selección | `Yi = D·mi` | 2 NOT + 4 AND de 3 |
| RS → JK | excitación del RS | `S = J·Q'`, `R = K·Q` | 2 AND (+ inversor de Q) |
| Flip-flop JK | 8 filas (J, K, Q) | `Q⁺ = JQ' + K'Q` | 2 AND + 1 OR |
| Flip-flop D / T | 2 filas | `Q⁺ = D` · `Q⁺ = T⊕Q` | cable / XOR |
| Boole / DeMorgan | 4 filas para demostrar | `(A+B)' = A'B'` | conversión a NAND |
| Semisumador | 4 filas | `S = A⊕B`, `C = AB` | XOR + AND |
| Sumador completo | 8 filas | `S = A⊕B⊕Cin`, `Cout = AB + Cin(A⊕B)` | 2 XOR + 2 AND + 1 OR |

> [!tip] Truco de examen
> Antes de dibujar, escribí al costado **cuántas compuertas** vas a usar y **cuáles**. Te ordena el dibujo y el
> profesor ve que sabés lo que estás haciendo.

---

## Relacionado
[[00 Índice — el final resuelto]] · [[00 Tanda 1 — índice]] · [[00 Tanda 2 — índice]] ·
[[Cómo dibujar los circuitos (checklist de pizarrón)]] · [[Tablas de verdad de memoria]]
