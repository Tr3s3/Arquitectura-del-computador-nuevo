---
tipo: indice
---
# Mapa de diagramas: qué gráfico tiene cada subtema

> [!abstract] Qué es esta nota
> La lista completa de los **104 subtemas** de `02 Materia/` con el **diagrama** que cada uno trae. Sirve
> para auditar la cobertura y para encontrar rápido el dibujo que hay que saber reproducir a mano en el
> final. Son **106 diagramas** embebidos sobre **97 archivos** distintos en `assets/`.

> [!tip] Cómo usarlo
> 1. Elegí la unidad que estás estudiando.
> 2. Abrí el subtema y copiá el dibujo **a mano** (el final es oral y se rinde dibujando).
> 3. Si el dibujo no te sale de memoria, ése es el subtema a repasar.

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

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[1.1.1 Compuerta AND, OR y NOT]] | ✅ | `compuertas.svg` |
| [[1.1.2 NAND, NOR, XOR y XNOR]] | ✅ | `compuertas_nand_nor_xor.svg` |
| [[1.1.3 Compuertas universales]] | ✅ | `nand_universal.svg` |
| [[1.2.1 Postulados, dualidad y teoremas]] | ✅ | `dualidad_teoremas.svg` |
| [[1.2.2 Leyes de DeMorgan]] | ✅ | `demorgan_circuitos.svg` |
| [[1.2.3 Simplificación analítica]] | ✅ | `simplificacion_compuertas.svg` |
| [[1.3.1 Mintérminos y maxtérminos]] | ✅ | `mintterminos_canonica.svg` |
| [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]] | ✅ | `karnaugh_3var.svg` |
| [[1.3.3 Don't care y criterios de agrupación]] | ✅ | `karnaugh_dontcare.svg` |
| [[1.4.1 Decodificador]] | ✅ | `decodificador_2x4.svg` · `decodificador_3x8.svg` |
| [[1.4.2 Codificador]] | ✅ | `codificador_8x3.svg` |
| [[1.4.3 Multiplexor]] | ✅ | `mux_4x1.svg` |
| [[1.4.4 Demultiplexor]] | ✅ | `demux_1x4.svg` |
| [[1.5.1 Semisumador y sumador completo]] | ✅ | `semisumador.svg` · `sumador_completo.svg` |
| [[1.5.2 Sumador de n bits y resta en complemento a 2]] | ✅ | `sumador_n_bits.svg` |

---

## Unidad 2 — Memorias y circuitos secuenciales

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[2.1.1 Biestable RS (NOR y NAND)]] | ✅ | `flipflops.svg` |
| [[2.1.2 Flip-flops D y T]] | ✅ | `flipflop_d_t_tiempos.svg` |
| [[2.1.3 Flip-flop JK y ecuaciones características]] | ✅ | `flipflop_jk_ecuaciones.svg` |
| [[2.1.4 Conversión entre biestables]] | ✅ | `flipflops.svg` |
| [[2.2.1 Registros PIPO y SISO]] | ✅ | `registros_pipo_siso.svg` |
| [[2.2.2 Registros SIPO y PISO]] | ✅ | `registros_sipo_piso.svg` |
| [[2.2.3 Contadores binarios y módulo N]] | ✅ | `contadores_modulo.svg` |
| [[2.3.1 Celda elemental de memoria]] | ✅ | `celda_memoria.svg` |
| [[2.3.2 SRAM y DRAM]] | ✅ | `sram_dram_refresco.svg` |
| [[2.3.3 Matriz, expansión y RAM 8x3]] | ✅ | `ram_8x3.svg` |
| [[2.4.1 ROM = decodificador + OR]] | ✅ | `rom_decodificador_or.svg` |
| [[2.4.2 PROM, EPROM, EEPROM y Flash]] | ✅ | `prom_flash_celda.svg` |
| [[2.5.1 Jerarquía y localidad]] | ✅ | `jerarquia_memorias.svg` |
| [[2.5.2 Caché: mapeos y políticas]] | ✅ | `cache_mapeos.svg` |
| [[2.5.3 AMAT y cálculo de mejora]] | ✅ | `amat_cache.svg` |
| [[2.6.1 Memoria virtual y paginación]] | ✅ | `memoria_virtual_tlb.svg` |
| [[2.6.2 Memoria auxiliar y memoria asociativa]] | ✅ | `memoria_asociativa_cam.svg` |
| [[2.7.1 Bits de dirección igual a log2 de celdas]] | ✅ | `bits_direccion.svg` |
| [[2.7.2 CodOp vs campo de dirección]] | ✅ | `codop_vs_direccion.svg` |

---

## Unidad 3 — Transferencia de registros y microoperaciones

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[3.1.1 Notación de transferencia entre registros]] | ✅ | `microoperaciones_bus.svg` |
| [[3.1.2 Bus único y buffers de 3 estados]] | ✅ | `buffer_tres_estados.svg` |
| [[3.1.3 Buses de datos, de direcciones y de control]] | ✅ | `buses_interno_externo.svg` |
| [[3.2.1 Estructura, G-P y señales de selección]] | ✅ | `alu_estructura.svg` |
| [[3.2.2 Operaciones aritméticas, lógicas y flags]] | ✅ | `flags_alu.svg` |
| [[3.3.1 AC, PC, IR, MAR y MBR]] | ✅ | `registros_cpu_mar.svg` |
| [[3.3.2 Base, índice, puntero de pila y estado]] | ✅ | `registros_cpu_mar.svg` |

---

## Unidad 4 — Organización y diseño básico

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[4.1.1 Unidades funcionales de una computadora]] | ✅ | `estructura_basica.svg` |
| [[4.1.2 IAS y el programa almacenado]] | ✅ | `ias_estructura.svg` |
| [[4.2.1 Especificación, registros y 4096x16]] | ✅ | `blue_flujo.svg` |
| [[4.2.2 Los 16 opcodes octales]] | ✅ | `blue_opcodes.svg` |
| [[4.2.3 Programar en BLUE]] | ✅ | `blue_programa_ram.svg` |
| [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] | ✅ | `ciclo_maquina.svg` |
| [[4.3.2 Búsqueda, los 8 pulsos]] | ✅ | `busqueda_pulsos.svg` |
| [[4.3.3 Ejecución instrucción por instrucción]] | ✅ | `lda24_pulsos.svg` |
| [[4.4.1 Funciones y señales de control]] | ✅ | `uc_cableada.svg` |
| [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] | ✅ | `estado_pulso_1_16.svg` |

---

## Unidad 5 — Programación básica y CPU convencional

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[5.1.1 Instrucción, opcode y operandos]] | ✅ | `instruccion_partes.svg` |
| [[5.1.2 Clasificación de las instrucciones]] | ✅ | `clasificacion_instrucciones.svg` |
| [[5.1.3 Registros de la CPU]] | ✅ | `registros_cpu_mar.svg` |
| [[5.2.1 Los 4 formatos y el campo único de dirección]] | ✅ | `formatos_instruccion.svg` |
| [[5.2.2 Cálculo de CodOp según el tamaño de memoria]] | ✅ | `codop_vs_direccion.svg` |
| [[5.3.1 Los 7 modos]] | ✅ | `modos_direccionamiento.svg` |
| [[5.3.2 Dirección efectiva y costo en accesos]] | ✅ | `ea_calculo.svg` |
| [[5.4.1 RIF, RID y RB]] | ✅ | `rif_rid_rb.svg` |
| [[5.4.2 Modificador de 2 bits y los 24 pulsos]] | ✅ | `lda24_pulsos.svg` |
| [[5.5.1 IRQ, SI y CP8]] | ✅ | `irq_logica.svg` |
| [[5.5.2 Máscara, pila y RTI]] | ✅ | `pila_rti.svg` |
| [[5.6.1 BIU, EU y segmentación]] | ✅ | `biu_eu_cola.svg` |
| [[5.6.2 La pila y el registro SP]] | ✅ | `pila_rti.svg` |

---

## Unidad 6 — Control microprogramado

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[6.1.1 Circuito, compuertas y señales]] | ✅ | `uc_cableada.svg` |
| [[6.2.1 Memoria de control y microinstrucción]] | ✅ | `uc_microprogramada.svg` |
| [[6.2.2 Secuenciamiento y microPC]] | ✅ | `micropc_flujo.svg` |
| [[6.3.1 Cableada vs microprogramada]] | ✅ | `cableada_vs_micro.svg` |
| [[6.3.2 El 8088, ROM de control 504x21]] | ✅ | `rom_control_8088.svg` |

---

## Unidad 7 — CPU y arquitecturas

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[7.1.1 Etapas y diagrama en escalera]] | ✅ | `pipeline.svg` |
| [[7.1.2 Hazards y sus soluciones]] | ✅ | `pipeline_hazards.svg` |
| [[7.1.3 Cálculo de speedup y límites]] | ✅ | `speedup_limites.svg` |
| [[7.2.1 Superscalar, superpipeline, SMT y multicore]] | ✅ | `anchura_superscalar_smt.svg` |
| [[7.2.2 Caché y predicción de saltos]] | ✅ | `prediccion_saltos.svg` |
| [[7.3.1 Tabla comparativa y ejemplos]] | ✅ | `cisc_risc.svg` |
| [[7.3.2 UC cableada vs microprogramada y load-store]] | ✅ | `load_store_risc.svg` |
| [[7.4.1 von Neumann vs Harvard]] | ✅ | `von_neumann_harvard.svg` |
| [[7.4.2 Buses internos y externos]] | ✅ | `buses_interno_externo.svg` |

---

## Unidad 8 — Paralelismo

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[8.1.1 Etapas segmentadas y suma de vectores]] | ✅ | `pipeline_aritmetico.svg` |
| [[8.1.2 Encadenamiento y speedup]] | ✅ | `encadenamiento.svg` |
| [[8.2.1 SIMD, registros vectoriales y GPU]] | ✅ | `simd_registros.svg` |
| [[8.2.2 Flynn, arreglos SIMD y conectados]] | ✅ | `flynn.svg` |
| [[8.2.3 Multiplicación de matrices]] | ✅ | `matriz_simd.svg` |
| [[8.3.1 Bancos de memoria y ancho de banda]] | ✅ | `memoria_entrelazada.svg` |
| [[8.3.2 Patrón de entrelazado y conflictos de banco]] | ✅ | `conflictos_banco.svg` |
| [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]] | ✅ | `amdahl_grafico.svg` |
| [[8.4.2 Monousuario vs multiusuario]] | ✅ | `multiusuario_escalabilidad.svg` |

---

## Unidad 9 — Hardware aritmético

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[9.1.1 Complemento a 2 y desbordamiento]] | ✅ | `complemento2_rango.svg` |
| [[9.1.2 Acarreo anticipado (G y P)]] | ✅ | `sumador_acarreo_anticipado.svg` |
| [[9.2.1 Sumas y desplazamientos]] | ✅ | `multiplicacion_registros.svg` |
| [[9.2.2 Algoritmo de Booth]] | ✅ | `booth_traza.svg` |
| [[9.2.3 Arreglo multiplicador]] | ✅ | `arreglo_multiplicador.svg` |
| [[9.3.1 Restauración y no restauración]] | ✅ | `division_restauracion.svg` |
| [[9.3.2 Sobreflujo y división con signo]] | ✅ | `division_signo.svg` |
| [[9.4.1 Formato, normalización y operaciones]] | ✅ | `punto_flotante_normalizacion.svg` |
| [[9.4.2 IEEE 754]] | ✅ | `ieee754_campos.svg` |
| [[9.5.1 Suma decimal corregida]] | ✅ | `bcd_correccion.svg` |

---

## Unidad 10 — Entrada y Salida

| Subtema | Diagrama | Archivo |
|---|---|---|
| [[10.1.1 Polling y sus límites]] | ✅ | `es_modos.svg` |
| [[10.1.2 Puertos, interfaces y handshake]] | ✅ | `handshake_tiempos.svg` |
| [[10.2.1 Mecanismo completo]] | ✅ | `es_modos.svg` |
| [[10.2.2 Interrupciones vectorizadas y prioridad]] | ✅ | `vector_prioridad.svg` |
| [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]] | ✅ | `dma.svg` |
| [[10.4.1 Discos, SSD y latencias]] | ✅ | `disco_latencias.svg` |
| [[10.4.2 Interfaces serie y paralelo]] | ✅ | `serie_paralelo_skew.svg` |

---

## Cómo se generan
| Archivo | Qué contiene |
|---|---|
| `tools/diagramas.py` | los 34 diagramas de la primera tanda (compuertas, memorias, pipeline, buses…) |
| `tools/diagramas_2.py` | los 63 de la segunda tanda (uno por subtema que faltaba) |
| `tools/` → `python3 diagramas_2.py` | regenera todos los SVG de `assets/` |

Los SVG están escritos a mano con una API mínima (`Svg`, `box`, `text`, `gate`, `arrow`…), no son imágenes
exportadas: se pueden leer, corregir y volver a generar.

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Cómo usar esta bóveda]]
