---
tipo: indice
---
# Mapa de diagramas: qué gráfico tiene cada subtema

> [!abstract] Qué es esta nota
> Los **104 subtemas** de `02 Materia/` con los gráficos que trae cada uno: el **diagrama propio**
> (dibujado a mano en SVG para esta bóveda) y la **figura del libro** copiada de la bibliografía.
> En total: **106 diagramas propios** sobre 97 SVG y **99 figuras de libro** (Quiroga y Stallings).

> [!tip] Cómo usarlo
> 1. Elegí la unidad que estás estudiando.
> 2. El **diagrama propio** es el que conviene reproducir a mano (está simplificado a lo que se pregunta).
> 3. La **figura del libro** es la fuente: sirve para ver el detalle real y para citar de dónde sale.
> 4. Si el subtema no te sale de memoria, ése es el que hay que repasar.

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
| [[1.1.1 Compuerta AND, OR y NOT]] | `compuertas` | `quiroga-f5-2` |
| [[1.1.2 NAND, NOR, XOR y XNOR]] | `compuertas_nand_nor_xor` | `quiroga-f5-6` · `quiroga-f5-7` · `quiroga-f5-4` |
| [[1.1.3 Compuertas universales]] | `nand_universal` | `quiroga-f5-10` |
| [[1.2.1 Postulados, dualidad y teoremas]] | `dualidad_teoremas` | — |
| [[1.2.2 Leyes de DeMorgan]] | `demorgan_circuitos` | — |
| [[1.2.3 Simplificación analítica]] | `simplificacion_compuertas` | — |
| [[1.3.1 Mintérminos y maxtérminos]] | `mintterminos_canonica` | — |
| [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]] | `karnaugh_3var` | — |
| [[1.3.3 Don't care y criterios de agrupación]] | `karnaugh_dontcare` | — |
| [[1.4.1 Decodificador]] | `decodificador_2x4` · `decodificador_3x8` | — |
| [[1.4.2 Codificador]] | `codificador_8x3` | — |
| [[1.4.3 Multiplexor]] | `mux_4x1` | — |
| [[1.4.4 Demultiplexor]] | `demux_1x4` | — |
| [[1.5.1 Semisumador y sumador completo]] | `semisumador` · `sumador_completo` | `quiroga-f5-17` |
| [[1.5.2 Sumador de n bits y resta en complemento a 2]] | `sumador_n_bits` | `quiroga-f5-19` |

---

## Unidad 2 — Memorias y circuitos secuenciales

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[2.1.1 Biestable RS (NOR y NAND)]] | `flipflops` | — |
| [[2.1.2 Flip-flops D y T]] | `flipflop_d_t_tiempos` | `quiroga-f6-34` |
| [[2.1.3 Flip-flop JK y ecuaciones características]] | `flipflop_jk_ecuaciones` | `quiroga-f6-30` |
| [[2.1.4 Conversión entre biestables]] | `flipflops` | — |
| [[2.2.1 Registros PIPO y SISO]] | `registros_pipo_siso` | `quiroga-f6-35` |
| [[2.2.2 Registros SIPO y PISO]] | `registros_sipo_piso` | — |
| [[2.2.3 Contadores binarios y módulo N]] | `contadores_modulo` | `quiroga-f6-36` |
| [[2.3.1 Celda elemental de memoria]] | `celda_memoria` | `quiroga-f9-4` |
| [[2.3.2 SRAM y DRAM]] | `sram_dram_refresco` | `stallings-f5-3` |
| [[2.3.3 Matriz, expansión y RAM 8x3]] | `ram_8x3` | `stallings-f5-5` |
| [[2.4.1 ROM = decodificador + OR]] | `rom_decodificador_or` | `quiroga-f6-23` |
| [[2.4.2 PROM, EPROM, EEPROM y Flash]] | `prom_flash_celda` | — |
| [[2.5.1 Jerarquía y localidad]] | `jerarquia_memorias` | `stallings-f4-1` |
| [[2.5.2 Caché: mapeos y políticas]] | `cache_mapeos` | `stallings-f4-8` · `stallings-f4-12` |
| [[2.5.3 AMAT y cálculo de mejora]] | `amat_cache` | `stallings-f4-5` |
| [[2.6.1 Memoria virtual y paginación]] | `memoria_virtual_tlb` | `quiroga-f14-1` · `stallings-f8-18` |
| [[2.6.2 Memoria auxiliar y memoria asociativa]] | `memoria_asociativa_cam` | `stallings-f8-19` |
| [[2.7.1 Bits de dirección igual a log2 de celdas]] | `bits_direccion` | `quiroga-f9-11` |
| [[2.7.2 CodOp vs campo de dirección]] | `codop_vs_direccion` | — |

---

## Unidad 3 — Transferencia de registros y microoperaciones

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[3.1.1 Notación de transferencia entre registros]] | `microoperaciones_bus` | `stallings-f16-5` |
| [[3.1.2 Bus único y buffers de 3 estados]] | `buffer_tres_estados` | `quiroga-f5-15` |
| [[3.1.3 Buses de datos, de direcciones y de control]] | `buses_interno_externo` | `stallings-f3-16` · `stallings-f3-19` |
| [[3.2.1 Estructura, G-P y señales de selección]] | `alu_estructura` | `quiroga-f7-1` · `stallings-f9-1` |
| [[3.2.2 Operaciones aritméticas, lógicas y flags]] | `flags_alu` | `quiroga-f7-25` |
| [[3.3.1 AC, PC, IR, MAR y MBR]] | `registros_cpu_mar` | `stallings-f1-5` |
| [[3.3.2 Base, índice, puntero de pila y estado]] | `registros_cpu_mar` | `stallings-f16-6` |

---

## Unidad 4 — Organización y diseño básico

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[4.1.1 Unidades funcionales de una computadora]] | `estructura_basica` | `stallings-f1-1` |
| [[4.1.2 IAS y el programa almacenado]] | `ias_estructura` | `stallings-f2-1` · `stallings-f2-4` |
| [[4.2.1 Especificación, registros y 4096x16]] | `blue_flujo` | — |
| [[4.2.2 Los 16 opcodes octales]] | `blue_opcodes` | — |
| [[4.2.3 Programar en BLUE]] | `blue_programa_ram` | — |
| [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] | `ciclo_maquina` | `stallings-f3-3` · `stallings-f3-6` |
| [[4.3.2 Búsqueda, los 8 pulsos]] | `busqueda_pulsos` | `quiroga-f7-10` |
| [[4.3.3 Ejecución instrucción por instrucción]] | `lda24_pulsos` | `quiroga-f7-13` · `quiroga-f7-14` |
| [[4.4.1 Funciones y señales de control]] | `uc_cableada` | `quiroga-f7-11` · `quiroga-f7-21` |
| [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] | `estado_pulso_1_16` | `stallings-f16-10` |

---

## Unidad 5 — Programación básica y CPU convencional

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[5.1.1 Instrucción, opcode y operandos]] | `instruccion_partes` | `stallings-f11-8` |
| [[5.1.2 Clasificación de las instrucciones]] | `clasificacion_instrucciones` | — |
| [[5.1.3 Registros de la CPU]] | `registros_cpu_mar` | `stallings-f1-5` |
| [[5.2.1 Los 4 formatos y el campo único de dirección]] | `formatos_instruccion` | — |
| [[5.2.2 Cálculo de CodOp según el tamaño de memoria]] | `codop_vs_direccion` | — |
| [[5.3.1 Los 7 modos]] | `modos_direccionamiento` | `stallings-f11-1` |
| [[5.3.2 Dirección efectiva y costo en accesos]] | `ea_calculo` | `stallings-f11-2` |
| [[5.4.1 RIF, RID y RB]] | `rif_rid_rb` | — |
| [[5.4.2 Modificador de 2 bits y los 24 pulsos]] | `lda24_pulsos` | `quiroga-f7-15` |
| [[5.5.1 IRQ, SI y CP8]] | `irq_logica` | `stallings-f7-6` · `stallings-f3-9` |
| [[5.5.2 Máscara, pila y RTI]] | `pila_rti` | `stallings-f10-8` |
| [[5.6.1 BIU, EU y segmentación]] | `biu_eu_cola` | `stallings-f12-2` |
| [[5.6.2 La pila y el registro SP]] | `pila_rti` | `stallings-f10-13` |

---

## Unidad 6 — Control microprogramado

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[6.1.1 Circuito, compuertas y señales]] | `uc_cableada` | `stallings-f16-4` |
| [[6.2.1 Memoria de control y microinstrucción]] | `uc_microprogramada` | `stallings-f17-2` · `stallings-f17-5` |
| [[6.2.2 Secuenciamiento y microPC]] | `micropc_flujo` | `stallings-f17-6` · `stallings-f17-7` |
| [[6.3.1 Cableada vs microprogramada]] | `cableada_vs_micro` | `stallings-f17-3` |
| [[6.3.2 El 8088, ROM de control 504x21]] | `rom_control_8088` | `stallings-f17-14` |

---

## Unidad 7 — CPU y arquitecturas

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[7.1.1 Etapas y diagrama en escalera]] | `pipeline` | `stallings-f12-10` · `stallings-f12-12` |
| [[7.1.2 Hazards y sus soluciones]] | `pipeline_hazards` | `stallings-f12-11` |
| [[7.1.3 Cálculo de speedup y límites]] | `speedup_limites` | `stallings-f14-5` |
| [[7.2.1 Superscalar, superpipeline, SMT y multicore]] | `anchura_superscalar_smt` | `stallings-f14-15` |
| [[7.2.2 Caché y predicción de saltos]] | `prediccion_saltos` | `stallings-f12-17` · `stallings-f12-16` |
| [[7.3.1 Tabla comparativa y ejemplos]] | `cisc_risc` | `stallings-f14-8` |
| [[7.3.2 UC cableada vs microprogramada y load-store]] | `load_store_risc` | `stallings-f12-15` |
| [[7.4.1 von Neumann vs Harvard]] | `von_neumann_harvard` | — |
| [[7.4.2 Buses internos y externos]] | `buses_interno_externo` | `stallings-f3-17` |

---

## Unidad 8 — Paralelismo

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[8.1.1 Etapas segmentadas y suma de vectores]] | `pipeline_aritmetico` | `stallings-f18-13` · `stallings-f18-15` |
| [[8.1.2 Encadenamiento y speedup]] | `encadenamiento` | `stallings-f18-19` |
| [[8.2.1 SIMD, registros vectoriales y GPU]] | `simd_registros` | — |
| [[8.2.2 Flynn, arreglos SIMD y conectados]] | `flynn` | — |
| [[8.2.3 Multiplicación de matrices]] | `matriz_simd` | — |
| [[8.3.1 Bancos de memoria y ancho de banda]] | `memoria_entrelazada` | — |
| [[8.3.2 Patrón de entrelazado y conflictos de banco]] | `conflictos_banco` | — |
| [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] | `amdahl_grafico` | `stallings-f18-7` · `stallings-f18-5` |
| [[8.4.2 Monousuario vs multiusuario]] | `multiusuario_escalabilidad` | `stallings-f18-12` · `stallings-f18-2` |

---

## Unidad 9 — Hardware aritmético

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[9.1.1 Complemento a 2 y desbordamiento]] | `complemento2_rango` | `stallings-f9-3` · `stallings-f9-5` |
| [[9.1.2 Acarreo anticipado (G y P)]] | `sumador_acarreo_anticipado` | — |
| [[9.2.1 Sumas y desplazamientos]] | `multiplicacion_registros` | `stallings-f9-7` · `stallings-f9-10` |
| [[9.2.2 Algoritmo de Booth]] | `booth_traza` | `stallings-f9-12` · `stallings-f9-13` |
| [[9.2.3 Arreglo multiplicador]] | `arreglo_multiplicador` | — |
| [[9.3.1 Restauración y no restauración]] | `division_restauracion` | `stallings-f9-15` · `stallings-f9-16` |
| [[9.3.2 Sobreflujo y división con signo]] | `division_signo` | — |
| [[9.4.1 Formato, normalización y operaciones]] | `punto_flotante_normalizacion` | `stallings-f9-23` · `stallings-f9-24` |
| [[9.4.2 IEEE 754]] | `ieee754_campos` | `stallings-f10-4` |
| [[9.5.1 Suma decimal corregida]] | `bcd_correccion` | — |

---

## Unidad 10 — Entrada y Salida

| Subtema | Diagrama propio | Figura de libro |
|---|---|---|
| [[10.1.1 Polling y sus límites]] | `es_modos` | `stallings-f7-1` |
| [[10.1.2 Puertos, interfaces y handshake]] | `handshake_tiempos` | `stallings-f7-3` · `stallings-f7-10` |
| [[10.2.1 Mecanismo completo]] | `es_modos` | `stallings-f3-12` |
| [[10.2.2 Interrupciones vectorizadas y prioridad]] | `vector_prioridad` | `stallings-f7-8` · `stallings-f3-14` |
| [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] | `dma` | `stallings-f7-11` · `stallings-f7-12` |
| [[10.4.1 Discos, SSD y latencias]] | `disco_latencias` | `stallings-f6-2` · `stallings-f6-6` |
| [[10.4.2 Interfaces serie y paralelo]] | `serie_paralelo_skew` | `stallings-f5-13` |

---

## Cómo se generan los dos tipos

| Archivo | Qué hace |
|---|---|
| `tools/diagramas.py` | los 34 diagramas propios de la primera tanda |
| `tools/diagramas_2.py` | los 63 de la segunda tanda: uno por subtema que faltaba |
| `tools/extraer_figuras.py` | **extrae las figuras de un PDF** (escaneado o vectorial) buscando el epígrafe `Fig. N.N` y recortando el bloque de contenido que está encima |
| `python3 diagramas_2.py` | regenera los SVG propios en `assets/` |
| `python3 tools/extraer_figuras.py libro.pdf salida/ prefijo_` | vuelve a sacar las figuras de un libro |

Los diagramas propios son SVG escritos con una API mínima (`Svg`, `box`, `gate`, `arrow`…): se leen y se
corrigen. Las figuras de libro son recortes PNG a 200 dpi de los PDF de la bibliografía, con la cita de
figura y página al pie; si el recorte sale mal, se vuelve a correr el extractor con otra franja.

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Cómo usar esta bóveda]] · [[00 Figuras de los libros (índice)]]
