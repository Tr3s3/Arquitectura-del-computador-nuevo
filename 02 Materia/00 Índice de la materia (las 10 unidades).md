---
tipo: moc
prioridad: maxima
---
# La materia completa — las 10 unidades

> [!abstract] Qué es esta carpeta
> El **programa de la cátedra**, unidad por unidad, para estudiarlo **de punta a punta**. Acá viven las notas que
> el final no pregunta (registros, contadores, memoria virtual, ALU, paralelismo, 8086, microprogramación) y acá
> está **el mapa que conecta todo**, incluidas las notas que están guardadas en
> [[00 Índice — el final resuelto|Modelo de final resuelto]].

> [!important] Cómo está armada
> ```
> 02 Materia/
> ├── 00 Índice de la materia (esta nota)
> ├── Unidad 1 — Circuitos de lógica digital/
> │   └── 00 Unidad N — temas y subtemas     ← el índice de la unidad
> ├── Unidad 2 — Memorias y circuitos secuenciales/
> │   ├── 00 Unidad 2 — temas y subtemas
> │   ├── Tema 2.2 Registros y contadores/    ← una carpeta por tema
> │   └── Tema 2.6 Memorias complementarias/
> ├── Unidad 3 … Unidad 10
> ```
> **Cada nota vive en un solo lugar.** La mayoría de los temas del programa coinciden con preguntas del final,
> así que su nota está en `01 Modelo de final resuelto/`; desde el índice de cada unidad **se llega igual**.

---

## Cómo se desarrolla cada unidad (el método)

> [!important] Unidad → Tema → Subtema, y al final una síntesis
> 1. **Cada tema tiene su carpeta** (`Tema N.M — nombre/`).
> 2. **Cada subtema es una nota** dentro de esa carpeta, con el detalle completo: definición, tabla, circuito,
>    ejemplo y errores típicos.
> 3. Cuando la unidad está **terminada**, se genera **`00 Síntesis — Unidad N`**: la unidad entera en **un solo
>    archivo**, para repasar o imprimir sin abrir nada más.

## Estado del desarrollo

| Unidad | Temas | Subtemas | Estado | Síntesis |
|---|---|---|---|---|
| **1** Circuitos de lógica digital | 5 | 15 | ✅ **desarrollada** | [[00 Síntesis — Unidad 1]] |
| **2** Memorias y circuitos secuenciales | 7 | 19 | ✅ **desarrollada** | [[00 Síntesis — Unidad 2]] |
| **3** Transferencia de registros y microoperaciones | 3 | 7 | ✅ **desarrollada** | [[00 Síntesis — Unidad 3]] |
| **4** Organización y diseño básico | 4 | 10 | ✅ **desarrollada** | [[00 Síntesis — Unidad 4]] |
| **5** Programación básica y CPU convencional | 6 | 13 | ✅ **desarrollada** | [[00 Síntesis — Unidad 5]] |
| **6** Control microprogramado | 3 | 5 | ✅ **desarrollada** | [[00 Síntesis — Unidad 6]] |
| **7** CPU y arquitecturas | 4 | 9 | ✅ **desarrollada** | [[00 Síntesis — Unidad 7]] |
| **8** Paralelismo | 4 | 9 | ✅ **desarrollada** | [[00 Síntesis — Unidad 8]] |
| **9** Hardware aritmético | 5 | 10 | ✅ **desarrollada** | [[00 Síntesis — Unidad 9]] |
| **10** Entrada y Salida | 4 | 7 | ✅ **desarrollada** | [[00 Síntesis — Unidad 10]] |
| **Total** | **45** | **104** | **104 subtemas escritos** | **10 de 10** ✅ |

> [!success] Materia completa
> Las **10 unidades** están desarrolladas: **45 temas**, **104 subtemas** en carpetas `Unidad → Tema → Subtema` y
> **una `00 Síntesis — Unidad N` por unidad** con todo el contenido junto. Para el parcial, empezar por la síntesis
> de la unidad que entra; para el final, por
> [[00 Índice — el final resuelto|el modelo de final resuelto]].

> [!tip] Todos los subtemas traen su diagrama
> Los **104 subtemas** tienen al menos **un diagrama** (circuito, formato de instrucción, tabla, traza o gráfico):
> **106 diagramas** sobre **97 SVG** en `assets/`. La lista completa, subtema por subtema, está en
> [[00 Mapa de diagramas (qué gráfico tiene cada subtema)]], y las **100 figuras de los libros**
> (Quiroga y Stallings) con su cita de página, en [[00 Figuras de los libros (índice)]].

## Las 10 unidades

| Unidad | Tema | Índice | Qué se estudia |
|---|---|---|---|
| **1** | Circuitos de lógica digital | [[00 Unidad 1 — temas y subtemas]] | compuertas, Boole, DeMorgan, Karnaugh, sumadores, MUX/DEMUX |
| **2** | Memorias y circuitos secuenciales | [[00 Unidad 2 — temas y subtemas]] | flip-flops, registros, contadores, celdas, RAM/ROM, caché, jerarquía |
| **3** | Transferencia de registros y microoperaciones | [[00 Unidad 3 — temas y subtemas]] | bus, microoperaciones, ALU |
| **4** | Organización y diseño básico | [[00 Unidad 4 — temas y subtemas]] | estructura, máquina BLUE, ciclos, unidad de control |
| **5** | Programación básica y CPU convencional | [[00 Unidad 5 — temas y subtemas]] | lenguaje máquina, formatos, modos, indexada, interrupciones, 8086 |
| **6** | Control microprogramado | [[00 Unidad 6 — temas y subtemas]] | UC cableada vs microprogramada, memoria de control |
| **7** | CPU y arquitecturas | [[00 Unidad 7 — temas y subtemas]] | pipeline, técnicas de velocidad, CISC/RISC |
| **8** | Paralelismo | [[00 Unidad 8 — temas y subtemas]] | pipeline aritmético, vectorial, SIMD, memoria entrelazada |
| **9** | Hardware aritmético | [[00 Unidad 9 — temas y subtemas]] | complemento a 2, Booth, división, punto flotante, BCD |
| **10** | Entrada / Salida | [[00 Unidad 10 — temas y subtemas]] | E/S programada, interrupciones, DMA, puertos e interfaces |

---

## Plan de 3 semanas para la materia completa

| Semana | Unidades | Qué hacer |
|---|---|---|
| **1. Los ladrillos** | 1 y 2 | compuertas → Boole/Karnaugh → sumadores → MUX/DEMUX → flip-flops → memorias. **Dibujar cada circuito.** |
| **2. La máquina** | 3, 4 y 5 | estructura, BLUE, ciclos, UC, formatos, modos, indexada, 8086 |
| **3. Lo avanzado** | 6 a 10 | microprogramación, pipeline, CISC/RISC, paralelismo, aritmética, E/S |

> [!tip] Regla de oro
> Por cada tema: (1) leé la nota, (2) **dibujá el circuito o el esquema sin mirar**, (3) resolvé el **TP** de esa
> unidad, (4) contá en voz alta qué resuelve ese concepto. Si hacés las cuatro, el tema es tuyo.
> Los TPs están en [[00 Índice de TPs y qué aporta cada uno]].

---

## Relacionado
[[00 Índice — el final resuelto]] · [[01 Mapa de la materia (MOC)]] ·
[[02 Plan de estudio — las 10 unidades]] · [[04 Resumen integrador de la materia]] ·
[[05 Fuentes y qué aporta cada una]]
