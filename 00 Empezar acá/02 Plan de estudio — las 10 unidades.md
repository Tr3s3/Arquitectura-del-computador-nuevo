---
tipo: guia
---
# Plan de estudio — las 10 unidades

> [!abstract] Cómo usar esta nota
> Es el plan de la cátedra convertido en una lista de temas **con su nota correspondiente**. Marcá `- [x]` cuando puedas explicar el tema en voz alta sin mirar.
>
> **Recordá la condición del examen:** el final es oral y, en la práctica, se aprueba **dibujando circuitos y explicando tablas de verdad**. Por eso cada bloque de abajo trae también el TP de la cátedra que lo ejercita: la teoría explica, el TP te obliga a dibujar. Si sólo hay tiempo para una cosa, hacé los TPs del [[00 Índice de TPs y qué aporta cada uno|índice]] delante de una hoja en blanco.

## Unidad 1 — Circuitos de lógica digital
Computadoras digitales · compuertas lógicas · álgebra booleana · circuitos combinacionales: semisumador, sumador completo.

- [ ] [[Compuertas lógicas]] — tabla de verdad y símbolos de las 7 compuertas

- [ ] [[Álgebra de Boole — postulados y teoremas]] — postulados, dualidad, simplificación

- [ ] [[Leyes de DeMorgan]] — enunciado y demostración por tabla

- [ ] [[Mintérminos y maxtérminos]] — SOP y POS

- [ ] [[Semisumador]] · [[Sumador completo]] — tabla, ecuaciones y gráfico

- TP: [[TP1 Compuertas lógicas]] · [[TP2 Álgebra de Boole]] · [[TP3 Simplificación analítica]] · [[TP4 Mintérminos, maxtérminos y Karnaugh]] · [[TP5 Sumadores]]

## Unidad 2 — Memorias (parte secuencial)

- [ ] [[Flip-Flops SR, D, JK y T]]

- [ ] [[Registros]] — carga paralela, desplazamiento, bidireccional

- [ ] [[Contadores]] — binario, con carga en paralelo

- [ ] [[Decodificador]] · [[Codificador]] · [[Multiplexor]] · [[Demultiplexor]]

- TP: [[TP6 Decodificadores y demultiplexores]] · [[TP7 Codificadores y multiplexores]] · [[TP8 Biestables RS]] · [[TP9 Biestables D, JK y T]] · [[TP10 Registros PIPO y SISO]] · [[TP11 Registros SIPO y PISO]]

## Unidad 2 — Memorias (parte memoria)

- [ ] [[Celda elemental de memoria]]

- [ ] [[Memoria RAM 8x3]] — mapa de direcciones y conexión a la CPU

- [ ] [[Memoria ROM y sus tipos]]

- [ ] [[Jerarquía de memorias]]

- [ ] [[Memoria caché]] — mapeos, escritura, inicialización

- [ ] (complementario) [[Memoria virtual y administración de memoria]] · [[Memoria auxiliar y memoria asociativa]]

- [ ] [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] — el cálculo de las memorias grandes

- TP: [[TP12 Memoria principal]] · [[TP13 Componentes internos]] · [[TP14 Buses]]

## Unidad 3 — Transferencia de registros y microoperaciones

- [ ] [[Flujo de información en BLUE (datos y direcciones)]] — transferencia entre registros, bus de tres estados

- [ ] Microoperaciones aritméticas: sumador, sumador-restador, incrementador (en [[ALU]])

- [ ] Microoperaciones lógicas y de desplazamiento (en [[ALU]] y [[Registros]])

## Unidad 4 — Organización y diseño básico

- [ ] [[Estructura básica de un computador]] — Von Neumann, unidades, buses

- [ ] [[Máquina BLUE — arquitectura y conjunto de instrucciones]]

- [ ] [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]]

- [ ] [[Ciclo de ejecución — todas las operaciones]] · [[Ciclo de la instrucción LDA (24 pulsos)]]

- [ ] [[Unidad de Control]] — funciones y señales de control

- [ ] [[Programar en BLUE — ejemplos]] · [[Lenguaje máquina y clasificación de instrucciones]]

- TP: [[TP15 Arquitectura de Von Neumann (IAS)]] · [[TP16 Ciclo de instrucción básico]]

## Unidad 5 — Programación básica

- [ ] [[Registros de la CPU]] — base, índice, puntero de pila, estado

- [ ] [[Modos de direccionamiento]]

- [ ] [[Formato de la instrucción (4 formatos)]]

- [ ] [[BLUE indexada (RIF, RID, nuevo formato)]]

- [ ] [[Interrupciones y entrada-salida]]

- TP: [[TP17 Formato básico de instrucciones]] · [[TP18 Direccionamiento de memoria]] · [[TP19 Modos de direccionamiento]] · [[TP20 Lenguaje máquina]]

## Unidad 6 — Control microprogramado

- [ ] [[Unidad de control cableada y microprogramada]] — memoria de control, secuenciamiento, microprograma de ejemplo

## Unidad 7 — CPU y arquitecturas

- [ ] [[Pipeline]] · [[Memoria caché]] (repaso) · [[Técnicas para aumentar la velocidad]]

- [ ] [[CISC y RISC]]

- [ ] Buses y tipos de bus → en [[Estructura básica de un computador]]

## Unidad 8 — Paralelismo

- [ ] [[Paralelismo y procesamiento vectorial]] — pipeline aritmético, vectorial, SIMD, memoria entrelazada

## Unidad 9 — Hardware aritmético

- [ ] [[Hardware aritmético (resumen)]] — suma/resta en complemento a 2, Booth, división, punto flotante, BCD

## Unidad 10 — Entrada/Salida

- [ ] [[Interrupciones y entrada-salida]] — transmisión serie/paralela, puertos, interfaces, controladores

- [ ] [[00 Síntesis — Unidad 10]] — **la unidad entera en un archivo** (polling, interrupciones, DMA, discos)

> [!success] Las 10 unidades están desarrolladas en `02 Materia/`
> Cada unidad tiene sus carpetas `Tema N.M/` con los subtemas y su **`00 Síntesis — Unidad N`**. Esta lista sirve como **orden de estudio**; el desarrollo completo de cada renglón está en el índice de su unidad.
