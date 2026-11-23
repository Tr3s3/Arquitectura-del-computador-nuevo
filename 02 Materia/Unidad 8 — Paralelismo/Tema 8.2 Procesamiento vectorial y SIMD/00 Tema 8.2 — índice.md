---
tipo: indice
unidad: 8
tema: "8.2"
---
# Tema 8.2 — Procesamiento vectorial y SIMD

> [!abstract] Qué se estudia acá
> **Una instrucción, muchos datos**: registros anchos que guardan varios elementos, la clasificación de Flynn, los arreglos de procesadores y el caso que siempre se pregunta: la **multiplicación de matrices**.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **8.2.1** SIMD, registros vectoriales y GPU | qué es SIMD y cuánto se gana | [[8.2.1 SIMD, registros vectoriales y GPU]] |
| **8.2.2** Flynn, arreglos SIMD y conectados | la clasificación completa y los arreglos de PE | [[8.2.2 Flynn, arreglos SIMD y conectados]] |
| **8.2.3** Multiplicación de matrices | el caso resuelto `C = A·B` | [[8.2.3 Multiplicación de matrices]] |

> [!important] La idea
> El vectorial **amortiza** el costo de buscar y decodificar la instrucción: una instrucción hace el trabajo de `n`. Es el mismo truco que el pipeline, pero por **ancho** en vez de por **tiempo**.

## Relacionado
[[00 Unidad 8 — temas y subtemas]] · [[00 Tema 8.1 — índice]] · [[00 Tema 8.3 — índice]] · [[Paralelismo y procesamiento vectorial]]
