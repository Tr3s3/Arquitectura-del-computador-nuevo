---
tipo: guia
prioridad: maxima
---
# Qué leer para cada pregunta principal (mapa de consulta)

> [!abstract] Para qué sirve esta nota
> Cada pregunta principal del final tiene **una nota maestra** en la bóveda (con el desarrollo completo y el
> guion oral) y, al final de esa nota, una sección **"Para ampliar: qué leer y qué buscar"**. Esta nota junta
> todo en una tabla: **qué fuente abrir para cada tema, en qué parte y qué mirar**. Así estudiás con material
> de consulta real y no con resúmenes de terceros.

---

## 1. Las tres capas de material (leelas en este orden)

| Capa | Qué es | Cuándo usarla |
|---|---|---|
| **1. Cátedra** | `blue.pdf` (Foster, cap. *"Una máquina elemental"*), **apuntes de las Unidades 1 a 5**, la **matriz del final** y los **TPs** | **Siempre primero**: es lo que se evalúa y lo que el profesor espera escuchar |
| **2. Bóveda** | las notas maestras de esta bóveda (desarrollo desde cero + guion oral + repreguntas) | Para entender y para practicar el oral |
| **3. Ampliación** | libros: Hamacher, Stallings, Patterson & Hennessy, Tanenbaum, Floyd, Mano, Brey | Sólo si querés profundizar o te preguntan algo que el apunte no cubre |

> [!warning] Sobre las páginas y los capítulos
> Los libros tienen **varias ediciones** y los capítulos cambian de número. Por eso en la bóveda se indica
> **qué sección/tema buscar** en vez de un número de página, salvo cuando el número sale del propio material de
> la cátedra (por ejemplo, las referencias que cita `memorias.pdf`).

---

## 2. Tabla maestra: pregunta → nota → qué consultar

| # | Pregunta principal | Nota maestra | Fuente de la cátedra (obligatoria) | Ampliación recomendada |
|---|---|---|---|---|
| 1 | **Flujo de información (direcciones y datos)** | [[Flujo de información en BLUE (datos y direcciones)]] | `blue.pdf` → *"El flujo de la información"* (figs. 3-5), *"Implementación de un esquema de bus común"* (figs. 8-9) · [[TP14 Buses]] | Hamacher (microoperaciones) · Stallings (buses) · Patterson & Hennessy (datapath) |
| 2 | **Formato de la instrucción (4 → 1 campo)** | [[Formato de la instrucción (4 formatos)]] | Apuntes **U5** → *"Formatos de instrucción"* · `blue.pdf` → Fig. 1 (palabra de dato vs de instrucción) · [[TP17 Formato básico de instrucciones]] | Hamacher (formatos) · Patterson & Hennessy (formatos R/I/J) · Brey (formato del 8086) |
| 3 | **Ciclo de máquina** | [[Ciclo de máquina]] | `blue.pdf` → *"El ciclo de máquina básico"*, *"Unidad de control"* (figs. 10-11), *"El ciclo de búsqueda"* (Tabla 2) · [[TP16 Ciclo de instrucción básico]] | Hamacher (fetch/decode/execute) · Stallings (ciclo de instrucción) · Tanenbaum |
| 4 | **Estructura básica del computador** | [[Estructura básica de un computador]] | Apuntes **U4** → los cuatro elementos · `blue.pdf` → Fig. 6 (esquema completo) · [[TP15 Arquitectura de Von Neumann (IAS)]] · [[TP14 Buses]] | Stallings (estructura y buses) · Patterson & Hennessy (cap. 1) · Tanenbaum (niveles) |
| 5 | **Memoria RAM 8×3 (3×8)** | [[Memoria RAM 8x3]] | Apuntes **U3** → memorias, celda elemental, RAM 8×3, organización 2D/3D · `memorias.pdf` → **7.3** (RAM estática/dinámica) · [[TP12 Memoria principal]] | Floyd (tema de memorias, ed. 1996: tema 12, págs. 594-644, *citado por la cátedra*) · Mano (memorias) · Fernández Ramos et al. (tema 7, págs. 177-192) |
| 6 | **Ciclo de ejecución: BLUE indexada y sin indexar** | [[Ciclo de ejecución — todas las operaciones]] + [[Ciclo de LDA indexada (los 24 pulsos)]] | `blue.pdf` → **Tablas 3, 4, 5 y 7** · Apuntes **U5** → *"Ciclos de instrucción"* (LDA 0/1/2/3, INI, ENI) · [[TP16 Ciclo de instrucción básico]] | Hamacher (microoperaciones) · Patterson & Hennessy (multiciclo) · Tanenbaum |
| 7 | **Unidad de Control: funciones y señales** | [[Unidad de Control]] (+ [[Cómo se implementa la Unidad de Control]]) | `blue.pdf` → *"Unidad de control"* y *"Circuitos de la unidad de control"* (**figs. 19-29**) | Hamacher (control cableado/microprogramado) · Tanenbaum (microprogramación) · Patterson & Hennessy (control) · Brey (UC del 8086) |
| 8 | **Interrupciones** | [[Interrupciones y entrada-salida]] | Apuntes **U5** → *"Interrupciones"*, *"Sistema elemental de interrupciones para BLUE indexada"*, *"Interrupciones vectorizadas"* · `blue.pdf` → *"Instrucciones de entrada y salida"* (Tabla 4) y Conclusiones | **Stallings** (cap. de E/S: interrupciones, DMA, prioridades) · Hamacher · Tanenbaum · Brey (interrupciones del 8086) |

### Y las tres de la matriz que también son "principales" en la práctica
| Pregunta (1.ª tanda de la matriz) | Nota maestra | Fuente de la cátedra | Ampliación |
|---|---|---|---|
| **BLUE vs BLUE indexada** | [[BLUE vs BLUE indexada — qué cambia y por qué]] | Apuntes **U5** → *"Nuevo hardware, nuevas instrucciones"*, *"Registro base"*, *"BLUE Indexada"* · `blue.pdf` → Conclusiones | Patterson & Hennessy (direccionamiento) · Brey (SI/DI) · Hamacher |
| **Ciclo LDA indexada, 24 pulsos** | [[Ciclo de LDA indexada (los 24 pulsos)]] | Apuntes **U5** → *"Ciclos de instrucción"* (tablas de `LDA 3/1/0, X`) | Hamacher (notación T0…Tn) · Patterson & Hennessy (multiciclo) |
| **¿Cómo se implementa la UC?** | [[Cómo se implementa la Unidad de Control]] | `blue.pdf` → figs. 19-29 y Tablas 2-7 · Apuntes U5 → sección del **8088** (ROM 504×21, PLA, microMAR) | Tanenbaum · Hamacher · Stallings |

### Segunda tanda de la matriz: las diez preguntas y su fuente

| # | Pregunta (2.ª tanda) | Nota maestra | Fuente de la cátedra (obligatoria) | Ampliación recomendada |
|---|---|---|---|---|
| 1 | **Celda elemental de memoria** | [[Celda elemental de memoria]] | Apuntes **U3** → *"Celda elemental de memoria"*, selección, lectura/escritura · `memorias.pdf` → **7.3.2/7.3.3** (SRAM de 6 transistores, DRAM de 1 T + capacitor, refresco) | Floyd · Mano · Patterson & Hennessy (SRAM/DRAM) |
| 2 | **CISC y RISC** | [[CISC y RISC]] | `Resumen final arqui.pdf` → *"Arquitectura CISC"* / *"Arquitectura RISC"* · Apuntes **U5** → sección del **8088** (UC microprogramada, ROM 504×21) · [[TP20 Lenguaje máquina]] | Patterson & Hennessy (cap. 1, el argumento original) · Stallings (RISC vs CISC) · Tanenbaum (brecha semántica) |
| 3 | **Pipeline** | [[Pipeline]] | `Resumen final arqui.pdf` → *"Pipeline"* (las 5 etapas, "3 operaciones en 8 pulsos") · `blue.pdf` → *"El ciclo de búsqueda"* · Apuntes U5 → **BIU/EU del 8088** (cola de 4 bytes) | Patterson & Hennessy (procesador segmentado: hazards y forwarding) · Stallings · Hamacher |
| 4 | **Interrupciones** | [[Interrupciones y entrada-salida]] | Apuntes **U5** → *"Interrupciones"*, *"Sistema elemental para BLUE indexada"*, *"Interrupciones vectorizadas"* · `blue.pdf` → *"Instrucciones de E/S"* y Conclusiones | Stallings (E/S e interrupciones, DMA) · Hamacher · Brey (interrupciones del 8086) |
| 5 | **Las 16 instrucciones, todos los pulsos** | [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | `blue.pdf` → **Tablas 2 a 7** (ciclo de búsqueda + instrucciones de 1 y 2 ciclos + E/S) · Apuntes U5 → *"Ciclos de instrucción"* | Stallings (UC) · Hamacher (señales temporizadas) |
| 6 | **Memoria ROM y sus tipos** | [[Memoria ROM y sus tipos]] | Apuntes **U3** → ROM y cuadro RAM/ROM · `memorias.pdf` → **7.2** (ROM con diodos/MOS, programación, FAMOS/FLOTOX) | Floyd (memorias) · Mano (ROM vs PLA/PAL) · Stallings |
| 7 | **Memoria caché** | [[Memoria caché]] | Apuntes **U3** → sección de **caché** (mapeos, políticas, inicialización, niveles) · [[TP12 Memoria principal]] | Patterson & Hennessy (jerarquía: el capítulo clave) · Stallings (diseño de caché) · Hamacher |
| 8 | **Registros base e índice (RIF, RID, RB)** | [[Registros base e índice]] | Apuntes **U5** → *"Nuevo hardware, nuevas instrucciones"*, *"Registro base"*, *"BLUE Indexada"* · [[TP19 Modos de direccionamiento]] | Stallings (indexado vs base) · Brey (`BX`/`SI`/`DI`/`BP`, segmentos) · Hamacher |
| 9 | **Jerarquía de memorias** | [[Jerarquía de memorias]] | Apuntes **U3** → comienzo de la unidad (parámetros) y jerarquía · `memorias.pdf` → transparencias iniciales (pirámide) · [[TP12 Memoria principal]] | Patterson & Hennessy · Stallings (memoria interna/externa) · Tanenbaum |
| 10 | **Modos de direccionamiento (y los 4 de la indexada)** | [[Modos de direccionamiento]] | [[TP19 Modos de direccionamiento]] (los 7 modos) · Apuntes **U5** → modos y *"BLUE Indexada"* (modificador de 2 bits) · [[BLUE indexada (RIF, RID, nuevo formato)]] | Stallings (cap. de modos de direccionamiento) · Hamacher · Brey (modos del 8086) |

### Tercera tanda de la matriz (peso 12): los circuitos y su fuente

| # | Pregunta (3.ª tanda) | Nota maestra | Fuente de la cátedra (obligatoria) | Ampliación recomendada |
|---|---|---|---|---|
| 1 | **Decodificadores** | [[Decodificador]] | Apuntes **U2** → decodificadores · [[TP6 Decodificadores y demultiplexores]] · `memorias.pdf` (decodificador de filas) | Floyd (combinacionales) · Mano (decodificador + OR = función) |
| 2 | **Codificadores** | [[Codificador]] | Apuntes **U2** → codificadores (con prioridad) · [[TP7 Codificadores y multiplexores]] | Floyd (74LS148, GS/EI/EO) · Mano |
| 3 | **Multiplexores** | [[Multiplexor]] | Apuntes **U2** → multiplexores · [[TP7 Codificadores y multiplexores]] | Floyd (74LS151) · Mano (MUX como generador de funciones) |
| 4 | **Demultiplexores** | [[Demultiplexor]] | Apuntes **U2** → demultiplexores · [[TP6 Decodificadores y demultiplexores]] | Floyd · Mano |
| 5 | **RS → JK con Karnaugh** | [[Conversión entre biestables (RS, JK, D, T)]] | Apuntes **U2** → conversión entre biestables · [[TP8 Biestables RS]] | Floyd (aplicaciones de FF) · Mano (diseño secuencial) |
| 6 | **FF D, T y RS (mapa y función)** | [[Flip-Flops SR, D, JK y T]] | Apuntes **U2** → biestables · [[TP9 Biestables D, JK y T]] | Floyd (cronogramas) · Mano |
| 7 | **Álgebra de Boole y DeMorgan** | [[Álgebra de Boole — postulados y teoremas]] + [[Leyes de DeMorgan]] | Apuntes **U2** → postulados y teoremas · [[TP2 Álgebra de Boole]] · [[TP3 Simplificación analítica]] | Floyd (álgebra booleana) · Mano · Tocci |
| 8 | **Sumadores** | [[Semisumador]] + [[Sumador completo]] | Apuntes **U2** → circuitos aritméticos · [[TP5 Sumadores]] | Floyd (aritméticas) · Mano (sumador-restador, overflow) |
| 9 | **RI y 3 ejemplos de instrucciones** | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] + [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | `blue.pdf` → Tabla 2 y repertorio · Apuntes **U5** (BLUE) · [[TP16 Ciclo de instrucción básico]] | Hamacher (repertorio) · Stallings (ciclo) |
| — | **Herramienta que usan 5, 6 y 7** | [[Mintérminos y maxtérminos]] | Apuntes **U2** → Karnaugh · [[TP4 Mintérminos, maxtérminos y Karnaugh]] | Floyd (Karnaugh) · Mano (Quine-McCluskey) |

---

## 3. La bibliografía, con qué es bueno cada libro

### Material de la cátedra (lo que se evalúa)
| Fuente | Qué es | Fuerte en |
|---|---|---|
| **`blue.pdf`** — Foster, C. C., *Computer Architecture*, 2ª ed., Van Nostrand Reinhold. Cap.: *"Una máquina elemental"* | el apunte base, traducido para la cátedra | **todo el ciclo de la BLUE**: instrucciones en octal, 8 pulsos, tablas por instrucción, UC con compuertas, bus común, E/S |
| **Apuntes de la cátedra** (111 págs.) | U1 *Sistemas de numeración* · U2 *Circuitos lógicos y digitales* · U3 *Memorias electrónicas* · U4 *Estructura básica de una computadora* · U5 *Arquitectura convencional* | formatos, modos, **BLUE indexada completa**, **interrupciones**, **8088** |
| **`memorias.pdf`** — *Dispositivos Electrónicos*, Tema 7: *Memorias semiconductoras* | material auxiliar de otra cátedra | **celdas ROM/SRAM/DRAM**, refresco, arquitectura de RAM, tiempos |
| **Los 21 TPs** | las consignas reales | la notación y el formato de respuesta que espera el profesor |
| **`Arqui Matriz.jpg`** | la matriz del final | **qué cae y con qué peso**: [[00 Matriz del final — las 3 tandas]] |

### Libros de ampliación (por orden de utilidad para esta materia)
| Libro | Bueno para | Ojo con |
|---|---|---|
| **Stallings, W., *Organización y arquitectura de computadores*** | **buses**, **E/S e interrupciones**, DMA, control | es amplio; andá al capítulo que necesitás |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | **microoperaciones**, control cableado/microprogramado, direccionamiento | notación formal al principio cuesta |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | entender el **por qué** (rendimiento, pipeline, jerarquía, datapath) | habla de MIPS/RISC-V, no de BLUE: usalo para comparar |
| **Tanenbaum, A., *Estructura de computadores*** | microprogramación, niveles, E/S | ediciones viejas tienen microprogramación muy detallada (bien para esto) |
| **Floyd, T. L., *Fundamentos de sistemas digitales*** | compuertas, Boole, combinacionales, **biestables**, **memorias** (con muchas figuras) | es de electrónica digital, no de arquitectura |
| **Mano, M., *Lógica digital y diseño de computadoras*** | memorias, decodificación, diseño de la UC | ídem |
| **Brey, B. B., *Los microprocesadores Intel 8086/8088…*** | la CPU real: registros, formato de instrucción, interrupciones | es bibliografía del **TP21**, no del final |
| **Fernández Ramos et al., *Dispositivos Electrónicos para Estudiantes de Informática***; **Malik, *Circuitos Electrónicos***; **Daza & García, *Ejercicios de Dispositivos Electrónicos*** | tecnología de memorias y ejercicios | los cita `memorias.pdf`, no la cátedra |

---

## 4. Cómo leer según el tiempo que tengas

**Si tenés 2 horas** (repaso de último momento):
1. `04 Resumen integrador de la materia` (20 min).
2. De cada nota maestra, **sólo el guion oral** ("Cómo responderlo en el final") y los errores típicos (60 min).
3. `Cómo dibujar los circuitos` + `Tablas de verdad de memoria` (40 min).

**Si tenés 2 días**:
- Día 1: las **5 fuentes de la cátedra** de la tabla maestra, en orden 1→8, leyendo **las notas maestras completas** y dibujando cada tema en una hoja.
- Día 2: **simulacro oral** de las 8 con el guion; y para cada tema que falle, volver a **la sección exacta** de la fuente de la cátedra (columna 4 de la tabla).

**Si tenés una semana**: agregá la **ampliación** de los temas con más peso (RAM 3×8, RISC/CISC, pipeline, interrupciones) y hacé los **TPs** de esos temas.

> [!tip] Regla de oro para citar fuentes en el oral
> Decí **siempre** primero la fuente de la cátedra ("según el apunte de la máquina elemental…", "según la
> Unidad 5…") y después, si querés, la ampliación ("en Hamacher esto se llama microoperación…"). **Nunca al
> revés**: el profesor evalúa su programa, no tu biblioteca.

---

## 5. Relacionado
[[00 Matriz del final — las 3 tandas]] · [[Banco de preguntas del final]] ·
[[Guion de respuestas — preguntas principales]] · [[00 Índice de TPs y qué aporta cada uno]] ·
[[05 Fuentes y qué aporta cada una]] · [[04 Resumen integrador de la materia]]
