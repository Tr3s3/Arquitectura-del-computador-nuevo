---
tipo: indice
unidad: 3
tema: "3.2"
---
# Tema 3.2 — La ALU

> [!abstract] Qué se estudia acá
> La **Unidad Aritmético-Lógica**: el bloque que ejecuta las operaciones sobre los datos. Cómo está armada (dos
> entradas, selector, salida), cómo se comunican los bloques entre sí con `G` y `P`, y qué son los **flags**.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **3.2.1** Estructura, G/P y señales de selección | qué entradas y salidas tiene y cómo se encadenan las etapas | [[3.2.1 Estructura, G-P y señales de selección]] |
| **3.2.2** Operaciones aritméticas, lógicas y flags | qué hace cada código y cómo se detecta cero, acarreo, signo y desborde | [[3.2.2 Operaciones aritméticas, lógicas y flags]] |

> [!important] La idea que hay que llevarse
> La ALU **no sabe restar, comparar ni multiplicar**: sabe **sumar**, **negar** y **aplicar una operación lógica**.
> Todo lo demás se consigue combinando eso, y eso lo decide el **selector** (que la UC maneja).

## Nota de desarrollo ampliado
La versión extensa de este tema (orientada al examen) está en la misma carpeta: **[[ALU]]**.

## Relacionado
[[00 Unidad 3 — temas y subtemas]] · [[00 Tema 3.1 — índice]] · [[00 Tema 3.3 — índice]]
