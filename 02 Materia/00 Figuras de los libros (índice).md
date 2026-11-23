---
tipo: indice
---
# Figuras de los libros: índice y procedencia

> [!abstract] Qué es esta nota
> Las **132 figuras** extraídas de los dos libros de la bibliografía y pegadas en los subtemas: **48 de Quiroga** y **84 de Stallings** (algunas figuras se usan en más de un subtema, así que hay más filas que figuras). Cada una está en su nota con la cita de figura y página, así que se puede citar en el final sin volver a buscar.

> [!info] Cómo se extrajeron
> Con `tools/extraer_figuras.py`: el script busca el epígrafe (`Fig. 7.10`, `Figura 4.1`), parte la página en bloques de contenido (franjas de tinta separadas por blanco) y recorta el bloque que está justo encima del epígrafe. Sirve igual para PDFs escaneados (Quiroga) que para vectoriales (Stallings): en el segundo caso usa los dibujos vectoriales para no confundir una figura con un párrafo de texto. En la segunda pasada se corrigió el caso que fallaba (figura y epígrafe pegados en el mismo bloque de tinta): de Quiroga se pasó de **49 a 122 figuras** detectadas, y de ahí salieron casi todas las que faltaban en las unidades 1, 2, 4 y 5.

> [!note] Las de clase no están en esta nota
> Acá sólo se catalogan las figuras de la **bibliografía**. Las **15 figuras del resumen de cátedra** (resumen de Said) están catalogadas en [[00 Mapa de diagramas (qué gráfico tiene cada subtema)]], al final.

## Quiroga — *Arquitectura de computadoras* (Alfaomega)

| Fig. | Página | Qué muestra | Subtema |
|---|---|---|---|
| 1.3 | 32 | Fig. 1.3 — Esquema básico de una computadora von Neumann | [[7.4.1 von Neumann vs Harvard]] |
| 3.5 | 82 | Fig. 3.5 — Código BCD exceso tres (no ponderado y autocomplementario) | [[1.6.1 Códigos ponderados y no ponderados]] |
| 3.6 | 83 | Fig. 3.6 — Código BCD Aiken (2-4-2-1): ponderado y autocomplementario | [[1.6.1 Códigos ponderados y no ponderados]] |
| 4.1 | 100 | Fig. 4.1 — Esquema de registros para la suma de 8 bits, con el acarreo serie y las banderas S, Z, C y V | [[9.1.2 Acarreo anticipado (G y P)]] |
| 5.2 | 119 | Fig. 5.2 — Compuerta AND | [[1.1.1 Compuerta AND, OR y NOT]] |
| 5.4 | 120 | Fig. 5.4 — Compuerta XOR | [[1.1.2 NAND, NOR, XOR y XNOR]] |
| 5.6 | 121 | Fig. 5.6 — Compuerta NAND | [[1.1.2 NAND, NOR, XOR y XNOR]] |
| 5.7 | 121 | Fig. 5.7 — Compuerta ÑOR | [[1.1.2 NAND, NOR, XOR y XNOR]] |
| 5.8 | 122 | Fig. 5.8 — Teorema de De Morgan aplicado a la suma lógica | [[1.2.2 Leyes de DeMorgan]] |
| 5.9 | 122 | Fig. 5.9 — Teorema de De Morgan aplicado al producto lógico | [[1.2.2 Leyes de DeMorgan]] |
| 5.10 | 123 | Fig. 5.10 — I mplementación de la negación con compuertas negadas | [[1.1.3 Compuertas universales]] |
| 5.12 | 123 | Fig. 5.12 — Diagrama de lógica | [[1.2.1 Postulados, dualidad y teoremas]] |
| 5.15 | 126 | Fig. 5.15 — Buffer triestado | [[3.1.2 Bus único y buffers de 3 estados]] |
| 5.16 | 126 | Fig. 5.16 — Sumador binario paralelo con acarreo serie (SS y SC en cadena) | [[9.1.2 Acarreo anticipado (G y P)]] |
| 5.17 | 127 | Fig. 5.17 — Circuito lógico del semisumador | [[1.5.1 Semisumador y sumador completo]] |
| 5.19 | 131 | Fig. 5.19 — Circuito lógico con las FN D del sumador completo | [[1.5.2 Sumador de n bits y resta en complemento a 2]] |
| 6.7 | 142 | Fig. 6.7 — Diagramas de simplificación (a, b, c, d) para la función F0 | [[1.3.3 Don't care y criterios de agrupación]] |
| 6.8 | 142 | Fig. 6.8 — Diagrama de lógica (parcial) de un circuito convertidor de código | [[1.2.3 Simplificación analítica]] |
| 6.10 | 143 | Fig. 6.10 — Diagrama de bloque del codificador decimal a BCD | [[1.4.2 Codificador]] |
| 6.11 | 143 | Fig. 6.11 — Diagrama de lógica correspondiente a F3 | [[1.3.1 Mintérminos y maxtérminos]] |
| 6.13 | 145 | Fig. 6.13 — Diagrama de bloque del decodificador n → 2ⁿ (2 → 4), sin entrada de habilitación | [[1.4.1 Decodificador]] |
| 6.15 | 146 | Fig. 6.15 — Diagrama de lógica de un decodificador 2 → 4 (dos inversores y cuatro AND) | [[1.4.1 Decodificador]] |
| 6.18 | 149 | Fig. 6.18 — Diagrama de bloque: el multiplexor conecta una de las salidas de los registros al bus y el demultiplexor reparte el dato del bus a un registro | [[1.4.3 Multiplexor]] |
| 6.19 | 149 | Fig. 6.19 — Diagrama de bloque de un demultiplexor: una entrada de dato, dos de selección y cuatro salidas | [[1.4.4 Demultiplexor]] |
| 6.20 | 149 | Fig. 6.20 — Diagrama de bloque de un multiplexor para cuatro entradas (D0 a D3) y dos entradas de selección | [[1.4.3 Multiplexor]] |
| 6.23 | 153 | Fig. 6.23 — Diagrama de bloque de cualquiera de las memorias de sólo lectura | [[2.4.1 ROM = decodificador + OR]] |
| 6.27 | 157 | Fig. 6.27 — Diagrama de lógica con compuertas NOR: biestable RS | [[2.1.1 Biestable RS (NOR y NAND)]] |
| 6.30 | 158 | Fig. 6.30 — Diagrama de lógica de un biestable J-K sincrónico | [[2.1.3 Flip-flop JK y ecuaciones características]] |
| 6.31 | 159 | Fig. 6.31 — Diagrama de bloque de la conversión de un biestable T a J-K (y la tabla de excitación que la justifica) | [[2.1.4 Conversión entre biestables]] |
| 6.34 | 159 | Fig. 6.34 — Diagrama de lógica de un biestable D sincrónico | [[2.1.2 Flip-flops D y T]] |
| 6.35 | 160 | Fig. 6.35 — Diagrama de bloque de un registro paralelo-paralelo | [[2.2.1 Registros PIPO y SISO]] |
| 6.36 | 160 | Fig. 6.36 — Diagrama de bloque de un contador progresivo de 8 eventos con biestables T | [[2.2.3 Contadores binarios y módulo N]] |
| 7.1 | 170 | Fig. 7.1 — Diagrama de bloque de un dispositivo que suma los bits de los registro A y B | [[3.2.1 Estructura, G-P y señales de selección]] |
| 7.6 | 175 | Fig. 7.6 — Formato de instrucción de la CPU de «X»: 4 bits de código de operación y 12 de dirección o ignorado | [[4.2.2 Los 16 opcodes octales]] |
| 7.7 | 175 | Fig. 7.7 — Memoria para instrucciones y para datos: 4 Kbytes = 4096 palabras de 16 bits ⇒ 2¹² ⇒ 12 bits de dirección | [[2.7.1 Bits de dirección igual a log2 de celdas]] |
| 7.9 | 177 | Fig. 7.9 — Código de instrucción: los 16 bits repartidos en OP y DATA | [[2.7.2 CodOp vs campo de dirección]] |
| 7.10 | 178 | Fig. 7.10 — Fase fetch | [[4.3.2 Búsqueda, los 8 pulsos]] |
| 7.11 | 179 | Fig. 7.11 — Estructura de una parte del módulo de control para la fase fetch | [[4.4.1 Funciones y señales de control]] |
| 7.13 | 182 | Fig. 7.13 — Fase execute LDA | [[4.3.3 Ejecución instrucción por instrucción]] |
| 7.14 | 183 | Fig. 7.14 — Fase execute ADA | [[4.3.3 Ejecución instrucción por instrucción]] |
| 7.15 | 184 | Fig. 7.15 — Fase execute SHR | [[5.4.2 Modificador de 2 bits y los 24 pulsos]] |
| 7.21 | 193 | Fig. 7.21 — Diseño parcial del control para la orden de lectura de la memoria | [[4.4.1 Funciones y señales de control]] |
| 7.25 | 196 | Fig. 7.25 — Instrucciones aritméticas y lógicas en la ALU | [[3.2.2 Operaciones aritméticas, lógicas y flags]] |
| 8.2 | 213 | Fig. 8.2 — Ciclo de instrucción para las n instrucciones de un programa | [[4.2.3 Programar en BLUE]] |
| 9.4 | 238 | Fig. 9.4 — Diagrama más detallado de la celda | [[2.3.1 Celda elemental de memoria]] |
| 14.1 | 362 | Fig. 14.1 — Traducción de la dirección virtual | [[2.6.1 Memoria virtual y paginación]] |
| — | 133 | Mapa de Karnaugh de 2 variables: dos casillas vecinas difieren en una sola variable, así que se agrupan (Quiroga, ejemplo 5.10.1) | [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]] |
| — | 133 | Mapa de Karnaugh de 3 variables: las columnas van en orden Gray (00, 01, 11, 10) para que dos casillas contiguas nunca cambien en más de un bit | [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]] |

## Stallings — *Organización y arquitectura de computadores*, 7ª ed.

| Fig. | Página | Qué muestra | Subtema |
|---|---|---|---|
| 1.1 | 32 | Fig. 1.1 — Una visión funcional de un computador | [[4.1.1 Unidades funcionales de una computadora]] |
| 1.5 | 36 | Fig. 1.5 — La unidad central de procesamiento (CPU) | [[5.1.3 Registros de la CPU]] |
| 1.5 | 36 | Fig. 1.5 — La unidad central de procesamiento (CPU) | [[3.3.1 AC, PC, IR, MAR y MBR]] |
| 2.1 | 42 | Fig. 2.1 — Estructura del computador IAS | [[4.1.2 IAS y el programa almacenado]] |
| 2.4 | 46 | Fig. 2.4 — Diagrama de flujo parcial de las operaciones del IAS | [[4.1.2 IAS y el programa almacenado]] |
| 3.3 | 84 | Fig. 3.3 — Ciclo de instrucción básico | [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] |
| 3.5 | 86 | Fig. 3.5 — Ejemplo de ejecución de un programa: contenidos de la memoria y registros de la CPU paso a paso | [[4.2.1 Especificación, registros y 4096x16]] |
| 3.6 | 87 | Fig. 3.6 — Diagrama de estados del ciclo de intrucción | [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] |
| 3.9 | 91 | Fig. 3.9 — Ciclo de instrucción con interrupciones | [[5.5.1 IRQ, SI y CP8]] |
| 3.12 | 95 | Fig. 3.12 — Diagrama de estados de un ciclo de instrucción, con interrupciones | [[10.2.1 Mecanismo completo]] |
| 3.14 | 97 | Fig. 3.14 — Ejemplo de secuencia temporal de varias interrupciones | [[10.2.2 Interrupciones vectorizadas y prioridad]] |
| 3.16 | 99 | Fig. 3.16 — Esquema de interconexión mediante un bus | [[3.1.3 Buses de datos, de direcciones y de control]] |
| 3.17 | 101 | Fig. 3.17 — Implementación física típica de una arquitectura de bus | [[7.4.2 Buses internos y externos]] |
| 3.19 | 106 | Fig. 3.19 — Temporización síncrona de las operaciones de bus | [[3.1.3 Buses de datos, de direcciones y de control]] |
| 4.1 | 130 | Fig. 4.1 — Jerarquía de memoria | [[2.5.1 Jerarquía y localidad]] |
| 4.5 | 135 | Fig. 4.5 — Operación de lectura de caché | [[2.5.3 AMAT y cálculo de mejora]] |
| 4.8 | 141 | Fig. 4.8 — Ejemplo de correspondencia directa | [[2.5.2 Caché, mapeos y políticas]] |
| 4.12 | 147 | Fig. 4.12 — Ejemplo de correspondencia asociativa por conjuntos de dos vías | [[2.5.2 Caché, mapeos y políticas]] |
| 5.3 | 178 | Fig. 5.3 — DRAM típica de 16 megabits (4M 4) | [[2.3.2 SRAM y DRAM]] |
| 5.5 | 181 | Fig. 5.5 — Organización de una memoria de 256 KB | [[2.3.3 Matriz, expansión y RAM 8x3]] |
| 5.11 | 186 | Fig. 5.11 — Código SEC-DED de Hamming | [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]] |
| 5.12 | 188 | Fig. 5.12 — RAM dinámica síncrona (SDRAM): varios chips en paralelo sobre el mismo bus de direcciones | [[8.3.1 Bancos de memoria y ancho de banda]] |
| 5.13 | 189 | Fig. 5.13 — Temporización de una lectura de SDRAM (longitud de ráfaga 4, | [[10.4.2 Interfaces serie y paralelo]] |
| 5.14 | 190 | Fig. 5.14 — Estructura RDRAM: un controlador y varios canales (RDRAM1 a RDRAMn) que trabajan en paralelo | [[8.3.2 Patrón de entrelazado y conflictos de banco]] |
| 6.2 | 200 | Fig. 6.2 — Organización de los datos en el disco | [[10.4.1 Discos, SSD y latencias]] |
| 6.6 | 203 | Fig. 6.6 — Pistas y cilindros | [[10.4.1 Discos, SSD y latencias]] |
| 7.1 | 231 | Fig. 7.1 — Módulo genérico de un módulo E/S | [[10.1.1 Polling y sus límites]] |
| 7.3 | 238 | Fig. 7.3 — Diagrama de bloques de un módulo de E/S | [[10.1.2 Puertos, interfaces y handshake]] |
| 7.6 | 244 | Fig. 7.6 — Procedimiento de interrupción simple | [[5.5.1 IRQ, SI y CP8]] |
| 7.8 | 248 | Fig. 7.8 — Uso del controlador de interrupciones 82C59A | [[10.2.2 Interrupciones vectorizadas y prioridad]] |
| 7.10 | 250 | Fig. 7.10 — Interfaz teclado/pantalla en el 82C55A | [[10.1.2 Puertos, interfaces y handshake]] |
| 7.11 | 252 | Fig. 7.11 — Diagrama de bloques típico de un módulo de DMA | [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] |
| 7.12 | 253 | Fig. 7.12 — Puntos de ruptura para el DMA y las interrupciones en un ciclo de instrucción | [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] |
| 8.18 | 303 | Fig. 8.18 — Funcionamiento de la paginación y del buffer de traducción | [[2.6.1 Memoria virtual y paginación]] |
| 8.19 | 304 | Fig. 8.19 — Buffer de traducción anticipada y funcionamiento de la caché | [[2.6.2 Memoria auxiliar y memoria asociativa]] |
| 9.1 | 325 | Fig. 9.1 — Entradas y salidas de la ALU | [[3.2.1 Estructura, G-P y señales de selección]] |
| 9.3 | 333 | Fig. 9.3 — Suma de números representados en complemento a dos | [[9.1.1 Complemento a 2 y desbordamiento]] |
| 9.5 | 335 | Fig. 9.5 — Descripción geométrica de los enteros en complemento a dos | [[9.1.1 Complemento a 2 y desbordamiento]] |
| 9.7 | 336 | Fig. 9.7 — Multiplicación de enteros binarios sin signo | [[9.2.1 Sumas y desplazamientos]] |
| 9.10 | 339 | Fig. 9.10 — Multiplicación de dos enteros sin signo de cuatro bits para producir | [[9.2.1 Sumas y desplazamientos]] |
| 9.12 | 340 | Fig. 9.12 — Algoritmo de Booth para la multiplicación en complemento a dos | [[9.2.2 Algoritmo de Booth]] |
| 9.13 | 341 | Fig. 9.13 — Ejemplo de aplicación del algoritmo de Booth (7 3) | [[9.2.2 Algoritmo de Booth]] |
| 9.15 | 344 | Fig. 9.15 — División de enteros binarios sin signo | [[9.3.1 Restauración y no restauración]] |
| 9.16 | 345 | Fig. 9.16 — Diagrama de flujo para la división de binarios sin signo | [[9.3.1 Restauración y no restauración]] |
| 9.23 | 356 | Fig. 9.23 — Multiplicación en coma flotante (Z ←X Y) | [[9.4.1 Formato, normalización y operaciones]] |
| 9.24 | 357 | Fig. 9.24 — División en coma flotante (Z ←X/Y) | [[9.4.1 Formato, normalización y operaciones]] |
| 10.4 | 383 | Fig. 10.4 — Formatos de datos numéricos en el Pentium | [[9.4.2 IEEE 754]] |
| 10.6 | 394 | Fig. 10.6 — Instrucciones de bifurcación (salto relativo `BRR`) | [[5.1.2 Clasificación de las instrucciones]] |
| 10.8 | 397 | Fig. 10.8 — Uso de una pila para implementar el anidamiento de subrutinas | [[5.5.2 Máscara, pila y RTI]] |
| 10.13 | 418 | Fig. 10.13 — Operaciones básicas con la pila | [[5.6.2 La pila y el registro SP]] |
| 10.15 | 421 | Fig. 10.15 — Comparación de tres programas para calcular lo mismo (pila, registros generales y registro único) | [[5.2.1 Los 4 formatos y el campo único de dirección]] |
| 11.1 | 431 | Fig. 11.1 — Modos de direccionamiento | [[5.3.1 Los 7 modos]] |
| 11.2 | 438 | Fig. 11.2 — Cálculos en el modo de direccionamiento del Pentium | [[5.3.2 Dirección efectiva y costo en accesos]] |
| 11.6 | 448 | Fig. 11.6 — Formatos de instrucciones utilizados en el PDP-11 | [[5.2.2 Cálculo de CodOp según el tamaño de memoria]] |
| 11.8 | 451 | Fig. 11.8 — Formato de instrucciones del Pentium | [[5.1.1 Instrucción, opcode y operandos]] |
| 12.2 | 462 | Fig. 12.2 — Estructura interna del procesador | [[5.6.1 BIU, EU y segmentación]] |
| 12.10 | 474 | Fig. 12.10 — Diagrama de tiempos del funcionamiento de un cauce de instrucciones | [[7.1.1 Etapas y diagrama en escalera]] |
| 12.11 | 474 | Fig. 12.11 — Efecto de un salto condicional en el funcionamiento de un cauce | [[7.1.2 Hazards y sus soluciones]] |
| 12.12 | 475 | Fig. 12.12 — Cauce de instrucciones de un procesador, con seis etapas | [[7.1.1 Etapas y diagrama en escalera]] |
| 12.15 | 480 | Fig. 12.15 — Buffer de bucles | [[7.3.2 UC cableada vs microprogramada y load-store]] |
| 12.16 | 482 | Fig. 12.16 — Diagrama de flujo de la predicción de saltos | [[7.2.2 Caché y predicción de saltos]] |
| 12.17 | 482 | Fig. 12.17 — Diagrama de estados de la predicción de saltos | [[7.2.2 Caché y predicción de saltos]] |
| 13.8 | 533 | Fig. 13.8 — Formatos de instrucciones del MIPS (formato de tres operandos) | [[5.2.1 Los 4 formatos y el campo único de dirección]] |
| 14.5 | 562 | Fig. 14.5 — Incremento de velocidad de diversas organizaciones de una máquina, | [[7.1.3 Cálculo de speedup y límites]] |
| 14.8 | 566 | Fig. 14.8 — Cauce segmentado del Pentium 4 | [[7.3.1 Tabla comparativa y ejemplos]] |
| 14.15 | 582 | Fig. 14.15 — Un procesador superescalar con un cauce doble | [[7.2.1 Superscalar, superpipeline, SMT y multicore]] |
| 16.4 | 631 | Fig. 16.4 — Diagrama de bloques de la unidad de control | [[6.1.1 Circuito, compuertas y señales]] |
| 16.5 | 633 | Fig. 16.5 — Caminos de datos y señales de control | [[3.1.1 Notación de transferencia entre registros]] |
| 16.6 | 635 | Fig. 16.6 — Procesador con bus interno | [[3.3.2 Base, índice, puntero de pila y estado]] |
| 16.10 | 642 | Fig. 16.10 — Unidad de control con entradas decodificadas | [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] |
| 17.2 | 649 | Fig. 17.2 — Organización de la memoria de control | [[6.2.1 Memoria de control y microinstrucción]] |
| 17.3 | 649 | Fig. 17.3 — Microarquitectura de una unidad de control | [[6.3.1 Cableada vs microprogramada]] |
| 17.5 | 652 | Fig. 17.5 — Unidad de control microprogramada de Wilkes | [[6.2.1 Memoria de control y microinstrucción]] |
| 17.6 | 657 | Fig. 17.6 — Lógica de control de salto con dos campos de dirección | [[6.2.2 Secuenciamiento y microPC]] |
| 17.7 | 658 | Fig. 17.7 — Lógica de control de salto con un único campo de dirección | [[6.2.2 Secuenciamiento y microPC]] |
| 17.14 | 670 | Fig. 17.14 — Organización de la unidad de control del LSI-11 | [[6.3.2 El 8088, ROM de control 504x21]] |
| 18.2 | 694 | Fig. 18.2 — Organizaciones de computador alternativas | [[8.4.2 Monousuario vs multiusuario]] |
| 18.4 | 696 | Fig. 18.4 — Diagrama de bloques genérico de un multiprocesador fuertemente acoplado | [[8.2.2 Flynn, arreglos SIMD y conectados]] |
| 18.5 | 697 | Fig. 18.5 — Organización de multiprocesador simétrico | [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] |
| 18.7 | 706 | Fig. 18.7 — Diagrama de transición de estados MESI | [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] |
| 18.12 | 724 | Fig. 18.12 — Organización CC-NUMA | [[8.4.2 Monousuario vs multiusuario]] |
| 18.13 | 727 | Fig. 18.13 — Ejemplo de suma vectorial | [[8.1.1 Etapas segmentadas y suma de vectores]] |
| 18.15 | 729 | Fig. 18.15 — Alternativas para la computación vectorial | [[8.1.1 Etapas segmentadas y suma de vectores]] |
| 18.19 | 734 | Fig. 18.19 — Programas alternativos de computación vectorial | [[8.1.2 Encadenamiento y speedup]] |

## Fuentes que se pueden explotar más

| Libro | Figuras detectadas | Qué cubre |
|---|---|---|
| Quiroga | 122 | compuertas, códigos (exceso 3, Aiken), algebra de Boole, Karnaugh, decodificadores, codificadores, MUX/DEMUX, biestables, registros, contadores, ROM, ciclo de instrucción, memorias, memoria virtual |
| Stallings | 159 | IAS, buses, caché, memoria interna, discos, E/S, DMA, aritmética (Booth, división), pipeline, superescalar, IA-64, microprogramación, multiprocesadores |
| Hamacher · Tanenbaum · Patterson | — | no están en PDF en esta bóveda |

Los recortes crudos quedaron en `_figs/` y `_figs2/` fuera de la bóveda, por si hace falta cambiar alguno. Para volver a recortar un mapa de Karnaugh (que en el libro no lleva epígrafe) se usa un `clip` manual sobre la página.

## Relacionado
[[00 Mapa de diagramas (qué gráfico tiene cada subtema)]] · [[00 Índice de la materia (las 10 unidades)]] · [[07 Plan de mejoras pendientes]]
