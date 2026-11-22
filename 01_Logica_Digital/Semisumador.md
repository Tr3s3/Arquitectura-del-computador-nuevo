---
unidad: 1
tipo: concepto
examen: practica
---
# Semisumador (half adder)

> [!abstract] En una frase
> El semisumador suma **dos bits** (A y B) sin considerar acarreo de entrada y entrega **suma (S)** y
> **acarreo (C)**: `S = A⊕B`, `C = A·B`. Es la mitad del sumador completo: sirve sólo para el bit menos
> significativo.

## Contexto
Sumar en binario es sumar columna por columna propagando el acarreo. La columna más simple (la primera,
la del LSB) no recibe acarreo: eso es exactamente lo que hace el semisumador. Como no acepta `Cin`,
**no sirve para encadenar** palabras de varios bits; para eso está el [[Sumador completo]].

## Tabla de verdad
| A | B | S (suma) | C (acarreo) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

## Funciones
- `S = A'B + AB' = A ⊕ B`  (XOR: 1 cuando los bits son distintos)
- `C = A·B`  (AND: acarreo sólo si ambos son 1)

En forma canónica: `S = Σm(1,2)`, `C = Σm(3)`.

## Circuito
Dos compuertas: una XOR y una AND sobre las mismas entradas.

![semisumador](../assets/semisumador.svg)

## Verificación con números
`1 + 1` en binario da `10` (dos): el semisumador devuelve S = 0 y C = 1 ⇒ "0 con acarreo 1" = 10₂. ✔
`0 + 1` da 01: S = 1, C = 0. ✔

> [!example] Del TP5
> El semisumador es el **ejercicio 1** del [[TP5 Sumadores|TP5]]: tabla de verdad + circuito combinacional.
> Después se encadena en el sumador completo (ej. 2) y en los de 4 y 8 bits (ej. 3 y 4).

## Cómo responderlo en el final (práctica)
1. Dibujar la tabla de verdad (4 filas).
2. Obtener las funciones por mintérminos y simplificar: `S = A⊕B`, `C = A·B`.
3. Dibujar el gráfico: entradas A y B a una XOR (salida S) y a una AND (salida C).
4. Cerrar con la limitación: **no tiene Cin** ⇒ sólo sirve para el LSB; el de la columna siguiente
   necesita un [[Sumador completo]].

## Errores típicos
- Dar `S = A + B` (eso es la OR; el 1+1 daría 1 y debería dar 0 con acarreo).
- Olvidar que C = A·B coincide con el acarreo del bit siguiente.

## Relacionado
[[Sumador completo]] · [[Compuertas lógicas]] · [[ALU]]
