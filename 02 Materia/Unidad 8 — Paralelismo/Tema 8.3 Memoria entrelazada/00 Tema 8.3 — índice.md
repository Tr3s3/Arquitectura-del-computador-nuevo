---
tipo: indice
unidad: 8
tema: "8.3"
---
# Tema 8.3 — Memoria entrelazada

> [!abstract] Qué se estudia acá
> Cómo **alimentar** a un procesador que consume un dato por ciclo: la memoria se parte en **bancos** que atienden **en paralelo**. Es la mitad del problema del paralelismo que **no** es cálculo.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **8.3.1** Bancos de memoria y ancho de banda | cuánta ganancia da y cómo se calcula | [[8.3.1 Bancos de memoria y ancho de banda]] |
| **8.3.2** Patrón de entrelazado y conflictos de banco | cuándo **no** funciona (stride) | [[8.3.2 Patrón de entrelazado y conflictos de banco]] |

> [!important] La fórmula
> `ancho de banda = (bancos × bytes por palabra) / tiempo de ciclo` y `banco = dirección mod nº de bancos`

## Relacionado
[[00 Unidad 8 — temas y subtemas]] · [[00 Tema 8.2 — índice]] · [[00 Tema 8.4 — índice]] · [[Jerarquía de memorias]] · [[Técnicas para aumentar la velocidad]]
