---
unidad: 1
tipo: concepto
examen: secundaria
---
# Mintérminos y maxtérminos

> [!abstract] En una frase
> Un **mintérmino** es un producto (AND) que vale 1 para **una sola** combinación de las variables;
> un **maxtérmino** es una suma (OR) que vale 0 para **una sola** combinación. Cualquier función se
> puede escribir como **suma de mintérminos (SOP)** o como **producto de maxtérminos (POS)**.

## Mintérminos
Para n variables hay 2ⁿ mintérminos. Cada mintérmino `mᵢ` se arma poniendo la variable negada si el bit
es 0 y directa si el bit es 1, con el subíndice igual al número binario de la combinación.

Con A B C:

| i | A B C | mintérmino mᵢ | maxtérmino Mᵢ |
|---|---|---|---|
| 0 | 0 0 0 | A'B'C' | A + B + C |
| 1 | 0 0 1 | A'B'C | A + B + C' |
| 2 | 0 1 0 | A'BC' | A + B' + C |
| 3 | 0 1 1 | A'BC | A + B' + C' |
| 4 | 1 0 0 | AB'C' | A' + B + C |
| 5 | 1 0 1 | AB'C | A' + B + C' |
| 6 | 1 1 0 | ABC' | A' + B' + C |
| 7 | 1 1 1 | ABC | A' + B' + C' |

**Regla:** el mintérmino usa la variable **directa cuando el bit es 1**; el maxtérmino usa la variable
**negada cuando el bit es 1** (son duales: `Mᵢ = (mᵢ)'`).

## Formas canónicas
- **SOP (suma de productos):** `F = Σm(1,3,5,7)` → OR de los mintérminos donde F = 1.
- **POS (producto de sumas):** `F = ΠM(0,2,4,6)` → AND de los maxtérminos donde F = 0.
Las dos formas describen **la misma función**: `Σm` de los unos = `ΠM` de los ceros.

> [!example] De tabla a función
> F(A,B,C) = 1 para las combinaciones 011, 101 y 110.
> - SOP: `F = A'BC + AB'C + ABC'`
> - POS: los ceros son 000, 001, 010, 100, 111 ⇒ `F = (A+B+C)(A+B+C')(A+B' + C)(A' + B + C)(A' + B' + C')`
>
> La SOP suele ser más corta; el POS es útil cuando hay pocos ceros. En la práctica se minimiza con
> **mapa de Karnaugh**.

## Para qué sirve en la materia
- El **decodificador** genera exactamente los mintérminos de la dirección: cada salida Yi es un mintérmino
  (ver [[Decodificador]]).
- La **suma de productos** es la forma natural de un circuito de dos niveles AND-OR, que es como se arma
  el [[Sumador completo]] y el [[Multiplexor]].
- El **mapa de Karnaugh** agrupa mintérminos adyacentes (que difieren en una variable) para eliminar esa
  variable: es álgebra de Boole hecha dibujo.

## Cómo responderlo en el final
Definir mintérmino/maxtérmino → dar la tabla de 3 variables como ejemplo → mostrar las dos formas
canónicas → decir que `Σm` de unos = `ΠM` de ceros y que el objetivo es minimizar.

## Errores típicos
- Invertir la regla: en el mintérmino la variable **no** se niega cuando el bit vale 1.
- Sumar mintérminos donde F = 0.
- Confundir `mᵢ` con la posición de la fila en la tabla si las variables están en otro orden.

## Relacionado
[[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] · [[Decodificador]]
