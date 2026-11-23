---
tipo: indice
unidad: 2
tema: "2.4"
---
# Tema 2.4 — ROM y memorias no volátiles

> [!abstract] Qué se estudia acá
> Las memorias que **no pierden el contenido** al apagar: la **ROM** (grabada de fábrica), sus variantes
> programables (PROM, EPROM, EEPROM) y la **Flash**. Su estructura interna es sorprendentemente simple:
> **un decodificador y un montón de compuertas OR**.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **2.4.1** ROM = decodificador + OR | por qué una ROM es literalmente una tabla de verdad | [[2.4.1 ROM = decodificador + OR]] |
| **2.4.2** PROM, EPROM, EEPROM y Flash | quién la graba, cuántas veces y cómo se borra | [[2.4.2 PROM, EPROM, EEPROM y Flash]] |

> [!important] La frase que resume el tema
> Una ROM de `2ⁿ × m` es **un decodificador de `n` a `2ⁿ`** seguido de **`m` compuertas OR**: cada palabra de la
> memoria es la **suma de mintérminos** de las direcciones donde esa columna vale 1.

## TPs y práctica
[[TP12 Memoria principal]] · [[TP13 Componentes internos]]

## Relacionado
[[00 Unidad 2 — temas y subtemas]] · [[00 Tema 2.3 — índice]] · [[00 Tema 2.5 — índice]] ·
[[Memoria ROM y sus tipos]]
