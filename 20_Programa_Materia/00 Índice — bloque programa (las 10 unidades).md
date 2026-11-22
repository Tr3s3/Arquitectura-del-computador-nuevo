---
tipo: moc
prioridad: maxima
---
# Bloque PROGRAMA — la materia completa, unidad por unidad

> [!abstract] Qué hay en este bloque
> El **programa de las 10 unidades de la cátedra** recorrido de punta a punta, para **entender la materia de
> manera integral** y no sólo contestar el final. Acá viven las notas que el modelo de final **no** pregunta
> (memoria virtual, contadores, registros, ALU, paralelismo, 8086, microprogramación) y acá está **el mapa que
> conecta todo**, incluidas las notas que viven en el [[00 Índice — bloque examen (las 3 tandas)|bloque examen]].

> [!important] La regla (para no buscar dos veces lo mismo)
> **Cada nota vive en un solo bloque**, en el lugar donde más se usa. La mayoría de los temas del programa
> coinciden con preguntas del final ⇒ su nota está en el **bloque examen**. Desde las unidades de abajo **se
> llega igual**: los links funcionan desde cualquier carpeta.

---

## Cómo está organizado

```
20_Programa_Materia/
├── 00 Índice — bloque programa (esta nota)
├── 01 Memorias, registros y contadores/   memoria virtual, memoria asociativa, contadores, registros
├── 02 La CPU y su control/                ALU, registros de la CPU, lenguaje máquina, programar en BLUE,
│                                          UC cableada y microprogramada
└── 03 Arquitecturas avanzadas/            técnicas de velocidad, paralelismo, 8086 (TP21), hardware aritmético
```

El resto del programa se estudia en el bloque examen, y los TPs están en `01_Material_Catedra/`
([[00 Índice de TPs y qué aporta cada uno]]).

---

## Unidad 1 — Circuitos de lógica digital
> Compuertas, álgebra de Boole, simplificación y los circuitos combinacionales (sumadores, decodificadores,
> codificadores, MUX/DEMUX).

- [[Compuertas lógicas]] · [[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] ·
  [[Mintérminos y maxtérminos]]
- Combinacionales: [[Semisumador]] · [[Sumador completo]] · [[Decodificador]] · [[Codificador]] ·
  [[Multiplexor]] · [[Demultiplexor]]
- **TPs**: [[TP1 Compuertas lógicas]] · [[TP2 Álgebra de Boole]] · [[TP3 Simplificación analítica]] ·
  [[TP4 Mintérminos, maxtérminos y Karnaugh]] · [[TP5 Sumadores]]
- **Fuente**: apuntes **U2** · Floyd (capítulos de compuertas y simplificación)

## Unidad 2 — Memorias y circuitos secuenciales
> Biestables y flip-flops, registros, contadores, y la memoria en todos sus niveles.

- [[Flip-Flops SR, D, JK y T]] · [[Conversión entre biestables (RS, JK, D, T)]]
- [[Registros]] · [[Contadores]] ← *este bloque*
- [[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]]
- [[Jerarquía de memorias]] · [[Memoria caché]] · [[Memoria virtual y administración de memoria]] ·
  [[Memoria auxiliar y memoria asociativa]] ← *las dos últimas, este bloque*
- Cálculo de memorias grandes: [[Espacio de direccionamiento y cálculo de CodOp-Dirección]]
- **TPs**: [[TP6 Decodificadores y demultiplexores]] · [[TP7 Codificadores y multiplexores]] ·
  [[TP8 Biestables RS]] · [[TP9 Biestables D, JK y T]] · [[TP10 Registros PIPO y SISO]] ·
  [[TP11 Registros SIPO y PISO]] · [[TP12 Memoria principal]] · [[TP13 Componentes internos]]
- **Fuente**: apuntes **U3** · `memorias.pdf` (Tema 7) · Floyd

## Unidad 3 — Transferencia de registros y microoperaciones
> Cómo se mueve un dato dentro de la CPU: microoperaciones y bus.

- [[Flujo de información en BLUE (datos y direcciones)]] — bus de tres estados, transferencias
- [[ALU]] ← *este bloque* (microoperaciones aritméticas, lógicas y de desplazamiento)
- [[Registros]] · [[Registros de la CPU]] ← *este bloque*
- **TP**: [[TP14 Buses]]
- **Fuente**: apuntes **U3-U4** · Hamacher (microoperaciones)

## Unidad 4 — Organización y diseño básico
> La computadora como sistema: unidades, buses, ciclo de instrucción y control.

- [[Estructura básica de un computador]] · [[Registros de la CPU]]
- [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Programar en BLUE — ejemplos]] ← *el segundo,
  este bloque*
- [[Proceso de manejo de una instrucción]] · [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] ·
  [[Ciclo de ejecución — todas las operaciones]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]
- [[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]]
- **TPs**: [[TP15 Arquitectura de Von Neumann (IAS)]] · [[TP16 Ciclo de instrucción básico]]
- **Fuente**: `blue.pdf` (Foster) · apuntes **U4**

## Unidad 5 — Programación básica y CPU convencional
> Lenguaje máquina, formatos, modos de direccionamiento y la BLUE indexada.

- [[Lenguaje máquina y clasificación de instrucciones]] ← *este bloque*
- [[Formato de la instrucción (4 formatos)]] · [[Modos de direccionamiento]] · [[Registros base e índice]]
- [[BLUE indexada (RIF, RID, nuevo formato)]] · [[BLUE vs BLUE indexada — qué cambia y por qué]] ·
  [[Ciclo de LDA indexada (los 24 pulsos)]]
- [[Interrupciones y entrada-salida]]
- **TPs**: [[TP17 Formato básico de instrucciones]] · [[TP18 Direccionamiento de memoria]] ·
  [[TP19 Modos de direccionamiento]] · [[TP20 Lenguaje máquina]]
- **Fuente**: apuntes **U5** · Brey (*Los microprocesadores Intel 8086/8088*)

## Unidad 6 — Control microprogramado
- [[Unidad de control cableada y microprogramada]] ← *este bloque*
- Apoyo: [[Cómo se implementa la Unidad de Control]] · [[CISC y RISC]]
- **Fuente**: apuntes **U5** (sección del **8088**: ROM de control 504×21) · Tanenbaum

## Unidad 7 — CPU y arquitecturas
- [[Pipeline]] · [[Técnicas para aumentar la velocidad]] ← *el segundo, este bloque*
- [[CISC y RISC]] · [[Memoria caché]] (repaso de la unidad 2)
- Buses y su tipología: [[Estructura básica de un computador]] · [[TP14 Buses]]
- **Fuente**: `Resumen final arqui.pdf` · Patterson & Hennessy · Stallings

## Unidad 8 — Paralelismo
- [[Paralelismo y procesamiento vectorial]] ← *este bloque* (pipeline aritmético, vectorial, SIMD, memoria
  entrelazada)
- Apoyo: [[Pipeline]]
- **Fuente**: Stallings · Patterson & Hennessy

## Unidad 9 — Hardware aritmético
- [[Hardware aritmético (resumen)]] ← *este bloque* (suma/resta en complemento a 2, Booth, división, punto
  flotante, BCD)
- Base: [[Semisumador]] · [[Sumador completo]] · [[ALU]]
- **Fuente**: apuntes **U2** · Hamacher · Stallings

## Unidad 10 — Entrada/Salida
- [[Interrupciones y entrada-salida]] (E/S programada, por interrupciones, DMA, puertos, interfaces)
- Apoyo: [[Memoria virtual y administración de memoria]] (DMA y buffers)
- **Fuente**: apuntes **U5** · Stallings (capítulo de E/S) · `blue.pdf` (instrucciones de E/S)

## Extras del programa que no están en la matriz
| Tema | Nota | Por qué importa |
|---|---|---|
| **8086/8088 y emu8086** | [[El 8086 como CPU convencional (TP21)]] | cierra la materia con una CPU **real** (CISC, microprogramada, segmentada) |
| **Memoria virtual** | [[Memoria virtual y administración de memoria]] | el último nivel de la jerarquía; paginación y TLB |
| **Memoria asociativa** | [[Memoria auxiliar y memoria asociativa]] | comparación en paralelo (caché y TLB) |
| **Contadores y registros** | [[Contadores]] · [[Registros]] | los circuitos secuenciales de la unidad 2 |
| **Unidad de control cableada y microprogramada** | [[Unidad de control cableada y microprogramada]] | el puente entre la UC de la BLUE y el 8088 |

---

## Cómo estudiar la materia completa (plan de 3 semanas)

| Semana | Qué | Notas |
|---|---|---|
| **1. Los ladrillos** | unidades 1-2: compuertas → Boole/Karnaugh → sumadores → MUX/DEMUX → flip-flops → memoria | [[Compuertas lógicas]] … [[Memoria caché]] |
| **2. La máquina** | unidades 3-5: estructura, BLUE, ciclos, UC, formatos, modos, indexada | [[Estructura básica de un computador]] … [[Interrupciones y entrada-salida]] |
| **3. Lo avanzado** | unidades 6-10: microprogramación, pipeline, RISC/CISC, paralelismo, aritmética, E/S, 8086 | [[Unidad de control cableada y microprogramada]] … [[El 8086 como CPU convencional (TP21)]] |

> [!tip] Regla de oro para estudiar integral
> Por cada unidad: (1) leé la nota, (2) **dibujá el circuito o el esquema sin mirar**, (3) resolvé el **TP** de
> esa unidad, (4) contá en voz alta qué resuelve ese concepto. Si podés hacer las cuatro, el tema es tuyo.
> Los TPs están en [[00 Índice de TPs y qué aporta cada uno]].

---

## Relacionado
[[00 Índice — bloque examen (las 3 tandas)]] · [[01 Mapa de la materia (MOC)]] ·
[[02 Plan de estudio — las 10 unidades]] · [[04 Resumen integrador de la materia]] ·
[[05 Fuentes y qué aporta cada una]]
