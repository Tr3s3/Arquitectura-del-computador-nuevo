---
tipo: indice
unidad: 1
tema: "1.6"
---
# Tema 1.6 — Códigos binarios

> [!abstract] Qué se estudia acá
> Un **código** es una regla que asigna a cada símbolo de un alfabeto (los dígitos 0 a 9, una letra, un comando) una combinación de `n` bits. Con `n` bits hay `2ⁿ` combinaciones: se pueden armar `2ⁿ!` códigos distintos. La cátedra estudia los que tienen **características especiales**: los **ponderados** (cada bit vale un peso), los **no ponderados** (una regla sin pesos, como el exceso 3) y los **continuos y cíclicos** (entre números seguidos cambia un solo bit, como el Gray y el Johnson).

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **1.6.1** Códigos ponderados y no ponderados | BCD natural `8-4-2-1`, **AIKEN** `2-4-2-1`, **exceso 3**, BCD empaquetado | [[1.6.1 Códigos ponderados y no ponderados]] |
| **1.6.2** Códigos continuos y cíclicos | **Gray** (reflejado) y **Johnson**: por qué cambia un solo bit | [[1.6.2 Códigos continuos y cíclicos]] |

> [!important] Por qué esto entra en el parcial
> Los códigos son la respuesta a *"¿qué codifica el codificador?"* (tema 1.4): un codificador de teclado decimal → BCD, un codificador de posición → Gray. Y en la práctica aparecen en todos lados: el BCD en las calculadoras, el exceso 3 en transmisión, el Gray en los codificadores ópticos, el Johnson en los contadores.

## TPs y práctica
[[TP2 Álgebra de Boole]] · [[TP6 Decodificadores y demultiplexores]] · [[TP7 Codificadores y multiplexores]]

## Relacionado
[[00 Unidad 1 — temas y subtemas]] · [[00 Tema 1.4 — índice]] · [[00 Tema 1.3 — índice]]
