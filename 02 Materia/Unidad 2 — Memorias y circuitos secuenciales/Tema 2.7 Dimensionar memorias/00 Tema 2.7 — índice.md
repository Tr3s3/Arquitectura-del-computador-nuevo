---
tipo: indice
unidad: 2
tema: "2.7"
---
# Tema 2.7 — Dimensionar memorias

> [!abstract] Qué se estudia acá
> Las dos cuentas que aparecen en **todos** los ejercicios y en el final: cuántos **bits de dirección** necesita una
> memoria según su tamaño, y cuántos bits le quedan al **código de operación** cuando la palabra de instrucción
> tiene que direccionar esa memoria.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **2.7.1** Bits de dirección = log₂ de celdas | pasar de "512 MB" a "27 bits" | [[2.7.1 Bits de dirección igual a log2 de celdas]] |
| **2.7.2** CodOp vs campo de dirección | cuántas instrucciones entran en una palabra | [[2.7.2 CodOp vs campo de dirección]] |

> [!important] Las dos fórmulas
> `bits de dirección = log₂(cantidad de celdas)` · `bits de CodOp = tamaño de palabra − bits de dirección`.
> La primera cuenta **cuántas celdas** hay (ojo: la celda puede tener varios bytes); la segunda reparte la
> **palabra de instrucción**.

## Relacionado
[[00 Unidad 2 — temas y subtemas]] · [[00 Tema 2.6 — índice]] · [[Espacio de direccionamiento y cálculo de CodOp-Dirección]]
