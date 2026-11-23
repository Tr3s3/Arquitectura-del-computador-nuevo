---
tipo: indice
unidad: 9
tema: "9.5"
---
# Tema 9.5 — Aritmética BCD

> [!abstract] Qué estudia
> La aritmética **decimal** con dígitos de 4 bits (**BCD**): por qué el sumador binario **no alcanza** y por qué hay que **sumar 6** cuando el resultado no es un dígito válido. Es la representación de la plata: sistemas financieros, contadores y el `DAA`/`DAS` del 8086.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **9.5.1** Suma decimal corregida | la regla del `+6` y la propagación del acarreo | [[9.5.1 Suma decimal corregida]] |

> [!important] La regla
> Si el resultado binario de un dígito es **> 9** o **hubo acarreo** ⇒ **sumar `0110`** y propagar el acarreo.

## Relacionado
[[00 Unidad 9 — temas y subtemas]] · [[00 Tema 9.4 — índice]] · [[Hardware aritmético (resumen)]]
