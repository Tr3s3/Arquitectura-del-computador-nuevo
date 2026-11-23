---
tipo: sintesis
unidad: 5
---
# Síntesis — Unidad 5: Programación básica y CPU convencional

> [!abstract] Qué es este archivo
> **Toda la Unidad 5 en un solo lugar**: los 6 temas y sus 13 subtemas, con las tablas, las fórmulas, las recetas de
> examen y las preguntas de autoevaluación. Sirve para **repasar antes del parcial** sin abrir 13 notas. Si algo
> necesita más detalle, cada sección enlaza a su subtema.

> [!tip] Cómo usarlo
> 1. Leer las **§1 a §7** de corrido (30 minutos).
> 2. Tapar la columna derecha de las tablas y **recitar**.
> 3. Hacer las **§11 Recetas de examen** con lápiz.
> 4. Contestar las **§13 preguntas** sin mirar.

## Índice
1. [[#1. La instrucción: opcode y operandos]]
2. [[#2. Clasificación de las instrucciones]]
3. [[#3. Registros de la CPU]]
4. [[#4. Formato de la instrucción y cálculo de CodOp]]
5. [[#5. Modos de direccionamiento]]
6. [[#6. La BLUE indexada (RIF, RID, RB) y los 24 pulsos]]
7. [[#7. Interrupciones]]
8. [[#8. El 8086: segmentación y BIU/EU]]
9. [[#9. La pila]]
10. [[#10. Tablas de memoria rápida]]
11. [[#11. Recetas de examen]]
12. [[#12. Errores que cuestan puntos]]
13. [[#13. Autoevaluación]]

---

## 1. La instrucción: opcode y operandos

Una instrucción tiene **dos partes**: el **opcode** (qué hacer, un número que la UC decodifica) y los **operandos**
(con qué: direcciones, registros o valores).

```
┌──────────────┬───────────────┬───────────────┬───────────────┐
│  opcode      │  operando 1   │  operando 2   │  operando 3   │
└──────────────┴───────────────┴───────────────┴───────────────┘
```

| Concepto | Definición |
|---|---|
| **Opcode** | código de operación; identifica la instrucción |
| **Operando explícito** | está escrito en la instrucción (`100` en `LDA 100`) |
| **Operando implícito** | lo pone el hardware (`AC` en `ADD 100` ⇒ `AC ← AC + M[100]`) |
| **Arquitectura de acumulador** | todo pasa por el `AC`: instrucción corta, programa largo |

En la **BLUE**: `15..12` opcode (4 bits) · `11..0` dirección (12 bits) ⇒ **16 instrucciones**, **4096 celdas**, **1
operando explícito**.
👉 [[5.1.1 Instrucción, opcode y operandos]]

## 2. Clasificación de las instrucciones

| Familia | BLUE | 8086 | Qué la identifica |
|---|---|---|---|
| **Transferencia** | `LDA`, `STA` | `MOV`, `PUSH`, `POP` | mueve sin transformar |
| **Aritméticas** | `ADD` | `ADD`, `SUB`, `INC`, `DEC`, `MUL`, `DIV` | cambia el valor con una cuenta |
| **Lógicas** | `AND`, `IOR`, `XOR`, `NOT` | igual + `TEST` | combina bit a bit |
| **Control (salto)** | `JMA`, `JMP`, `SRJ`, `HLT` | `JMP`, `JZ`, `CALL`, `RET` | cambia el `PC` |
| **Entrada/Salida** | `INP`, `OUT` | `IN`, `OUT` | toca las líneas de E/S |
| **Desplazamiento** | `RAL` | `SHL`, `SHR`, `ROL`, `ROR` | mueve bits |
| **Control del sistema** | `HLT`, `NOP`, `CSA` | `HLT`, `NOP`, `INT`, `IRET` | estado de la máquina |

**Condicionales:** la BLUE no tiene; las arma con `CSA` + `JMA`. El 8086 tiene saltos que miran los **flags**
(`JZ`, `JNZ`, `JC`…).
👉 [[5.1.2 Clasificación de las instrucciones]]

## 3. Registros de la CPU

### Los 14 del 8086 (todos de 16 bits)
| Grupo | Registros | Para qué |
|---|---|---|
| Propósito general | `AX`, `BX`, `CX`, `DX` | datos (acumulador, base, contador, auxiliar); se parten en `H`/`L` |
| Punteros | `SP`, `BP` | tope de pila / base del marco |
| Índices | `SI`, `DI` | origen y destino de arreglos |
| Segmento | `CS`, `DS`, `SS`, `ES` | base de código, datos, pila, extra |
| Instrucción | `IP` | próximo desplazamiento |
| Estado | `FLAGS` | `Z, C, S, O, P, I, D` |

### Comparación
| | BLUE | 8086 | RISC |
|---|---|---|---|
| Cantidad | 5 + estado | **14** | ~32 |
| Ancho | 12/16 | 16 | 32/64 |
| Acumulador | `AC` (obligatorio) | `AX` (preferido) | ninguno |
| Segmentos | no | **sí** (4 × 64 KB) | no |

👉 [[5.1.3 Registros de la CPU]]

## 4. Formato de la instrucción y cálculo de CodOp

### Los 4 formatos (mismo cálculo `X = A + B`)
| Formato | Cómo | Instrucciones | Máquina |
|---|---|---|---|
| **4 dir.** | `ADD X, A, B, próxima` | 1 | teórico |
| **3 dir.** | `ADD X, A, B` | 1 | RISC |
| **2 dir.** | `MOV X,A` · `ADD X,B` | 2 | CISC (8086) |
| **1 dir.** | `LDA A` · `ADD B` · `STA X` | 3 | **acumulador (BLUE)** |

**Regla:** más direcciones ⇒ programa más corto e instrucción más larga.

### Cálculo de CodOp
```
d = log₂(celdas)        CodOp = palabra − d        instrucciones = 2^CodOp
```
| Memoria | Celda | `d` | Palabra | `CodOp` | Instr. |
|---|---|---|---|---|---|
| **4096 (BLUE)** | 16 bits | 12 | 16 | **4** | **16** |
| 512 MB | 4 B | 27 | 32 | 5 | 32 |
| 1 GB | 4 B | 28 | 32 | 4 | 16 |
| 256 KB | 2 B | 17 | 24 | 7 | 128 |

Si no alcanza: palabra más larga · **formato variable** · registros índice · segmentos · banco de registros.
👉 [[5.2.1 Los 4 formatos y el campo único de dirección]] · [[5.2.2 Cálculo de CodOp según el tamaño de memoria]]

## 5. Modos de direccionamiento

| # | Modo | Dirección efectiva | Accesos |
|---|---|---|---|
| 1 | **Inmediato** | el operando **es** el campo | **0** |
| 2 | **Directo** | `EA = campo` | 1 |
| 3 | **Indirecto** | `EA = M[campo]` | **2** |
| 4 | **De registro** | el operando está en el registro | **0** |
| 5 | **Registro indirecto** | `EA = R` | 1 |
| 6 | **Desplazamiento / indexado** | `EA = R + desplazamiento` | 1 |
| 7 | **De pila** | `EA = SP` (tope) | 1 |

### Ejemplo con los mismos datos
`M[30] = 50` · `M[50] = 0042` · `R1 = 0030` · `R2 = 100` · `RIF = 100` · `M[100] = 0042`
| Modo | Cuenta | Resultado |
|---|---|---|
| Inmediato `LDI 30` | — | `AC = 30` |
| Directo `LDA 30` | `EA = 30` | `AC = M[30]` |
| Indirecto `LDA @30` | `EA = M[30] = 50` | `AC = 0042` |
| Registro `ADD R1` | — | usa `0030` |
| Reg. indirecto `LDA (R2)` | `EA = 100` | `AC = 0042` |
| Indexado `LDA 2(RIF)` | `EA = 102` | `AC = M[102]` |
| Pila `POP` | `EA = SP` | dato del tope |

**Para qué:** constante ⇒ inmediato · global ⇒ directo · puntero/lista ⇒ indirecto · **arreglo** ⇒ indexado ·
**subrutina** ⇒ pila.
👉 [[5.3.1 Los 7 modos]] · [[5.3.2 Dirección efectiva y costo en accesos]]

## 6. La BLUE indexada (RIF, RID, RB) y los 24 pulsos

### Los registros y la fórmula
```
EA = RB + campo [+ RIF | RID | RIF + RID]
```
| Registro | Se suma | Para qué |
|---|---|---|
| **RB** | **siempre** | reubicar el programa (lo maneja el sistema) |
| **RIF** | según modificador | recorrer el arreglo de **origen** (lectura) |
| **RID** | según modificador | recorrer el arreglo de **destino** (escritura) |

### El modificador de 2 bits
| Mod | EA |
|---|---|
| `00` | `RB + campo` |
| `01` | `+ RIF` |
| `10` | `+ RID` |
| `11` | `+ RIF + RID` |

### El formato (2 palabras = 32 bits)
`5 opcode` + `2 mod` + `9 campo (desplazamiento)` + `16 dirección` ⇒ **32 instrucciones**, **64 K** de memoria.

### Los costos en pulsos
| Tipo de instrucción | Básica | Indexada | Indexada index. | Indexada indirecta |
|---|---|---|---|---|
| Sin memoria (HLT, NOP, NOT, RAL…) | 8 | 16 | 16 | — |
| Con memoria (ADD, LDA, STA) | **16** | 16 | **24** | **32** |

**Los 24 pulsos** = 8 (búsqueda 1.ª palabra) + 8 (búsqueda 2.ª palabra + cálculo de la EA) + 8 (ejecución).
**Se paga 50 % más de tiempo por instrucción** para tener arreglos sin auto modificación, 64 K y 32 instrucciones.
👉 [[5.4.1 RIF, RID y RB]] · [[5.4.2 Modificador de 2 bits y los 24 pulsos]]

## 7. Interrupciones

### La señal
`IRQ` (pide el periférico) · `SI` (habilita la CPU) · `CP8` (recién al final de la instrucción)
⇒ **`IRQ · SI · CP8 = 1`** ⇒ se atiende.

### Polling vs interrupción
| | Consulta (polling) | Interrupción |
|---|---|---|
| Quién avisa | la CPU pregunta (`INP` en un lazo) | el periférico (`IRQ`) |
| Costo | gasta ciclos preguntando | casi nulo |
| Cuándo | eventos predecibles | eventos asíncronos |

### El ciclo completo
```
CP8: IRQ·SI = 1  →  guardar PC (y estado)  →  PC ← dirección de la ISR
                 →  SI ← 0 automático  →  ejecutar la rutina
                 →  limpiar el flag del periférico  →  POP estado  →  RTI (POP PC, SI ← 1)
```
**Máscara:** cada línea tiene su bit; en 0 se ignora. **Prioridad:** si llegan dos, gana la más alta.
👉 [[5.5.1 IRQ, SI y CP8]] · [[5.5.2 Máscara, pila y RTI]]

## 8. El 8086: segmentación y BIU/EU

```
dirección física (20 bits) = segmento × 16 + desplazamiento
```
| Par | Apunta a |
|---|---|
| `CS:IP` | código |
| `DS:SI` / `DS:BX` | datos |
| `SS:SP` / `SS:BP` | pila |
| `ES:DI` | extra (destino) |

`CS = 1000h`, `IP = 0023h` ⇒ física `10023h`. **Segmento = 64 KB · total = 1 MB · pueden solaparse.**

| Unidad | Qué hace | Registros |
|---|---|---|
| **BIU** | calcula la dirección física, trae instrucciones a la **cola de 6 bytes** | `CS`, `DS`, `SS`, `ES`, `IP` |
| **EU** | decodifica y ejecuta | `AX`-`DX`, `SP`, `BP`, `SI`, `DI`, `FLAGS` |

**BIU + EU en paralelo = primer prefetch del x86** (semilla del pipeline).
👉 [[5.6.1 BIU, EU y segmentación]]

## 9. La pila

**LIFO**, apuntada por `SS:SP`, **crece hacia direcciones menores**.

| Instrucción | Qué hace | `SP` |
|---|---|---|
| `PUSH AX` | `SP ← SP − 2`; `M[SS:SP] ← AX` | decrece |
| `POP AX` | `AX ← M[SS:SP]`; `SP ← SP + 2` | crece |

**Usos:** subrutinas (`CALL` apila `IP`, `RET` lo saca) · interrupciones (`INT`/`IRET`) · variables locales (con
`BP` como marco).
**Errores:** desbordamiento (más `PUSH` que espacio) · subdesbordamiento (más `POP` que datos) · no hay protección.
👉 [[5.6.2 La pila y el registro SP]]

## 10. Tablas de memoria rápida

### Los 16 opcodes de la BLUE (octal) y sus ciclos
| Op | Instrucción | Ciclos | Pulsos |
|---|---|---|---|
| `00` | `HLT` | 1 | 8 |
| `01` | `ADD` | **2** | **16** |
| `02` | `XOR` | **2** | **16** |
| `03` | `AND` | **2** | **16** |
| `04` | `IOR` | **2** | **16** |
| `05` | `NOT` | 1 | 8 |
| `06` | `LDA` | **2** | **16** |
| `07` | `STA` | **2** | **16** |
| `10` | `SRJ` | 1 | 8 |
| `11` | `JMA` | 1 | 8 |
| `12` | `JMP` | 1 | 8 |
| `13` | `INP` | 2+n | 16+ |
| `14` | `OUT` | 2+n | 16+ |
| `15` | `RAL` | 1 | 8 |
| `16` | `CSA` | 1 | 8 |
| `17` | `NOP` | 1 | 8 |

### Los números de la BLUE
| Dato | Valor |
|---|---|
| Memoria | 4096 × 16 |
| Dirección | 12 bits |
| Opcode | 4 bits ⇒ 16 instrucciones |
| Ciclo de reloj | 125 ns |
| Ciclo de máquina | 8 pulsos = 1 µs |
| Palabra indexada | 32 bits (2 palabras) |

### Fórmulas de la unidad
| Qué | Fórmula |
|---|---|
| Bits de dirección | `d = log₂ celdas` |
| Campo de operación | `CodOp = palabra − d` |
| Instrucciones posibles | `2^CodOp` |
| Indexada | `EA = RB + campo [+ RIF/RID]` |
| Segmentación 8086 | `física = segmento × 16 + desplazamiento` |
| Interrupción | `IRQ · SI · CP8` |

## 11. Recetas de examen

> [!example] Receta 1 — "¿Cuántas instrucciones y cuántos bits de opcode?"
> 1. Capacidad ÷ tamaño de celda = **nº de celdas**.
> 2. `d = log₂ celdas`.
> 3. `CodOp = palabra − d`.
> 4. Si piden **cantidad**: `2^CodOp`. Si piden **bits**: `CodOp`.
> 5. Verificar: `CodOp + d = palabra`.

> [!example] Receta 2 — "Calcule la EA y los accesos"
> 1. Identificar el **modo** (¿el campo es el dato? ¿es la dirección? ¿hay registro?).
> 2. Escribir la **fórmula** del modo.
> 3. Sustituir con los valores del enunciado → **EA**.
> 4. Contar accesos: **0** (inmediato/registro) · **1** (directo/indexado/pila) · **2** (indirecto).
> 5. Si el enunciado da un lazo de `n` vueltas, multiplicar.

> [!example] Receta 3 — "¿Cuántos pulsos y cuánto tarda esta instrucción en la BLUE?"
> 1. ¿Va a memoria? ⇒ 2 ciclos (16 pulsos); si no, 1 ciclo (8 pulsos).
> 2. ¿Es indexada con `mod ≠ 00`? ⇒ **24**; ¿indirecta? ⇒ **32**.
> 3. Tiempo = pulsos × 125 ns.
> 4. Programa completo: sumar los pulsos de **todas** las instrucciones + la búsqueda de cada una.

> [!example] Receta 4 — "Describa el manejo de una interrupción"
> 1. **Detección:** `IRQ·SI·CP8` al final de la instrucción.
> 2. **Contexto:** guardar `PC` (hardware) y los registros que use la rutina (software).
> 3. **Desvío:** cargar en el `PC` la dirección de la ISR (vector o dirección fija).
> 4. **Inhibición:** `SI ← 0` mientras dura la rutina.
> 5. **Servicio:** procesar y **limpiar el flag del periférico**.
> 6. **Retorno:** `RTI` restaura registros y `PC`, y pone `SI ← 1`.

> [!example] Receta 5 — "¿Cómo direcciona 1 MB un registro de 16 bits?" (8086)
> 1. `CS` dice el **segmento**, `IP` el **desplazamiento**.
> 2. `física = segmento × 16 + desplazamiento`.
> 3. Verificar que no pase de `FFFFFh`.
> 4. Aclarar: 64 KB por segmento, **1 MB** total, segmentos solapables.

## 12. Errores que cuestan puntos

| Error | Lo correcto |
|---|---|
| "La dirección de la instrucción **es** el operando" | es **dónde está** (o el valor, si es inmediato) |
| `CodOp = d − palabra` | `CodOp = palabra − d` |
| Dar `CodOp` cuando piden **cantidad** | `2^CodOp` |
| Contar 1 acceso en el **inmediato** | **0 accesos** (viene en la instrucción) |
| Sumar un acceso extra en el **indexado** | la suma la hace la ALU: **1 acceso** |
| Confundir **directo** e **indirecto** | directo: el campo **es** la dirección; indirecto: la **contiene** |
| Confundir **registro** y **registro indirecto** | registro: el dato **está** ahí; indirecto: ahí está la **dirección** |
| Decir que `RB` se suma sólo en los indexados | **siempre** se suma |
| Decir 24 pulsos para **todas** las indexadas | las que no van a memoria son **16** |
| Decir "ADD = 1 ciclo" en la BLUE | **2 ciclos / 16 pulsos** (necesita buscar el operando) |
| Atender la interrupción **en medio** de una instrucción | siempre en **`CP8`** |
| Volver de una ISR con `RET` | con **`RTI`** |
| `segmento + desplazamiento` | `segmento × 16 + desplazamiento` |
| "El 8086 direcciona 64 KB" | **1 MB** (64 KB es un segmento) |
| Decir que `SP` **aumenta** al apilar | **decrece** |

## 13. Autoevaluación

1. ¿Qué dos partes tiene toda instrucción? ¿Cuál es implícita en la BLUE y por qué?
2. Nombrá las **cinco familias** de instrucciones con dos ejemplos de la BLUE en total.
3. ¿Cuántos registros tiene el 8086 y cómo se agrupan? ¿Cuáles son de 16 bits y se parten en dos?
4. Escribí `X = A + B` en los **cuatro formatos**. ¿Cuál usa la BLUE y cuántas instrucciones necesita?
5. Una memoria de 512 MB con celdas de 4 B y palabra de 32 bits: ¿cuántos bits de dirección, cuántos de opcode y
   cuántas instrucciones admite?
6. Enumerá los **7 modos** de direccionamiento con su fórmula de `EA` y su cantidad de accesos.
7. Diferencia **directo / indirecto** y **de registro / registro indirecto** con un ejemplo cada uno.
8. ¿Qué suma **siempre** la BLUE indexada? ¿Y qué suma sólo a veces? ¿Para qué sirve cada cosa?
9. Explicá **por qué** una `LDA` indexada cuesta **24 pulsos** y una básica **16**. ¿Qué se gana a cambio?
10. ¿Qué tres condiciones hacen falta para que se atienda una interrupción? ¿En qué pulso se evalúa y por qué?
11. ¿Qué pasa si la rutina de servicio no limpia el flag del periférico? ¿Y si vuelve con `RET`?
12. Calculá la dirección física de `CS = 2000h`, `IP = 0140h`. ¿Cuántos bytes abarca un segmento?
13. ¿Por qué `PUSH` **decrementa** `SP`? ¿Qué guarda `CALL` y qué guarda `INT`?

---

## Relacionado
[[00 Unidad 5 — temas y subtemas]] · [[00 Síntesis — Unidad 4]] · [[00 Unidad 6 — temas y subtemas]] ·
[[00 Índice de la materia (las 10 unidades)]]
