---
unidad: 1
tipo: concepto
examen: practica
---
# Compuertas lógicas

> [!abstract] En una frase
> La compuerta es el **bloque mínimo de hardware** que realiza una operación del álgebra de Boole:
> recibe una o más entradas binarias y entrega una salida binaria según su tabla de verdad.
> Todo el computador es una red enorme de compuertas.

## Contexto: ¿por qué binario y por qué compuertas?
Un computador digital trabaja con dos niveles de tensión (por ejemplo 0 V y 5 V) que se interpretan
como **0** y **1**. La ventaja es la inmunidad al ruido: reconstruir dos niveles es fácil, reconstruir
diez no. Como esos dos niveles se comportan según el álgebra de Boole, cada función lógica tiene un
circuito electrónico directo. Ese circuito es la compuerta.

## Las siete compuertas de la cátedra

| A | B | AND (A·B) | OR (A+B) | NAND | NOR | XOR (A⊕B) | XNOR |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

La NOT es de una entrada: `NOT A = A' = Ā`, y vale 1 cuando A = 0.

**Cómo leerlas sin memorizar la tabla**
- AND = "todas": la salida es 1 sólo si **todas** las entradas son 1.
- OR = "alguna": la salida es 1 si **alguna** entrada es 1.
- NAND / NOR = la AND / OR negada. Como toda función se puede armar con NAND o con NOR, se las llama **compuertas universales**.
- XOR = "distintas": vale 1 cuando las entradas **son diferentes**. Es la compuerta de la suma sin acarreo
  (por eso aparece en el [[Semisumador]]) y del comparador de igualdad.

> [!tip] Regla mnemotécnica de XOR
> **XOR = OR de las diferencias**: `A⊕B = A'·B + A·B'`. Si te olvidás, escribí esa fórmula: es un [[Mintérminos y maxtérminos|mintérmino]] doble.

## Por qué importa para el resto de la materia
- La **ALU** es un conjunto de compuertas que, según el código de operación, deja pasar el resultado
  de una suma (sumadores de la Unidad 9), de una AND, de una XOR, etc.
- El **decodificador** de una memoria es una matriz de AND: cada palabra de la memoria se habilita con
  un mintérmino de la dirección (ver [[Memoria RAM 8x3]]).
- El **multiplexor**, que es el que decide *qué* valor circula por un bus, también es AND-OR
  (ver [[Multiplexor]]).
- Los **biestables** de la Unidad 2 se arman con dos compuertas NOR o NAND realimentadas
  (ver [[Flip-Flops SR, D, JK y T]]).

## Cómo responderlo en el final
1. Definición: "una compuerta es la realización física de un operador booleano; tiene una tabla de verdad".
2. Nombrar las siete y su función en una frase cada una.
3. Cerrar con la idea de jerarquía: compuerta → circuito combinacional → bloque funcional (ALU, decodificador,
   registro) → unidad (CPU, memoria) → computador. **Todo lo digital se construye con compuertas.**

## Errores típicos
- Confundir OR con **OR exclusiva**: en OR, 1+1 = 1 (no hay acarreo).
- Decir que NAND es "AND negada" y dibujarla sin el círculo de negación.
- Olvidar que las compuertas son **combinacionales**: no tienen memoria, su salida depende sólo de
  la entrada en ese instante (a diferencia de los biestables).

## Relacionado
[[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] · [[Sumador completo]] · [[ALU]]
