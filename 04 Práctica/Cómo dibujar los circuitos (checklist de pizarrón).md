---
unidad: 0
tipo: practica
examen: practica
prioridad: maxima
---
# Cómo dibujar los circuitos (checklist de pizarrón)

> [!abstract] Si el final práctico es "dibujar y explicar la tabla de verdad"
> Entonces lo que se evalúa es: **(1)** que el circuito esté bien armado, **(2)** que la tabla de verdad corresponda a ese circuito y **(3)** que puedas explicar **por qué**. Esta nota es el orden exacto de trazos para cada circuito, con los rótulos que no se pueden olvidar.

## Regla general para cualquier circuito

1. **Entradas a la izquierda, salidas a la derecha.** Siempre.

2. **Poné nombre a todas las señales intermedias** (S1, C1, A·B…): es lo que te permite explicar el circuito y lo que muestra que entendés.

3. **Tabla de verdad primero, circuito después.** Es más fácil dibujar del que se conoce la función.

4. **Verificá con una fila**: elegí una combinación de entrada, recorré el dibujo y comprobá que la salida coincide con la tabla. Eso se dice en voz alta: "con A=1, B=0, la XOR da 1…".

5. **Cerrá con la ecuación** escrita arriba del dibujo.

## Los seis circuitos del final, en orden de trazo

### 1) Semisumador

1. Dibujá **dos compuertas en paralelo**: XOR arriba, AND abajo.

2. Las **mismas dos entradas** (A, B) entran a las dos compuertas — marcalo con un punto de conexión.

3. Salidas: **S** (de la XOR) y **C** (de la AND).

4. Ecuaciones arriba: `S = A⊕B`, `C = A·B`.

5. Frase: "el semisumador no tiene Cin, sirve sólo para el bit menos significativo".

![semisumador.svg](../assets/semisumador.svg)

### 2) Sumador completo

1. **XOR 1** con A y B ⇒ salida **S1**.

2. **AND 1** con A y B ⇒ **A·B** (acarreo generado).

3. **XOR 2** con S1 y Cin ⇒ **S**.

4. **AND 2** con S1 y Cin ⇒ **S1·Cin** (acarreo propagado).

5. **OR** de A·B y S1·Cin ⇒ **Cout**.

6. Decir: "Cout = generado + propagado; encadenando n de estos se suma en n bits".

![sumador_completo.svg](../assets/sumador_completo.svg)

### 3) Sumador de n bits (4 u 8)

1. Una **fila de bloques** rotulados **FA** (o el dibujo completo de cada uno, si hay lugar).

2. Arriba: `A3 B3 | A2 B2 | A1 B1 | A0 B0` (MSB a la izquierda).

3. Abajo: `S3 S2 S1 S0`.

4. **Línea de acarreo** de derecha a izquierda: `Cin = 0 → FA0 → C1 → FA1 → … → Cout`.

5. Verificá con una suma concreta en el costado (ver [[TP5 Sumadores]]).

### 4) Decodificador 2→4 (o 3→8)

1. **Inversores** a la izquierda (uno por variable, arriba).

2. **Una AND por salida**, en columna, con sus dos (o tres) entradas.

3. Cada AND recibe la combinación que le corresponde: `Y0 ← A1'A0'`, `Y1 ← A1'A0`, …

4. Salidas rotuladas **Y0…Y3** y la ecuación al lado de cada una.

5. Frase: "cada salida es un mintérmino: siempre hay **una sola** en 1".

![decodificador_2x4.svg](../assets/decodificador_2x4.svg)

### 5) Demultiplexor 1→4
Igual que el decodificador pero **el dato D entra a todas las AND** (3 entradas cada una: D + los dos selectores). Frase: "la salida seleccionada **copia D**; las demás quedan en 0. Con D = 1 es un decodificador".

![demux_1x4.svg](../assets/demux_1x4.svg)

### 6) Multiplexor 4→1

1. **Cuatro AND de 3 entradas** en columna (cada una: su dato + los dos selectores).

2. **Una OR de 4 entradas** a la derecha que junta las cuatro salidas.

3. Ecuación arriba: `Y = I0·S1'S0' + I1·S1'S0 + I2·S1S0' + I3·S1S0`.

4. Frase: "sólo un AND está habilitado ⇒ sólo un dato llega a la OR".

![mux_4x1.svg](../assets/mux_4x1.svg)

### 7) Biestable RS (y de ahí D, JK, T)

1. Dibujá **dos compuertas NOR (o NAND) cruzadas**: la salida de una entra a la otra.

2. Rotulá **Q** y **Q'** en las salidas.

3. Marcá S y R a la izquierda; si es **sincrónico**, agregá las **AND con el reloj C**.

4. Tabla: `0 0 → mantiene`, `1 0 → set`, `0 1 → reset`, `1 1 → prohibido` (con NOR; con NAND se invierte).

5. Para el **D**: `S = D`, `R = D'` (y comentá que se resuelve el estado prohibido).

6. Para el **JK**: `S = J·Q'`, `R = K·Q` (la realimentación produce el toggle).

![flipflops.svg](../assets/flipflops.svg)

> [!tip] Los tres rótulos que no se pueden olvidar
> **Nombres de entradas y salidas** · **señales intermedias** · **ecuación de cada salida**. Un circuito sin rótulos no se puede explicar, y si no lo podés explicar, no cuenta.

## Cómo se "explica la tabla de verdad" (guion de 60 segundos)

1. "Esta tabla tiene **n variables**, por eso **2ⁿ filas**."

2. "La salida vale 1 en las filas … que son los **mintérminos**."

3. "Por eso la función es `F = Σm(...) = …`."

4. "Simplificando (álgebra o Karnaugh) queda `F = …`, que se implementa con **estas compuertas**."

5. "Verifico: con la entrada X el circuito da Y, igual que la tabla."

## Qué hacer si te dan la tabla y no el circuito

1. Escribí los mintérminos (las filas con salida 1).

2. Sumalos (SOP) y simplificá (álgebra o Karnaugh).

3. Dibujá **una AND por término** y **una OR final**.

4. Si la función es muy simple, usá directamente la compuerta (XOR, NAND, etc.).

## Qué hacer si te dan el circuito y no la tabla

1. Ponele nombre a cada nodo interno.

2. Escribí la función de cada compuerta de izquierda a derecha.

3. Reemplazá hasta tener F en función de las entradas.

4. Armá la tabla con 2ⁿ filas y evaluá (o simplificá primero y evaluá después).

## Enlaces
[[Tablas de verdad de memoria]] · [[Prácticas resueltas]] · [[TP5 Sumadores]] · [[TP6 Decodificadores y demultiplexores]] · [[TP7 Codificadores y multiplexores]] · [[TP8 Biestables RS]] · [[TP9 Biestables D, JK y T]]
