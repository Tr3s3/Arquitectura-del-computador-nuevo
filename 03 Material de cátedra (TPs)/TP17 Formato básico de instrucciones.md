---
tp: 17
unidad: 4
tipo: tp
prioridad: alta
---
# TP17 — Formato básico de instrucciones

> [!abstract] Consigna (cátedra)
> **Ej. 1:** características del formato básico de una **palabra instrucción**; partes que la componen; **gráfico de una palabra instrucción de 2 bytes**. **Ej. 2:** características del formato de una **palabra dato**; gráfico de una palabra de **4 bytes**. **Ej. 3:** gráfico de una memoria principal de **256 MB con celdas de 1 byte**, ubicando una palabra instrucción de 2 bytes y una palabra dato de 4 bytes (direcciones en **hexadecimal**).

## Ej. 1 — Palabra instrucción (2 bytes = 16 bits)
Tiene **dos partes**:

| Campo | Bits | Contenido |
|---|---|---|
| **CodOp** (código de operación) | **4** | qué operación se hace (16 operaciones posibles) |
| **Dirección** | **12** | dirección del operando en memoria (2¹² = 4096 posiciones) |

```
 ┌──────┬──────────────────────────────┐
 │CodOp │         Dirección            │
 │4 bits│           12 bits            │
 └──────┴──────────────────────────────┘
```
**Ejemplo del TP:** `0000 0101 0000 0001` ⇒ CodOp `0000`, dirección `0101 0000 0001` (= 0x501).

## Ej. 2 — Palabra dato (4 bytes = 32 bits)
La palabra dato **no se divide**: usa **todos los bits** para el dato (un número, una dirección o un carácter). Si la celda de memoria es más chica que la palabra, el dato se **reparte en varias celdas consecutivas**.
```
 ┌──────────────────────────────────────────────────────┐
 │                     Datos  (32 bits)                 │
 └──────────────────────────────────────────────────────┘
```
**Ejemplo del TP:** `0000 0000 0000 0000 0000 0000 1100 1001` ⇒ valor `0x000000C9`.

## Ej. 3 — Memoria de 256 MB con celdas de 1 byte

1. **Cantidad de celdas** = 256 MB / 1 B = 256 M celdas = 2²⁸ celdas.

2. **Bits de dirección** = log₂(2²⁸) = **28 bits** ⇒ direcciones de `0x0000000` a `0xFFFFFFF`.

3. **Ubicación de las palabras**: cada celda tiene **1 byte**, así que la palabra instrucción de 2 bytes ocupa **2 celdas consecutivas** y la palabra dato de 4 bytes ocupa **4 celdas consecutivas**:

```
 Dirección   Contenido
 0x0000000   ┌──────────────┐
             │ CodOp(4) Dir(12) │ ← byte alto de la palabra instrucción
 0x0000001   │  (resto)         │ ← byte bajo  (ocupa 2 celdas)
 0x0000002   ┌──────────────┐
             │ dato byte 3  │
 0x0000003   │ dato byte 2  │   ← palabra dato de 4 bytes
 0x0000004   │ dato byte 1  │      (4 celdas consecutivas)
 0x0000005   │ dato byte 0  │
 ...
 0xFFFFFFF   └──────────────┘
```

> [!tip] El punto que se evalúa
> **La celda no tiene por qué coincidir con la palabra.** Si la celda es de 1 byte y la palabra de 2 o 4 bytes, la palabra se guarda en **varias celdas consecutivas** y hace falta **más de un acceso** para traerla. Ese es el motivo por el que los diseños reales usan celdas del tamaño de la palabra (o directamente palabras de 2 bytes), y es el tema del [[TP18 Direccionamiento de memoria]].

## Enlaces
Desarrollo: [[Formato de la instrucción (4 formatos)]] · [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] Siguiente: [[TP18 Direccionamiento de memoria]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Formato básico de instrucciones y código de operación](https://www.youtube.com/watch?v=FtzdL81PgrQ) | FNE Profesor |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
