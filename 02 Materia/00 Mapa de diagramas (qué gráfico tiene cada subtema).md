---
tipo: indice
---
# Mapa de diagramas: qué gráfico tiene cada subtema

> [!abstract] Qué es esta nota
> Los **107 subtemas** de `02 Materia/` con los gráficos que trae cada uno: el **diagrama propio** (dibujado en SVG para esta bóveda), la **figura del libro** copiada de la bibliografía y la **figura de clase** sacada del resumen de Said. En total: **100 diagramas propios**, **132 figuras de libro** (Quiroga y Stallings) y **15 figuras de clase**, en **99 de los 107** subtemas: los 8 que no tienen figura externa son temas que no están ni en la bibliografía ni en el resumen, y quedan con el diagrama propio.

> [!tip] Cómo usarlo
> 1. Elegí la unidad que estás estudiando.
> 2. El **diagrama propio** es el que conviene reproducir a mano (está simplificado a lo que se pregunta).
> 3. La **figura del libro** es la fuente: sirve para ver el detalle real y para citar de dónde sale.
> 4. La **figura de clase** (si la hay) es la que se parece al pizarrón: el esquema del profesor y la tabla del
>    TP. Va después de la del libro, en el mismo subtema.

## Índice

1. [[#Unidad 1 — Circuitos de lógica digital]]

2. [[#Unidad 2 — Memorias y circuitos secuenciales]]

3. [[#Unidad 3 — Transferencia de registros y microoperaciones]]

4. [[#Unidad 4 — Organización y diseño básico]]

5. [[#Unidad 5 — Programación básica y CPU convencional]]

6. [[#Unidad 6 — Control microprogramado]]

7. [[#Unidad 7 — CPU y arquitecturas]]

8. [[#Unidad 8 — Paralelismo]]

9. [[#Unidad 9 — Hardware aritmético]]

10. [[#Unidad 10 — Entrada y Salida]]

---

## Unidad 1 — Circuitos de lógica digital

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[1.1.1 Compuerta AND, OR y NOT]] | `compuertas` | Q 5.2 |
| [[1.1.2 NAND, NOR, XOR y XNOR]] | `compuertas_nand_nor_xor` | Q 5.6 + Q 5.7 + Q 5.4 |
| [[1.1.3 Compuertas universales]] | `nand_universal` | Q 5.10 |
| [[1.2.1 Postulados, dualidad y teoremas]] | `dualidad_teoremas` | Q 5.12 |
| [[1.2.2 Leyes de DeMorgan]] | `demorgan_circuitos` | Q 5.8 + Q 5.9 |
| [[1.2.3 Simplificación analítica]] | `simplificacion_compuertas` | Q 6.8 |
| [[1.3.1 Mintérminos y maxtérminos]] | `mintterminos_canonica` | Q 6.11 |
| [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]] | `karnaugh_3var` | Q Karnaugh 2 y 3 var |
| [[1.3.3 Don't care y criterios de agrupación]] | `karnaugh_dontcare` | Q 6.7 |
| [[1.4.1 Decodificador]] | `decodificador_2x4` · `decodificador_3x8` | — |
| [[1.4.2 Codificador]] | `codificador_8x3` | Q 6.10 |
| [[1.4.3 Multiplexor]] | `mux_4x1` | Q 6.20 + Q 6.18 |
| [[1.4.4 Demultiplexor]] | `demux_1x4` | Q 6.19 |
| [[1.5.1 Semisumador y sumador completo]] | `semisumador` · `sumador_completo` | `quiroga-f5-17` |
| [[1.5.2 Sumador de n bits y resta en complemento a 2]] | `sumador_n_bits` | Q 5.19 |
| [[1.6.1 Códigos ponderados y no ponderados]] | `codigos_ponderados` | Q 3.5 + Q 3.6 |
| [[1.6.2 Códigos continuos y cíclicos]] | `codigos_continuos` | — |

---

## Unidad 2 — Memorias y circuitos secuenciales

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[2.1.1 Biestable RS (NOR y NAND)]] | `flipflops` | Q 6.27 |
| [[2.1.2 Flip-flops D y T]] | `flipflop_d_t_tiempos` | Q 6.34 |
| [[2.1.3 Flip-flop JK y ecuaciones características]] | `flipflop_jk_ecuaciones` | Q 6.30 |
| [[2.1.4 Conversión entre biestables]] | `flipflops` | Q 6.31 |
| [[2.2.1 Registros PIPO y SISO]] | `registros_pipo_siso` | Q 6.35 |
| [[2.2.2 Registros SIPO y PISO]] | `registros_sipo_piso` | — |
| [[2.2.3 Contadores binarios y módulo N]] | `contadores_modulo` | Q 6.36 |
| [[2.3.1 Celda elemental de memoria]] | `celda_memoria` | Q 9.4 |
| [[2.3.2 SRAM y DRAM]] | `sram_dram_refresco` | S 5.3 |
| [[2.3.3 Matriz, expansión y RAM 8x3]] | `ram_8x3` | S 5.5 |
| [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]] | `deteccion_errores` | S 5.11 |
| [[2.4.1 ROM = decodificador + OR]] | `rom_decodificador_or` | Q 6.23 |
| [[2.4.2 PROM, EPROM, EEPROM y Flash]] | `prom_flash_celda` | — |
| [[2.5.1 Jerarquía y localidad]] | `jerarquia_memorias` | S 4.1 |
| [[2.5.2 Caché: mapeos y políticas]] | `cache_mapeos` | S 4.8 + S 4.12 |
| [[2.5.3 AMAT y cálculo de mejora]] | `amat_cache` | S 4.5 |
| [[2.6.1 Memoria virtual y paginación]] | `memoria_virtual_tlb` | Q 14.1 + S 8.18 |
| [[2.6.2 Memoria auxiliar y memoria asociativa]] | `memoria_asociativa_cam` | S 8.19 |
| [[2.7.1 Bits de dirección igual a log2 de celdas]] | `bits_direccion` | Q 7.7 |
| [[2.7.2 CodOp vs campo de dirección]] | `codop_vs_direccion` | Q 7.9 |

---

## Unidad 3 — Transferencia de registros y microoperaciones

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[3.1.1 Notación de transferencia entre registros]] | `microoperaciones_bus` | S 16.5 |
| [[3.1.2 Bus único y buffers de 3 estados]] | `buffer_tres_estados` | Q 5.15 |
| [[3.1.3 Buses de datos, de direcciones y de control]] | `buses_interno_externo` | S 3.16 + S 3.19 |
| [[3.2.1 Estructura, G-P y señales de selección]] | `alu_estructura` | Q 7.1 + S 9.1 |
| [[3.2.2 Operaciones aritméticas, lógicas y flags]] | `flags_alu` | Q 7.25 |
| [[3.3.1 AC, PC, IR, MAR y MBR]] | `registros_cpu_mar` | S 1.5 |
| [[3.3.2 Base, índice, puntero de pila y estado]] | `registros_cpu_mar` | S 16.6 |

---

## Unidad 4 — Organización y diseño básico

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[4.1.1 Unidades funcionales de una computadora]] | `estructura_basica` | S 1.1 |
| [[4.1.2 IAS y el programa almacenado]] | `ias_estructura` | S 2.1 + S 2.4 |
| [[4.2.1 Especificación, registros y 4096x16]] | `blue_flujo` | S 3.5 |
| [[4.2.2 Los 16 opcodes octales]] | `blue_opcodes` | Q 7.6 |
| [[4.2.3 Programar en BLUE]] | `blue_programa_ram` | Q 8.2 |
| [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] | `ciclo_maquina` | S 3.3 + S 3.6 |
| [[4.3.2 Búsqueda, los 8 pulsos]] | `busqueda_pulsos` | Q 7.10 |
| [[4.3.3 Ejecución instrucción por instrucción]] | `lda24_pulsos` | Q 7.13 + Q 7.14 |
| [[4.4.1 Funciones y señales de control]] | `uc_cableada` | Q 7.11 + Q 7.21 |
| [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] | `estado_pulso_1_16` | S 16.10 |

---

## Unidad 5 — Programación básica y CPU convencional

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[5.1.1 Instrucción, opcode y operandos]] | `instruccion_partes` | S 11.8 |
| [[5.1.2 Clasificación de las instrucciones]] | `clasificacion_instrucciones` | S 10.6 |
| [[5.1.3 Registros de la CPU]] | `registros_cpu_mar` | S 1.5 |
| [[5.2.1 Los 4 formatos y el campo único de dirección]] | `formatos_instruccion` | S 10.15 + S 13.8 |
| [[5.2.2 Cálculo de CodOp según el tamaño de memoria]] | `codop_vs_direccion` | S 11.6 |
| [[5.3.1 Los 7 modos]] | `modos_direccionamiento` | S 11.1 |
| [[5.3.2 Dirección efectiva y costo en accesos]] | `ea_calculo` | S 11.2 |
| [[5.4.1 RIF, RID y RB]] | `rif_rid_rb` | — |
| [[5.4.2 Modificador de 2 bits y los 24 pulsos]] | `lda24_pulsos` | Q 7.15 |
| [[5.5.1 IRQ, SI y CP8]] | `irq_logica` | S 7.6 + S 3.9 |
| [[5.5.2 Máscara, pila y RTI]] | `pila_rti` | S 10.8 |
| [[5.6.1 BIU, EU y segmentación]] | `biu_eu_cola` | S 12.2 |
| [[5.6.2 La pila y el registro SP]] | `pila_rti` | S 10.13 |

---

## Unidad 6 — Control microprogramado

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[6.1.1 Circuito, compuertas y señales]] | `uc_cableada` | S 16.4 |
| [[6.2.1 Memoria de control y microinstrucción]] | `uc_microprogramada` | S 17.2 + S 17.5 |
| [[6.2.2 Secuenciamiento y microPC]] | `micropc_flujo` | S 17.6 + S 17.7 |
| [[6.3.1 Cableada vs microprogramada]] | `cableada_vs_micro` | S 17.3 |
| [[6.3.2 El 8088, ROM de control 504x21]] | `rom_control_8088` | S 17.14 |

---

## Unidad 7 — CPU y arquitecturas

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[7.1.1 Etapas y diagrama en escalera]] | `pipeline` | S 12.10 + S 12.12 |
| [[7.1.2 Hazards y sus soluciones]] | `pipeline_hazards` | S 12.11 |
| [[7.1.3 Cálculo de speedup y límites]] | `speedup_limites` | S 14.5 |
| [[7.2.1 Superscalar, superpipeline, SMT y multicore]] | `anchura_superscalar_smt` | S 14.15 |
| [[7.2.2 Caché y predicción de saltos]] | `prediccion_saltos` | S 12.17 + S 12.16 |
| [[7.3.1 Tabla comparativa y ejemplos]] | `cisc_risc` | S 14.8 |
| [[7.3.2 UC cableada vs microprogramada y load-store]] | `load_store_risc` | S 12.15 |
| [[7.4.1 von Neumann vs Harvard]] | `von_neumann_harvard` | Q 1.3 |
| [[7.4.2 Buses internos y externos]] | `buses_interno_externo` | S 3.17 |

---

## Unidad 8 — Paralelismo

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[8.1.1 Etapas segmentadas y suma de vectores]] | `pipeline_aritmetico` | S 18.13 + S 18.15 |
| [[8.1.2 Encadenamiento y speedup]] | `encadenamiento` | S 18.19 |
| [[8.2.1 SIMD, registros vectoriales y GPU]] | `simd_registros` | — |
| [[8.2.2 Flynn, arreglos SIMD y conectados]] | `flynn` | S 18.4 |
| [[8.2.3 Multiplicación de matrices]] | `matriz_simd` | — |
| [[8.3.1 Bancos de memoria y ancho de banda]] | `memoria_entrelazada` | S 5.12 |
| [[8.3.2 Patrón de entrelazado y conflictos de banco]] | `conflictos_banco` | S 5.14 |
| [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] | `amdahl_grafico` | S 18.7 + S 18.5 |
| [[8.4.2 Monousuario vs multiusuario]] | `multiusuario_escalabilidad` | S 18.12 + S 18.2 |

---

## Unidad 9 — Hardware aritmético

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[9.1.1 Complemento a 2 y desbordamiento]] | `complemento2_rango` | S 9.3 + S 9.5 |
| [[9.1.2 Acarreo anticipado (G y P)]] | `sumador_acarreo_anticipado` | Q 4.1 + Q 5.16 |
| [[9.2.1 Sumas y desplazamientos]] | `multiplicacion_registros` | S 9.7 + S 9.10 |
| [[9.2.2 Algoritmo de Booth]] | `booth_traza` | S 9.12 + S 9.13 |
| [[9.2.3 Arreglo multiplicador]] | `arreglo_multiplicador` | — |
| [[9.3.1 Restauración y no restauración]] | `division_restauracion` | S 9.15 + S 9.16 |
| [[9.3.2 Sobreflujo y división con signo]] | `division_signo` | — |
| [[9.4.1 Formato, normalización y operaciones]] | `punto_flotante_normalizacion` | S 9.23 + S 9.24 |
| [[9.4.2 IEEE 754]] | `ieee754_campos` | S 10.4 |
| [[9.5.1 Suma decimal corregida]] | `bcd_correccion` | — |

---

## Unidad 10 — Entrada y Salida

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[10.1.1 Polling y sus límites]] | `es_modos` | S 7.1 |
| [[10.1.2 Puertos, interfaces y handshake]] | `handshake_tiempos` | S 7.3 + S 7.10 |
| [[10.2.1 Mecanismo completo]] | `es_modos` | S 3.12 |
| [[10.2.2 Interrupciones vectorizadas y prioridad]] | `vector_prioridad` | S 7.8 + S 3.14 |
| [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] | `dma` | S 7.11 + S 7.12 |
| [[10.4.1 Discos, SSD y latencias]] | `disco_latencias` | S 6.2 + S 6.6 |
| [[10.4.2 Interfaces serie y paralelo]] | `serie_paralelo_skew` | S 5.13 |

---

## Figuras de clase (resumen de Said)

Las **15 figuras** del resumen de cátedra que aportaban algo que ni los libros ni el diagrama propio daban: el árbol de clasificación de biestables, el panel frontal de la BLUE, la tabla de los 16 nombres de instrucciones, el esquema de E/S con sus 64 dispositivos y toda la unidad de la BLUE indexada (formato, modos, ciclos y la comparación con la original). Están en `assets/catedra-said-*.png`, con la página del PDF en el pie.

| Subtema | Figura de clase | Qué aporta |
|---|---|---|
| [[1.4.3 Multiplexor]] | `catedra-said-mux-integrado` | el MUX 4:1 dibujado como integrado: cuatro canales, dos selectores y una salida |
| [[2.1.1 Biestable RS (NOR y NAND)]] | `catedra-said-clasificacion-biestables` | el árbol asíncronos / sincrónicos que ordena toda la unidad 2 |
| [[4.1.2 IAS y el programa almacenado]] | `catedra-said-formato-palabra-ias` | los dos formatos de la palabra de 40 bits: dato contra instrucción |
| [[4.2.1 Especificación, registros y 4096x16]] | `catedra-said-panel-frontal-blue` | la consola completa con sus seis pulsadores y sus 16 llaves |
| [[4.2.2 Los 16 opcodes octales]] | `catedra-said-formato-ri` · `catedra-said-16-instrucciones-nombres` | el corte 15..12 / 11..0 y los 16 nombres en castellano |
| [[4.3.3 Ejecución instrucción por instrucción]] | `catedra-said-es-blue` | la E/S de la BLUE: 8 líneas de dato, 6 de selección y 64 dispositivos |
| [[5.2.1 Los 4 formatos y el campo único de dirección]] | `catedra-said-formatos-comparacion` | qué elimina cada formato al bajar de 4 a 1 dirección |
| [[5.4.1 RIF, RID y RB]] | `catedra-said-blue-indexada` | el plano completo: los tres registros, el sumador y los dos decodificadores |
| [[5.4.2 Modificador de 2 bits y los 24 pulsos]] | `catedra-said-formato-indexada` · `catedra-said-modos-modificador` · `catedra-said-lda3-ejecucion` · `catedra-said-ciclos-por-modo` · `catedra-said-original-vs-indexada` | las dos palabras, los cuatro modos, los ciclos por modo y la comparación con la original |
| [[7.1.1 Etapas y diagrama en escalera]] | `catedra-said-etapas-pipeline` | las cinco etapas IF-ID-EX-MEM-WB con su función |

> [!note] Las 53 que no se usaron
> De las **68 imágenes** del resumen, **15** quedaron en la bóveda y **53** no: son **capturas de texto** (enunciados, listas, definiciones) o **tablas y dibujos que ya estaban mejor resueltos** en el diagrama propio del subtema (compuertas, DeMorgan, semisumador, sumador completo, flip-flops, pirámide de memorias, mapeos de caché, buses, pulsos de la búsqueda, los cuatro formatos en bloque, CISC contra RISC). Una captura de 500 px no mejora un SVG que dice lo mismo **y** está explicado en el texto de al lado, así que **no se borró ningún diagrama propio**: la comparación está archivada en el detalle de M4, en [[07 Plan de mejoras pendientes]].

## Cómo se generan los dos tipos

| Archivo | Qué hace |
|---|---|
| `tools/diagramas.py` | los 34 diagramas propios de la primera tanda |
| `tools/diagramas_2.py` | el resto: uno por subtema (incluye códigos y errores) |
| `tools/extraer_figuras.py` | **extrae las figuras de un PDF** buscando el epígrafe `Fig. N.N` y recortando el bloque de contenido que está encima |
| `python3 diagramas_2.py` | regenera los SVG propios en `assets/` |

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Figuras de los libros (índice)]] · [[00 Cómo usar esta bóveda]]
