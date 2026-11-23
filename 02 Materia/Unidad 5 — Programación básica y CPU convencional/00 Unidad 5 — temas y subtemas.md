---
tipo: indice
unidad: 5
---
# Unidad 5 — Programación básica y CPU convencional

> [!abstract] Qué pide la unidad
> Cómo **se le dice a la máquina qué hacer**: lenguaje máquina, formato de la instrucción, modos de
> direccionamiento, la **BLUE indexada** (con registros índice y base), interrupciones, y el salto a una **CPU
> real** (el 8088/8086 del TP21).

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 5 — Programación básica y CPU convencional/
├── 5.1 Lenguaje máquina/
│   ├── 5.1.1 Instrucción: opcode y operandos
│   └── 5.1.2 Clasificación de las instrucciones
├── 5.2 Formato de la instrucción/
│   ├── 5.2.1 Los 4 formatos y el campo único de dirección
│   └── 5.2.2 Cálculo de CodOp según el tamaño de memoria
├── 5.3 Modos de direccionamiento/
│   ├── 5.3.1 Los 7 modos
│   └── 5.3.2 Dirección efectiva y costo en accesos
├── 5.4 La BLUE indexada/
│   ├── 5.4.1 RIF, RID y RB
│   └── 5.4.2 Modificador de 2 bits y los 24 pulsos
├── 5.5 Interrupciones/
│   ├── 5.5.1 IRQ·SI·CP8 y polling del flag
│   └── 5.5.2 Máscara, pila y RTI
└── 5.6 El 8086/8088/
    ├── 5.6.1 BIU, EU y segmentación
    └── 5.6.2 UC microprogramada y emu8086
```

**6 temas y 12 subtemas.** Cada subtema va a ser **una nota** dentro de la carpeta de su tema,
y al terminar la unidad se genera **`00 Síntesis — Unidad 5`** con todo el contenido junto (como ya está hecho en
[[00 Síntesis — Unidad 1|la Unidad 1]]).

| Tema | Subtemas | Estado |
|---|---|---|
| **5.1 Lenguaje máquina** | 5.1.1 Instrucción: opcode y operandos · 5.1.2 Clasificación de las instrucciones | ⏳ a desarrollar |
| **5.2 Formato de la instrucción** | 5.2.1 Los 4 formatos y el campo único de dirección · 5.2.2 Cálculo de CodOp según el tamaño de memoria | ⏳ a desarrollar |
| **5.3 Modos de direccionamiento** | 5.3.1 Los 7 modos · 5.3.2 Dirección efectiva y costo en accesos | ⏳ a desarrollar |
| **5.4 La BLUE indexada** | 5.4.1 RIF, RID y RB · 5.4.2 Modificador de 2 bits y los 24 pulsos | ⏳ a desarrollar |
| **5.5 Interrupciones** | 5.5.1 IRQ·SI·CP8 y polling del flag · 5.5.2 Máscara, pila y RTI | ⏳ a desarrollar |
| **5.6 El 8086/8088** | 5.6.1 BIU, EU y segmentación · 5.6.2 UC microprogramada y emu8086 | ⏳ a desarrollar |

> [!note] Qué hay ya de esta unidad
> El **desarrollo de examen** de casi todos estos temas ya está escrito (está enlazado más abajo, en la tabla de
> material disponible). Lo que falta es la **versión de programa**: el subtema desarrollado en la carpeta de su
> tema, con el detalle de la cursada y los TPs.

## Material ya disponible de esta unidad
| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **5.1 Lenguaje máquina** | instrucción = opcode + operandos · clasificación (transferencia, aritméticas, lógicas, control, E/S) · ensamblador vs máquina | [[Lenguaje máquina y clasificación de instrucciones]] · `Tema 5.1 Lenguaje máquina y registros/` |
| **5.2 Registros de la CPU** | AC, PC, IR, MAR, MBR · base, índice, puntero de pila, estado | [[Registros de la CPU]] · `Tema 5.1 Lenguaje máquina y registros/` |
| **5.3 Formato de la instrucción** | los 4 formatos de la cátedra → 1 campo de dirección · 4+12 · cálculo de CodOp | [[Formato de la instrucción (4 formatos)]] · carpeta `Tanda 1/1.7` y su `Apoyo a la pregunta/` |
| **5.4 Modos de direccionamiento** | inmediato, directo, indirecto, registro, registro indirecto, desplazamiento, pila · EA | [[Modos de direccionamiento]] · carpeta `Tanda 2/2.10` |
| **5.5 La BLUE indexada** | RIF, RID, RB · sumador de direcciones · modificador de 2 bits · 24 pulsos | [[BLUE indexada (RIF, RID, nuevo formato)]] · [[BLUE vs BLUE indexada — qué cambia y por qué]] · carpeta `Tanda 1/1.2` y su `Apoyo a la pregunta/` |
| **5.6 Interrupciones** | `IRQ·SI·CP8` · polling, máscara, pila, RTI, vectorizadas | [[Interrupciones y entrada-salida]] · carpeta `Tanda 2/2.8` |
| **5.7 El 8086/8088 (CPU real)** | BIU + EU · segmentos · 14 registros · UC microprogramada (ROM 504×21) · emu8086 | [[El 8086 como CPU convencional (TP21)]] · `Tema 5.4 El 8086 (TP21)/` |

---

## Qué hay que saber hacer al terminar la unidad
1. **Escribir un programa chico** en el lenguaje de la BLUE (con lazos y arreglos).
2. **Partir** la instrucción en campos y calcular cuántos bits necesita el CodOp.
3. **Calcular la dirección efectiva** en cada modo, diciendo cuántos accesos a memoria cuesta.
4. Explicar **qué agrega la indexada** y qué cuesta (24 pulsos).
5. Describir el **manejo de una interrupción** de punta a punta.

## TPs de la unidad
[[TP17 Formato básico de instrucciones]] · [[TP18 Direccionamiento de memoria]] ·
[[TP19 Modos de direccionamiento]] · [[TP20 Lenguaje máquina]] · [[TP21 intro al emu8086]]

## Fuente de la cátedra
Apuntes **Unidad 5 — Arquitectura convencional** (formatos, modos, BLUE indexada, interrupciones, 8088) ·
Brey (*Los microprocesadores Intel 8086/8088*) · `El_manual_del_Microprocesador.pdf`.

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 4 — temas y subtemas]] ·
[[00 Unidad 6 — temas y subtemas]]
