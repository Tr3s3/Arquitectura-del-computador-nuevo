---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P05 · Memoria RAM 8×3

> [!question] Pregunta
> Dibuje y explique una memoria RAM de 8 palabras de 3 bits (8×3): cómo se selecciona una palabra, cómo se lee y cómo se escribe.

## 1. Teoría previa

**RAM (Random Access Memory).** Memoria de acceso aleatorio: cualquier posición tarda lo mismo en leerse o escribirse. Es volátil (pierde el contenido sin alimentación) y permite leer y escribir.

**Parámetros de toda memoria** (los cuatro que se pueden preguntar):

| Parámetro | En la 8×3 |
|---|---|
| Unidad de almacenamiento | 1 bit (la celda) |
| Capacidad | 8 × 3 = 24 bits |
| Tiempo de acceso | el que tarda una palabra desde que se direcciona |
| Tipo de acceso | aleatorio |

**Cuentas básicas.**
- 8 palabras = 2³ → **3 bits de dirección** (A2 A1 A0).
- Cada palabra tiene **3 bits de datos** (D2 D1 D0).
- Capacidad total: 8 × 3 = **24 bits**.

**Decodificador 3→8.** Tiene 3 entradas y 8 salidas. Para cada combinación de entrada, **una sola** salida vale 1. Es el mecanismo que activa una única palabra.

**Buffer de tres estados.** Conecta la salida al bus cuando está habilitado, y la desconecta (alta impedancia) cuando no. Sin él, las 8 palabras pelearían por el bus.

## 2. Contexto

La RAM 8×3 es el modelo didáctico de **toda** memoria. El profesor la pide porque quiere ver que entendés: (a) la relación entre bits de dirección y cantidad de palabras, (b) el rol del decodificador, (c) cómo se conecta al bus. Es la pregunta de peso alto y tiene un dibujo obligatorio.

## 3. Gráfico

![[P05-ram-8x3.svg]]

*Lectura:* a la izquierda está el mapa de direcciones (dirección → contenido). En el centro, el decodificador 3→8 activa una línea; esa línea habilita una palabra de 3 bits. La salida pasa por el buffer hacia el bus de datos. CS y R/W' controlan la operación.

## 4. Desarrollo detallado

### 4.1 Mapa de direcciones (la tabla que se dibuja)

| Dirección | Contenido (3 bits) |
|---|---|
| 000 | 010 |
| 001 | 110 |
| 010 | 001 |
| 011 | 100 |
| 100 | 111 |
| 101 | 011 |
| 110 | 000 |
| 111 | 101 |

### 4.2 Lectura, paso a paso

1. La CPU pone la dirección (por ejemplo `010`) en las líneas A2 A1 A0.
2. El decodificador activa la salida 2 (solamente).
3. La palabra 2 pone sus 3 bits (`001`) en las líneas de salida del buffer.
4. El buffer está habilitado porque **CS = 1** y **R/W' = 1** (lectura). El dato va al bus de datos.

### 4.3 Escritura, paso a paso

1. La dirección (`010`) entra al decodificador.
2. El dato a escribir está en el bus de datos.
3. Con **CS = 1** y **R/W' = 0** (escritura), en el flanco de reloj los 3 flip-flops de la palabra seleccionada cargan el dato.
4. Las demás palabras no cambian porque sus líneas de selección valen 0.

### 4.4 Rol de CS (chip select)

CS habilita el chip completo. Si CS = 0, el chip no responde aunque la dirección sea correcta. Es imprescindible cuando hay **varios chips** en el mismo bus: sólo uno debe hablar.

### 4.5 Organización 2D y 3D

- **2D** (esta RAM): una línea de selección por palabra. Simple, pero el decodificador crece con el número de palabras.
- **3D**: dos decodificadores más chicos (filas y columnas) cuyas salidas deben coincidir. Se usa en memorias grandes porque ahorra hardware.

### 4.6 Expansión

- **Horizontal** (más bits por palabra): mismas direcciones y CS, datos en paralelo.
- **Vertical** (más palabras): datos y control compartidos, y un decodificador que genera CS para cada chip.

### 4.7 Relación con BLUE

El mismo esquema escalado es la memoria de BLUE: 12 bits de dirección → 4096 palabras, de 16 bits cada una.

## 5. Cómo se responde (4 minutos)

1. **Definición:** "Es una memoria de 8 palabras de 3 bits, 24 bits en total, con 3 bits de dirección."
2. **Dibujo:** decodificador 3→8, las 8 palabras, buffer de tres estados, CS y R/W'.
3. **Desarrollo:** lectura y escritura paso a paso con un ejemplo.
4. **Cierre:** "La dirección es el índice de la fila; el decodificador enciende una sola."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Para qué sirve el decodificador si ya mando la dirección? | Convierte el número en una única línea encendida, que activa una sola palabra. |
| ¿Qué pasa si se activan dos CS a la vez? | Dos chips ponen datos en el bus: conflicto. Por eso se usan tres estados y se activa sólo uno. |
| ¿Cuántos bits de dirección tiene una memoria de 1024 palabras? | 10 (2¹⁰ = 1024). |
| Error común | Olvidar CS en el dibujo. Sin CS el chip no se puede expandir. |

## 7. Relacionado

- [[Memoria RAM 8x3]] · [[2.3.3 Matriz, expansión y RAM 8x3]] · [[Tablas de verdad de memoria]]
- [[P04 Estructura básica de un computador]] · [[S01 Memoria RAM (celda elemental)]]
