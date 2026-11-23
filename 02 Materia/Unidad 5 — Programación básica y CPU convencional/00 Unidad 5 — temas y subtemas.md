---
tipo: indice
unidad: 5
---
# Unidad 5 — Programación básica y CPU convencional

> [!abstract] Qué pide la unidad
> Cómo **se le dice a la máquina qué hacer**: lenguaje máquina, formato de la instrucción, modos de
> direccionamiento, la **BLUE indexada** (con registros índice y base), interrupciones, y el salto a una **CPU
> real** (el 8088/8086 del TP21).

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
