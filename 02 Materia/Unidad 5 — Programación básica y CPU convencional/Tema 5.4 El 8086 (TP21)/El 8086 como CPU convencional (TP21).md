---
unidad: 5
tipo: concepto
examen: apoyo
prioridad: media
---
# El 8086/8088 como CPU convencional (TP21)

> [!abstract] En una frase
> El **8088/8086** es el ejemplo de "CPU real" que usa la cátedra para mostrar todo lo anterior en un chip
> comercial: **BIU + EU** (búsqueda separada de ejecución = pipeline incipiente), **14 registros de 16 bits**,
> **UC microprogramada** y **segmentación** de la memoria de 1 MB en 4 segmentos de 64 KB.

> [!note] Esta nota es de apoyo
> La matriz del final **no lo pregunta**, pero el [[TP21 intro al emu8086|TP21]] pide programar en emu8086 y
> el apunte lo menciona al hablar de arquitectura convencional y microprogramación. Saber lo básico te
> permite **conectar** ("el 8086 hace lo mismo que la BLUE, pero con más registros y microprogramado").

## Por qué aparece en esta materia
Todo el cuatrimestre se construyó una máquina mínima (la BLUE) para entender: bus único, ciclo de búsqueda y
ejecución, instrucciones de 1 palabra, modos de direccionamiento. El 8086/8088 muestra **lo mismo, ya
industrializado**: mismos conceptos, con más registros, más modos y un repertorio enorme.

## Cómo está partido por dentro (lo importante)
| Unidad | Qué hace |
|---|---|
| **BIU** (Bus Interface Unit) | **busca** instrucciones en memoria, las guarda en una **cola FIFO de 4 bytes**, maneja el bus y le pasa los operandos a la EU |
| **EU** (Execution Unit) | **ejecuta**: tiene la UC, la ALU y 9 registros de 16 bits |

Como la BIU busca **mientras** la EU ejecuta, el 8086 ya tiene **pipeline**: es el mismo principio de la
figura de [[Pipeline]], aplicado a la búsqueda de instrucciones (prefetch).

## Los 14 registros
| Grupo | Registros | Para qué |
|---|---|---|
| **Generales** (16 bits, cuatro direccionables también como 8) | `AX` (acumulador, AH/AL), `BX` (**base**), `CX` (contador, CH/CL), `DX` (datos, DH/DL) | cuentas, direccionamiento, contadores, E/S |
| **Punteros / índices** | `SP` (puntero de pila), `BP` (puntero base), **`SI`** (índice fuente), **`DI`** (índice destino) | pila y recorrido de arreglos: **son los RIF/RID de la BLUE indexada**, en un chip real |
| **De segmento** | `CS` (código), `DS` (datos), `SS` (pila), `ES` (extra) | cada uno apunta a un bloque de 64 KB |
| **De estado** | `FLAGS` (CF, ZF, SF, OF, IF…) | resultados y control (el flag **IF** habilita interrupciones = el `SI` de la BLUE) |

## La segmentación (y el cálculo de 20 bits)
El 8086 tiene registros de **16 bits** pero direcciona **1 MB (2²⁰)**. La solución: **segmento × 16 +
desplazamiento** (o sea, el segmento se corre 4 bits y se suma):

```
  dirección física (20 bits) = CS/DS/SS/ES × 10h + desplazamiento de 16 bits
```
Ese registro de segmento es exactamente la idea del **registro base** de la BLUE indexada: un desplazamiento
global que se suma a la dirección que indica la instrucción ([[Registros base e índice]]).

## Modos de direccionamiento del 8086 (mapa rápido)
| Modo | Cómo se forma la dirección |
|---|---|
| Inmediato | el operando está en la instrucción |
| De registro | el operando está en un registro |
| Directo | `DS:[desplazamiento]` |
| **Indexado** | `[SI]` o `[DI]` (+ desplazamiento opcional) |
| **Base + indexado** | `[BX + SI]`, `[BP + DI]`, … |
| **Base + indexado con desplazamiento** | `[BX + SI + desplazamiento]` |
| De pila | `PUSH` / `POP` con `SP` |

Es la versión "completa" de los 4 modos del modificador de la BLUE indexada
([[Modos de direccionamiento]]).

## La UC del 8088 es microprogramada
- ROM de control de **504 palabras de 21 bits** con unos **90 microprocedimientos**.
- Cada instrucción usa **al menos un microprocedimiento**; hay microprocedimientos **compartidos** (por
  ejemplo, el cálculo de direcciones).
- El opcode, mediante una **PLA**, produce la **dirección inicial** del microprograma; el `microMAR` la carga.
- Microinstrucción: campos *fuente* (5), *destino* (5), *tipo* (3), *ALU* (4), *registro* (3), *condición* (1).

Desarrollo del concepto: [[Cómo se implementa la Unidad de Control]].

## Lo que pide el TP21 (emu8086)
- Instalar/abrir **emu8086** y escribir un programa mínimo: `MOV`, `ADD`, `INT 21h` / `INT 20h`.
- Entender que en el 8086 el programa **se arma con instrucciones simples** (RISC-style: load/store y
  operaciones registro-registro), a diferencia de la BLUE, donde todo pasa por el acumulador y la memoria.
- Ver los registros cambiar paso a paso en el emulador: es la mejor forma de "ver" lo que en la BLUE se explica
  con pulsos.

## Cómo lo mencionás en el final (sin que te pidan el tema)
> "La BLUE es el modelo didáctico; una CPU real como el 8088 tiene lo mismo: registros índice (SI/DI), un
> registro base (los de segmento), interrupciones con flag de habilitación y una UC microprogramada; además
> parte la búsqueda de la ejecución en dos unidades (BIU y EU), que es un pipeline de instrucciones."

## Errores típicos
- Decir que el 8086 tiene registros de 20 bits: tiene **16**, y la dirección de 20 bits se **calcula**.
- Confundir `SI`/`DI` (índices) con `CS`/`DS`/`SS`/`ES` (segmentos).
- Pensar que la cola de 4 bytes es una caché: es una **cola de instrucciones** (prefetch), no una caché.

## Relacionado
[[Registros base e índice]] · [[Modos de direccionamiento]] · [[Cómo se implementa la Unidad de Control]] ·
[[Pipeline]] · [[CISC y RISC]] · [[TP21 intro al emu8086]]
