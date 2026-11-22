---
tipo: examen
---
# Banco de preguntas del final

> [!abstract] Cómo usar esta nota
> Es el **índice maestro**: las preguntas tal como vienen en el modelo, cada una con su nota de desarrollo
> y la **respuesta mínima** (30 segundos) que tenés que poder decir sin pensar. Si una respuesta no te sale
> en 30 segundos, entrá a la nota.
>
> Para el **oral**: la matriz real del final (las 3 tandas, con los pesos que anotó el profesor) está en
> [[00 Matriz del final — las 3 tandas]]; el guion hablado de las 8 principales, en
> [[Guion de respuestas — preguntas principales]]; la vista de pájaro, en
> [[04 Resumen integrador de la materia]]; el trazo de los circuitos, en
> [[Cómo dibujar los circuitos (checklist de pizarrón)]].

> [!important] Empezá por la matriz
> Si tenés poco tiempo, no leas este banco de arriba a abajo: abrí [[00 Matriz del final — las 3 tandas]],
> elegí una tanda y respondé en voz alta con lo que linkea cada ítem. Este banco sirve como índice general
> de temas; la matriz dice **qué cae junto y con qué peso**.

## Preguntas principales (valen la nota)
| # | Pregunta | Nota de desarrollo | Respuesta mínima |
|---|---|---|---|
| 1 | **Flujo de información (dato y direcciones)** | [[Flujo de información en BLUE (datos y direcciones)]] | Bus único: por pulso, una fuente habilita su salida de tres estados y un destino carga. Direcciones (12 bits) van por PC/IR → MAR → memoria; datos (16 bits) van memoria → MBR → IR/AC o AC → MBR → memoria |
| 2 | **Formato de la instrucción (las 4)** | [[Formato de la instrucción (4 formatos)]] | 4, 3, 2 y 1 dirección. Más direcciones = instrucción más larga y menos instrucciones; menos direcciones = instrucción corta, más instrucciones y un operando implícito (AC). BLUE usa 1 dirección: `opcode 4 + dirección 12` |
| 3 | **Ciclo de máquina** (y las 16 instrucciones con todos sus pulsos) | [[Ciclo de máquina]] + [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | Búsqueda → decodificación → ejecución, repetido mientras RUN = 1. STATE pasa de F (fetch) a E (execute). Cada pulso = una microoperación |
| 4 | **Estructura básica (cada unidad y buses)** | [[Estructura básica de un computador]] | CPU (UC + ALU + registros), memoria, E/S, unidas por bus de datos (16), de direcciones (12) y de control. Von Neumann: una memoria para programa y datos |
| 5 | **Memoria RAM 8×3** | [[Memoria RAM 8x3]] | 8 palabras × 3 bits = 24 bits; 3 bits de dirección (000–111), 3 de datos; decodificador 3→8 elige la palabra; CS habilita el chip y R/W' define lectura o escritura |
| 6 | **Ciclo de ejecución de BLUE indexada y sin indexar** | [[BLUE indexada (RIF, RID, nuevo formato)]] + [[Ciclo de ejecución — todas las operaciones]] | Sin indexar: `MAR ← IR(dir)`, lectura, `AC ← MBR`. Indexada: la EA se calcula con el sumador de direcciones (`EA = D ± RIF/RID`) y el modificador de 2 bits elige el modo (directo/indirecto/RIF/RID) |
| 7 | **UC: funciones y señales de control; importancia y ejemplos** | [[Unidad de Control]] | Cuatro funciones: sincronizar, decodificar, secuenciar y generar señales. Ejemplos: `MEMR`, `MARin`, `PCinc`, `MBRout`, `ALUop`, `load flags`. Sin ellas nada se transfiere: la UC es la que "manda" |
| 8 | **Interrupciones** | [[Interrupciones y entrada-salida]] | Pedido de atención que rompe la secuencia: termina la instrucción, guarda contexto (PC/flags), salta a la rutina de servicio, atiende, restaura y retorna. Polling vs vectorizadas; prioridades; en BLUE: SI, INT, INTACK, estados F/E/I |

## Preguntas secundarias
| # | Pregunta | Nota | Respuesta mínima |
|---|---|---|---|
| 1 | Memoria RAM: **celda elemental** | [[Celda elemental de memoria]] | 1 bit + línea de selección + R/W' + buffer de tres estados. SRAM = latch; DRAM = capacitor con refresco |
| 2 | **Flip-flops** | [[Flip-Flops SR, D, JK y T]] | Biestable = memoria de 1 bit, secuencial, por flanco. S-R (`Q=S+R'Q`, 1-1 prohibido), D (`Q=D`), J-K (`Q=JQ'+K'Q`, toggle), T (`Q=T⊕Q`) |
| 3 | **Modos de direccionamiento** (ventajas del indexado) | [[Modos de direccionamiento]] | **Siete**: inmediato, directo, indirecto, registro, registro indirecto, desplazamiento y pila. El indexado permite recorrer arreglos con un solo código, ahorra bits de dirección y es reubicable |
| 4 | **Memoria ROM** | [[Memoria ROM y sus tipos]] | No volátil, sólo lectura: máscara, PROM, EPROM (UV), EEPROM, Flash. Uso: firmware, tablas y **memoria de control** del microprograma |
| 5 | **Jerarquía de memorias** | [[Jerarquía de memorias]] | Registros → L1 → L2/L3 → RAM → disco → cinta: velocidad y costo por bit suben hacia arriba, capacidad baja. Funciona por **localidad** temporal y espacial |
| 6 | **Pipeline** (definir y ejemplificar) | [[Pipeline]] | Etapas solapadas: 4 etapas y n instrucciones dan `4+(n−1)` ciclos en lugar de `4n`. Conflictos: datos (forwarding), control (predicción), estructurales |
| 7 | **Arquitectura CISC y RISC** | [[CISC y RISC]] | CISC: instrucciones complejas, longitud variable, opera sobre memoria, UC microprogramada (x86). RISC: instrucciones simples de longitud fija, load/store, muchos registros, UC cableada, pipeline (ARM) |
| 8 | **Manejo de una instrucción: qué es y en qué unidad se usa** | [[Ciclo de búsqueda (7 y 8 pulsos)]] + [[Unidad de Control]] | Es el ciclo búsqueda–decodificación–ejecución; se realiza en la **UC** (que genera las señales) con los registros PC, MAR, MBR, IR y la ALU |
| 9 | **7 y 8 pulsos del ciclo de búsqueda** | [[Ciclo de búsqueda (7 y 8 pulsos)]] | 7 pasos: MAR←PC, MEMR, MBR←dato, PC+1, IR←MBR, decodificar, STATE←E. El 8.º pulso es la espera de memoria (o el incremento solapado) |
| 10 | **Ciclo de ejecución para todas las operaciones** | [[Ciclo de ejecución — todas las operaciones]] | Cuatro familias: transferencia (LDA/STA), ALU (ADD/SUB/AND/OR/XOR/NOT), control (JMP/JZ/JC/NOP/HLT) y E/S (IN/OUT). Cada una con su secuencia de microoperaciones |
| 11 | **Ciclo LDA (24 pulsos)** | [[Ciclo de la instrucción LDA (24 pulsos)]] | 8 de búsqueda + 16 de ejecución (8 microoperaciones × 2 pulsos). Secuencia: `MAR←IR(dir)`, MEMR, `MBR←M[MAR]`, `AC←MBR`, flags, `STATE←F` |
| 12 | **Operaciones de máquina BLUE y qué hace cada una** | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] | 16 opcodes: LDA, STA, ADD, SUB, AND, OR, XOR, NOT, JMP, JZ, JC, IN, OUT, NOP, HLT (+1). Recorrer la tabla diciendo la microoperación de cada una |

## Preguntas que se desprenden de los TPs (cayeron o pueden caer)
El modelo no las enumera, pero están **explícitas** en los trabajamientos prácticos de la cátedra; si la mesa
abre cualquiera de estos temas, esto es lo que hay que decir.

| Tema | Nota | Respuesta mínima | TP |
|---|---|---|---|
| **BLUE vs BLUE indexada** | [[BLUE vs BLUE indexada — qué cambia y por qué]] | 16 vs 32 opcodes · 4096 vs 65 536 celdas · 4+12 (1 palabra) vs 5+2+9+16 (2 palabras) · 1 vs 4 modos · +RIF, RID, RB, Σ, W, X | apuntes U5 |
| **LDA indexada (24 pulsos)** | [[Ciclo de LDA indexada (los 24 pulsos)]] | 3 ciclos de 8: búsqueda + traer el campo de dirección y sumar el índice + ir al operando. Directo 24 · indirecto 32 | apuntes U5 |
| **Cómo se implementa la UC** | [[Cómo se implementa la Unidad de Control]] | Cableada: decodificador 1→16 + compuertas `estado · pulso · instrucción` unidas con OR (`REF`, `ARITH`, `DTA`). Microprogramada: memoria de control, microinstrucción, PLA, secuenciador | blue.pdf / U6 |
| **Registros base e índice** | [[Registros base e índice]] | Índice: lo maneja el programador, se suma sólo en los modos 2/3, sirve para recorrer arreglos. Base: lo maneja el sistema, se suma siempre, sirve para reubicar | apuntes U5 |
| **Conversión de biestables** | [[Conversión entre biestables (RS, JK, D, T)]] | RS→JK: `S = J·Q̄`, `R = K·Q` (Karnaugh). JK→D: `D = J·Q̄ + K̄·Q`. T: `J = K = T` | TP8 / TP9 |
|---|---|---|---|
| **Buses**: definición y tipos | [[Estructura básica de un computador]] | "Vía que conecta 2+ dispositivos; todos reciben." Datos (bidireccional, ancho = palabra), direcciones (unidireccional, ancho = capacidad de memoria) y control (lectura/escritura, petición/cesión de bus, interrupción) | [[TP14 Buses]] |
| **Espacio de direccionamiento y CodOp** | [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] | `celdas = memoria / tamaño de celda`; `bits de dirección = log₂(celdas)`; `bits de CodOp = palabra − dirección`. Si da negativo, **hay que agrandar la celda** | [[TP17 Formato básico de instrucciones]] + [[TP18 Direccionamiento de memoria]] |
| **IAS y el formato de 40 bits** | [[Estructura básica de un computador]] | Instrucción de **20 bits en dos mitades de 8+12**: una operación y una dirección por mitad; palabra de 40 bits = 2 instrucciones | [[TP15 Arquitectura de Von Neumann (IAS)]] |
| **Lenguaje máquina y clasificación de instrucciones** | [[Lenguaje máquina y clasificación de instrucciones]] | Código directamente ejecutable; se clasifican por **función** (transferencia, aritméticas, lógicas, control, E/S) y por **formato/nº de operandos** | [[TP20 Lenguaje máquina]] |
| **Componentes internos del equipo** | [[Estructura básica de un computador]] | CPU (UC, ALU, registros), memoria, buses, E/S, reloj, fuentes; el "Speccy" del TP como ejemplo de arquitectura completa | [[TP13 Componentes internos]] |
| **RAM vs ROM (cuadro)** | [[Memoria ROM y sus tipos]] | RAM: volátil, lectura/escritura, rápida. ROM: no volátil, sólo lectura, para firmware y memoria de control | [[TP12 Memoria principal]] |
| **Registros de corrimiento** | [[Registros]] | PIPO (carga paralela), SISO (serie puro), SIPO (entra serie, sale paralelo), PISO (entra paralelo, sale serie) | [[TP10 Registros PIPO y SISO]] + [[TP11 Registros SIPO y PISO]] |
| **Codificadores** | [[Codificador]] | Inverso del decodificador: `2ⁿ` entradas → `n` salidas; una OR por bit | [[TP7 Codificadores y multiplexores]] |

## Prácticas (se resuelven en el pizarrón)
| # | Práctica | Nota | Qué hay que entregar |
|---|---|---|---|
| 1 | **Sumador completo** | [[Sumador completo]] | Tabla de verdad (8 filas), funciones simplificadas y gráfico |
| 2 | **Decodificador** | [[Decodificador]] | Definición, tabla 2→4, funciones por mintérmino, gráfico |
| 3 | **Demultiplexor** | [[Demultiplexor]] | Tabla 1→4, funciones `Yi = D·sel`, gráfico, diferencia con el decodificador |
| 4 | **Multiplexor** | [[Multiplexor]] | Tabla 4→1, ecuación SOP, gráfico, uso en el bus |
| 5 | **Álgebra de Boole: definición, 3 postulados, DeMorgan** | [[Álgebra de Boole — postulados y teoremas]] + [[Leyes de DeMorgan]] | Definición, tres postulados, las dos leyes de DeMorgan demostradas por tabla |
| 6 | **Conjunto de instrucciones + registro de instrucción + 3 ejemplos** | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] + [[Programar en BLUE — ejemplos]] | Tabla de opcodes, rol del IR, y 3 instrucciones ensambladas y explicadas |
| 7 | **Celda elemental y caché** | [[Celda elemental de memoria]] + [[Memoria caché]] | Celda de 1 bit + mapeos/asociatividad/escritura de la caché |

## Temas del plan que pueden caer "de arrastre"
- [[Memoria virtual y administración de memoria]] · [[Memoria auxiliar y memoria asociativa]]
- [[Unidad de control cableada y microprogramada]]
- [[Técnicas para aumentar la velocidad]] · [[Paralelismo y procesamiento vectorial]] · [[Hardware aritmético (resumen)]]
- [[Registros]] · [[Contadores]] · [[Codificador]] · [[Jerarquía de memorias]]

## Plan de acción de la última semana
1. Respondé en voz alta las **8 principales** mirando sólo la columna "respuesta mínima".
2. Hacé las **7 prácticas** en hoja en blanco, cronometradas (10 min cada una).
3. Pasá por [[Autoevaluación]] y volvé a las notas de lo que falles.
4. El día previo: [[Guion de respuestas — preguntas principales]] + una leída a
   [[04 Resumen integrador de la materia]].
5. Si queda tiempo muerto: [[00 Índice de TPs y qué aporta cada uno]] sirve de repaso rápido de los 20 TPs.
