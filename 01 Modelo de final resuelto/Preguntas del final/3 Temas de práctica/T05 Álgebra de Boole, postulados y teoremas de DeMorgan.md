---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T05 · Álgebra de Boole: definición, 3 postulados y DeMorgan

> [!question] Pregunta
> Defina el álgebra de Boole, enuncie los postulados y demuestre los teoremas de DeMorgan.

## 1. Teoría previa

**Álgebra de Boole.** Es el álgebra de las variables que toman sólo dos valores: 0 y 1. Tiene tres operaciones básicas:

| Operación | Símbolo | Vale 1 cuando… |
|---|---|---|
| AND | `A · B` | ambas valen 1 |
| OR | `A + B` | alguna vale 1 |
| NOT | `A'` | A vale 0 |

**Postulados.** Son las reglas que se aceptan sin demostrar y definen el álgebra. Los tres principales que se piden:

| # | Postulado | Forma OR | Forma AND |
|---|---|---|---|
| 1 | Identidad | `A + 0 = A` | `A · 1 = A` |
| 2 | Conmutativa | `A + B = B + A` | `A · B = B · A` |
| 3 | Distributiva | `A + BC = (A+B)(A+C)` | `A(B+C) = AB + AC` |
| (4) | Complemento | `A + A' = 1` | `A · A' = 0` |
| (5) | Dominancia | `A + 1 = 1` | `A · 0 = 0` |

**Teoremas.** Se deducen de los postulados. Los más usados: idempotencia (`A+A = A`), involución (`(A')' = A`), absorción (`A + AB = A`), DeMorgan y consenso.

## 2. Contexto

El álgebra de Boole es la **herramienta** para simplificar funciones. Es lo que te deja pasar de una tabla de verdad a un circuito con menos compuertas. Por eso el profesor la pregunta junto con las prácticas de circuitos.

## 3. Gráfico

![[T05-boole-demorgan.svg]]

*Lectura:* arriba, las cuatro compuertas básicas. Abajo, la equivalencia de DeMorgan: un NAND es lo mismo que un OR con entradas negadas, y un NOR es un AND con entradas negadas.

## 4. Desarrollo detallado

### 4.1 Demostración de DeMorgan por tabla de verdad

**Primera ley:** `(A · B)' = A' + B'`

| A | B | A·B | (A·B)' | A' | B' | A' + B' |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Columna (A·B)' igual a columna A' + B': **demostrado**.

**Segunda ley:** `(A + B)' = A' · B'`

| A | B | A+B | (A+B)' | A' | B' | A'·B' |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Columna (A+B)' igual a A'·B': **demostrado**.

### 4.2 Regla práctica
Para negar una expresión: se cambia AND por OR, OR por AND, y cada variable por su negada. Por ejemplo, `(A + B·C)' = A'·(B' + C')`.

### 4.3 Uso en la simplificación
Ejemplo: `A·B + A·B' + A'·B`.
- Con `A·B + A·B' = A` (teorema de combinación): queda `A + A'·B`.
- Con el teorema de absorción variante (`A + A'B = A + B`): queda `A + B`.
- Resultado: 4 compuertas se reducen a 1 OR.

## 5. Cómo se responde (4 minutos)

1. **Definición:** "Álgebra sobre variables de dos valores, con AND, OR y NOT."
2. **Postulados:** identidad, conmutativa, distributiva, complemento y dominancia.
3. **DeMorgan:** enunciado de las dos leyes y demostración por tabla.
4. **Gráfico:** las compuertas y la equivalencia NAND / OR.
5. **Cierre:** "Con DeMorgan se cambia AND por OR negando todo: así se diseña con compuertas NAND o NOR."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué es el complemento? | A + A' = 1 y A · A' = 0. |
| ¿Por qué DeMorgan sirve? | Permite construir cualquier función con NAND o con NOR. |
| ¿Cuánto vale A + A·B? | A (absorción). |
| Error común | Escribir `(A·B)' = A'·B'`. La ley correcta es `A' + B'`. |

## 7. Relacionado

- [[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] · [[Compuertas lógicas]]
- [[1.1.2 NAND, NOR, XOR y XNOR]] · [[T01 Sumador completo (tabla de verdad, funciones y gráfico)]]
