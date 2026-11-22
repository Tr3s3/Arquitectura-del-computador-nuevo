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

## El RI: el registro que sostiene la instrucción

> [!note] Si es la primera vez que ves esto
> **RI** = **Registro de Instrucción** (en los apuntes también aparece como **IR**, *Instruction Register*).
> Es un registro de **16 bits** cuya única misión es **guardar la instrucción que se está ejecutando**. Es la
> memoria de trabajo de la Unidad de Control: mientras la instrucción está en el RI, la UC la puede mirar
> **todas las veces que quiera** (en cada uno de los 8 pulsos) sin volver a la memoria.

**Por qué es imprescindible:** al final del ciclo de búsqueda, el dato que llegó por el bus es **la
instrucción**. Si no se guardara en algún lado, en el pulso siguiente el bus ya tendría otra cosa y la máquina
"se olvidaría" de qué estaba haciendo. El RI es el que **conserva la orden** durante los 8 pulsos.

**Cómo se parte (esto es lo que se pregunta):**

```
   RI (16 bits)
   ┌──────────────┬────────────────────────────┐
   │  CodOp (4)   │   Campo de dirección (12)  │
   └──────┬───────┴─────────────┬──────────────┘
          │                     │
          ▼                     ▼
  decodificador 4→16        al MAR (o al sumador
  (¿qué instrucción es?)     de direcciones si es indexada)
```

| Bits del RI | A dónde van | Qué hacen |
|---|---|---|
| **RI15–RI12** (CodOp) | **decodificador 4 → 16** | activa **una** de las 16 líneas de instrucción |
| **RI11–RI0** (dirección) | **MAR** (en CP1 del 2.º ciclo) | es la dirección del operando |
| **RI5–RI0** (en `INP`/`OUT`) | al **selector de dispositivo** | elige el periférico |

**Cómo se carga:** en el ciclo de búsqueda, **CP6**: `strobe MBR` ⇒ el contenido del MBR pasa al RI. Es el
último pulso útil de la búsqueda (en CP7 se decodifica y en CP8 se decide si hace falta un segundo ciclo).

> [!important] La frase que ordena toda la 1.ª tanda
> **El RI es el que convierte "un dato que pasó por el bus" en "una instrucción que la máquina ejecuta".**
> Sin RI no hay decodificación posible: la UC no tiene qué decodificar.

---

## Tres ejemplos de instrucciones, paso a paso

Los tres casos que conviene tener aceitados: uno de **transferencia** (`LDA`), uno de **ALU** (`ADD`) y uno de
**control de flujo** (`JMP`). Todos arrancan con el **mismo ciclo de búsqueda** (CP1 a CP8).

### Ejemplo 1 — `LDA XXXX` (opcode `06`): cargar el AC desde memoria

**Qué hace:** `AC ← M[XXXX]`. **Cuánto tarda:** **16 pulsos** (2 ciclos de máquina).

| Ciclo | Pulsos | Microoperaciones | Señales |
|---|---|---|---|
| **Búsqueda** | CP1 | `PC → MAR` | `CP·F·Read` |
| | CP2–CP4 | `PC + 1 → PC` (se suma **mientras** la memoria busca) | `CP·F` |
| | CP5 | `M[MAR] → MBR` | `strobe MBR` |
| | CP6 | `MBR → IR` | `CP·F` |
| | CP7 | decodificación (`CodOp` al decodificador 4→16) | — |
| | CP8 | `E → State` (pasa a ejecución) | `CP·F·LDA` |
| **Ejecución** | CP1 | `IR(11–0) → MAR` + `Read` | `CP·E·LDA` |
| | CP2–CP4 | (espera la memoria) | — |
| | CP5 | `M[MAR] → MBR` | `strobe MBR` |
| | CP6–CP7 | — | — |
| | CP8 | `MBR → AC` | `CP·E·LDA` |

**Cómo contarlo en 20 segundos:** "Trae la instrucción (8 pulsos), y en el segundo ciclo pone la dirección del
RI en el MAR, espera la memoria y copia el MBR al AC. Son **16 pulsos**: la mitad para saber qué hacer, la otra
mitad para hacerlo."

### Ejemplo 2 — `ADD XXXX` (opcode `01`): sumar un valor de memoria al AC

**Qué hace:** `AC ← AC + M[XXXX]`. **Cuánto tarda:** **16 pulsos**.

| Ciclo | Pulsos clave | Microoperación | Detalle |
|---|---|---|---|
| Búsqueda | CP1–CP8 | igual que siempre | (idéntico en las 16 instrucciones) |
| Ejecución | CP1 | `IR(11–0) → MAR` + `Read` | dirección del sumando |
| | CP2 | **`AC → Z`** | el AC se guarda en el registro de entrada de la ALU |
| | CP5 | `M[MAR] → MBR` | llega el operando |
| | CP6 | **`MBR → Y`** | segundo operando de la ALU |
| | CP8 | **`SUM → AC`** | la ALU suma Z + Y y el resultado vuelve al AC |

> [!tip] Lo que hay que remarcar
> En **CP2** la máquina ya está preparando la ALU (`AC → Z`) mientras la memoria todavía está buscando el dato.
> Eso es **solapamiento**: el mismo truco del `PC+1` en la búsqueda. La suma no ocurre antes de CP8 porque
> recién ahí está el segundo operando.

### Ejemplo 3 — `JMP XXXX` (opcode `12`): salto incondicional

**Qué hace:** `PC ← XXXX`. **Cuánto tarda:** **8 pulsos** (¡**un solo** ciclo!).

| Ciclo | Pulsos | Microoperación |
|---|---|---|
| Búsqueda | CP1–CP6 | trae la instrucción al RI (igual que siempre) |
| | CP7 | decodifica: ya se sabe que es `JMP` |
| | **CP8** | **`IR(11–0) → PC`** ⇒ el salto ocurre **en el mismo ciclo de búsqueda** |

**Por qué es de un solo ciclo:** no hay **nada** que buscar en memoria. La dirección del salto ya está en el RI;
basta con copiarla al PC. Por eso `JMP`, `JMA`, `SRJ`, `HLT`, `NOP`, `NOT`, `RAL` y `CSA` son de **8 pulsos**
(ver [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]).

**Contraste que conviene decir:** "`JMP` no necesita un segundo ciclo porque no accede a memoria; `LDA` y `ADD`
sí, porque tienen que ir a buscar el operando. Ésa es la regla: **1 ciclo = 8 pulsos** si no hay referencia a
memoria; **2 ciclos = 16 pulsos** si la hay."

## Los tres grupos funcionales (los 16 opcodes reales)
1. **Transferencia de datos** (`LDA`, `STA`): el AC habla con la memoria.
2. **Operaciones con la ALU** (`ADD`, `XOR`, `AND`, `IOR`, `NOT`): operan sobre el AC.
3. **Control de flujo** (`JMP`, `JMA`, `SRJ`, `HLT`, `NOP`, `RAL`, `CSA`) y **E/S** (`INP`, `OUT`).

> [!warning] Cuidado con los nombres
> En BLUE **no hay** `SUB` (se resta sumando el complemento a dos: `NOT` + `ADD`), ni `JZ`/`JC` (el salto
> condicional es **`JMA`**, que salta si el AC es negativo: mira `A15`), ni `IN`/`OUT` (son **`INP`**/**`OUT`**).
> Si el oral te sale con los nombres del 8086, aclaralo: "en BLUE el equivalente es…".

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

## Cómo responderlo en el final (4–5 minutos)

> [!warning] El ítem de la 3.ª tanda dice
> "**Conjunto de instrucciones: el RI y 3 ejemplos de instrucciones**". O sea: no alcanza con leer la tabla;
> hay que **explicar el RI** y **desarrollar tres instrucciones**.

1. **Definición (20 s).** BLUE: máquina didáctica de von Neumann, bus único, programa almacenado.
2. **Especificación (40 s).** 4096 × 16, 12 bits de dirección, instrucción de 16 = **4 opcode + 12 dirección**,
   16 opcodes, registros PC/MAR (12) y MBR/IR/AC (16).
3. **Diagrama (60 s).** Dibujar los bloques y el bus único; aclarar que **por pulso pasa una sola transferencia**.
4. **El RI (40 s).** "Registro de Instrucción, 16 bits: los 4 de arriba van al decodificador 4→16 y los 12 de
   abajo al MAR. Se carga en CP6 con `strobe MBR`. Es lo que conserva la orden durante los 8 pulsos."
5. **La tabla por grupos (40 s).** Transferencia / ALU / control de flujo y E/S, con los **nombres reales**
   (`IOR`, `JMA`, `INP`).
6. **Los tres ejemplos (90 s).** `LDA` (16 pulsos: CP1 al MAR, CP8 MBR→AC), `ADD` (16: CP2 AC→Z, CP6 MBR→Y,
   CP8 SUM→AC) y `JMP` (**8**: CP8 IR→PC).
7. **Cierre (20 s).** "La regla es simple: **sin referencia a memoria, 8 pulsos; con referencia, 16**. Y todo
   está gobernado por `estado · pulso · instrucción`."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Qué es el RI y para qué sirve? | Registro de Instrucción: guarda la instrucción en ejecución para que la UC la decodifique pulso a pulso |
| ¿Cómo se parte el RI? | `CodOp` (4 bits, a los 15-12) y **campo de dirección** (12 bits, a los 11-0) |
| ¿En qué pulso se carga el RI? | **CP6** del ciclo de búsqueda (`strobe MBR`) |
| ¿Cuántos bits tiene una instrucción? | **16** = 4 + 12 |
| ¿Cuántas instrucciones distintas? | **16** (2⁴ combinaciones del CodOp) |
| ¿Por qué `JMP` tarda 8 y `LDA` 16? | Porque `JMP` no accede a memoria: la dirección ya está en el RI |
| ¿Qué instrucciones son de 8 pulsos? | `HLT`, `NOP`, `JMP`, `JMA`, `SRJ`, `CSA`, `NOT`, `RAL` |
| ¿Y las de 16? | `LDA`, `STA`, `ADD`, `XOR`, `AND`, `IOR` (y `INP`/`OUT`, que además usan la E/S) |
| ¿Dónde está el RI en el diagrama? | Entre el MBR y la UC: recibe del bus y alimenta al decodificador y al MAR |
| ¿El RI es lo mismo que el PC? | **No**: el PC dice **dónde está** la próxima instrucción; el RI tiene **la instrucción actual** |



## Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **`blue.pdf`** (Foster, *Una máquina elemental*) | la descripción de la máquina y la **Tabla 2** (ciclo de búsqueda) y las tablas de instrucciones | el repertorio **original**, con los opcodes en octal y el papel del IR | **Es la fuente literal** de esta pregunta |
| **Apuntes de cátedra**, *Unidad 5* | sección de la **BLUE**: registros, conjunto de instrucciones, ciclos | la tabla que usa la cátedra y el detalle de `RI11-0 → MAR` | Alineación con el vocabulario del profesor |
| **[[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]** | nota de la bóveda | los 8 pulsos de **cada** una de las 16 | El desarrollo completo de los ejemplos |
| **[[Ciclo de búsqueda (7 y 8 pulsos)]]** · **[[Ciclo de máquina]]** | notas de la bóveda | el tronco común y por qué son 8 pulsos de 125 ns | Prerrequisito de los ejemplos |
| **[[Registros de la CPU]]** | nota de la bóveda | qué hace cada registro (PC, MAR, MBR, IR, AC) y su tamaño | Para no confundir RI con PC |
| **[[TP16 Ciclo de instrucción básico]]** · **[[TP17 Formato básico de instrucciones]]** | los TPs | el formato de la instrucción y el ciclo pedidos | Lo que se entrega |
| **[[Cómo se implementa la Unidad de Control]]** | nota de la bóveda | cómo el CodOp del RI se convierte en señales | El paso siguiente |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **repertorio de instrucciones** | el concepto de registro de instrucción y los formatos | Formalización |
| **Stallings, *Organización y arquitectura de computadores*** | capítulos de **ciclo de instrucción** y **repertorio** | el papel del IR y del PC en el ciclo | Contexto |

## Errores típicos
- Decir que la instrucción tiene 16 bits de opcode (son 16 **combinaciones** de 4 bits).
- Confundir el AC (dato) con el IR (instrucción).
- Olvidar que `NOT`, `NOP`, `HLT` no necesitan dirección (usan los 16 bits completos o los ignoran).
- Decir que BLUE tiene registros de propósito general (¡tiene uno solo: el AC!).

## Relacionado
[[Flujo de información en BLUE (datos y direcciones)]] · [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[BLUE indexada (RIF, RID, nuevo formato)]] · [[Programar en BLUE — ejemplos]]
