---
tipo: indice
unidad: 9
tema: "9.1"
---
# Tema 9.1 — Suma y resta

> [!abstract] Qué se estudia acá
> La base de **todo** el hardware aritmético: el **sumador**. Cómo se representa el signo (y por qué **complemento a 2**), cómo se resta con el **mismo** sumador, cómo se detecta el **desbordamiento** y cómo se hace **rápido** (acarreo anticipado con `G` y `P`).

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **9.1.1** Complemento a 2 y desbordamiento | representar, restar y detectar `V` | [[9.1.1 Complemento a 2 y desbordamiento]] |
| **9.1.2** Acarreo anticipado (G y P) | por qué el sumador es el camino crítico | [[9.1.2 Acarreo anticipado (G y P)]] |

> [!important] Las tres fórmulas
> `A − B = A + B' + 1` · `C(i+1) = G(i) + P(i)·C(i)` · `V = Cin(MSB) ⊕ Cout(MSB)`

## Relacionado
[[00 Unidad 9 — temas y subtemas]] · [[00 Tema 9.2 — índice]] · [[3.2.1 Estructura, G-P y señales de selección]] · [[Hardware aritmético (resumen)]]
