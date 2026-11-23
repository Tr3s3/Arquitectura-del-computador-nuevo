---
tp: 6
unidad: 2
tipo: tp
prioridad: alta
---
# TP6 — Decodificadores y demultiplexores

> [!abstract] Consigna (cátedra)
> Construir, **con tabla de verdad y circuito combinacional**, los decodificadores y demultiplexores
> (el TP pide el decodificador 2→4 y 3→8, y el demultiplexor 1→4).

## Qué hay que saber para resolverlo
Los dos circuitos se dibujan **igual**: un conjunto de compuertas **AND** (una por salida) y los
**inversores** que generan las variables negadas. La diferencia está en la ecuación:

- **Decodificador**: `Yi = mintérmino i de las entradas` (una sola salida en 1).
- **Demultiplexor**: `Yi = D · mintérmino i del selector` (una sola salida **toma el valor de D**).

## Decodificador 2 → 4
| A1 | A0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

`Y0 = A1'A0'` · `Y1 = A1'A0` · `Y2 = A1A0'` · `Y3 = A1A0`
Circuito: **2 NOT + 4 AND de 2 entradas**.

![decodificador_2x4.svg](../assets/decodificador_2x4.svg)

## Decodificador 3 → 8
8 salidas (una por cada combinación de A2 A1 A0), **3 NOT + 8 AND de 3 entradas**. Es el que se usa para
seleccionar una palabra de memoria o habilitar un registro.

![decodificador_3x8.svg](../assets/decodificador_3x8.svg)

## Demultiplexor 1 → 4
| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| 0 | 0 | D | 0 | 0 | 0 |
| 0 | 1 | 0 | D | 0 | 0 |
| 1 | 0 | 0 | 0 | D | 0 |
| 1 | 1 | 0 | 0 | 0 | D |

`Y0 = D·S1'S0'` · `Y1 = D·S1'S0` · `Y2 = D·S1S0'` · `Y3 = D·S1S0`
Circuito: **2 NOT + 4 AND de 3 entradas** (el dato D entra a todas).

![demux_1x4.svg](../assets/demux_1x4.svg)

> [!tip] La respuesta que cierra bien
> "Un decodificador es un demultiplexor con la entrada de datos fija en 1". Si te piden la diferencia,
> esa frase resuelve la pregunta y muestra que entendiste los dos.

## Enlaces
Desarrollo: [[Decodificador]] · [[Demultiplexor]] · Aplicación: [[Memoria RAM 8x3]]
Siguiente: [[TP7 Codificadores y multiplexores]]
