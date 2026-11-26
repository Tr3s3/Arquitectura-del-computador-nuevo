---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S01 · Memoria RAM: celda elemental

> [!question] Pregunta
> Describa la celda elemental de una memoria RAM: qué elementos tiene, cómo guarda un bit y cómo se lee y se escribe. Diferencia entre SRAM y DRAM.

## 1. Teoría previa

**Celda elemental.** Es el circuito que guarda **un bit**. Toda memoria se construye repitiendo celdas en una matriz.

**Cuatro bloques de la celda:**

| Bloque | Para qué sirve | Qué pasa si falta |
|---|---|---|
| Biestable (o capacitor) | guardar el bit | no hay memoria, hay cable |
| Línea de selección | que la celda sepa que la eligieron | todas responderían a la vez |
| Línea L/E (o R/W') | decidir lectura o escritura | escribirías cuando querés leer |
| Buffer de tres estados | conectarse o desconectarse del bus | todas las celdas pelearían por el bus |

**SRAM vs DRAM.**

| | SRAM | DRAM |
|---|---|---|
| Qué guarda el bit | biestable (dos inversores realimentados) | capacitor (cargado = 1) |
| Transistores por celda | ~6 | 1 transistor + 1 capacitor |
| ¿Necesita refresco? | no | sí, el capacitor se descarga |
| Velocidad | más rápida | más lenta |
| Densidad y costo | menor densidad, más cara | mucho más densa y barata |
| Dónde se usa | caché y registros | memoria principal |

## 2. Contexto

Es la pregunta que va "de abajo hacia arriba": de la celda a la memoria. Aparece en el final porque conecta la RAM 8×3 (P05) con la caché (T07). Si la explicás bien, las otras memorias te salen solas.

## 3. Gráfico

![[S01-celda-elemental.svg]]

*Lectura:* el biestable guarda el bit. La línea de selección y la L/E llegan desde arriba. A la derecha, el buffer de tres estados conecta la salida al bus de datos compartido.

## 4. Desarrollo detallado

### 4.1 Escritura
1. La línea de selección activa la celda.
2. L/E = escritura: el dato del bus entra al biestable.
3. El biestable queda con ese valor mientras haya alimentación.

### 4.2 Lectura
1. La línea de selección activa la celda.
2. L/E = lectura: el buffer se habilita y el valor del biestable sale al bus.
3. Al terminar, el buffer vuelve a alta impedancia.

### 4.3 Qué pasa en la DRAM
El capacitor pierde carga con el tiempo. Hay que **refrescar** (leer y reescribir) las filas periódicamente. Por eso la DRAM es más lenta pero mucho más densa.

### 4.4 Organización de la matriz
- **2D**: una línea de selección por fila de palabras.
- **3D**: dos decodificadores más chicos (filas y columnas) deben coincidir; ahorra hardware en memorias grandes.

## 5. Cómo se responde (2–3 minutos)

1. **Definición:** "La celda es el circuito que guarda un bit, con selección, L/E y buffer de tres estados."
2. **Dibujo:** biestable, selección, L/E, buffer, bus.
3. **Diferencia:** SRAM con biestable (rápida, cara, caché); DRAM con capacitor (densa, refresco, memoria principal).
4. **Cierre:** "Repitiendo la celda en una matriz se forma la memoria."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Por qué la DRAM necesita refresco? | El capacitor se descarga por fugas. |
| ¿Por qué la caché es SRAM? | Porque es rápida y no necesita refresco. |
| ¿Para qué sirve el buffer de tres estados? | Para que sólo una celda hable en el bus. |
| Error común | Decir que la memoria "guarda" sin especificar el biestable o el capacitor. |

## 7. Relacionado

- [[Celda elemental de memoria]] · [[2.3.2 SRAM y DRAM]] · [[P05 Memoria RAM 8x3]]
