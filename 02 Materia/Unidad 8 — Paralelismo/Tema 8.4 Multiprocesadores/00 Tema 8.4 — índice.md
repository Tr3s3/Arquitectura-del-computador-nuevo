---
tipo: indice
unidad: 8
tema: "8.4"
---
# Tema 8.4 — Multiprocesadores

> [!abstract] Qué se estudia acá
> El paralelismo **MIMD**: varios procesadores (o núcleos) con sus propios flujos de instrucciones. Los dos
> problemas que aparecen al instante son la **coherencia de las cachés** (todos tienen copia de los mismos datos) y
> el **límite de la ley de Amdahl** (no se gana proporcionalmente).

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **8.4.1** Multicore, coherencia de caché y ley de Amdahl | el problema y su techo matemático | [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] |
| **8.4.2** Monousuario vs multiusuario | latencia contra productividad | [[8.4.2 Monousuario vs multiusuario]] |

> [!important] Las dos fórmulas
> `S(n) = 1 / ((1 − f) + f/n)` (Amdahl) · `S(n) = n` sólo si `f = 1` (nunca en la práctica)

## Relacionado
[[00 Unidad 8 — temas y subtemas]] · [[00 Tema 8.3 — índice]] · [[00 Unidad 9 — temas y subtemas]] ·
[[Paralelismo y procesamiento vectorial]]
