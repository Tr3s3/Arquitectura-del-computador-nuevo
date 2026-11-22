---
unidad: 2
tipo: concepto
examen: practica
prioridad: alta
---
# Multiplexor (MUX)

> [!note] Si es la primera vez que ves esto
> Un multiplexor es **un conmutador de vías**: muchos cables entran, uno solo sale, y un par de señales de
> selección deciden **cuál** de las entradas pasa a la salida. Se usa para todo lo que signifique "elegir
> uno entre varios": elegir qué registro pone su contenido en el bus, elegir qué índice entra al sumador de
> direcciones, elegir un canal de televisión por un mismo cable. Es el inverso del demultiplexor y el primo
> del decodificador: **mismo concepto de selección, distinta dirección del flujo**.

> [!abstract] En una frase
> El multiplexor es un **selector de datos**: tiene 2ⁿ entradas de datos, n entradas de **selección** y
> **una sola salida**; la salida toma el valor de la entrada indicada por el código de selección.
> Ecuación de un MUX 4→1: `Z = S1'S0'D0 + S1'S0D1 + S1S0'D2 + S1S0D3`.

## Contexto: el bus necesita un MUX
En un bus, **muchos registros quieren escribir y sólo uno puede hacerlo por vez**. El multiplexor es el
circuito que decide **cuál** de las fuentes llega al bus. Por eso aparece en:
- la selección de la fuente que entra a la ALU (AC, MBR, RIF/RID…),
- el bus de datos de la memoria,
- la selección de la próxima dirección del PC (PC+1, dirección de salto, dirección de interrupción),
- el interior de cada registro de desplazamiento con carga paralela ([[Registros]]).

## Multiplexor 4 a 1 — tabla de verdad
| S1 | S0 | Z |
|---|---|---|
| 0 | 0 | D0 |
| 0 | 1 | D1 |
| 1 | 0 | D2 |
| 1 | 1 | D3 |

![mux_4x1](../assets/mux_4x1.svg)

**Estructura:** por cada entrada de datos, una compuerta AND de 3 entradas (el dato + los dos selectores,
negados o no según corresponda) y una **OR final** de 4 entradas. Es decir: **AND-OR = suma de productos**.

## Expansión (jerarquía de MUX)
- Un MUX **8→1** se arma con dos 4→1 y un 2→1 final que elige entre las dos salidas con el bit más
  significativo.
- Un MUX **16→1** con cinco 4→1 (dos niveles).
- Esta estructura en árbol es exactamente cómo se implementa un **bus de muchos maestros**.

## Multiplexor como función universal
Con un MUX de 2ⁿ entradas **se puede implementar cualquier función de n variables**: se conectan las
n variables a las entradas de selección y cada entrada de datos se lleva a 0 o 1 según la tabla de verdad
(F = 1 ⇒ Dᵢ = 1). Es la alternativa al mapa de Karnaugh cuando la función es desordenada.

## Aplicaciones
1. Selección de fuente en el bus de la CPU ([[Flujo de información en BLUE (datos y direcciones)]]).
2. Selección de registros y de operandos en la [[ALU]].
3. Transmisión paralelo→serie (junto con un registro de desplazamiento): un MUX que va eligiendo bits
   uno por uno.
4. En las [[Memoria caché]]/memorias: selección de banco.

> [!example] Del TP7 (y su notación)
> El [[TP7 Codificadores y multiplexores|TP7]] pide **MUX 2x1, 4x1 y 8x1** y usa la notación
> **I0…In − S0 S1 − Y**. Usá esas letras en el examen (y en los codificadores, **D0…Dn − X Y Z**).

## Cómo responderlo en el final (práctica)
1. Definición (selector de datos, 2ⁿ → 1).
2. Tabla de verdad del 4→1.
3. **Función**: `Z = S1'S0'D0 + S1'S0D1 + S1S0'D2 + S1S0D3`.
4. **Gráfico**: 4 AND de 3 entradas + OR de 4 (o el bloque trapezoidal con sus pines D0…D3, S1 S0, Z).
5. Cerrar con el uso: es el que decide qué fuente escribe en el bus.

> [!tip] Demultiplexor vs multiplexor
> El MUX es **N → 1** (muchas entradas, una salida). El [[Demultiplexor]] es **1 → N**.
> Mnemotecnia: **MUX = "muchos a uno"**.

## Errores típicos
- Escribir la ecuación sin negar los selectores (cada producto debe valer 1 sólo para su combinación).
- Decir que el MUX tiene memoria: **no**, es puramente combinacional.
- Confundir el selector con el dato: el selector elige, el dato se transmite.

## Relacionado
[[Demultiplexor]] · [[Decodificador]] · [[Registros]] · [[Flujo de información en BLUE (datos y direcciones)]]
