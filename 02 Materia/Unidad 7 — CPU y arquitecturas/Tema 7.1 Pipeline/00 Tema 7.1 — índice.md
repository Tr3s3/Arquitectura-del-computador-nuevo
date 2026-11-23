---
tipo: indice
unidad: 7
tema: "7.1"
---
# Tema 7.1 — Pipeline

> [!abstract] Qué se estudia acá
> El **paralelismo a nivel de instrucciones**: partir la ejecución en **etapas fijas** que trabajan sobre
> instrucciones distintas al mismo tiempo. Con `k` etapas y `n` instrucciones se tarda **`k + (n − 1)`** ciclos en
> vez de `k·n`, pero aparecen los **tres conflictos** que recortan la ganancia.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **7.1.1** Etapas y diagrama en escalera | las 5 etapas y la cuenta `k + (n−1)` | [[7.1.1 Etapas y diagrama en escalera]] |
| **7.1.2** Hazards y sus soluciones | estructural / datos / control | [[7.1.2 Hazards y sus soluciones]] |
| **7.1.3** Cálculo de speedup y límites | el speedup **real** con stalls y saltos | [[7.1.3 Cálculo de speedup y límites]] |

> [!important] La frase de cierre
> El pipeline **no hace más rápida una instrucción**: hace que **terminen más por unidad de tiempo**.

## Relacionado
[[00 Unidad 7 — temas y subtemas]] · [[00 Tema 7.2 — índice]] · [[Pipeline]] · [[8.1.1 Etapas segmentadas y suma de vectores]]
