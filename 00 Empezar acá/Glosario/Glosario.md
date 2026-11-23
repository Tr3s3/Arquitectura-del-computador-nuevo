---
tipo: glosario
---
# Glosario

> [!abstract] Qué es esta nota
> El glosario completo de la materia: **180 conceptos**, cada uno con una **ficha** que explica **qué es**, **para qué sirve**, **cuáles son sus características** y **en qué subtema se estudia**. Acá está el **índice alfabético** (cada concepto enlaza a su ficha); las fichas están en diez notas, una por unidad.

> [!tip] Cómo usarlo
> 1. **Si te trabaste con una palabra en el oral:** buscala acá (Ctrl+F) y hacé clic para ir a la ficha.
> 2. **Antes del parcial:** recorré el índice letra por letra tapando la columna "En una línea"; los conceptos
>    que no te salen son los que hay que repasar.
> 3. **Al estudiar una unidad:** abrí la ficha de esa unidad (tabla de abajo), que está ordenada como se estudia.
> 4. **Al final:** mirá "Términos que se confunden", que es donde se pierden puntos en el final.

> [!info] Qué trae cada ficha
> | Campo | Para qué sirve |
> |---|---|
> | **Qué es** | la definición mínima, para no quedar en blanco |
> | **Para qué sirve** | el uso real: por qué existe el concepto |
> | **Características** | las propiedades que se preguntan (fórmulas, números, límites) |
> | **Se estudia en** | el subtema donde está desarrollado con ejemplo resuelto y diagrama |

## Las diez notas del glosario

| Unidad | Fichas | Qué cubre | Nota |
|---|---|---|---|
| **1** | 31 | circuitos de lógica digital | [[Glosario — Unidad 1]] |
| **2** | 34 | memorias y circuitos secuenciales | [[Glosario — Unidad 2]] |
| **3** | 12 | transferencia de registros y microoperaciones | [[Glosario — Unidad 3]] |
| **4** | 13 | organización y diseño básico | [[Glosario — Unidad 4]] |
| **5** | 20 | programación básica y CPU convencional | [[Glosario — Unidad 5]] |
| **6** | 10 | control microprogramado | [[Glosario — Unidad 6]] |
| **7** | 15 | CPU y arquitecturas | [[Glosario — Unidad 7]] |
| **8** | 16 | paralelismo | [[Glosario — Unidad 8]] |
| **9** | 15 | hardware aritmético | [[Glosario — Unidad 9]] |
| **10** | 14 | entrada y salida | [[Glosario — Unidad 10]] |
| **Total** | **180** | — | — |

## Índice alfabético

### A

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 9#Acarreo anticipado (carry look-ahead)\|Acarreo anticipado (carry look-ahead)]] | Generar los acarreos en paralelo con lógica `G` (genera) y `P` (propaga) en vez de esperar la cascada | U9 |
| [[Glosario — Unidad 1#Acarreo (carry) y resta en complemento a 2\|Acarreo (carry) y resta en complemento a 2]] | El acarreo es el 1 que "se lleva" a la columna siguiente | U1 |
| [[Glosario — Unidad 8#Acoplamiento (fuerte y débil)\|Acoplamiento (fuerte y débil)]] | Grado de dependencia entre procesadores: fuerte si comparten memoria y reloj; débil si se comunican por mensajes | U8 |
| [[Glosario — Unidad 7#Adelantamiento (forwarding)\|Adelantamiento (forwarding)]] | Llevar el resultado de una etapa posterior directamente a la entrada de la etapa que lo necesita, sin esperar a que se escriba en el registro | U7 |
| [[Glosario — Unidad 1#AIKEN (2-4-2-1)\|AIKEN (2-4-2-1)]] | Código ponderado de 4 bits con pesos `2-4-2-1`; el 9 se escribe `1111` | U1 |
| [[Glosario — Unidad 9#Algoritmo de Booth\|Algoritmo de Booth]] | Multiplicación con signo sin separar los signos: mira el par `(Q0, Q−1)` y decide sumar, restar o nada | U9 |
| [[Glosario — Unidad 3#ALU\|ALU]] | Unidad aritmético-lógica: recibe dos operandos y una selección de operación, y devuelve el resultado más las banderas | U3 |
| [[Glosario — Unidad 2#AMAT\|AMAT]] | *Average Memory Access Time*: el tiempo promedio de un acceso, `AMAT = h + m × P` (acierto + tasa de fallos × penalidad) | U2 |
| [[Glosario — Unidad 3#Ancho de palabra y de dirección\|Ancho de palabra y de dirección]] | Cuántos bits tiene un dato (palabra) y cuántos tiene una dirección | U3 |
| [[Glosario — Unidad 1#AND (Y lógica)\|AND (Y lógica)]] | Compuerta que da 1 sólo si todas sus entradas son 1 (`Y = A·B`) | U1 |
| [[Glosario — Unidad 8#Arreglo conectado (network)\|Arreglo conectado (network)]] | Red de procesadores conectados entre vecinos (malla, hipercubo, árbol) que intercambian datos | U8 |
| [[Glosario — Unidad 9#Arreglo multiplicador\|Arreglo multiplicador]] | Multiplicador combinacional: `n²` celdas que suman todos los productos parciales de una vez | U9 |

### B

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 8#Banco de memoria y entrelazado\|Banco de memoria y entrelazado]] | Dividir la memoria en bancos que se pueden acceder en paralelo; el entrelazado asigna direcciones consecutivas a bancos distintos | U8 |
| [[Glosario — Unidad 3#Banderas (Z, C, V, N)\|Banderas (Z, C, V, N)]] | Bits de estado que la ALU actualiza en cada operación: Z cero, C acarreo, V desborde con signo, N negativo | U3 |
| [[Glosario — Unidad 3#Base, índice, puntero de pila y estado\|Base, índice, puntero de pila y estado]] | Registros auxiliares: base (dirección de un bloque), índice (desplazamiento dentro de él), SP (tope de la pila) y registro de estado (banderas) | U3 |
| [[Glosario — Unidad 1#BCD (decimal codificado en binario)\|BCD (decimal codificado en binario)]] | Representación en la que cada dígito decimal ocupa 4 bits con los pesos `8-4-2-1` | U1 |
| [[Glosario — Unidad 9#BCD y corrección +6\|BCD y corrección +6]] | Aritmética decimal con dígitos BCD; cuando un nible pasa de 9 o hay acarreo, se le suma 6 | U9 |
| [[Glosario — Unidad 2#Biestable (latch) RS\|Biestable (latch) RS]] | Circuito secuencial de dos compuertas cruzadas (NOR o NAND) que memoriza 1 bit mientras tenga alimentación | U2 |
| [[Glosario — Unidad 2#Bits de dirección\|Bits de dirección]] | Cantidad de líneas de dirección necesarias para acceder a todas las palabras de una memoria: `bits = log₂(cantidad de palabras)` | U2 |
| [[Glosario — Unidad 5#BIU y EU (8086)\|BIU y EU (8086)]] | La CPU del 8086 partida en dos: BIU (bus interface unit: busca instrucciones y datos) y EU (execution unit: las ejecuta) | U5 |
| [[Glosario — Unidad 4#BLUE\|BLUE]] | La máquina didáctica de la cátedra: 4096 palabras × 16 bits, bus único, arquitectura de acumulador, 16 instrucciones de una dirección | U4 |
| [[Glosario — Unidad 3#Buffer de tres estados\|Buffer de tres estados]] | Amplificador cuya salida puede ser `0`, `1` o alta impedancia (`Z`): desconectado | U3 |
| [[Glosario — Unidad 7#Bus interno y externo (FSB)\|Bus interno y externo (FSB)]] | Interno: dentro del chip, une registros y ALU. Externo: en la placa, une CPU con memoria y periféricos; el clásico es el FSB (a través del puente norte) | U7 |
| [[Glosario — Unidad 3#Bus único\|Bus único]] | Un solo conjunto de líneas que todos los registros comparten para mover datos | U3 |
| [[Glosario — Unidad 3#Buses de datos, de direcciones y de control\|Buses de datos, de direcciones y de control]] | Los tres grupos de líneas que conectan la CPU con memoria y periféricos | U3 |
| [[Glosario — Unidad 4#Búsqueda (fetch) y ejecución (execute)\|Búsqueda (fetch) y ejecución (execute)]] | Las dos fases de un ciclo de instrucción: traer la instrucción de memoria y hacer lo que dice | U4 |

### C

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 2#Caché, línea y bloque\|Caché, línea y bloque]] | Caché: memoria SRAM chica y rápida que copia partes de la principal. Línea (o bloque): la unidad que se copia y se trae/expulsa de una vez | U2 |
| [[Glosario — Unidad 3#Camino de datos (datapath)\|Camino de datos (datapath)]] | El conjunto de registros, bus y ALU por donde circulan los datos, más el cableado que los une | U3 |
| [[Glosario — Unidad 6#Campo de dirección de control\|Campo de dirección de control]] | Los bits de la microinstrucción que indican a dónde ir si se cumple la condición de salto | U6 |
| [[Glosario — Unidad 5#Campo único de dirección\|Campo único de dirección]] | Formato en el que la instrucción tiene un solo campo de dirección, porque el otro operando es implícito (`AC`) | U5 |
| [[Glosario — Unidad 4#Capacidad de memoria\|Capacidad de memoria]] | Cuántos bits guarda una memoria: `palabras × bits por palabra` | U4 |
| [[Glosario — Unidad 2#Celda de memoria\|Celda de memoria]] | Circuito que guarda 1 bit y tiene cuatro partes: biestable, selección, lectura/escritura y buffer de 3 estados | U2 |
| [[Glosario — Unidad 4#Ciclo de instrucción, de máquina y de reloj\|Ciclo de instrucción, de máquina y de reloj]] | Las tres escalas de tiempo: pulso de reloj (125 ns) < ciclo de máquina (8 pulsos = 1 µs) < ciclo de instrucción (1 o 2 ciclos de máquina) | U4 |
| [[Glosario — Unidad 6#Circuito de control (bloque)\|Circuito de control (bloque)]] | El bloque que, dado el opcode del `IR`, el estado y el pulso, genera todas las señales | U6 |
| [[Glosario — Unidad 7#CISC\|CISC]] | Arquitectura de instrucciones complejas, de tamaño variable, que pueden operar sobre memoria (x86) | U7 |
| [[Glosario — Unidad 8#Clasificación de Flynn\|Clasificación de Flynn]] | Las cuatro clases de máquinas según cuántas instrucciones y cuántos datos procesan por vez: SISD, SIMD, MISD y MIMD | U8 |
| [[Glosario — Unidad 5#Clasificación de las instrucciones\|Clasificación de las instrucciones]] | Los grupos del repertorio: transferencia de datos, aritméticas, lógicas, de control de flujo, de entrada/salida y de manejo de pila | U5 |
| [[Glosario — Unidad 1#Codificador\|Codificador]] | El inverso del decodificador: de `2ⁿ` (o menos) líneas activas a un código de `n` bits | U1 |
| [[Glosario — Unidad 1#Código binario\|Código binario]] | Regla que asigna a cada símbolo (un dígito, una letra) una combinación de `n` bits | U1 |
| [[Glosario — Unidad 1#Código de Gray\|Código de Gray]] | Código continuo y cíclico: entre un número y el siguiente cambia un solo bit | U1 |
| [[Glosario — Unidad 1#Código Johnson\|Código Johnson]] | Código continuo y cíclico que se genera con un registro de desplazamiento realimentado con la salida negada | U1 |
| [[Glosario — Unidad 2#CodOp contra campo de dirección\|CodOp contra campo de dirección]] | El reparto de los bits de una instrucción entre código de operación y dirección | U2 |
| [[Glosario — Unidad 8#Coherencia de caché\|Coherencia de caché]] | Protocolo que garantiza que, si un núcleo escribe una dirección, los demás no sigan usando una copia vieja | U8 |
| [[Glosario — Unidad 9#Complemento a 2\|Complemento a 2]] | Representación de enteros con signo: el negativo se obtiene invirtiendo todos los bits y sumando 1 | U9 |
| [[Glosario — Unidad 1#Compuerta lógica\|Compuerta lógica]] | Circuito electrónico mínimo que realiza una operación lógica sobre una o más señales binarias y devuelve una salida binaria | U1 |
| [[Glosario — Unidad 1#Compuerta universal\|Compuerta universal]] | Compuerta con la que se puede armar cualquier función lógica sin usar otra: lo son la NAND y la NOR | U1 |
| [[Glosario — Unidad 8#Conflicto de banco\|Conflicto de banco]] | Situación en la que dos accesos simultáneos caen en el mismo banco y hay que serializarlos | U8 |
| [[Glosario — Unidad 2#Contador\|Contador]] | Registro que recorre una secuencia de estados con cada pulso de reloj | U2 |
| [[Glosario — Unidad 2#Contador módulo N\|Contador módulo N]] | Contador que cuenta `N` estados y vuelve a empezar (no tiene por qué ser `2ⁿ`) | U2 |
| [[Glosario — Unidad 6#Control cableado\|Control cableado]] | Unidad de control hecha con compuertas y flip-flops: cada señal es una función lógica del estado y del pulso | U6 |
| [[Glosario — Unidad 6#Control microprogramado\|Control microprogramado]] | Unidad de control que guarda las señales como datos en una memoria de control: cada microinstrucción dice qué señales activar en un pulso | U6 |
| [[Glosario — Unidad 2#Conversión entre biestables\|Conversión entre biestables]] | Armar un tipo de flip-flop con otro: por ejemplo, un D usando un JK | U2 |

### D

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 5#De pila\|De pila]] | El operando está en el tope de la pila, apuntado por `SP`; la instrucción no lleva dirección | U5 |
| [[Glosario — Unidad 5#De registro y registro indirecto\|De registro y registro indirecto]] | De registro: el operando está en un registro. Registro indirecto: el registro contiene la dirección del operando | U5 |
| [[Glosario — Unidad 1#Decodificador\|Decodificador]] | Circuito que convierte un código de `n` bits en una de `2ⁿ` líneas activas (`Yi = mi`) | U1 |
| [[Glosario — Unidad 4#Decodificador de instrucción\|Decodificador de instrucción]] | Circuito que toma los bits de opcode del `IR` y activa una línea por instrucción | U4 |
| [[Glosario — Unidad 1#Demultiplexor (DEMUX)\|Demultiplexor (DEMUX)]] | Reparte una entrada de dato hacia una de `2ⁿ` salidas | U1 |
| [[Glosario — Unidad 9#Desbordamiento (overflow, V)\|Desbordamiento (overflow, V)]] | El resultado no entra en `n` bits con signo: pasó de `+2ⁿ⁻¹−1` o bajó de `−2ⁿ⁻¹` | U9 |
| [[Glosario — Unidad 7#Detención (stall) y NOP\|Detención (stall) y NOP]] | Stall: congelar el cauce uno o más ciclos. NOP: instrucción vacía que ocupa el ciclo | U7 |
| [[Glosario — Unidad 5#Dirección efectiva (EA)\|Dirección efectiva (EA)]] | La dirección final que se pone en el `MAR` para acceder al operando | U5 |
| [[Glosario — Unidad 10#Disco rígido (HDD)\|Disco rígido (HDD)]] | Almacenamiento magnético con platos giratorios y cabezal móvil | U10 |
| [[Glosario — Unidad 9#División con restauración\|División con restauración]] | Algoritmo de división que resta y, si el resto da negativo, lo restaura (vuelve a sumar el divisor) antes de desplazar | U9 |
| [[Glosario — Unidad 9#División con signo y sobreflujo\|División con signo y sobreflujo]] | Regla de signos (`cociente` = XOR de los signos; `resto` con el signo del dividendo) y el caso en que el cociente no entra en `n` bits | U9 |
| [[Glosario — Unidad 9#División sin restauración\|División sin restauración]] | Variante que no deshace la resta: si el resto quedó negativo, en la vuelta siguiente suma en vez de restar | U9 |
| [[Glosario — Unidad 10#DMA (acceso directo a memoria)\|DMA (acceso directo a memoria)]] | Un controlador mueve datos entre periférico y memoria sin pasar por la CPU | U10 |
| [[Glosario — Unidad 1#Don't care (condición "no importa")\|Don't care (condición "no importa")]] | Combinación de entrada que nunca va a ocurrir (o cuya salida da igual): se marca `X` en la tabla | U1 |
| [[Glosario — Unidad 1#Dualidad\|Dualidad]] | Regla que permite obtener una identidad gemela de otra: se cambia AND por OR, OR por AND, 0 por 1 y 1 por 0 | U1 |

### E

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 2#Ecuación característica\|Ecuación característica]] | Fórmula que dice cómo queda el estado siguiente (`Q⁺`) en función de las entradas y del estado actual | U2 |
| [[Glosario — Unidad 8#Encadenamiento (chaining)\|Encadenamiento (chaining)]] | Permitir que la salida de una operación entre a otra sin pasar por los registros, apenas está disponible | U8 |
| [[Glosario — Unidad 10#Entrada/salida (E/S)\|Entrada/salida (E/S)]] | Todo intercambio de datos entre la computadora y el mundo exterior: teclado, pantalla, disco, red | U10 |
| [[Glosario — Unidad 8#Escalabilidad\|Escalabilidad]] | Capacidad del sistema de mantener el rendimiento cuando crecen la carga o los recursos | U8 |
| [[Glosario — Unidad 1#Escalas de integración (SSI, MSI, LSI, VLSI)\|Escalas de integración (SSI, MSI, LSI, VLSI)]] | Clasificación de los circuitos integrados según cuántas compuertas entran en un chip | U1 |
| [[Glosario — Unidad 4#estado · pulso · instrucción\|estado · pulso · instrucción]] | La forma canónica de una señal de control: se activa sólo si el estado es el correcto y el pulso es el correcto y (si hace falta) la instrucción es la que corresponde | U4 |
| [[Glosario — Unidad 1#Exceso 3\|Exceso 3]] | Código no ponderado que se obtiene sumando 3 al binario puro del dígito | U1 |
| [[Glosario — Unidad 9#Exceso (bias) — exceso 64, exceso 127\|Exceso (bias) — exceso 64, exceso 127]] | Forma de guardar el exponente sumándole una constante, para que todos los valores sean positivos: `E_guardado = e + exceso` | U9 |
| [[Glosario — Unidad 2#Expansión de memoria y chip select\|Expansión de memoria y chip select]] | Unir varios chips para lograr más palabras (expansión de palabra) o palabras más anchas (expansión de bit), y elegir cuál responde con la señal `CS` | U2 |

### F

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 2#Flip-flop D\|Flip-flop D]] | Flip-flop que copia la entrada en el flanco: `Q⁺ = D` | U2 |
| [[Glosario — Unidad 2#Flip-flop JK\|Flip-flop JK]] | Flip-flop con dos entradas que setea (`J = 1, K = 0`), resetea (`J = 0, K = 1`), mantiene (`0,0`) y alterna (`1,1`) | U2 |
| [[Glosario — Unidad 2#Flip-flop T\|Flip-flop T]] | Flip-flop que alterna cuando `T = 1` y mantiene cuando `T = 0`: `Q⁺ = T ⊕ Q` | U2 |
| [[Glosario — Unidad 1#Forma canónica (SOP y POS)\|Forma canónica (SOP y POS)]] | Expresión en la que todos los términos contienen todas las variables: SOP = suma de productos (mintérminos), POS = producto de sumas (maxtérminos) | U1 |
| [[Glosario — Unidad 5#Formatos de instrucción (4, 3, 2, 1 y 0 direcciones)\|Formatos de instrucción (4, 3, 2, 1 y 0 direcciones)]] | Cuántas direcciones de operando lleva la instrucción en su codificación | U5 |

### H

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 3#Habilitación (enable) y reloj\|Habilitación (enable) y reloj]] | La señal `enable` (o `LOAD`) permite que un registro tome el dato del bus sólo en un pulso determinado; el `CLK` marca cuándo | U3 |
| [[Glosario — Unidad 2#Hamming y síndrome\|Hamming y síndrome]] | Código corrector: los bits de control van en las potencias de 2 y el síndrome (patrón de fallas de los controles) indica la posición del bit con error | U2 |
| [[Glosario — Unidad 10#Handshake (STB y ACK)\|Handshake (STB y ACK)]] | Protocolo de acuse mutuo: el emisor avisa `STB` (strobe: "el dato está puesto") y el receptor contesta `ACK` ("lo tomé") | U10 |

### I

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 4#IAS\|IAS]] | La primera computadora con programa almacenado (von Neumann, 1945): 1000 palabras de 40 bits, `AC` y `MQ` de 40 bits, `PC`, `MAR`, `MBR`, `IR` | U4 |
| [[Glosario — Unidad 9#IEEE 754\|IEEE 754]] | El estándar de punto flotante: simple (32 bits: 1 + 8 + 23, exceso 127) y doble (64 bits: 1 + 11 + 52, exceso 1023) | U9 |
| [[Glosario — Unidad 5#Indexado (con desplazamiento)\|Indexado (con desplazamiento)]] | La dirección efectiva es `base o índice + desplazamiento` | U5 |
| [[Glosario — Unidad 5#Indirecto\|Indirecto]] | El campo de la instrucción apunta a una celda que contiene la dirección del operando | U5 |
| [[Glosario — Unidad 5#Inmediato y directo\|Inmediato y directo]] | Inmediato: el operando es el campo de la instrucción. Directo: el campo es la dirección del operando | U5 |
| [[Glosario — Unidad 5#Instrucción\|Instrucción]] | La orden mínima que entiende la CPU: qué operación, con qué datos y dónde están | U5 |
| [[Glosario — Unidad 10#Interfaces serie y paralelo\|Interfaces serie y paralelo]] | Paralelo: varios bits a la vez por varias líneas. Serie: un bit por vez por una línea | U10 |
| [[Glosario — Unidad 10#Interrupción\|Interrupción]] | Pedido asincrónico de un dispositivo para que la CPU lo atienda, dejando lo que está haciendo | U10 |
| [[Glosario — Unidad 10#Interrupción vectorizada y vector de interrupciones\|Interrupción vectorizada y vector de interrupciones]] | Vector: la dirección de la rutina de servicio. Vectorizada: en lugar de preguntar quién fue, el dispositivo entrega un número y la CPU salta a la dirección guardada en la tabla de vectores | U10 |
| [[Glosario — Unidad 5#IRQ, SI y CP8\|IRQ, SI y CP8]] | Las tres condiciones para aceptar una interrupción: `IRQ` (el pedido), `SI` (interrupciones habilitadas) y `CP8` (fin del ciclo de instrucción) | U5 |

### J

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 2#Jerarquía de memoria\|Jerarquía de memoria]] | Escalonamiento registros → caché → memoria principal → disco donde arriba hay poca capacidad y mucha velocidad, y abajo al revés | U2 |

### L

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 10#Latencia, IOPS y ancho de banda\|Latencia, IOPS y ancho de banda]] | Latencia: tiempo de una operación. IOPS: operaciones por segundo. Ancho de banda: datos por segundo | U10 |
| [[Glosario — Unidad 8#Ley de Amdahl\|Ley de Amdahl]] | `S = 1 / ((1 − p) + p/N)`: la mejora total está limitada por la parte no paralelizable | U8 |
| [[Glosario — Unidad 7#Load/store\|Load/store]] | Regla de RISC: el acceso a memoria sólo ocurre en instrucciones `LOAD` y `STORE`; el resto opera registro a registro | U7 |
| [[Glosario — Unidad 2#Localidad (temporal y espacial)\|Localidad (temporal y espacial)]] | Propiedad de los programas: temporal = lo que se usó se vuelve a usar pronto; espacial = lo que está al lado se usa después | U2 |
| [[Glosario — Unidad 2#LRC y CRC\|LRC y CRC]] | LRC: paridad longitudinal por bloque (un byte de paridad por columna). CRC: código polinómico: el bloque se divide por un polinomio generador y se manda el resto | U2 |

### M

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 9#Mantisa y exponente\|Mantisa y exponente]] | Mantisa: los dígitos significativos. Exponente: la escala (potencia de 2) | U9 |
| [[Glosario — Unidad 1#Mapa de Karnaugh\|Mapa de Karnaugh]] | Grilla de `2ⁿ` celdas donde cada celda es un mintérmino, ordenadas en código Gray, para simplificar a ojo | U1 |
| [[Glosario — Unidad 2#Mapeos: directo, asociativo y por conjuntos\|Mapeos: directo, asociativo y por conjuntos]] | Dónde puede ir a parar un bloque de la memoria principal dentro de la caché | U2 |
| [[Glosario — Unidad 5#Máscara y prioridad\|Máscara y prioridad]] | Máscara: bits que habilitan o inhiben cada interrupción. Prioridad: cuál se atiende si llegan varias a la vez | U5 |
| [[Glosario — Unidad 1#Maxtérmino\|Maxtérmino]] | Suma que vale 0 en una sola fila de la tabla de verdad | U1 |
| [[Glosario — Unidad 2#Memoria asociativa (CAM)\|Memoria asociativa (CAM)]] | Memoria que se busca por contenido y no por dirección: se compara la clave contra todas las entradas a la vez | U2 |
| [[Glosario — Unidad 6#Memoria de control\|Memoria de control]] | La ROM (o RAM de control) que guarda el microprograma; se direcciona con el microPC | U6 |
| [[Glosario — Unidad 2#Memoria virtual y paginación\|Memoria virtual y paginación]] | Técnica que da a cada programa un espacio de direcciones falso (virtual), traducido a direcciones físicas por páginas de tamaño fijo. Para sirve. Permitir programas más grandes que la RAM, aislar… | U2 |
| [[Glosario — Unidad 6#Microcódigo vertical y horizontal\|Microcódigo vertical y horizontal]] | Dos estilos de codificar la microinstrucción: horizontal = un bit por señal; vertical = un código compacto por grupo de señales | U6 |
| [[Glosario — Unidad 6#Microinstrucción\|Microinstrucción]] | La palabra de la memoria de control: contiene todas las señales que se activan en un pulso, más información de secuenciamiento | U6 |
| [[Glosario — Unidad 3#Microoperación\|Microoperación]] | Operación elemental que se hace en un pulso de reloj: mover un dato, incrementar un registro, sumar dos registros | U3 |
| [[Glosario — Unidad 6#MicroPC y microprograma\|MicroPC y microprograma]] | MicroPC: registro que apunta a la microinstrucción actual. Microprograma: la secuencia de microinstrucciones que ejecuta una instrucción de máquina | U6 |
| [[Glosario — Unidad 1#Mintérmino\|Mintérmino]] | Producto que vale 1 en una sola fila de la tabla de verdad (todas las variables, negadas o no) | U1 |
| [[Glosario — Unidad 2#MMU y TLB\|MMU y TLB]] | MMU: unidad que traduce direcciones. TLB: caché asociativa de esas traducciones | U2 |
| [[Glosario — Unidad 5#Modificador de 2 bits\|Modificador de 2 bits]] | Campo que dice qué índices se suman a la dirección: ninguno, `RIF`, `RID` o los dos | U5 |
| [[Glosario — Unidad 4#Modificar el PC (PC + 1)\|Modificar el PC (PC + 1)]] | La microoperación que incrementa el contador de programa después de buscar la instrucción | U4 |
| [[Glosario — Unidad 5#Modo de direccionamiento\|Modo de direccionamiento]] | La regla que dice cómo se calcula la dirección del operando a partir de lo que dice la instrucción | U5 |
| [[Glosario — Unidad 8#Monousuario contra multiusuario\|Monousuario contra multiusuario]] | Dos escenarios de uso: un solo usuario con todos los recursos, o muchos usuarios compitiendo por ellos | U8 |
| [[Glosario — Unidad 7#Multicore\|Multicore]] | Varios núcleos completos en el mismo chip, cada uno con su pipeline | U7 |
| [[Glosario — Unidad 1#Multiplexor (MUX)\|Multiplexor (MUX)]] | Selector: de `2ⁿ` entradas de dato elige una y la manda a la salida, según `n` bits de selección | U1 |
| [[Glosario — Unidad 8#Multiplicación de matrices y paralelismo\|Multiplicación de matrices y paralelismo]] | El cálculo clásico `C = A × B` (cada elemento es un producto escalar) usado para medir paralelismo | U8 |
| [[Glosario — Unidad 9#Multiplicación por sumas y desplazamientos\|Multiplicación por sumas y desplazamientos]] | Multiplicar como en decimal: por cada bit del multiplicador, se suma el multiplicando (si el bit es 1) y se desplaza | U9 |

### N

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 1#NAND y NOR\|NAND y NOR]] | AND negada y OR negada: `Y = (A·B)'` y `Y = (A + B)'` | U1 |
| [[Glosario — Unidad 2#Nivel y flanco\|Nivel y flanco]] | Un circuito es sensible al nivel si actúa mientras el reloj está en 1 (o en 0), y sensible al flanco si actúa sólo en la transición (subida o bajada) | U2 |
| [[Glosario — Unidad 9#Normalización\|Normalización]] | Dejar la mantisa con forma fija (`1.xxx` en IEEE 754; `0,1xxx` con `1/2 ≤ M < 1` en la convención de la cátedra) ajustando el exponente | U9 |
| [[Glosario — Unidad 1#NOT (inversor)\|NOT (inversor)]] | Compuerta de una entrada que niega: `Y = A'` | U1 |
| [[Glosario — Unidad 8#NUMA y cluster\|NUMA y cluster]] | NUMA: varios procesadores con memorias locales, con tiempos de acceso distintos según dónde esté el dato. Cluster: computadoras completas unidas por red | U8 |

### O

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 4#Opcode octal\|Opcode octal]] | El código de operación de cada instrucción de la BLUE, escrito en octal (`00` a `17`) | U4 |
| [[Glosario — Unidad 5#Opcode y operando\|Opcode y operando]] | Opcode: código de la operación (4 bits en la BLUE). Operando: el dato o la dirección sobre la que se opera | U5 |
| [[Glosario — Unidad 1#OR (O lógica)\|OR (O lógica)]] | Compuerta que da 1 si al menos una entrada es 1 (`Y = A + B`) | U1 |
| [[Glosario — Unidad 2#Organización 2D y 3D\|Organización 2D y 3D]] | Formas de ubicar las celdas: 2D = una sola línea de selección (matriz simple, memorias chicas); 3D = dos líneas de selección (fila y columna) con decodificadores separados | U2 |

### P

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 8#Paralelismo\|Paralelismo]] | Hacer varias operaciones a la vez, en lugar de una tras otra | U8 |
| [[Glosario — Unidad 2#Paridad\|Paridad]] | Un bit extra que hace que la cantidad de unos del grupo sea par (o impar) | U2 |
| [[Glosario — Unidad 5#Pila (PUSH y POP)\|Pila (PUSH y POP)]] | Estructura LIFO en memoria; `PUSH` apila y `POP` desapila, con `SP` como puntero al tope | U5 |
| [[Glosario — Unidad 7#Pipeline (cauce)\|Pipeline (cauce)]] | Técnica de solapar etapas: mientras una instrucción se ejecuta, la siguiente se decodifica y la de más allá se busca | U7 |
| [[Glosario — Unidad 2#PIPO y SISO\|PIPO y SISO]] | PIPO: entrada y salida en paralelo (todo a la vez). SISO: entrada y salida en serie (bit por bit) | U2 |
| [[Glosario — Unidad 2#Políticas de escritura y de reemplazo\|Políticas de escritura y de reemplazo]] | Escritura: `write-through` (escribe en caché y en memoria) o `write-back` (sólo en caché, marca la línea "sucia" y la baja después). Reemplazo: qué línea se sacrifica (LRU, FIFO, aleatorio) | U2 |
| [[Glosario — Unidad 10#Polling (E/S programada)\|Polling (E/S programada)]] | La CPU pregunta una y otra vez si el periférico está listo, en un bucle | U10 |
| [[Glosario — Unidad 1#Postulado\|Postulado]] | Verdad básica del álgebra de Boole que no se demuestra (se acepta) y de la que salen los teoremas | U1 |
| [[Glosario — Unidad 7#Predicción de saltos\|Predicción de saltos]] | Adivinar si un salto se toma (y a dónde) para no detener el cauce | U7 |
| [[Glosario — Unidad 10#Prioridad de interrupciones\|Prioridad de interrupciones]] | Orden en que se atienden las interrupciones cuando llegan varias a la vez o una mientras se atiende otra | U10 |
| [[Glosario — Unidad 8#Procesamiento vectorial y registro vectorial\|Procesamiento vectorial y registro vectorial]] | Instrucciones que operan sobre muchos elementos con un solo código de operación, usando registros anchos (por ejemplo 128, 256 o 512 bits) | U8 |
| [[Glosario — Unidad 4#Programa almacenado\|Programa almacenado]] | Idea de von Neumann: las instrucciones se guardan en la misma memoria que los datos | U4 |
| [[Glosario — Unidad 2#PROM, EPROM, EEPROM y Flash\|PROM, EPROM, EEPROM y Flash]] | Las ROM programables: | U2 |
| [[Glosario — Unidad 10#Puerto e interfaz\|Puerto e interfaz]] | Puerto: la "ventanilla" numerada por la que se lee o escribe un dispositivo. Interfaz: el circuito que adapta señales, tensiones y velocidad entre el bus y el periférico | U10 |
| [[Glosario — Unidad 4#Pulso de búsqueda (CP1 a CP8)\|Pulso de búsqueda (CP1 a CP8)]] | Los ocho pulsos del ciclo de búsqueda: traer la instrucción de memoria al `IR` | U4 |
| [[Glosario — Unidad 9#Punto flotante\|Punto flotante]] | Formato `signo · exponente · mantisa` que representa números con coma "que se mueve": `(−1)^S × M × 2^E` | U9 |

### R

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 2#Refresco\|Refresco]] | Reescritura periódica de cada fila de una DRAM, porque el capacitor se descarga solo | U2 |
| [[Glosario — Unidad 2#Registro\|Registro]] | Conjunto de `n` flip-flops con el mismo reloj que guarda una palabra de `n` bits | U2 |
| [[Glosario — Unidad 3#Registros de la CPU (AC, PC, IR, MAR, MBR)\|Registros de la CPU (AC, PC, IR, MAR, MBR)]] | Las "cajas" donde la CPU guarda lo que está usando: acumulador, contador de programa, registro de instrucción, registro de dirección y buffer de memoria | U3 |
| [[Glosario — Unidad 7#Riesgo (hazard)\|Riesgo (hazard)]] | Situación que impide que la próxima instrucción entre al pipeline en el ciclo previsto | U7 |
| [[Glosario — Unidad 5#RIF, RID y RB\|RIF, RID y RB]] | Los registros que agrega la BLUE indexada: `RIF` (índice fuente), `RID` (índice destino) y `RB` (base) | U5 |
| [[Glosario — Unidad 7#RISC\|RISC]] | Arquitectura de instrucciones simples y de tamaño fijo, con load/store y muchos registros (ARM, MIPS) | U7 |
| [[Glosario — Unidad 10#Robo de ciclo (cycle stealing)\|Robo de ciclo (cycle stealing)]] | El controlador de DMA toma prestado un ciclo del bus para mover un dato, mientras la CPU espera | U10 |
| [[Glosario — Unidad 2#ROM\|ROM]] | Memoria de sólo lectura: el contenido se fija al fabricar el chip | U2 |
| [[Glosario — Unidad 6#ROM de control del 8088 (504 × 21)\|ROM de control del 8088 (504 × 21)]] | La memoria de control concreta del 8088: 504 microinstrucciones de 21 bits | U6 |
| [[Glosario — Unidad 5#RTI (retorno de interrupción)\|RTI (retorno de interrupción)]] | Instrucción que restaura el estado guardado y devuelve el control al programa interrumpido | U5 |

### S

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 4#Señal de control\|Señal de control]] | Cada una de las líneas que la unidad de control activa para que se haga una microoperación (`PCout`, `MARin`, `MEMout`, `ALUadd`…) | U4 |
| [[Glosario — Unidad 6#Secuenciamiento y salto condicional\|Secuenciamiento y salto condicional]] | La lógica que decide cuál es la próxima microinstrucción: la siguiente en secuencia o un salto | U6 |
| [[Glosario — Unidad 8#Segmentación de operaciones (pipelining de datos)\|Segmentación de operaciones (pipelining de datos)]] | Aplicar la idea del pipeline a un cálculo repetitivo sobre un vector: una suma entra a la etapa 1 mientras la anterior está en la 2 | U8 |
| [[Glosario — Unidad 5#Segmento y offset\|Segmento y offset]] | El 8086 arma la dirección física como `segmento × 16 + offset`, con registros de 16 bits | U5 |
| [[Glosario — Unidad 1#Semisumador\|Semisumador]] | Circuito que suma dos bits y da suma y acarreo: `S = A ⊕ B`, `Cout = A·B` | U1 |
| [[Glosario — Unidad 8#SIMD\|SIMD]] | *Single Instruction, Multiple Data*: una instrucción, muchos datos en paralelo | U8 |
| [[Glosario — Unidad 1#Simplificación analítica\|Simplificación analítica]] | Reducir una expresión booleana aplicando postulados y teoremas hasta que no se pueda achicar más | U1 |
| [[Glosario — Unidad 2#SIPO y PISO\|SIPO y PISO]] | SIPO: entra en serie, sale en paralelo. PISO: entra en paralelo, sale en serie | U2 |
| [[Glosario — Unidad 10#Skew (desfasaje)\|Skew (desfasaje)]] | Diferencia de tiempo de llegada entre líneas de un bus paralelo | U10 |
| [[Glosario — Unidad 7#SMT (multihilo simultáneo)\|SMT (multihilo simultáneo)]] | Un núcleo que mantiene dos o más hilos y toma instrucciones de cualquiera de ellos en cada ciclo | U7 |
| [[Glosario — Unidad 7#Speedup y techo `k`\|Speedup y techo `k`]] | `S = T_sin / T_con`, y en un pipeline con `k` etapas: `S = k·n / (k + n − 1)` | U7 |
| [[Glosario — Unidad 2#SRAM y DRAM\|SRAM y DRAM]] | Las dos tecnologías de RAM: SRAM = 6 transistores (latch), DRAM = 1 transistor + 1 capacitor | U2 |
| [[Glosario — Unidad 10#SSD\|SSD]] | Almacenamiento en memoria flash: no tiene partes móviles | U10 |
| [[Glosario — Unidad 1#Sumador completo (FA)\|Sumador completo (FA)]] | Suma tres bits (`A`, `B`, `Cin`) y da `S` y `Cout` | U1 |
| [[Glosario — Unidad 7#Superpipeline\|Superpipeline]] | Pipeline con más etapas (más finas) para poder subir la frecuencia | U7 |
| [[Glosario — Unidad 7#Superscalar\|Superscalar]] | Pipeline que emite más de una instrucción por ciclo, con varias vías en paralelo | U7 |

### T

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 2#Tabla de estados y de excitación\|Tabla de estados y de excitación]] | La de estados dice qué pasa con `Q` para cada entrada; la de excitación dice qué entrada hay que poner para pasar de un estado a otro | U2 |
| [[Glosario — Unidad 1#Tabla de verdad\|Tabla de verdad]] | Tabla que lista todas las combinaciones posibles de las entradas de una función y la salida en cada una: `2ⁿ` filas para `n` variables | U1 |
| [[Glosario — Unidad 1#Teoremas de DeMorgan\|Teoremas de DeMorgan]] | Dos identidades que convierten una negación de una operación en la operación contraria de las negaciones: `(A·B)' = A' + B'` y `(A+B)' = A'·B'` | U1 |
| [[Glosario — Unidad 3#Transferencia entre registros (RTL)\|Transferencia entre registros (RTL)]] | Notación que describe qué registro copia a cuál en un pulso: `R1 ← R2` (o `R2out, R1in`) | U3 |

### U

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 4#Unidad funcional\|Unidad funcional]] | Cada gran bloque de una computadora: entrada, salida, memoria, ALU y unidad de control | U4 |

### V

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 7#von Neumann contra Harvard\|von Neumann contra Harvard]] | von Neumann: una memoria y un bus para instrucciones y datos. Harvard: memorias y buses separados | U7 |

### X

| Concepto | En una línea | Unidad |
|---|---|---|
| [[Glosario — Unidad 1#XOR y XNOR\|XOR y XNOR]] | XOR (o exclusivo): `Y = A ⊕ B`, vale 1 cuando las entradas son distintas. XNOR: la negación | U1 |

---

## Términos que se confunden (y no son lo mismo)

Es la sección que más puntos salva en el final: casi todas las confusiones son de **una palabra**.

| Par | La diferencia en una línea |
|---|---|
| **Acarreo `C`** vs **desborde `V`** | `C` es aritmética **sin** signo (se salió del byte); `V` es **con** signo (dos positivos dieron negativo) |
| **Paridad** vs **Hamming** | la paridad **detecta** 1 bit; Hamming **corrige** 1 bit porque el síndrome da la posición |
| **SRAM** vs **DRAM** | latch de 6 transistores sin refresco vs 1 transistor + capacitor con refresco (64 ms / 4096 = 15,6 µs) |
| **Pipeline** vs **superscalar** | pipeline: etapas solapadas, como máximo 1 instrucción por ciclo; superscalar: **varias** por ciclo |
| **Multicore** vs **SMT** | multicore: núcleos **físicos** nuevos; SMT: dos hilos en **el mismo** núcleo |
| **Indirecto** vs **registro indirecto** | el indirecto busca la dirección **en memoria** (2 accesos); el de registro, **en un registro** (1 acceso) |
| **Caché** vs **memoria virtual** | la caché acelera el acceso a la RAM; la memoria virtual **traduce** direcciones y permite programas más grandes que la RAM |
| **Mapeo directo** vs **asociativo** | directo: un solo lugar posible; asociativo: cualquier lugar (más hardware, menos conflictos) |
| **Write-through** vs **write-back** | `through` escribe siempre en memoria; `back` sólo marca la línea y la baja cuando la desalojan |
| **ROM** vs **RAM** | ROM: no volátil, sólo lectura (o reprogramable); RAM: volátil, lectura y escritura |
| **EEPROM** vs **Flash** | EEPROM borra **byte a byte**; flash borra **por bloques** |
| **Exceso 64** vs **IEEE 754** | la cátedra usa exceso 64 con 7 bits y mantisa `1/2 ≤ M < 1`; IEEE usa exceso 127 y `1.M` implícito |
| **Polling** vs **interrupción** | polling: la CPU pregunta; interrupción: el dispositivo avisa |
| **DMA** vs **E/S programada** | DMA mueve el bloque sin la CPU; la programada ocupa la CPU en cada byte |
| **Nivel** vs **flanco** | el latch actúa mientras el reloj vale 1; el flip-flop sólo en la transición |
| **SOP** vs **POS** | SOP suma productos (mintérminos, AND-OR); POS multiplica sumas (maxtérminos, OR-AND) |
| **Codificador** vs **decodificador** | codificador: de muchas líneas a un código; decodificador: de un código a una línea |
| **MUX** vs **DEMUX** | MUX: muchas entradas → una salida; DEMUX: una entrada → muchas salidas |
| **Von Neumann** vs **Harvard** | un bus y una memoria para todo vs buses y memorias separadas para instrucciones y datos |
| **CISC** vs **RISC** | instrucciones complejas de tamaño variable vs simples y fijas, con load/store |
| **Control cableado** vs **microprogramado** | compuertas: rápido y rígido vs ROM de control: flexible y más lento |
| **Interrupción** vs **excepción** | la interrupción es externa y asincrónica; la excepción la provoca la propia instrucción (división por cero, `INT`) |

## Relacionado
[[01 Mapa de la materia (MOC)]] · [[00 Índice de la materia (las 10 unidades)]] · [[00 Cómo usar esta bóveda]] · [[00 Mapa de diagramas (qué gráfico tiene cada subtema)]] · [[07 Plan de mejoras pendientes]]
