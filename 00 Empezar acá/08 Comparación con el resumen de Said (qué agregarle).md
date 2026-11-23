---
tipo: informe
---
# Comparación con el resumen de Said — qué se le podía agregar

> [!abstract] Qué es esta nota
> Comparé el resumen **«RESUMEN ARQUI FINAL SAID»** (44 páginas, 8.218 palabras, 68 imágenes) contra toda la bóveda,
> punto por punto. Resultado: **cubría las unidades 1 a 5** y de esos temas la bóveda ya tenía **35 de 40 puntos**.
> De los 5 restantes, **4 se agregaron** y **1 destapó un error** que la bóveda tenía y ya está corregido.
> Todo lo que se cambió está al final, con el archivo donde quedó.

## Qué trae el resumen de Said

| Dato | Valor |
|---|---|
| Páginas / palabras | 44 / 8.218 |
| Imágenes | **68** (circuitos, tablas de verdad, ciclos de máquina de la BLUE) |
| Unidades que cubre | **1, 2, 3, 4 y 5** — no llega a la 6 (microprogramación), 7 (pipeline/hazards), 8 (paralelismo), 9 (aritmética) ni 10 (E/S) |
| Estilo | definiciones cortas + tabla/figura, sin ejemplos resueltos ni cuentas |

**Cómo se numeran las unidades (ojo, no coincide con el plan de 10):**

| Said | La bóveda |
|---|---|
| Unidad 1 — Circuitos lógicos | Unidad 1 (`1.1` a `1.6`) |
| Unidad 2 — Memorias (biestables, registros, contadores, **y también** decodificadores/MUX) | Unidad 2 (`2.1` a `2.7`) + los combinacionales en **1.4** |
| Unidad 3 — Memorias electrónicas (RAM, ROM, celda, DRAM) | Unidad 2 (`2.3` a `2.4`) |
| Unidad 4 — «la gloriosa»: estructura, IAS, BLUE | Unidades **3 y 4** |
| Unidad 5 — Formatos, direccionamiento, BLUE indexada, pipeline, CISC/RISC | Unidad **5** (`5.1` a `5.4`) + pipeline y CISC/RISC en **7.1** y **7.3** |

> [!tip] Para el oral
> Si el profesor nombra "Unidad 3" o "la gloriosa", sabés a qué carpeta ir. El contenido es el mismo; cambia el corte.

## Punto por punto: los 40 temas que cubre Said

**Cubiertos en la bóveda (35).** Cada fila se verificó buscando el concepto, no la palabra.

| Tema del resumen | Dónde está en la bóveda | Estado |
|---|---|---|
| Bit, byte, nibble; sistema binario | [[1.1.1 Compuerta AND, OR y NOT]] · [[Glosario — Unidad 1]] | ✅ |
| Compuertas, postulados, dualidad, De Morgan | [[1.2.1 Postulados, dualidad y teoremas]] · [[1.2.2 Leyes de DeMorgan]] | ✅ |
| Semisumador y sumador completo (tabla + circuito) | [[1.5.1 Semisumador y sumador completo]] · [[1.5.2 Sumador de n bits y resta en complemento a 2]] | ✅ |
| Biestables: asíncronos vs síncronos, por nivel vs por flanco | [[2.1.1 Biestable RS (NOR y NAND)]] · [[2.1.2 Flip-flops D y T]] · [[2.1.3 Flip-flop JK y ecuaciones características]] | ✅ |
| Conversión entre biestables (no está en Said, sí en la bóveda) | [[2.1.4 Conversión entre biestables]] | ✅ |
| Decodificador, codificador, MUX, DEMUX | [[1.4.1 Decodificador]] · [[1.4.2 Codificador]] · [[1.4.3 Multiplexor]] · [[1.4.4 Demultiplexor]] | ✅ |
| Registros SISO, PIPO, SIPO, PISO | [[2.2.1 Registros PIPO y SISO]] · [[2.2.2 Registros SIPO y PISO]] | ✅ |
| Contadores sincrónicos y asincrónicos, módulo N | [[2.2.3 Contadores binarios y módulo N]] | ✅ |
| RAM/ROM: volátil, no volátil, lectura/escritura | [[2.3.2 SRAM y DRAM]] · [[2.4.1 ROM = decodificador + OR]] · [[2.4.2 PROM, EPROM, EEPROM y Flash]] | ✅ |
| Celda elemental, línea de selección, `L/E`, buffer triestado | [[2.3.1 Celda elemental de memoria]] | ✅ |
| RAM didáctica con sus 6 partes (matriz, decodificador, buffers, `C/S`) | [[2.3.3 Matriz, expansión y RAM 8x3]] | ✅ |
| DRAM: capacitor + MOSFET, refresco | [[2.3.2 SRAM y DRAM]] | ✅ |
| Los 4 elementos de una computadora; funciones de la CPU | [[4.1.1 Unidades funcionales de una computadora]] | ✅ |
| Pasos de la ejecución de una instrucción | [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] · [[4.3.2 Búsqueda, los 8 pulsos]] | ✅ |
| UC: decodificador, generador de señales, RI; registros | [[3.3.1 AC, PC, IR, MAR y MBR]] · [[4.4.1 Funciones y señales de control]] | ✅ |
| ALU: acumulador, temporales, registro de estado | [[3.2.1 Estructura, G-P y señales de selección]] · [[3.2.2 Operaciones aritméticas, lógicas y flags]] | ✅ |
| RISC y CISC (tabla comparativa) | [[7.3.1 Tabla comparativa y ejemplos]] · [[7.3.2 UC cableada vs microprogramada y load-store]] | ✅ |
| Tres buses; `READ`, `WRITE`, `INT`, `RESET` | [[3.1.3 Buses de datos, de direcciones y de control]] · [[4.4.1 Funciones y señales de control]] | ✅ |
| von Neumann: principios, memoria única, ciclo | [[7.4.1 von Neumann vs Harvard]] · [[4.1.2 IAS y el programa almacenado]] | ✅ |
| IAS: 1000 × 40, instrucción 8 + 12, AC y MQ | [[4.1.2 IAS y el programa almacenado]] | ✅ |
| BLUE: 4096 × 16, bus único, instrucción de 16 bits | [[4.2.1 Especificación, registros y 4096x16]] | ✅ |
| BLUE: los 16 opcodes en octal | [[4.2.2 Los 16 opcodes octales]] | ✅ |
| BLUE: registros y sus anchos (PC, MAR, MBR, IR, AC) | [[4.2.1 Especificación, registros y 4096x16]] | ✅ |
| BLUE: flujo de datos y de direcciones (CSA, Deposit, LDA, STA, SRJ, Z e Y) | [[Flujo de información en BLUE (datos y direcciones)]] | ✅ |
| Ciclo de búsqueda pulso por pulso (PC→MAR, PC+1, MBR→IR) | [[4.3.2 Búsqueda, los 8 pulsos]] | ✅ |
| Instrucciones de 1 ciclo y de 2 ciclos | [[4.3.3 Ejecución instrucción por instrucción]] | ✅ |
| E/S de la BLUE: `TRA` y `R`, 6 bits de dispositivo, 8 bits de dato | [[4.3.3 Ejecución instrucción por instrucción]] | ✅ |
| Formato de 4, 3, 2 y 1 dirección (`ADD A,B,C,D`) | [[5.2.1 Los 4 formatos y el campo único de dirección]] | ✅ |
| Modos directo y por registro | [[5.3.1 Los 7 modos]] · [[5.3.2 Dirección efectiva y costo en accesos]] | ✅ |
| BLUE indexada: RIF/RID, 5 bits de CodOp, 16 de dirección, 2 de modificador | [[5.4.1 RIF, RID y RB]] · [[5.4.2 Modificador de 2 bits y los 24 pulsos]] | ✅ |
| Sumador de direcciones y decodificador del modificador | [[5.4.1 RIF, RID y RB]] · [[Cómo se implementa la Unidad de Control]] | ✅ |
| Registro base: lo maneja el Monitor, reubica programas | [[5.4.1 RIF, RID y RB]] · [[Registros base e índice]] | ✅ |
| `INI`, `ENI`, `LIX` y los ciclos de la indexada (24 / 32 pulsos) | [[BLUE indexada (RIF, RID, nuevo formato)]] · [[Ciclo de LDA indexada (los 24 pulsos)]] | ✅ |
| Pipelining (idea y objetivo) | [[7.1.1 Etapas y diagrama en escalera]] · [[7.1.3 Cálculo de speedup y límites]] | ✅ |
| Lenguaje máquina: transferencia, aritméticas, control de flujo | [[5.1.2 Clasificación de las instrucciones]] | ✅ |

**Faltaban (5) → ya agregados o corregidos**

| Tema | Qué pasó |
|---|---|
| **`punto fijo` y «15 bits de magnitud + 1 de signo»** en la BLUE | **agregado** a la tabla de especificación |
| **La consola de la BLUE**: 16 llaves de 3 posiciones, 16 leds, y qué hace cada pulsador (START, STOP, LOAD PC, DEPOSIT, EXAMINE, MASTER CLEAR) | **agregado**: sección `## La consola` + receta para cargar un programa a mano |
| **SRAM 1024 × 1 (Intel 2102)**, el chip de ejemplo | **agregado** con la cuenta de los 10 bits de dirección |
| **Tipo de acceso**: aleatorio, en serie, directo, asociativo | **agregado**: tabla + el aviso de que "RAM" no significa "memoria" |
| **Notación RAM 3×8 vs 8×3** | **agregado** como aviso: es la misma memoria, 8 filas × 3 columnas |

**Y un error de la bóveda que destapó el resumen:** la bóveda decía que `INP`/`OUT` usan *los 8 bits bajos* para
identificar el dispositivo (0 a 255). **Es 6 bits ⇒ 64 dispositivos.** Lo verifiqué en `uploads/blue.pdf`, que dice
literalmente *"Transmite IR 5-0 a través de las líneas de selección de dispositivo"* y *"se pueden conectar más de
64 dispositivos"*. **Corregido** en [[4.2.1 Especificación, registros y 4096x16]].

## Lo que la bóveda tiene y el resumen de Said no

No hace falta agregarlo desde Said (ya está), pero conviene saberlo para no comparar mal los dos materiales:

| Bloque | La bóveda | Said |
|---|---|---|
| Simplificación: mintérminos, Karnaugh, don't care | 4 subtemas + figuras del libro | no lo trata |
| Códigos: BCD, Aiken, exceso 3, Gray, Johnson, paridad, Hamming | 4 subtemas | no lo trata |
| Jerarquía de memoria, caché, AMAT, memoria virtual, TLB | 8 subtemas | no lo trata |
| Interrupciones: `IRQ·SI·CP8`, máscara, prioridad, vector, `RTI` | 4 subtemas | no lo trata |
| Unidad de control **microprogramada**: microPC, secuenciamiento, ROM 504×21 | 5 subtemas | no lo trata |
| Pipeline: hazards, forwarding, stalls, speedup, predicción | 5 subtemas | sólo el concepto |
| Paralelismo: vectorial, SIMD, Flynn, bancos, Amdahl, coherencia | 9 subtemas | no lo trata |
| Aritmética: Booth, división, IEEE 754, BCD corregido | 10 subtemas | no lo trata |
| E/S: polling, handshake, DMA, discos, SSD, interfaces | 7 subtemas | no lo trata (sólo la E/S de la BLUE) |
| Ejemplos resueltos y errores típicos | en los **107** subtemas | no tiene |

## Lo que sí valdría la pena tomar de este resumen

1. **Sus 68 imágenes** son capturas de clase (circuitos y ciclos de la BLUE dibujados por la cátedra). Podrían
   entrar como figuras de cátedra en los 9 subtemas que no tienen figura de libro — es exactamente la **M4** del
   [[07 Plan de mejoras pendientes]].
2. **Su forma de escribir**: definición de tres líneas + tabla + figura. Sirve como molde para la **M7** (ficha de
   una página por unidad).
3. **Nada más**: en contenido, la bóveda lo cubre y lo excede; el valor de este resumen es que confirma **qué
   recorta la cátedra** para el final (U1–U5) y con qué palabras lo dice.

## Relacionado
[[06 Validación de contenido (resúmenes, TPs y claridad)]] · [[07 Plan de mejoras pendientes]] ·
[[05 Fuentes y qué aporta cada una]] · [[01 Mapa de la materia (MOC)]]
