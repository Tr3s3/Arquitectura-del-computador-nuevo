---
unidad: 1
tipo: concepto
examen: practica
---
# Álgebra de Boole — postulados y teoremas

> [!note] Si es la primera vez que ves esto
> El álgebra normal tiene números y operaciones (`+`, `×`). El **álgebra de Boole** tiene **sólo 1 y 0** y
> **tres** operaciones (OR, AND, NOT). Es el "idioma" con el que se escribe lo que hace un circuito. Sirve
> para algo muy concreto: **un circuito más chico es más barato, más rápido y consume menos**, y para
> achicarlo hay que saber reescribir su fórmula como se reescribe una expresión matemática. Cada regla de
> esta nota es una "cuenta permitida" que te deja simplificar. Si no las sabés, no podés simplificar nada.

> [!abstract] En una frase
> El álgebra de Boole es un sistema algebraico con **dos valores (0 y 1)**, tres operaciones
> (OR, AND, NOT) y un conjunto de **postulados** del que se deducen **teoremas** que permiten
> simplificar funciones lógicas (y por lo tanto, ahorrar compuertas).

## Definición formal (la que se pide en el final)
"Es un álgebra definida sobre un conjunto de dos elementos, B = {0, 1}, cerrada respecto de dos
operaciones binarias (+ = OR, · = AND) y una unaria (' = NOT), que cumple los postulados de
identidad, conmutatividad, distributividad y complemento."

## Los postulados
Son las reglas que se aceptan **sin demostración** (definen el álgebra).

| # | Postulado | Forma OR | Forma AND |
|---|---|---|---|
| 1 | **Identidad** (elemento neutro) | A + 0 = A | A · 1 = A |
| 2 | **Conmutativa** | A + B = B + A | A · B = B · A |
| 3 | **Asociativa** | A + (B + C) = (A + B) + C | A·(B·C) = (A·B)·C |
| 4 | **Distributiva** | A + (B·C) = (A+B)·(A+C) | A·(B + C) = A·B + A·C |
| 5 | **Complemento** | A + A' = 1 | A · A' = 0 |
| 6 | **Dominancia** (elemento nulo) | A + 1 = 1 | A · 0 = 0 |

> [!tip] Tres postulados para el final
> Si te piden "tres postulados", los más seguros (y los que se usan en toda simplificación) son:
> **identidad, distributiva y complemento**. Podés agregar conmutativa y dominancia para redondear.

## Teoremas (se deducen de los postulados)
| Teorema | Forma OR | Forma AND |
|---|---|---|
| Idempotencia | A + A = A | A · A = A |
| Involución (doble negación) | (A')' = A | — |
| Absorción | A + A·B = A | A·(A + B) = A |
| Absorción (variante) | A + A'·B = A + B | A·(A' + B) = A·B |
| Asociatividad del complemento | (A+B)' = A'·B' | (A·B)' = A' + B' | ← **DeMorgan** |
| Consenso | A·B + A'·C + B·C = A·B + A'·C | (A+B)(A'+C)(B+C) = (A+B)(A'+C) |

**Principio de dualidad:** si en una identidad válida se cambian 0↔1, ·↔+ y se mantienen las
variables, la identidad resultante también es válida. Es lo que permite escribir cada teorema en
sus dos formas sin memorizar el doble.

## Ejemplo de simplificación (estilo práctico)
Simplificar `F = A·B + A·B' + A'·B`:

```
F = A·B + A·B'  +  A'·B
  = A·(B + B')  +  A'·B      (distributiva)
  = A·1         +  A'·B      (complemento)
  = A           +  A'·B      (identidad)
  = A + B                    (absorción: A + A'B = A + B)
```

De 3 compuertas AND de 2 entradas + 1 OR de 3 a **una sola OR**: eso es ahorro de hardware y de
retardo de propagación. Ese es el sentido práctico del álgebra.

> [!example] Lo que pide la cátedra (TP2 y TP3)
> En el [[TP2 Álgebra de Boole|TP2]] hay que **demostrar** las leyes con tabla de verdad **y** con el circuito
> equivalente; en el [[TP3 Simplificación analítica|TP3]], simplificar una función **citando en cada paso la
> ley, regla o teorema** aplicado (eso es lo que se corrige). Práctica con Karnaugh: [[TP4 Mintérminos, maxtérminos y Karnaugh|TP4]].

## Cómo responderlo en el final
1. Definir el álgebra (conjunto {0,1}, operaciones +, ·, ', postulados).
2. Enunciar **tres postulados** (identidad, distributiva, complemento) y decir qué permiten (transformar
   una expresión sin cambiar su tabla de verdad).
3. Nombrar los teoremas principales y remarcar **DeMorgan** ([[Leyes de DeMorgan]]).
4. Cerrar con el objetivo: **minimizar la función = menos compuertas = más rápido y más barato**.

## Errores típicos
- Aplicar la distributiva "al revés" en forma incorrecta: en Boole **sí** vale `A + B·C = (A+B)(A+C)`
  (a diferencia del álgebra común).
- Usar `A + A'·B = A + B` sin justificar: conviene nombrar el teorema de absorción.
- Confundir dualidad (intercambiar operadores y elementos neutros) con complemento (negar variables).

## Relacionado
[[Leyes de DeMorgan]] · [[Mintérminos y maxtérminos]] · [[Compuertas lógicas]]
