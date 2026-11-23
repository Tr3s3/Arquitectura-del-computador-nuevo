---
tp: 7
unidad: 2
tipo: tp
prioridad: alta
---
# TP7 — Codificadores y multiplexores

> [!abstract] Consigna (cátedra)
> **Ej. 1:** codificador **4x2** y **8x3** con tabla de verdad y circuito combinacional.
> **Ej. 2:** multiplexor **2x1**, **4x1** y **8x1** con tabla de verdad y circuito combinacional.

> [!note] Notación de la cátedra
> Los TPs usan **I0…In** para las entradas de datos, **S0 S1 S2** para la selección y **Y** para la salida;
> en los codificadores usan **D0…Dn** para las entradas y **X Y Z** para las salidas. Conviene usar esas
> letras en el examen.

## Codificador 4x2
| D0 | D1 | D2 | D3 | X | Y |
|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 | 1 | 1 |

`X = D2 + D3`  ·  `Y = D1 + D3`  → **2 OR** (sólo dos compuertas).

## Codificador 8x3
| Entrada activa | X | Y | Z |
|---|---|---|---|
| D0 | 0 | 0 | 0 |
| D1 | 0 | 0 | 1 |
| D2 | 0 | 1 | 0 |
| D3 | 0 | 1 | 1 |
| D4 | 1 | 0 | 0 |
| D5 | 1 | 0 | 1 |
| D6 | 1 | 1 | 0 |
| D7 | 1 | 1 | 1 |

`X = D4+D5+D6+D7` · `Y = D2+D3+D6+D7` · `Z = D1+D3+D5+D7` → **3 OR de 4 entradas**.

> [!warning] Límite que conviene mencionar
> Si se activan dos entradas a la vez, la salida es la OR de los dos códigos (basura). Por eso en la
> práctica se usa un **codificador con prioridad** (74LS148), con las señales **GS** (hay pedido) y **EI/EO**
> (encadenamiento). Decir esto sube nota.

## Multiplexor 2x1
| S | Y |
|---|---|
| 0 | I0 |
| 1 | I1 |

`Y = I0·S' + I1·S`  → **1 NOT + 2 AND + 1 OR**

## Multiplexor 4x1
| S1 | S0 | Y |
|---|---|---|
| 0 | 0 | I0 |
| 0 | 1 | I1 |
| 1 | 0 | I2 |
| 1 | 1 | I3 |

`Y = I0·S1'S0' + I1·S1'S0 + I2·S1S0' + I3·S1S0`
Circuito: **2 NOT + 4 AND de 3 entradas + 1 OR de 4 entradas**.

![mux_4x1.svg](../assets/mux_4x1.svg)

## Multiplexor 8x1
Misma idea con 3 selectores: **8 AND de 4 entradas + 1 OR de 8**, con `Y = Σ (Ii · mintérmino de S)`.
Para dibujarlo sin morir: **un AND por entrada**, cada uno habilitado por la combinación de S2 S1 S0 que le
corresponde.

> [!tip] Regla general para todos
> **Codificador** = OR (2ⁿ → n) · **Decodificador** = AND con inversores (n → 2ⁿ) ·
> **Multiplexor** = AND + OR (2ⁿ → 1) · **Demultiplexor** = AND con D (1 → 2ⁿ).
> Si te acordás de esa tabla, los cinco circuitos del final salen solos.

## Enlaces
Desarrollo: [[Codificador]] · [[Multiplexor]] · Uso en la CPU: [[Flujo de información en BLUE (datos y direcciones)]]
Siguiente: [[TP8 Biestables RS]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Codificadores 4x2 y 8x3: funcionamiento y diseño](https://www.youtube.com/watch?v=sz7W2u1THdQ) | Les Ingenieurs |
| ▶️ | [Multiplexor 4x1](https://www.youtube.com/watch?v=gTcU-FrRioM) | Les Ingenieurs |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo
> desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se
> toma en el parcial).

