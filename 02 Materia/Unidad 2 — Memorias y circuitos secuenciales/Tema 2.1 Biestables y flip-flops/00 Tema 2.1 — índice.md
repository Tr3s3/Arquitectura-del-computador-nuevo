---
tipo: indice
unidad: 2
tema: "2.1"
---
# Tema 2.1 — Biestables y flip-flops

> [!abstract] Qué se estudia acá
> El paso de lo **combinacional** (la salida depende sólo de las entradas) a lo **secuencial** (la salida depende
> también de lo que pasó antes). El elemento que **recuerda un bit** es el biestable; con él se construyen
> registros, contadores y toda la memoria.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **2.1.1** Biestable RS (NOR y NAND) | el primer circuito con memoria y su estado prohibido | [[2.1.1 Biestable RS (NOR y NAND)]] |
| **2.1.2** Flip-flops D y T | guardar un dato (D) y contar/togglear (T) | [[2.1.2 Flip-flops D y T]] |
| **2.1.3** Flip-flop JK y ecuaciones características | el biestable completo, con su ecuación desde Karnaugh | [[2.1.3 Flip-flop JK y ecuaciones características]] |
| **2.1.4** Conversión entre biestables | usar un JK donde hace falta un D, o al revés | [[2.1.4 Conversión entre biestables]] |

> [!important] Las cuatro ecuaciones que hay que saber de memoria
> **RS:** `Q⁺ = S + R'Q` · **D:** `Q⁺ = D` · **JK:** `Q⁺ = JQ' + K'Q` · **T:** `Q⁺ = T⊕Q`.
> Todas salen del **mismo procedimiento**: tabla de estados → mapa de Karnaugh → función.

## TPs y práctica
[[TP8 Biestables RS]] · [[TP9 Biestables D, JK y T]]

## Relacionado
[[00 Unidad 2 — temas y subtemas]] · [[00 Tema 2.2 — índice]] · [[Flip-Flops SR, D, JK y T]] ·
[[Conversión entre biestables (RS, JK, D, T)]]
