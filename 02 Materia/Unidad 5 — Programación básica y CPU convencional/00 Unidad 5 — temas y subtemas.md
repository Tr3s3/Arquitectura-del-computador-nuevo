---
tipo: indice
unidad: 5
---
# Unidad 5 — Programación básica y CPU convencional

> [!abstract] Qué pide la unidad
> Cómo **se le dice a la máquina qué hacer**: lenguaje máquina, formato de la instrucción, modos de direccionamiento, la **BLUE indexada** (con registros índice y base), interrupciones, y el salto a una **CPU real** (el 8086 del TP21).

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 5 completa (lectura de corrido)]]**: los **13 subtemas** pegados en un solo archivo, con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 5]]) es el resumen de una página; el archivo completo es el desarrollo entero.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 5 — Programación básica y CPU convencional/
├── Tema 5.1 Lenguaje máquina/
│   ├── 5.1.1 Instrucción, opcode y operandos
│   ├── 5.1.2 Clasificación de las instrucciones
│   └── 5.1.3 Registros de la CPU
├── Tema 5.2 Formato de la instrucción/
│   ├── 5.2.1 Los 4 formatos y el campo único de dirección
│   └── 5.2.2 Cálculo de CodOp según el tamaño de memoria
├── Tema 5.3 Modos de direccionamiento/
│   ├── 5.3.1 Los 7 modos
│   └── 5.3.2 Dirección efectiva y costo en accesos
├── Tema 5.4 La BLUE indexada/
│   ├── 5.4.1 RIF, RID y RB
│   └── 5.4.2 Modificador de 2 bits y los 24 pulsos
├── Tema 5.5 Interrupciones/
│   ├── 5.5.1 IRQ·SI·CP8 y polling del flag
│   └── 5.5.2 Máscara, pila y RTI
└── Tema 5.6 El 8086/
    ├── 5.6.1 BIU, EU y segmentación
    └── 5.6.2 La pila y el registro SP
```

**6 temas y 13 subtemas.** Cada subtema es **una nota** dentro de la carpeta de su tema. La unidad está **cerrada** y todo su contenido quedó reunido en **[[00 Síntesis — Unidad 5]]**.

| Tema | Subtemas | Estado |
|---|---|---|
| **5.1 Lenguaje máquina** | 5.1.1 Instrucción, opcode y operandos · 5.1.2 Clasificación de las instrucciones · 5.1.3 Registros de la CPU | ✅ |
| **5.2 Formato de la instrucción** | 5.2.1 Los 4 formatos y el campo único de dirección · 5.2.2 Cálculo de CodOp según el tamaño de memoria | ✅ |
| **5.3 Modos de direccionamiento** | 5.3.1 Los 7 modos · 5.3.2 Dirección efectiva y costo en accesos | ✅ |
| **5.4 La BLUE indexada** | 5.4.1 RIF, RID y RB · 5.4.2 Modificador de 2 bits y los 24 pulsos | ✅ |
| **5.5 Interrupciones** | 5.5.1 IRQ·SI·CP8 y polling del flag · 5.5.2 Máscara, pila y RTI | ✅ |
| **5.6 El 8086** | 5.6.1 BIU, EU y segmentación · 5.6.2 La pila y el registro SP | ✅ |

## Los 6 temas, de un vistazo

| Tema | Índice | La idea en una línea |
|---|---|---|
| **5.1** | [[00 Tema 5.1 — índice]] | instrucción = opcode + operandos; cinco familias |
| **5.2** | [[00 Tema 5.2 — índice]] | 4/3/2/1 direcciones y `CodOp = palabra − dirección` |
| **5.3** | [[00 Tema 5.3 — índice]] | 7 modos, cada uno con su `EA` y su costo en accesos |
| **5.4** | [[00 Tema 5.4 — índice]] | `EA = RB + campo [+RIF/RID]` y 24 pulsos |
| **5.5** | [[00 Tema 5.5 — índice]] | `IRQ·SI·CP8`, máscara, pila y `RTI` |
| **5.6** | [[00 Tema 5.6 — índice]] | `segmento × 16 + desplazamiento`, BIU + EU |

## Material de examen ya disponible de esta unidad

| Tema | Nota de desarrollo | Dónde está además |
|---|---|---|
| **5.1 Lenguaje máquina** | [[Lenguaje máquina y clasificación de instrucciones]] · [[Registros de la CPU]] | `Tema 5.1 Lenguaje máquina/` |
| **5.2 Formato de la instrucción** | [[Formato de la instrucción (4 formatos)]] | `Tanda 1/1.7` + su `Apoyo a la pregunta/` |
| **5.3 Modos de direccionamiento** | [[Modos de direccionamiento]] | `Tanda 2/2.10` |
| **5.4 La BLUE indexada** | [[BLUE indexada (RIF, RID, nuevo formato)]] · [[BLUE vs BLUE indexada — qué cambia y por qué]] | `Tanda 1/1.2` + su `Apoyo a la pregunta/` |
| **5.5 Interrupciones** | [[Interrupciones y entrada-salida]] | `Tanda 2/2.8` |
| **5.6 El 8086** | [[El 8086 como CPU convencional (TP21)]] | `Tema 5.6 El 8086/` · TP21 |

---

## Qué hay que saber hacer al terminar la unidad

1. **Escribir un programa chico** en el lenguaje de la BLUE (con lazos y arreglos).

2. **Partir** la instrucción en campos y calcular cuántos bits necesita el CodOp.

3. **Calcular la dirección efectiva** en cada modo, diciendo cuántos accesos a memoria cuesta.

4. Explicar **qué agrega la indexada** y qué cuesta (24 pulsos frente a 16).

5. Describir el **manejo de una interrupción** de punta a punta (hasta el `RTI`).

6. Explicar la **segmentación** del 8086 y la división **BIU / EU**.

## TPs de la unidad
[[TP17 Formato básico de instrucciones]] · [[TP18 Direccionamiento de memoria]] · [[TP19 Modos de direccionamiento]] · [[TP20 Lenguaje máquina]] · [[TP21 intro al emu8086]]

## Fuente de la cátedra
Apuntes **Unidad 5 — Arquitectura convencional** (formatos, modos, BLUE indexada, interrupciones, 8088) · Brey (*Los microprocesadores Intel 8086/8088*) · `El_manual_del_Microprocesador.pdf`.

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 4 — temas y subtemas]] · [[00 Unidad 6 — temas y subtemas]] · [[00 Síntesis — Unidad 5]]
