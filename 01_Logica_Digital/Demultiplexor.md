---
unidad: 2
tipo: concepto
examen: practica
prioridad: alta
---
# Demultiplexor (DEMUX)

> [!abstract] En una frase
> Es lo inverso del [[Multiplexor]]: recibe **una entrada de datos D** y la dirige a **una de las 2ⁿ
> salidas**, la que indica el código de selección; las demás salidas quedan en 0.

## Contexto
Cuando un solo dato debe llegar a **muchos destinos posibles** (por ejemplo, escribir el mismo dato en
uno de varios registros, o repartir datos desde una línea a varios periféricos) se usa un DEMUX.
También es el modelo del **demultiplexado de direcciones**: una dirección decodificada que "se reparte".

## Demultiplexor 1 a 4 — tabla de verdad
| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| 0 | 0 | **D** | 0 | 0 | 0 |
| 0 | 1 | 0 | **D** | 0 | 0 |
| 1 | 0 | 0 | 0 | **D** | 0 |
| 1 | 1 | 0 | 0 | 0 | **D** |

## Funciones
`Y0 = D·S1'·S0'`  `Y1 = D·S1'·S0`  `Y2 = D·S1·S0'`  `Y3 = D·S1·S0`

![demux_1x4](assets/demux_1x4.svg)

**Estructura:** 4 compuertas **AND de 3 entradas**: en cada una entra el dato D y la combinación de
selectores que la habilita. (Si el dato D es siempre 1, el DEMUX se comporta como un **decodificador**:
por eso "DEMUX con D = 1" y "decodificador" son casi lo mismo.)

## DEMUX vs decodificador (pregunta de examen)
- **Decodificador**: n entradas de código → 2ⁿ salidas; la salida activa es **siempre 1**.
- **DEMUX**: n entradas de código + 1 entrada de **datos** → 2ⁿ salidas; la salida activa **copia el dato**
  (puede ser 1 o 0).
⇒ Un decodificador es un DEMUX cuya entrada de datos está fija en 1. En la práctica muchos fabricantes usan
el mismo C.I. para las dos funciones.

## Aplicaciones
1. Repartir un dato hacia uno de varios registros o periféricos.
2. **Escritura en memoria** de varios chips (la señal de escritura se demultiplexa por banco).
3. Distribución de pulsos de reloj/ habilitación a distintos bloques (clock gating).
4. Conversión serie → paralelo cuando se usa junto con un registro de desplazamiento.

## Cómo responderlo en el final (práctica)
1. Definición (1 → 2ⁿ, dirige el dato).
2. Tabla de verdad del 1→4.
3. Funciones `Yi = D · (selector correspondiente)`.
4. Gráfico: 4 AND de 3 entradas con D común y los selectores.
5. Relación con el decodificador y con el MUX (uno reparte, el otro selecciona).

## Errores típicos
- Dejar el dato afuera de la ecuación (`Y0 = S1'S0'` sería un decodificador, no un DEMUX).
- Invertir la cantidad de entradas y salidas.
- Pensar que pueden estar activas dos salidas: **siempre una sola** lleva el dato.

## Relacionado
[[Multiplexor]] · [[Decodificador]] · [[Memoria RAM 8x3]]
