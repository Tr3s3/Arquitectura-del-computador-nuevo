---
tipo: indice
unidad: 1
---
# Unidad 1 — Circuitos de lógica digital

> [!abstract] Qué pide la unidad
> Entender que **un circuito digital es una tabla de verdad hecha hardware**: compuertas → álgebra de Boole →
> simplificación (Karnaugh) → circuitos combinacionales (decodificadores, MUX, sumadores). Todo lo de esta unidad
> se rinde **dibujando**.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 1 completa (lectura de corrido)]]**: los **17 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 1]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.

> [!success] Unidad desarrollada
> Los **6 temas** y sus **17 subtemas** están escritos, y hay **dos archivos con toda la unidad junta**:
> el resumen de una página (**[[00 Síntesis — Unidad 1]]**) y el desarrollo completo para leer de corrido
> (**[[00 Unidad 1 completa (lectura de corrido)]]**). Estado: ✅ completa.

## La estructura de la unidad

```
Unidad 1 — Circuitos de lógica digital/
├── 00 Unidad 1 — temas y subtemas   (esta nota)
├── 00 Síntesis — Unidad 1           (toda la unidad en un solo archivo)
├── 00 Unidad 1 completa (lectura de corrido)   ← los subtemas pegados, para leer de corrido
├── Tema 1.1 Compuertas lógicas/
│   ├── 1.1.1 Compuerta AND, OR y NOT
│   ├── 1.1.2 NAND, NOR, XOR y XNOR
│   └── 1.1.3 Compuertas universales
├── Tema 1.2 Álgebra de Boole/
│   ├── 1.2.1 Postulados, dualidad y teoremas
│   ├── 1.2.2 Leyes de DeMorgan
│   └── 1.2.3 Simplificación analítica
├── Tema 1.3 Formas canónicas y Karnaugh/
│   ├── 1.3.1 Mintérminos y maxtérminos
│   ├── 1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables
│   └── 1.3.3 Don't care y criterios de agrupación
├── Tema 1.4 Bloques combinacionales/
│   ├── 1.4.1 Decodificador
│   ├── 1.4.2 Codificador
│   ├── 1.4.3 Multiplexor
│   └── 1.4.4 Demultiplexor
├── Tema 1.5 Aritmética combinacional/
└── Tema 1.6 Códigos binarios/
    ├── 1.5.1 Semisumador y sumador completo
    └── 1.5.2 Sumador de n bits y resta en complemento a 2
```

## Tema por tema

| Tema | Subtemas (notas) | Índice |
|---|---|---|
| **1.1 Compuertas lógicas** | [[1.1.1 Compuerta AND, OR y NOT]] · [[1.1.2 NAND, NOR, XOR y XNOR]] · [[1.1.3 Compuertas universales]] | [[00 Tema 1.1 — índice]] |
| **1.2 Álgebra de Boole** | [[1.2.1 Postulados, dualidad y teoremas]] · [[1.2.2 Leyes de DeMorgan]] · [[1.2.3 Simplificación analítica]] | [[00 Tema 1.2 — índice]] |
| **1.3 Formas canónicas y Karnaugh** | [[1.3.1 Mintérminos y maxtérminos]] · [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]] · [[1.3.3 Don't care y criterios de agrupación]] | [[00 Tema 1.3 — índice]] |
| **1.4 Bloques combinacionales** | [[1.4.1 Decodificador]] · [[1.4.2 Codificador]] · [[1.4.3 Multiplexor]] · [[1.4.4 Demultiplexor]] | [[00 Tema 1.4 — índice]] |
| **1.6 Códigos binarios** | [[1.6.1 Códigos ponderados y no ponderados]] · [[1.6.2 Códigos continuos y cíclicos]] | [[00 Tema 1.6 — índice]] |
| **1.5 Aritmética combinacional** | [[1.5.1 Semisumador y sumador completo]] · [[1.5.2 Sumador de n bits y resta en complemento a 2]] | [[00 Tema 1.5 — índice]] |

---

## Qué hay que saber hacer al terminar la unidad
1. **Escribir la tabla de verdad** de cualquier función de 2 a 4 variables.
2. **Pasar de la tabla a la función** (`Σm`) y **simplificarla** con Karnaugh.
3. **Dibujar el circuito** con las compuertas, contando cuántas usa.
4. **Reconocer los 4 bloques combinacionales** por su tabla (decodificador, codificador, MUX, DEMUX).
5. **Sumar y restar en binario** con semisumador, sumador completo y `A + B' + 1`.

## TPs de la unidad
[[TP1 Compuertas lógicas]] · [[TP2 Álgebra de Boole]] · [[TP3 Simplificación analítica]] ·
[[TP4 Mintérminos, maxtérminos y Karnaugh]] · [[TP5 Sumadores]] · (apoyo) [[TP6 Decodificadores y demultiplexores]] ·
[[TP7 Codificadores y multiplexores]]

## Fuente de la cátedra
Apuntes **Unidad 2 — Circuitos lógicos y digitales** · Floyd (compuertas, álgebra y simplificación) ·
Mano (lógica combinacional).

## Desarrollo de examen de estos temas
[[00 Tanda 3 — índice]] (la tanda de peso 12): [[Compuertas lógicas]] · [[Álgebra de Boole — postulados y teoremas]] ·
[[Leyes de DeMorgan]] · [[Mintérminos y maxtérminos]] · [[Decodificador]] · [[Codificador]] · [[Multiplexor]] ·
[[Demultiplexor]] · [[Semisumador]] · [[Sumador completo]]

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Síntesis — Unidad 1]] · [[00 Unidad 2 — temas y subtemas]]
