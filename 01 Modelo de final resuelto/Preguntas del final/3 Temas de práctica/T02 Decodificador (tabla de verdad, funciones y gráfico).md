---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T02 · Decodificador (tabla de verdad, funciones y gráfico)

> [!question] Pregunta
> Explique el decodificador: tabla de verdad, funciones y gráfico (2 → 4).

## 1. Teoría previa

**Decodificador.** Circuito combinacional con `n` entradas y `2ⁿ` salidas. Para cada combinación de entrada, **una sola** salida vale 1 (la que tiene el número de esa combinación). Es el circuito que "elige" una línea.

**Mintérmino.** Un producto que vale 1 para exactamente una combinación. En un decodificador 2→4, cada salida es un mintérmino de `A1` y `A0`.

**Uso.** Activar una palabra de memoria (la RAM 8×3 tiene un decodificador 3→8), elegir un periférico, o implementar funciones lógicas.

## 2. Contexto

El decodificador es la pieza que **direcciona** memoria. Si entendés el decodificador, entendés cómo se elige una palabra en P05 y cómo se elige una celda de la ROM en S04.

## 3. Gráfico

![[T02-decodificador.svg]]

*Lectura:* las entradas A1 y A0 llegan a la izquierda; las salidas Y0 a Y3 salen a la derecha. La tabla de abajo muestra qué salida vale 1 para cada entrada.

## 4. Desarrollo detallado

### 4.1 Tabla de verdad 2 → 4

| A1 | A0 | Y3 | Y2 | Y1 | Y0 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 |

### 4.2 Funciones

Cada salida es un mintérmino:
- `Y0 = A1'·A0'`
- `Y1 = A1'·A0`
- `Y2 = A1·A0'`
- `Y3 = A1·A0`

Es decir, `Yi = m_i` (el mintérmino del número i).

### 4.3 Circuito

- Dos inversores para `A1'` y `A0'`.
- Cuatro compuertas **AND** de dos entradas, una por cada mintérmino.
- Si hay habilitación `EN`, se agrega una entrada más a cada AND (sólo activa la salida si EN = 1).

### 4.4 Ejemplo de uso
Para elegir la palabra 2 de una memoria, se pone `A1A0 = 10`. Sólo `Y2` vale 1, y ese es el CS o la línea de selección de esa palabra.

## 5. Cómo se responde (4 minutos)

1. **Definición:** "Tiene n entradas y 2ⁿ salidas; sólo una vale 1 según la entrada."
2. **Tabla:** las 4 filas de 2 → 4.
3. **Funciones:** `Yi = m_i`, con las cuatro ecuaciones.
4. **Gráfico:** inversores, cuatro AND.
5. **Cierre:** "Es el circuito que convierte un número en una línea encendida."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántas salidas tiene un 3 → 8? | 8. |
| ¿Cuántas AND necesita un 2 → 4? | 4. |
| ¿Qué pasa con EN = 0? | Todas las salidas quedan en 0. |
| Error común | Confundir el decodificador con el multiplexor. El decodificador activa una salida según la entrada; el multiplexor elige una entrada. |

## 7. Relacionado

- [[Decodificador]] · [[1.4.1 Decodificador]] · [[TP6 Decodificadores y demultiplexores]]
- [[T03 Demultiplexor (tabla de verdad, funciones y gráfico)]] · [[T04 Multiplexor (tabla de verdad, funciones y gráfico)]] · [[P05 Memoria RAM 8x3]]
