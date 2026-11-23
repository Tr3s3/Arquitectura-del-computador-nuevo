---
tipo: guia
---
# Fuentes y qué aporta cada una

> [!abstract] Para qué sirve esta nota
> Para saber **de dónde sale cada dato** de la bóveda y **qué hacer si la mesa pregunta "¿esto de dónde lo sacaste?"**. En el final, citar la fuente correcta (apunte, TP, libro) suma tanto como la respuesta.

## Material entregado por la cátedra

| Fuente | Qué es | Qué aporta a la bóveda |
|---|---|---|
| **`blue.pdf`** | Capítulo *"Una máquina elemental"* de **Caxton Foster, *Computer Architecture*** (el apunte base de la cátedra) | **La fuente primaria de todo el final**: las 16 instrucciones en octal, los 8 pulsos del ciclo de búsqueda, las tablas de CP1-CP8 por instrucción, los biestables RUN/STATE/TRA, el árbol de decodificación, las compuertas de la UC, la E/S con TRA y R |
| **`apuntes-arquitectura de computadores.pdf`** | Apuntes de la cátedra, **Unidades 1 a 5** (111 páginas) | Formatos de instrucción, modos de direccionamiento, **BLUE indexada completa** (RIF, RID, RB, sumador de direcciones, formato de 5+2+9+16), **los ciclos de LDA 0/1/2/3 y de INI/ENI**, el **sistema de interrupciones** (SI, IRQ, estados F/E/I, SKF, EMR, RTI, vectorizadas), el **8088** y su UC microprogramada |
| **`Arqui Matriz.jpg`** | La **matriz del final** con las 3 tandas y el peso de cada tema | El orden y el peso real de estudio: ver [[00 Matriz del final — las 3 tandas]] |
| **`Resumen final arqui.pdf`** y **`2do intento FINAL ARQUITECTURA.pdf`** | Resúmenes de alumnos que siguen los apuntes | Redacción "de examen" de memorias, celda elemental, RAM 8×3, caché, pipeline, CISC/RISC, interrupciones; sirven para ver **cómo se contesta**, no como fuente de verdad |
| **`RESUMEN ARQUI FINAL SAID.pdf`** (44 p.) | Resumen de alumno que cubre **U1 a U5**, con 68 capturas de clase | Organización de la cátedra en 5 unidades, la **consola de la BLUE** (llaves y pulsadores), **punto fijo 15 + signo**, **SRAM 1024×1 (2102)**, tipos de acceso a memoria. Comparación completa: [[08 Comparación con el resumen de Said (qué agregarle)]] |
| **`memorias.pdf`** | Material de Dispositivos Electrónicos (Tema 7: memorias semiconductoras) | Detalle de **celdas ROM (diodo/transistor/MOS)**, SRAM vs DRAM, refresco, arquitectura básica de RAM, tiempos de acceso |
| **Trabajos prácticos TP1–TP21** | Las consignas reales de la cátedra | Qué se pide exactamente en cada tema y con qué notación: ver [[00 Índice de TPs y qué aporta cada uno]] |
| **`TP21-intro-al-emu8086.pdf`** | Introducción al emulador emu8086 | Programación en ensamblador del 8086: ver [[El 8086 como CPU convencional (TP21)]] |
| **`El_manual_del_Microprocesador.pdf`** | Manual divulgativo del microprocesador y la PC | Contexto de hardware real (encapsulados, zócalos, chipsets) para el ítem "componentes internos de la computadora" |
| **`plan de estudio.txt`** | Programa de las 10 unidades | El orden "oficial" de la materia: [[02 Plan de estudio — las 10 unidades]] |
| **`TEMAS FINAL.docx`** | Modelo de final (8 principales, 12 secundarias, 7 prácticas) | La lista original de temas; ver [[Banco de preguntas del final]] |

> [!warning] Dos PDF (`Resumen2-20pag`, `Resumen3-13pags`) son **imágenes escaneadas** (no tienen texto
> extraíble). No se usaron porque su contenido está cubierto por los otros resúmenes y por los apuntes. Si querés que los incorpore, pasalos por OCR o contame qué tienen de distinto.

## Cómo se resolvieron los conflictos entre fuentes
Cuando dos fuentes no coincidían, se aplicó este criterio (y la bóveda lo deja anotado con `> [!warning]`):

| Conflicto | Qué dice cada fuente | Qué quedó en la bóveda |
|---|---|---|
| **Códigos de operación** | El **apunte (Foster)** usa octal (`00` HLT, `01` ADD, `06` LDA, `07` STA, `12` JMP…). El **simulador del TP16** usa decimal (`1` cargar, `5` sumar, `2`/`3` almacenar, `C` parar) | Las dos, aclaradas; la tabla oficial es la **octal** |
| **Pulsos de la LDA** | Algunos resúmenes cuentan "8 + 16 a dos pulsos por microorden". El apunte cuenta **ciclos de máquina de 8** | **BLUE base 16 · BLUE indexada 24** (3 ciclos), como el apunte |
| **"7 u 8 pulsos"** | La búsqueda termina en CP7; el ciclo tiene 8 | 7 pasos; el 8.º era la **reescritura de la memoria de ferrita** y hoy se usa para ejecutar |
| **Dispositivos de E/S de la BLUE** | Un resumen contaba **8 bits ⇒ 256** dispositivos; el apunte de Foster dice *"IR 5-0 a las líneas de selección"* ⇒ **6 bits = 64** | **64 dispositivos** (dato de 8 bits); corregido en [[4.2.1 Especificación, registros y 4096x16]] |
| **RAM "8×3" vs "3×8"** | Apuntes: 8×3 · Matriz del final: 3×8 | El mismo circuito: **8 posiciones de 3 bits** = 24 bits |
| **Interrupciones** | La BLUE de Foster **no tiene** interrupciones | Se estudian las que **agrega la cátedra** sobre la BLUE indexada |
| **TP5: `1101 + 0111`** | El TP imprime `1 1100` | Es `1 0100` (20): error de tipeo del TP (ver [[TP5 Sumadores]]) |
| **TP18: 1 GB / 4 B** | El PDF dice 2²⁷ celdas | Son **2²⁸** celdas ⇒ 28 bits de dirección (ver [[TP18 Direccionamiento de memoria]]) |

## Qué NO está en la bóveda (todavía)

- Microprogramación **en detalle** de una máquina didáctica completa (sí está el concepto, el formato de microinstrucción y el ejemplo del 8088: [[Cómo se implementa la Unidad de Control]]).

- El **8086 a nivel de instrucciones** más allá de lo que pide el TP21.

- Los dos resúmenes escaneados.

## Relacionado
[[00 Cómo usar esta bóveda]] · [[00 Matriz del final — las 3 tandas]] · [[00 Índice de TPs y qué aporta cada uno]] · [[04 Resumen integrador de la materia]]
