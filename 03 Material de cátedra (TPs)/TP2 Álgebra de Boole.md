---
tp: 2
unidad: 1
tipo: tp
---
# TP2 — Álgebra de Boole

> [!abstract] Consigna (cátedra)
> **"Álgebra de Boole: ¿qué es? ¿para qué sirve? Desarrolle sus leyes, reglas y teoremas, mediante las tablas de verdad y circuitos lógicos."**

## Qué hay que saber para resolverlo
No alcanza con enunciar: la cátedra pide **demostrar** cada ley con **tabla de verdad** y mostrar el **circuito equivalente**. Estructura de la respuesta oral:

1. **Definición**: álgebra sobre B = {0, 1} con tres operaciones (+, ·, ') que cumple los postulados de identidad, conmutatividad, distributividad y complemento.

2. **Para qué sirve**: para **diseñar, analizar y simplificar** circuitos digitales. Toda función lógica tiene una expresión booleana y toda expresión un circuito de compuertas; simplificar = **menos compuertas, menos costo, menos retardo**. Permite **sintetizar** (de la tabla al circuito) y **analizar** (del circuito a la función).

3. **Postulados** (se aceptan sin demostrar): identidad, conmutativa, asociativa, distributiva, complemento, dominancia.

4. **Teoremas** (se demuestran): idempotencia, involución, absorción, DeMorgan, consenso.

5. **Dualidad**: intercambiando 0↔1 y +↔· toda identidad válida sigue siendo válida.

6. **Circuito equivalente**: para cada ley, dibujar las dos versiones y decir "misma tabla de verdad ⇒ mismo comportamiento, pero con menos compuertas".

> [!tip] Cómo "demostrar" rápido en el oral
> Armá una tabla con **todas las columnas de las dos expresiones** y mostrá que son idénticas (4 u 8 filas). Después dibujá las dos versiones del circuito y señalá cuál usa menos compuertas. Eso es exactamente lo que pide el TP.

## Leyes y teoremas — tabla de referencia

| Nombre | Forma OR | Forma AND |
|---|---|---|
| Identidad | A + 0 = A | A · 1 = A |
| Dominancia | A + 1 = 1 | A · 0 = 0 |
| Idempotencia | A + A = A | A · A = A |
| Complemento | A + A' = 1 | A · A' = 0 |
| Involución | (A')' = A | — |
| Conmutativa | A + B = B + A | A·B = B·A |
| Asociativa | (A+B)+C = A+(B+C) | (A·B)·C = A·(B·C) |
| Distributiva | A + B·C = (A+B)(A+C) | A(B+C) = AB + AC |
| Absorción | A + A·B = A | A(A+B) = A |
| Absorción (2) | A + A'B = A + B | A(A'+B) = AB |
| **DeMorgan** | (A+B)' = A'·B' | (A·B)' = A' + B' |
| Consenso | AB + A'C + BC = AB + A'C | (A+B)(A'+C)(B+C) = (A+B)(A'+C) |

## Enlaces
Desarrollo: [[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] Siguiente: [[TP3 Simplificación analítica]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Leyes básicas del álgebra de Boole](https://www.youtube.com/watch?v=4vQdCfCmVoc) | Clases en Línea |
| ▶️ | [Reglas 1 a 9 del álgebra de Boole](https://www.youtube.com/watch?v=Buk8kMQ3XjM) | Clases en Línea |
| ▶️ | [Reglas 10, 11 y 12 con demostración](https://www.youtube.com/watch?v=OjsO6Uqr-ms) | Clases en Línea |
| ▶️ | [1.er teorema de DeMorgan](https://www.youtube.com/watch?v=VL5v4et23oc) | Estudia con Marisol |
| ▶️ | [2.º teorema de DeMorgan](https://www.youtube.com/watch?v=VSGAyg8xOmM) | Estudia con Marisol |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
