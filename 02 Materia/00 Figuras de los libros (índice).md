---
tipo: indice
---
# Figuras de los libros: índice y procedencia

> [!abstract] Qué es esta nota
> Las **100 figuras** extraídas de los dos libros de la bibliografía y pegadas en los subtemas:
> **24 de Quiroga** y **76 de Stallings**. Cada una está en su nota con la cita de figura y página,
> así que se puede citar en el final sin volver a buscar.

> [!info] Cómo se extrajeron
> Con `tools/extraer_figuras.py`: el script busca el epígrafe (`Fig. 7.10`, `Figura 4.1`), parte la página en
> bloques de contenido (franjas de tinta separadas por blanco) y recorta el bloque que está justo encima del
> epígrafe. Sirve igual para PDFs escaneados (Quiroga) que para vectoriales (Stallings): en el segundo caso usa
> los dibujos vectoriales para no confundir una figura con un párrafo de texto.

## Quiroga — *Arquitectura de computadoras* (Alfaomega)

| Fig. | Página | Qué muestra | Subtema |
|---|---|---|---|
| 5.2 | 119 | Compuerta AND | [[1.1.1 Compuerta AND, OR y NOT]] |
| 5.4 | 120 | Compuerta XOR | [[1.1.2 NAND, NOR, XOR y XNOR]] |
| 5.6 | 121 | Compuerta NAND | [[1.1.2 NAND, NOR, XOR y XNOR]] |
| 5.7 | 121 | Compuerta ÑOR | [[1.1.2 NAND, NOR, XOR y XNOR]] |
| 5.10 | 123 | I mplementación de la negación con compuertas negadas | [[1.1.3 Compuertas universales]] |
| 5.15 | 126 | Buffer triestado | [[3.1.2 Bus único y buffers de 3 estados]] |
| 5.17 | 127 | Circuito lógico del semisumador | [[1.5.1 Semisumador y sumador completo]] |
| 5.19 | 131 | Circuito lógico con las FN D del sumador completo | [[1.5.2 Sumador de n bits y resta en complemento a 2]] |
| 6.23 | 153 | Diagrama de bloque de cualquiera de las memorias de sólo lectura | [[2.4.1 ROM = decodificador + OR]] |
| 6.30 | 158 | Diagrama de lógica de un biestable J-K sincrónico | [[2.1.3 Flip-flop JK y ecuaciones características]] |
| 6.34 | 159 | Diagrama de lógica de un biestable D sincrónico | [[2.1.2 Flip-flops D y T]] |
| 6.35 | 160 | Diagrama de bloque de un registro paralelo-paralelo | [[2.2.1 Registros PIPO y SISO]] |
| 6.36 | 160 | Diagrama de bloque de un contador progresivo de 8 eventos con biestabl | [[2.2.3 Contadores binarios y módulo N]] |
| 7.1 | 170 | Diagrama de bloque de un dispositivo que suma los bits de los registro | [[3.2.1 Estructura, G-P y señales de selección]] |
| 7.10 | 178 | Fase fetch | [[4.3.2 Búsqueda, los 8 pulsos]] |
| 7.11 | 179 | Estructura de una parte del módulo de control para la fase fetch | [[4.4.1 Funciones y señales de control]] |
| 7.13 | 182 | Fase execute LDA | [[4.3.3 Ejecución instrucción por instrucción]] |
| 7.14 | 183 | Fase execute ADA | [[4.3.3 Ejecución instrucción por instrucción]] |
| 7.15 | 184 | Fase execute SHR | [[5.4.2 Modificador de 2 bits y los 24 pulsos]] |
| 7.21 | 193 | Diseño parcial del control para la orden de lectura de la memoria | [[4.4.1 Funciones y señales de control]] |
| 7.25 | 196 | Instrucciones aritméticas y lógicas en la ALU | [[3.2.2 Operaciones aritméticas, lógicas y flags]] |
| 9.4 | 238 | Diagrama más detallado de la celda | [[2.3.1 Celda elemental de memoria]] |
| 9.11 | 254 | Inserción de un chip. Fig. 9.12. Esquema de un módulo. Fig. 9.13. Inse | [[2.7.1 Bits de dirección igual a log2 de celdas]] |
| 14.1 | 362 | Traducción de la dirección virtual | [[2.6.1 Memoria virtual y paginación]] |

## Stallings — *Organización y arquitectura de computadores*, 7ª ed.

| Fig. | Página | Qué muestra | Subtema |
|---|---|---|---|
| 1.1 | 32 | Una visión funcional de un computador | [[4.1.1 Unidades funcionales de una computadora]] |
| 1.5 | 36 | La unidad central de procesamiento (CPU) | [[3.3.1 AC, PC, IR, MAR y MBR]] |
| 1.5 | 36 | La unidad central de procesamiento (CPU) | [[5.1.3 Registros de la CPU]] |
| 2.1 | 42 | Estructura del computador IAS | [[4.1.2 IAS y el programa almacenado]] |
| 2.4 | 46 | Diagrama de flujo parcial de las operaciones del IAS | [[4.1.2 IAS y el programa almacenado]] |
| 3.3 | 84 | Ciclo de instrucción básico | [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] |
| 3.6 | 87 | Diagrama de estados del ciclo de intrucción | [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] |
| 3.9 | 91 | Ciclo de instrucción con interrupciones | [[5.5.1 IRQ, SI y CP8]] |
| 3.12 | 95 | Diagrama de estados de un ciclo de instrucción, con interrupciones | [[10.2.1 Mecanismo completo]] |
| 3.14 | 97 | Ejemplo de secuencia temporal de varias interrupciones | [[10.2.2 Interrupciones vectorizadas y prioridad]] |
| 3.16 | 99 | Esquema de interconexión mediante un bus | [[3.1.3 Buses de datos, de direcciones y de control]] |
| 3.17 | 101 | Implementación física típica de una arquitectura de bus | [[7.4.2 Buses internos y externos]] |
| 3.19 | 106 | Temporización síncrona de las operaciones de bus | [[3.1.3 Buses de datos, de direcciones y de control]] |
| 4.1 | 130 | Jerarquía de memoria | [[2.5.1 Jerarquía y localidad]] |
| 4.5 | 135 | Operación de lectura de caché | [[2.5.3 AMAT y cálculo de mejora]] |
| 4.8 | 141 | Ejemplo de correspondencia directa | [[2.5.2 Caché: mapeos y políticas]] |
| 4.12 | 147 | Ejemplo de correspondencia asociativa por conjuntos de dos vías | [[2.5.2 Caché: mapeos y políticas]] |
| 5.3 | 178 | DRAM típica de 16 megabits (4M 4) | [[2.3.2 SRAM y DRAM]] |
| 5.5 | 181 | Organización de una memoria de 256 KB | [[2.3.3 Matriz, expansión y RAM 8x3]] |
| 5.13 | 189 | Temporización de una lectura de SDRAM (longitud de ráfaga 4, | [[10.4.2 Interfaces serie y paralelo]] |
| 6.2 | 200 | Organización de los datos en el disco | [[10.4.1 Discos, SSD y latencias]] |
| 6.6 | 203 | Pistas y cilindros | [[10.4.1 Discos, SSD y latencias]] |
| 7.1 | 231 | Módulo genérico de un módulo E/S | [[10.1.1 Polling y sus límites]] |
| 7.3 | 238 | Diagrama de bloques de un módulo de E/S | [[10.1.2 Puertos, interfaces y handshake]] |
| 7.6 | 244 | Procedimiento de interrupción simple | [[5.5.1 IRQ, SI y CP8]] |
| 7.8 | 248 | Uso del controlador de interrupciones 82C59A | [[10.2.2 Interrupciones vectorizadas y prioridad]] |
| 7.10 | 250 | Interfaz teclado/pantalla en el 82C55A | [[10.1.2 Puertos, interfaces y handshake]] |
| 7.11 | 252 | Diagrama de bloques típico de un módulo de DMA | [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] |
| 7.12 | 253 | Puntos de ruptura para el DMA y las interrupciones en un ciclo de inst | [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] |
| 8.18 | 303 | Funcionamiento de la paginación y del buffer de traducción | [[2.6.1 Memoria virtual y paginación]] |
| 8.19 | 304 | Buffer de traducción anticipada y funcionamiento de la caché | [[2.6.2 Memoria auxiliar y memoria asociativa]] |
| 9.1 | 325 | Entradas y salidas de la ALU | [[3.2.1 Estructura, G-P y señales de selección]] |
| 9.3 | 333 | Suma de números representados en complemento a dos | [[9.1.1 Complemento a 2 y desbordamiento]] |
| 9.5 | 335 | Descripción geométrica de los enteros en complemento a dos | [[9.1.1 Complemento a 2 y desbordamiento]] |
| 9.7 | 336 | Multiplicación de enteros binarios sin signo | [[9.2.1 Sumas y desplazamientos]] |
| 9.10 | 339 | Multiplicación de dos enteros sin signo de cuatro bits para producir | [[9.2.1 Sumas y desplazamientos]] |
| 9.12 | 340 | Algoritmo de Booth para la multiplicación en complemento a dos | [[9.2.2 Algoritmo de Booth]] |
| 9.13 | 341 | Ejemplo de aplicación del algoritmo de Booth (7 3) | [[9.2.2 Algoritmo de Booth]] |
| 9.15 | 344 | División de enteros binarios sin signo | [[9.3.1 Restauración y no restauración]] |
| 9.16 | 345 | Diagrama de flujo para la división de binarios sin signo | [[9.3.1 Restauración y no restauración]] |
| 9.23 | 356 | Multiplicación en coma flotante (Z ←X Y) | [[9.4.1 Formato, normalización y operaciones]] |
| 9.24 | 357 | División en coma flotante (Z ←X/Y) | [[9.4.1 Formato, normalización y operaciones]] |
| 10.4 | 383 | Formatos de datos numéricos en el Pentium | [[9.4.2 IEEE 754]] |
| 10.8 | 397 | Uso de una pila para implementar el anidamiento de subrutinas | [[5.5.2 Máscara, pila y RTI]] |
| 10.13 | 418 | Operaciones básicas con la pila | [[5.6.2 La pila y el registro SP]] |
| 11.1 | 431 | Modos de direccionamiento | [[5.3.1 Los 7 modos]] |
| 11.2 | 438 | Cálculos en el modo de direccionamiento del Pentium | [[5.3.2 Dirección efectiva y costo en accesos]] |
| 11.8 | 451 | Formato de instrucciones del Pentium | [[5.1.1 Instrucción, opcode y operandos]] |
| 12.2 | 462 | Estructura interna del procesador | [[5.6.1 BIU, EU y segmentación]] |
| 12.10 | 474 | Diagrama de tiempos del funcionamiento de un cauce de instrucciones | [[7.1.1 Etapas y diagrama en escalera]] |
| 12.11 | 474 | Efecto de un salto condicional en el funcionamiento de un cauce | [[7.1.2 Hazards y sus soluciones]] |
| 12.12 | 475 | Cauce de instrucciones de un procesador, con seis etapas | [[7.1.1 Etapas y diagrama en escalera]] |
| 12.15 | 480 | Buffer de bucles | [[7.3.2 UC cableada vs microprogramada y load-store]] |
| 12.16 | 482 | Diagrama de flujo de la predicción de saltos | [[7.2.2 Caché y predicción de saltos]] |
| 12.17 | 482 | Diagrama de estados de la predicción de saltos | [[7.2.2 Caché y predicción de saltos]] |
| 14.5 | 562 | Incremento de velocidad de diversas organizaciones de una máquina, | [[7.1.3 Cálculo de speedup y límites]] |
| 14.8 | 566 | Cauce segmentado del Pentium 4 | [[7.3.1 Tabla comparativa y ejemplos]] |
| 14.11 | 573 | Estructura de cauces del PowerPC 601 [POTT94] | [[7.2.1 Superscalar, superpipeline, SMT y multicore]] |
| 14.15 | 582 | Un procesador superescalar con un cauce doble | [[7.2.1 Superscalar, superpipeline, SMT y multicore]] |
| 16.4 | 631 | Diagrama de bloques de la unidad de control | [[6.1.1 Circuito, compuertas y señales]] |
| 16.5 | 633 | Caminos de datos y señales de control | [[3.1.1 Notación de transferencia entre registros]] |
| 16.6 | 635 | Procesador con bus interno | [[3.3.2 Base, índice, puntero de pila y estado]] |
| 16.10 | 642 | Unidad de control con entradas decodificadas | [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] |
| 17.2 | 649 | Organización de la memoria de control | [[6.2.1 Memoria de control y microinstrucción]] |
| 17.3 | 649 | Microarquitectura de una unidad de control | [[6.3.1 Cableada vs microprogramada]] |
| 17.5 | 652 | Unidad de control microprogramada de Wilkes | [[6.2.1 Memoria de control y microinstrucción]] |
| 17.6 | 657 | Lógica de control de salto con dos campos de dirección | [[6.2.2 Secuenciamiento y microPC]] |
| 17.7 | 658 | Lógica de control de salto con un único campo de dirección | [[6.2.2 Secuenciamiento y microPC]] |
| 17.14 | 670 | Organización de la unidad de control del LSI-11 | [[6.3.2 El 8088, ROM de control 504x21]] |
| 18.2 | 694 | Organizaciones de computador alternativas | [[8.4.2 Monousuario vs multiusuario]] |
| 18.5 | 697 | Organización de multiprocesador simétrico | [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] |
| 18.7 | 706 | Diagrama de transición de estados MESI | [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] |
| 18.12 | 724 | Organización CC-NUMA | [[8.4.2 Monousuario vs multiusuario]] |
| 18.13 | 727 | Ejemplo de suma vectorial | [[8.1.1 Etapas segmentadas y suma de vectores]] |
| 18.15 | 729 | Alternativas para la computación vectorial | [[8.1.1 Etapas segmentadas y suma de vectores]] |
| 18.19 | 734 | Programas alternativos de computación vectorial | [[8.1.2 Encadenamiento y speedup]] |

## Fuentes que se pueden explotar más
| Libro | Figuras detectadas | Qué cubre |
|---|---|---|
| Quiroga | 49 | compuertas, biestables, registros, contadores, ROM, ciclo de instrucción, memorias, memoria virtual |
| Stallings | 159 | IAS, buses, caché, memoria interna, discos, E/S, DMA, aritmética (Booth, división), pipeline, superescalar, IA-64, microprogramación, multiprocesadores |
| Hamacher · Tanenbaum · Patterson | — | no están en PDF en esta bóveda |

Los recortes crudos (los 208) quedaron en `_figs/` fuera de la bóveda, por si hace falta cambiar alguno.

## Relacionado
[[00 Mapa de diagramas (qué gráfico tiene cada subtema)]] · [[00 Índice de la materia (las 10 unidades)]]
