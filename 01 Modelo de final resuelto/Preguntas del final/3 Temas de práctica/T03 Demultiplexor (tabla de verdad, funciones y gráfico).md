---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T03 · Demultiplexor (tabla de verdad, funciones y gráfico)

> [!question] Pregunta
> Explique el demultiplexor 1 → 4: tabla de verdad, funciones, gráfico y en qué se diferencia del decodificador.

## 1. Teoría previa

**Demultiplexor (DEMUX).** Circuito con **una entrada de datos D**, `n` líneas de selección y `2ⁿ` salidas. Envía el dato D a **una** de las salidas, la que indica la selección. Las demás salidas valen 0.

**Relación con el decodificador.** Un demultiplexor es un decodificador al que se le agrega una entrada de datos D: `Yi = D · (mintérmino i)`.

## 2. Contexto

El demux aparece en el final porque es el "complemento" del multiplexor: uno reparte, el otro recoge. Es también el circuito que usa un bus para enviar un dato a un solo destino.

## 3. Gráfico

![[T03-demultiplexor.svg]]

*Lectura:* el dato D entra a la izquierda; las selecciones S1 S0 controlan a cuál salida va. La tabla muestra qué salida recibe D para cada selección.

## Figuras reales (libros y resumen de cátedra)

![[libro-quiroga-f6-19.png]]

*Fig. 6.19 — Diagrama de bloque de un demultiplexor de cuatro salidas.* · Quiroga, *Arquitectura de computadoras*, p. 149

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Tabla de verdad 1 → 4

| S1 | S0 | Y3 | Y2 | Y1 | Y0 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | D |
| 0 | 1 | 0 | 0 | D | 0 |
| 1 | 0 | 0 | D | 0 | 0 |
| 1 | 1 | D | 0 | 0 | 0 |

### 4.2 Funciones

- `Y0 = D · S1'·S0'`
- `Y1 = D · S1'·S0`
- `Y2 = D · S1·S0'`
- `Y3 = D · S1·S0`

Es decir, `Yi = D · (selección i)`.

### 4.3 Circuito

- Dos inversores para `S1'` y `S0'`.
- Cuatro AND de **tres** entradas: D, y los dos bits de selección (o sus negados).

### 4.4 Diferencia con el decodificador

| | Decodificador | Demultiplexor |
|---|---|---|
| Entradas de datos | ninguna | una (D) |
| Entradas de selección | n | n |
| Salidas | 2ⁿ | 2ⁿ |
| Salida activa | la que indica la entrada, a 1 | la que indica la selección, con el valor de D |
| Uso típico | direccionar una palabra | enviar un dato a un destino |

Un decodificador con `EN` se convierte en demux usando EN como entrada de datos D.

## 5. Cómo se responde (4 minutos)

1. **Definición:** "Un dato D que se envía a una de 2ⁿ salidas según la selección."
2. **Tabla:** 1 → 4 con D en la salida elegida.
3. **Funciones:** `Yi = D · sel_i`.
4. **Gráfico:** cuatro AND de tres entradas.
5. **Diferencia:** el decodificador no tiene entrada de datos; el demux sí.

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué pasa si D = 0? | Todas las salidas valen 0. |
| ¿Cuántas líneas de selección tiene un 1 → 8? | 3. |
| ¿Es lo mismo que un multiplexor? | No: el multiplexor elige una entrada y la pone en la salida. El demux reparte una entrada. |
| Error común | Escribir `Yi = sel_i` sin D. |

## 7. Relacionado

- [[Demultiplexor]] · [[TP6 Decodificadores y demultiplexores]]
- [[T02 Decodificador (tabla de verdad, funciones y gráfico)]] · [[T04 Multiplexor (tabla de verdad, funciones y gráfico)]]
