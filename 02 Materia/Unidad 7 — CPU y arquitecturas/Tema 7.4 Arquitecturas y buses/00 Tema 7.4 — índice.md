---
tipo: indice
unidad: 7
tema: "7.4"
---
# Tema 7.4 — Arquitecturas y buses

> [!abstract] Qué se estudia acá
> Dos decisiones de **estructura**: si la memoria es **una** (von Neumann) o **dos** (Harvard), y cómo se
> **conectan** los bloques por **buses** (interno del chip y externo del sistema), con su ancho de banda.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **7.4.1** von Neumann vs Harvard | el cuello de botella y el híbrido de las cachés | [[7.4.1 von Neumann vs Harvard]] |
| **7.4.2** Buses internos y externos | las tres líneas del bus y el cálculo de ancho de banda | [[7.4.2 Buses internos y externos]] |

> [!important] Las dos fórmulas
> `ancho de banda = (bits del bus / 8) × frecuencia` · y el "cuello de botella de von Neumann": buscar instrucción
> y dato **no** pueden ir a la vez (si hay un solo bus).

## Relacionado
[[00 Unidad 7 — temas y subtemas]] · [[00 Tema 7.3 — índice]] · [[00 Unidad 3 — temas y subtemas]] ·
[[4.1.1 Unidades funcionales de una computadora]]
