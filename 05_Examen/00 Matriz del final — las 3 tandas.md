---
tipo: examen
prioridad: maxima
---
# Matriz del final — las 3 tandas (foto del profesor)

> [!abstract] Qué es esta nota
> Es la **matriz real** que reparte el final en tres tandas, tal como está en la foto que pasaste.
> Cada ítem tiene al lado un número (el peso o la frecuencia con que cae según la cátedra) y cada uno
> está enlazado a la nota donde está desarrollado **y dibujado**.
>
> **Cómo se rinde:** la 1.ª tanda son 8 preguntas de la máquina BLUE (la columna vertebral); la 2.ª tanda
> son 10 temas de memoria y arquitectura; la 3.ª tanda es **todo con gráficos, tablas de verdad paso a paso
> y funciones**. Es un oral: se aprueba **dibujando y explicando el dibujo**.

> [!tip] Cada nota tiene su sección **"Para ampliar"**
> Al final de cada nota maestra hay una tabla de **qué material de consulta leer** para ese tema (qué fuente, en
> qué parte y qué buscar). El conjunto está reunido en
> [[01 Qué leer para cada pregunta principal]] — es el mapa de bibliografía del final.

> [!important] Regla de oro que se desprende de la matriz
> La 3.ª tanda dice literalmente *"todo esto con gráficos y tablas de verdad paso a paso y funciones"*.
> Es decir: **no alcanza con decir la definición**. De cada circuito hay que entregar
> **tabla de verdad → funciones (simplificadas) → circuito dibujado**. Si practicás eso, las tres tandas
> se resuelven igual.

---

## 1.ª tanda — la máquina (8 preguntas)

| # | Pregunta (texto de la matriz) | Peso | Nota | Qué dibujar sí o sí |
|---|---|---|---|---|
| 1 | **Diferencias entre la máquina BLUE y la BLUE indexada** | 8 | [[BLUE vs BLUE indexada — qué cambia y por qué]] | Las dos máquinas lado a lado (opcode 4 vs 5 bits + modificador 2 + dirección 16) |
| 2 | **Ciclo de instrucción de LDA de la BLUE indexada, con esquema y los 24 pulsos** ("podés hacer LDA 3, X") | 8 | [[Ciclo de LDA indexada (los 24 pulsos)]] | La línea de tiempo de 3 ciclos de máquina = 24 pulsos, con CP1…CP24 |
| 3 | **Flujo de direcciones y flujo de datos** | 7 | [[Flujo de información en BLUE (datos y direcciones)]] | Los 5 registros sobre el bus, con flechas separadas para direcciones (12) y datos (16) |
| 4 | **Memoria RAM 3×8** ("¿gráfico?" anotado al lado) | 10 | [[Memoria RAM 8x3]] | El decodificador 3→8 + las 8 celdas de 3 bits + CS y L/E |
| 5 | **Estructura básica del computador** | 5 | [[Estructura básica de un computador]] | CPU + memoria + E/S unidas por los 3 buses |
| 6 | **¿Cómo se implementa la unidad de control?** | 7 | [[Cómo se implementa la Unidad de Control]] | El árbol de decodificación de 4 bits → 16 líneas, y las compuertas de señales |
| 7 | **Formato de instrucciones (de 4 campos a 1 campo)** | 8 | [[Formato de la instrucción (4 formatos)]] | Las 4 cajas, de la más larga a la más corta, con `X = A + B` |
| 8 | **Ciclo de máquina** | 6 | [[Ciclo de máquina]] | El bucle búsqueda/ejecución con los FF RUN, STATE y el CLOCK |

## 2.ª tanda — memorias y arquitectura (10 preguntas)

| # | Pregunta | Peso | Nota | Qué dibujar |
|---|---|---|---|---|
| 1 | **Memoria RAM: celda elemental** | 4 | [[Celda elemental de memoria]] | El biestable + línea de selección + L/E + buffer de 3 estados |
| 2 | **Arquitectura RISC y CISC** | 10 | [[CISC y RISC]] | Dos columnas comparativas + un ejemplo de instrucción de cada una |
| 3 | **Pipeline** | 10 | [[Pipeline]] | El diagrama de etapas solapadas con el ejemplo de BLUE (8 pulsos → 3 operaciones) |
| 4 | **Interrupciones** | 9 | [[Interrupciones y entrada-salida]] | La línea IRQ → SI → guardar PC → rutina → RTI, y los estados F/E/I |
| 5 | **Ciclo de máquina de las 16 instrucciones (todos los pulsos) de la máquina BLUE** | 6-7 | [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | La tabla de 16 filas × CP7/CP8 (+ los ciclos extra de LDA/STA/ADD/INP/OUT) |
| 6 | **Memoria ROM** | 4 | [[Memoria ROM y sus tipos]] | La celda ROM (diodo/transistor) + matriz con el decodificador |
| 7 | **Memoria caché** | 4 | [[Memoria caché]] | Los tres mapeos (directo, asociativo, asociativo por conjuntos) |
| 8 | **Registros base e índice** | 8 | [[Registros base e índice]] | RIF/RID + RB entrando al sumador de direcciones |
| 9 | **Jerarquía de memoria** | 4 | [[Jerarquía de memorias]] | La pirámide con velocidad/costo/capacidad |
| 10 | **Modos de direccionamiento (en la BLUE indexada)** | 8 | [[Modos de direccionamiento]] | Los 4 modos del campo modificador (0, 1, 2, 3) con la EA de cada uno |

## 3.ª tanda — circuitos con tabla de verdad, funciones y gráfico (peso 12)

> [!warning] Lo que se corrige en esta tanda
> Cada ítem se resuelve **en este orden**: (1) tabla de verdad, (2) función o funciones, (3) simplificación
> si se pide, (4) **circuito dibujado** con las compuertas. Si falta el circuito o la función, la tabla sola
> no alcanza.

| # | Pregunta | Nota | Entregable |
|---|---|---|---|
| 1 | **Decodificadores** | [[Decodificador]] | Tabla 2→4 y 3→8, `Yi = m_i`, circuito |
| 2 | **Codificadores** | [[Codificador]] | Tabla 4→2 y 8→3, una OR por bit de salida, circuito |
| 3 | **Multiplexores** | [[Multiplexor]] | Tabla 4→1, `Y = S1'S0'I0 + …`, circuito con AND-OR |
| 4 | **Demultiplexores** | [[Demultiplexor]] | Tabla 1→4, `Yi = D · sel`, circuito, diferencia con el decodificador |
| 5 | **Cómo pasar de un flip-flop RS a JK** (mapa de Karnaugh y función booleana) | [[Conversión entre biestables (RS, JK, D, T)]] | Tabla de excitación RS + mapa K de J y de K ⇒ `J = S`, `K = R` |
| 6 | **Flip-flop tipo D, T y RS** (mapa de Karnaugh y función booleana) | [[Conversión entre biestables (RS, JK, D, T)]] | Ecuaciones características + mapa K de cada uno |
| 7 | **Álgebra de Boole, sus leyes y reglas (teorema de DeMorgan)** | [[Álgebra de Boole — postulados y teoremas]] + [[Leyes de DeMorgan]] | Postulados, leyes con su dual, DeMorgan demostrado por tabla |
| 8 | **Sumadores** | [[Semisumador]] + [[Sumador completo]] | Tabla, `S = A⊕B`, `C = A·B`; y el completo con sus 8 filas |
| + | **Conjunto de instrucciones: el RI y 3 ejemplos de instrucciones** | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] + [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | La tabla de opcodes, qué hace el IR y 3 instrucciones explicadas paso a paso |

---

## Cómo se estudia esta matriz (plan de 5 días)

| Día | Qué | Tiempo |
|---|---|---|
| 1 | **1.ª tanda completa**, dibujando las 8. Es el corazón: si sabés esto, sabés el 60 % de la materia | 4 h |
| 2 | **2.ª tanda**: memorias (celda, RAM 3×8, ROM, caché, jerarquía) | 4 h |
| 3 | **2.ª tanda**: arquitectura (RISC/CISC, pipeline, interrupciones, base e índice, modos) | 4 h |
| 4 | **3.ª tanda**: los 8 circuitos con tabla + función + dibujo, cronometrados a 10 min cada uno | 4 h |
| 5 | **Simulacro**: respondé la matriz en voz alta sacando 2 preguntas al azar de cada tanda | 3 h |

> [!tip] Orden de los pesos
> Sumando los números que anotó el profesor: **3.ª tanda (12) > RISC/CISC y pipeline (10) > RAM 3×8 (10) >
> interrupciones (9) > BLUE vs indexada, LDA 24 pulsos, formato, base e índice, modos (8) > UC, flujo (7) >
> ciclo de máquina, 16 instrucciones (6-7) > estructura, celda, ROM, caché, jerarquía (4-5)**.
> Los cinco temas de peso 8-10 son: **RAM 3×8, RISC/CISC, pipeline, interrupciones y los circuitos de la 3.ª tanda**.

## Lo que la matriz NO pregunta pero necesitás para responderla
- [[04 Resumen integrador de la materia]] — el mapa general (leelo primero).
- [[Compuertas lógicas]] — sin compuertas no hay circuito que dibujar.
- [[Flip-Flops SR, D, JK y T]] — base del punto 5 y 6 de la 3.ª tanda.
- [[Registros de la CPU]] — PC, MAR, MBR, IR, AC: aparecen en todas las respuestas.
- [[Unidad de Control]] — para el punto 6 de la 1.ª tanda.

## Relacionado
[[01 Qué leer para cada pregunta principal]] · [[Banco de preguntas del final]] · [[Guion de respuestas — preguntas principales]] ·
[[Cómo dibujar los circuitos (checklist de pizarrón)]] · [[Tablas de verdad de memoria]] ·
[[00 Índice de TPs y qué aporta cada uno]]
