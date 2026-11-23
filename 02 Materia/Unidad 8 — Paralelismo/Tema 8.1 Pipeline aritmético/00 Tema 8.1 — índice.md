---
tipo: indice
unidad: 8
tema: "8.1"
---
# Tema 8.1 — Pipeline aritmético

> [!abstract] Qué se estudia acá
> Segmentar **dentro de la ALU**: en vez de una suma en serie de 4 pasos, cuatro bloques que trabajan a la vez
> sobre elementos distintos del vector. Es el mismo principio del pipeline de instrucciones, un nivel más abajo.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **8.1.1** Etapas segmentadas y suma de vectores | el diagrama en escalera y la cuenta `k + (n−1)` | [[8.1.1 Etapas segmentadas y suma de vectores]] |
| **8.1.2** Encadenamiento y speedup | cómo se alimenta una etapa con el resultado de otra | [[8.1.2 Encadenamiento y speedup]] |

> [!important] Las dos fórmulas
> `ciclos = k + (n − 1)` · `speedup = k·n / (k + n − 1) → k`

## Relacionado
[[00 Unidad 8 — temas y subtemas]] · [[00 Tema 8.2 — índice]] · [[Pipeline]] ·
[[Paralelismo y procesamiento vectorial]]
