---
tipo: indice
unidad: 1
tema: "1.5"
---
# Tema 1.5 — Aritmética combinacional

> [!abstract] Qué se estudia acá
> Cómo se **suma y se resta con compuertas**: del semisumador (2 bits, sin acarreo entrante) al sumador completo (con acarreo) y de ahí al sumador de n bits que la ALU usa para todo, incluida la resta.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **1.5.1** Semisumador y sumador completo | sumar dos bits con y sin acarreo entrante | [[1.5.1 Semisumador y sumador completo]] |
| **1.5.2** Sumador de n bits y resta en complemento a 2 | encadenar sumadores, restar con `A + B' + 1` | [[1.5.2 Sumador de n bits y resta en complemento a 2]] |

> [!tip] Por qué importa
> **Todo** lo que hace una ALU se reduce a sumar: la resta es una suma, la multiplicación es sumas y desplazamientos, la comparación es una resta. Si entendés el sumador completo, entendés la ALU.

## TPs y práctica
[[TP5 Sumadores]]

## Relacionado
[[00 Unidad 1 — temas y subtemas]] · [[00 Tema 1.4 — índice]] · [[Semisumador]] · [[Sumador completo]]
