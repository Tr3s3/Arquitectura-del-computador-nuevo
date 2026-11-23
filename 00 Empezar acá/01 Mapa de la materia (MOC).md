---
tipo: moc
---
# Mapa de la materia (MOC)

> [!abstract] El recorrido completo en una línea
> De la compuerta al computador: **lógica** → **memoria y secuenciales** → **CPU y máquina BLUE** →
> **técnicas de mejora (pipeline, caché, RISC)** → **entrada/salida**.

> [!tip] Si tenés poco tiempo
> El camino corto es: [[04 Resumen integrador de la materia]] → [[Banco de preguntas del final]] →
> [[Guion de respuestas — preguntas principales]]. Este mapa es para **entender el orden** de la materia.

## Las dos formas de recorrer la bóveda
| Si querés… | Entrá por | Cómo está organizado |
|---|---|---|
| **preparar el final** (las 27 preguntas de la matriz) | [[00 Índice — el final resuelto]] | `Tanda 1\|2\|3` → `N. Pregunta/` → los archivos de esa pregunta |
| **estudiar la materia completa** (las 10 unidades) | [[00 Índice de la materia (las 10 unidades)]] | `Unidad N — nombre/` → `Tema/` → subtemas |

Las unidades de abajo son el **orden lógico** de la materia; cada una lista las notas y, entre paréntesis, la
carpeta donde vive cada una (la mayoría está en `01 Modelo de final resuelto/`, porque el final se lleva casi
todo el desarrollo). Los índices de unidad están en `02 Materia/Unidad N — …/`.

## Unidad 1 — Circuitos de lógica digital

→ Índice de la unidad: [[00 Unidad 1 — temas y subtemas]]
- [[Álgebra de Boole — postulados y teoremas]]
- [[Leyes de DeMorgan]]
- [[Compuertas lógicas]]
- [[Mintérminos y maxtérminos]]
- [[Semisumador]] · [[Sumador completo]]
- Practica: [[Decodificador]] · [[Codificador]] · [[Multiplexor]] · [[Demultiplexor]]

## Unidad 2 — Memorias y circuitos secuenciales

→ Índice de la unidad: [[00 Unidad 2 — temas y subtemas]]
- [[Flip-Flops SR, D, JK y T]]
- [[Registros]] · [[Contadores]]
- [[Celda elemental de memoria]]
- [[Memoria RAM 8x3]]
- [[Memoria ROM y sus tipos]]
- [[Jerarquía de memorias]] · [[Memoria caché]]
- [[Memoria RAM 8x3]] ya está arriba; cálculo de memoria grande: [[Espacio de direccionamiento y cálculo de CodOp-Dirección]]
- Complementario: [[Memoria virtual y administración de memoria]] · [[Memoria auxiliar y memoria asociativa]]

## Unidad 3 y 4 — Transferencia, estructura y máquina BLUE

→ Índices: [[00 Unidad 3 — temas y subtemas]] · [[00 Unidad 4 — temas y subtemas]]
- [[Estructura básica de un computador]]
- [[Registros de la CPU]] · [[ALU]] · [[Unidad de Control]]
- [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
- [[Flujo de información en BLUE (datos y direcciones)]]
- [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]]
- [[Ciclo de ejecución — todas las operaciones]] · [[Ciclo de la instrucción LDA (24 pulsos)]]
- [[Programar en BLUE — ejemplos]] · [[Lenguaje máquina y clasificación de instrucciones]]

## Unidad 5 — Formatos, direccionamiento, interrupciones

→ Índice de la unidad: [[00 Unidad 5 — temas y subtemas]]
- [[Formato de la instrucción (4 formatos)]]
- [[Modos de direccionamiento]]
- [[BLUE indexada (RIF, RID, nuevo formato)]]
- [[Interrupciones y entrada-salida]]

## Unidad 6 y 7 — Control y arquitecturas

→ Índices: [[00 Unidad 6 — temas y subtemas]] · [[00 Unidad 7 — temas y subtemas]]
- [[Unidad de control cableada y microprogramada]]
- [[Pipeline]] · [[CISC y RISC]] · [[Técnicas para aumentar la velocidad]]

## Unidad 8 y 9 — Paralelismo y hardware aritmético

→ Índices: [[00 Unidad 8 — temas y subtemas]] · [[00 Unidad 9 — temas y subtemas]]
- [[Paralelismo y procesamiento vectorial]]
- [[Hardware aritmético (resumen)]]

## Material de cátedra — los 21 TPs

→ Índice: [[00 Índice de TPs y qué aporta cada uno]] · Unidad 10: [[00 Unidad 10 — temas y subtemas]]
- [[00 Índice de TPs y qué aporta cada uno]] ← qué agrega cada TP y a qué nota de teoría corresponde
- [[TP1 Compuertas lógicas]] · [[TP2 Álgebra de Boole]] · [[TP3 Simplificación analítica]] · [[TP4 Mintérminos, maxtérminos y Karnaugh]]
- [[TP5 Sumadores]] · [[TP6 Decodificadores y demultiplexores]] · [[TP7 Codificadores y multiplexores]]
- [[TP8 Biestables RS]] · [[TP9 Biestables D, JK y T]] · [[TP10 Registros PIPO y SISO]] · [[TP11 Registros SIPO y PISO]]
- [[TP12 Memoria principal]] · [[TP13 Componentes internos]] · [[TP14 Buses]]
- [[TP15 Arquitectura de Von Neumann (IAS)]] · [[TP16 Ciclo de instrucción básico]] · [[TP17 Formato básico de instrucciones]]
- [[TP18 Direccionamiento de memoria]] · [[TP19 Modos de direccionamiento]] · [[TP20 Lenguaje máquina]]

## Máquina BLUE en profundidad (lo que más cae)
- [[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Registros base e índice]]
- [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · [[Ciclo de LDA indexada (los 24 pulsos)]]
- [[Cómo se implementa la Unidad de Control]]
- [[Conversión entre biestables (RS, JK, D, T)]] (3.ª tanda del final)

## Examen
- [[00 Matriz del final — las 3 tandas]] ← **la foto del profesor, con pesos**
- [[04 Resumen integrador de la materia]] ← **la materia en 6 secciones, para leer el día antes**
- [[Banco de preguntas del final]] ← **el índice de todo**
- [[Guion de respuestas — preguntas principales]] ← qué decir y qué dibujar en el oral
- [[Cómo dibujar los circuitos (checklist de pizarrón)]] · [[Tablas de verdad de memoria]]
- [[Prácticas resueltas]] · [[Autoevaluación]]
## Glosario
**[[Glosario]]**: los **180 conceptos** de la materia, cada uno con ficha desarrollada (qué es, para qué sirve,
características y en qué subtema se estudia). Índice alfabético + los 23 pares que se confunden.
- [[Glosario — Unidad 1]] · [[Glosario — Unidad 2]] · [[Glosario — Unidad 3]] · [[Glosario — Unidad 4]] · [[Glosario — Unidad 5]]
- [[Glosario — Unidad 6]] · [[Glosario — Unidad 7]] · [[Glosario — Unidad 8]] · [[Glosario — Unidad 9]] · [[Glosario — Unidad 10]]

## Validación y mejoras
[[06 Validación de contenido (resúmenes, TPs y claridad)]]: qué se auditó contra los resúmenes y los TPs, y qué se agregó.
[[07 Plan de mejoras pendientes]]: el backlog con prioridades, esfuerzo y cómo se haría cada mejora.

