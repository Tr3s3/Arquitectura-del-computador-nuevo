---
unidad: 1
tipo: concepto
examen: practica
---
# Leyes de DeMorgan

> [!abstract] En una frase
> **El complemento de una suma es el producto de los complementos** y **el complemento de un producto
> es la suma de los complementos**. En símbolos:
> `(A + B)' = A' · B'`  y  `(A · B)' = A' + B'`.

## Por qué es una ley y no una fórmula más
Se demuestra con **tabla de verdad** (8 columnas, 4 filas) y es la justificación formal de que
NAND y NOR sean **compuertas universales**.

| A | B | A+B | (A+B)' | A'·B' | A·B | (A·B)' | A'+B' |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | **1** | **1** | 0 | **1** | **1** |
| 0 | 1 | 1 | **0** | **0** | 0 | **1** | **1** |
| 1 | 0 | 1 | **0** | **0** | 0 | **1** | **1** |
| 1 | 1 | 1 | **0** | **0** | 1 | **0** | **0** |

Las columnas 4ª y 5ª son idénticas ⇒ primera ley. Las columnas 7ª y 8ª son idénticas ⇒ segunda ley.

## Lectura en compuertas (lo que hay que saber decir)
- `(A·B)'` es una **NAND**. DeMorgan dice que una NAND equivale a una **OR con las entradas negadas**:
  `NAND(A,B) = A' + B'`. Es decir: la NAND es negar cada entrada y después OR.
- `(A+B)'` es una **NOR**, equivalente a una **AND con las entradas negadas**: `NOR(A,B) = A'·B'`.
- Consecuencia práctica: **cualquier función se puede implementar usando sólo NAND o sólo NOR**,
  y en la práctica los circuitos integrados se fabrican así (es más barato fabricar un solo tipo de compuerta).

## Generalización a n variables
`(A + B + C + …)' = A'·B'·C'·…` y `(A·B·C·…)' = A' + B' + C' + …`.
Se aplica **de adentro hacia afuera**: primero se niega la operación de mayor jerarquía.

> [!example] Ejemplo tipo práctico
> Pasar a forma con sólo compuertas NAND: `F = A·B + C·D`
>
> 1. Negar dos veces (involución): `F = ((A·B + C·D)')'`
> 2. DeMorgan sobre la suma: `(A·B + C·D)' = (A·B)' · (C·D)'`
> 3. Queda `F = ( (A·B)' · (C·D)' )'` → **dos NAND para los productos y una NAND final** (NAND de 2 entradas, 3 compuertas en total).

> [!example] Ejemplo con variables negadas
> `F = (A + B')·C'`. Aplicando DeMorgan al primer factor: `(A + B')' = A'·B`, no conviene;
> en cambio si el enunciado pide todo en NAND: `F = ((A + B')·C')'' = ( (A+B')' + C )'` → `A+B'` se hace con
> una NAND de `A'` y `B`. Moraleja: **DeMorgan sirve para cambiar el "tipo" de compuerta sin cambiar la función**.

## Cómo responderlo en el final
1. Enunciar las dos leyes (forma OR y forma AND) con su dualidad.
2. Demostrar una con tabla de verdad (rápido: 4 filas).
3. Explicar la consecuencia: NAND/NOR universales, y que permite implementar una función mínima
   usando el tipo de compuerta disponible.
4. Mencionar la generalización a n variables.

## Errores típicos
- Negar sólo la primera variable: `(A+B)' ≠ A' + B'` (¡es el error más común!).
- Olvidar que DeMorgan **también cambia el operador** (· por +, o + por ·).
- Aplicarlo sin respetar la jerarquía: `(A + B·C)' = A' · (B·C)' = A'·(B' + C')`.

## Relacionado
[[Álgebra de Boole — postulados y teoremas]] · [[Compuertas lógicas]] · [[Multiplexor]]
