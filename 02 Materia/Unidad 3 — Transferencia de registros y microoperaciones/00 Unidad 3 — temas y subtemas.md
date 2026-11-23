---
tipo: indice
unidad: 3
---
# Unidad 3 — Transferencia de registros y microoperaciones

> [!abstract] Qué pide la unidad
> Entender **cómo se mueve y se transforma un dato dentro de la CPU**: cada paso elemental es una
> **microoperación**, todas viajan por **un bus** (con buffers de tres estados), las cuentas las hace la **ALU** y
> los datos viven en **registros**. Es la unidad que después hace posible entender el ciclo de instrucción.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 3 completa (lectura de corrido)]]**: los **7 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 3]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.

> [!success] Unidad desarrollada
> Los **3 temas** y sus **7 subtemas** están escritos, y hay **dos archivos con toda la unidad junta**:
> el resumen de una página (**[[00 Síntesis — Unidad 3]]**) y el desarrollo completo para leer de corrido
> (**[[00 Unidad 3 completa (lectura de corrido)]]**). Estado: ✅ completa.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 3 — Transferencia de registros y microoperaciones/
├── 00 Unidad 3 — temas y subtemas   (esta nota)
├── 00 Síntesis — Unidad 3           (toda la unidad en un solo archivo)
├── 00 Unidad 3 completa (lectura de corrido)   ← los subtemas pegados, para leer de corrido
├── Tema 3.1 Microoperaciones y bus/
│   ├── 3.1.1 Notación de transferencia entre registros
│   ├── 3.1.2 Bus único y buffers de 3 estados
│   └── 3.1.3 Buses de datos, de direcciones y de control
├── Tema 3.2 La ALU/                      (+ la nota ampliada ALU)
│   ├── 3.2.1 Estructura, G-P y señales de selección
│   └── 3.2.2 Operaciones aritméticas, lógicas y flags
└── Tema 3.3 Registros de la CPU/
    ├── 3.3.1 AC, PC, IR, MAR y MBR
    └── 3.3.2 Base, índice, puntero de pila y estado
```

## Tema por tema

| Tema | Subtemas (notas) | Índice |
|---|---|---|
| **3.1 Microoperaciones y bus** | [[3.1.1 Notación de transferencia entre registros]] · [[3.1.2 Bus único y buffers de 3 estados]] · [[3.1.3 Buses de datos, de direcciones y de control]] | [[00 Tema 3.1 — índice]] |
| **3.2 La ALU** | [[3.2.1 Estructura, G-P y señales de selección]] · [[3.2.2 Operaciones aritméticas, lógicas y flags]] | [[00 Tema 3.2 — índice]] |
| **3.3 Registros de la CPU** | [[3.3.1 AC, PC, IR, MAR y MBR]] · [[3.3.2 Base, índice, puntero de pila y estado]] | [[00 Tema 3.3 — índice]] |

---

## Qué hay que saber hacer al terminar la unidad
1. Escribir **microoperaciones** con notación de transferencia (`MAR ← PC`, `AC ← AC + MBR`).
2. Explicar **por qué un bus único obliga a una transferencia por pulso**, y contar los pulsos de un ejemplo.
3. Justificar el **buffer de tres estados** y qué pasaría sin él.
4. Decir el tamaño y la función de los **tres buses** (datos, direcciones, control).
5. Decir **qué hace la ALU** con `S`, `Cin`, `G` y `P`, y qué significan los cuatro **flags**.
6. Nombrar los **nueve registros** y para qué sirve cada uno.

## TPs de la unidad
[[TP14 Buses]] · (apoyo) [[TP13 Componentes internos]] · [[TP5 Sumadores]]

## Fuente de la cátedra
Apuntes **Unidad 4 — Estructura básica de una computadora** · `blue.pdf` (bus común, registros y microoperaciones
de la máquina elemental) · Hamacher (microoperaciones y bus).

## Desarrollo de examen de estos temas
[[00 Tanda 1 — índice]]: [[Flujo de información en BLUE (datos y direcciones)]] ·
[[Estructura básica de un computador]] · [[Ciclo de máquina]] ·
Tanda 2: [[Registros base e índice]] · y la nota ampliada [[ALU]]

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Síntesis — Unidad 3]] ·
[[00 Unidad 2 — temas y subtemas]] · [[00 Unidad 4 — temas y subtemas]]
