---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Máquina BLUE — arquitectura y conjunto de instrucciones

> [!abstract] En una frase
> BLUE es la **computadora didáctica** de la cátedra: 4096 palabras de 16 bits, 5 registros visibles
> (PC, IR, MAR, MBR, AC), un bus único y 16 instrucciones de 4 bits de código + 12 bits de dirección.
> Sirve para que todo lo que dicen los libros se pueda ver en un diagrama de 20 cm.

## Especificación
| Parámetro | Valor | Consecuencia |
|---|---|---|
| Palabra | 16 bits | el bus de datos es de 16 bits |
| Memoria | 4096 × 16 bits | **12 bits de dirección** (2¹² = 4096) |
| Instrucción (sin indexar) | 16 bits | `opcode (4) + dirección (12)` |
| Instrucciones | 16 | 4 bits de opcode |
| Registros | PC (12), MAR (12), MBR (16), IR (16), AC (16) | ver [[Registros de la CPU]] |
| Buses | datos 16, direcciones 12, control | bus **único** ⇒ una transferencia por pulso |
| Unidades | UC + ALU + memoria + E/S | ver [[Estructura básica de un computador]] |

## Diagrama de bloques
![blue_flujo](../assets/blue_flujo.svg)

## El conjunto de instrucciones (las 16)
La tabla **oficial** es la del apunte de Foster (el que usa la cátedra), en **octal**:

| Octal | Mnemónico | Qué hace | Microoperación | Pulsos |
|---|---|---|---|---|
| `00` | **HLT** | detiene la máquina | `RUN ← 0` | 8 |
| `01` | **ADD** | suma al AC el contenido de XXXX | `AC ← AC + M[XXXX]` | 16 |
| `02` | **XOR** | OR exclusiva bit a bit | `AC ← AC ⊕ M[XXXX]` | 16 |
| `03` | **AND** | AND bit a bit | `AC ← AC · M[XXXX]` | 16 |
| `04` | **IOR** | OR inclusiva bit a bit | `AC ← AC + M[XXXX]` | 16 |
| `05` | **NOT** | complemento a uno del AC | `AC ← AC'` | 8 |
| `06` | **LDA** | carga el AC con el contenido de XXXX | `AC ← M[XXXX]` | 16 |
| `07` | **STA** | almacena el AC en XXXX | `M[XXXX] ← AC` | 16 |
| `10` | **SRJ** | salto a subrutina (guarda el PC en el AC) | `AC ← PC+1` · `PC ← XXXX` | 8 |
| `11` | **JMA** | salto condicional si el AC es negativo | `si A15=1: PC ← XXXX` | 8 |
| `12` | **JMP** | salto incondicional | `PC ← XXXX` | 8 |
| `13` | **INP** | entrada de 8 bits desde el dispositivo YY | `AC[7..0] ← (YY)` | 16+ |
| `14` | **OUT** | salida de 8 bits al dispositivo YY | `(YY) ← AC[15..8]` | 16+ |
| `15` | **RAL** | rota el AC un lugar a la izquierda | `AC ← 2·AC` (cíclico) | 8 |
| `16` | **CSA** | copia el registro de llaves en el AC | `AC ← SR` | 8 |
| `17` | **NOP** | no hace nada | — | 8 |

> [!important] Por qué HLT es `00` y NOP es `17`
> Fue **a propósito**: si la máquina salta por error a una zona de memoria **borrada (todo 0)**, encuentra un
> **HLT** y se detiene en vez de seguir ejecutando basura. Y si ejecuta una palabra **toda de unos** (la
> palabra de detención típica), encuentra un **NOP** y no rompe nada. Es una decisión de **diseño defensivo**
> que vale la pena mencionar: suma puntos y demuestra que entendiste el conjunto, no que lo memorizaste.

> [!warning] Ojo con el simulador del TP16
> El **simulador** del [[TP16 Ciclo de instrucción básico|TP16]] usa una numeración **decimal y simplificada**
> (`1` cargar, `2`/`3` almacenar, `5` sumar, `C` parar) que **no** es la tabla de la máquina. En el oral decí
> "según el simulador del TP…" y "según la tabla octal de la máquina…", y seguí con las microoperaciones:
> **lo que se evalúa es la secuencia de pulsos**. Detalle en
> [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]].

## Los tres grupos funcionales
1. **Transferencia de datos** (`LDA`, `STA`): el AC habla con la memoria.
2. **Operaciones** (`ADD`, `SUB`, `AND`, `OR`, `XOR`, `NOT`): el AC habla con la ALU.
3. **Control de flujo** (`JMP`, `JZ`, `JC`, `HLT`, `NOP`) y **E/S** (`IN`, `OUT`).

**Sin instrucciones de registro a registro**: como hay un solo AC, todo operando de la ALU sale del AC y
vuelve al AC. Eso es lo que hace que BLUE sea "una dirección" (ver
[[Formato de la instrucción (4 formatos)]]) y lo que después la indexada mejora.

## Estados y señales propias de BLUE
| Elemento | Función |
|---|---|
| **RUN** | 1 = ejecutando; `HLT` lo apaga |
| **STATE** | F = búsqueda, E = ejecución |
| **CLOCK** | pulsos; una microoperación por pulso |
| **Z, C** | flags consultados por `JZ` y `JC` |
| **SI** (en la indexada) | habilita/deshabilita interrupciones |

## Cómo se programaría algo simple
```
        LDA  x       ; AC ← M[x]
        ADD  y       ; AC ← AC + M[y]
        STA  z       ; M[z] ← AC
        HLT
x:      .word 5      ; datos en memoria
y:      .word 7
z:      .word 0
```
Ver más en [[Programar en BLUE — ejemplos]].

## Cómo responderlo en el final
1. Definir BLUE como máquina didáctica de von Neumann con bus único.
2. Dar la especificación: 4096×16, 12 bits de dirección, 16 bits de palabra, 16 opcodes.
3. Dibujar el diagrama de bloques con los 5 registros y los 3 buses.
4. Recorrer la tabla de instrucciones por grupos y explicar **qué hace cada una**.
5. Mencionar RUN/STATE/CLOCK y que cada pulso ejecuta una microoperación.

## Errores típicos
- Decir que la instrucción tiene 16 bits de opcode (son 16 **combinaciones** de 4 bits).
- Confundir el AC (dato) con el IR (instrucción).
- Olvidar que `NOT`, `NOP`, `HLT` no necesitan dirección (usan los 16 bits completos o los ignoran).
- Decir que BLUE tiene registros de propósito general (¡tiene uno solo: el AC!).

## Relacionado
[[Flujo de información en BLUE (datos y direcciones)]] · [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[BLUE indexada (RIF, RID, nuevo formato)]] · [[Programar en BLUE — ejemplos]]
