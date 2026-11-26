---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S12 · Operaciones de máquina BLUE

> [!question] Pregunta
> Enumere las operaciones de la máquina BLUE y explique qué hacía cada una.

## 1. Teoría previa

**Código de operación (opcode).** En BLUE son **4 bits**, es decir, **16 instrucciones**. En la tabla oficial de la cátedra (apunte de Foster), los códigos se escriben en **octal**.

**Formato.** `opcode 4 bits + dirección 12 bits`, en una palabra de 16 bits.

**Notación.** `X` es la dirección que viene en la instrucción; `M[X]` es el contenido de esa celda; `AC` es el acumulador.

## 2. Contexto

Es la tabla más útil del final: si la sabés, podés responder P03, P06, S10 y S11. Es también la fuente de la pregunta "qué hace cada una". Atención: el **simulador del TP16** usa otra numeración (1, 5, 2, C), que es una ayuda didáctica, no la tabla de la máquina.

## 3. Gráfico

![[S12-operaciones-blue.svg]]

*Lectura:* la tabla con el código en octal, el mnemónico, lo que hace y los pulsos.

## 4. Desarrollo detallado

### 4.1 La tabla de las 16 operaciones

| Octal | Mnemónico | Qué hace | Pulsos |
|---|---|---|---|
| 00 | HLT | detiene la máquina (RUN ← 0) | 8 |
| 01 | ADD | AC ← AC + M[X] | 16 |
| 02 | XOR | AC ← AC ⊕ M[X] | 16 |
| 03 | AND | AC ← AC · M[X] | 16 |
| 04 | IOR | AC ← AC + M[X] (OR inclusiva) | 16 |
| 05 | NOT | AC ← AC' (complemento a uno) | 8 |
| 06 | LDA | AC ← M[X] | 16 |
| 07 | STA | M[X] ← AC | 16 |
| 10 | SRJ | salto a subrutina: AC ← PC + 1, PC ← X | 8 |
| 11 | JMA | salto si AC es negativo (A15 = 1): PC ← X | 8 |
| 12 | JMP | salto incondicional: PC ← X | 8 |
| 13 | INP | AC[7..0] ← dispositivo YY | 16+ |
| 14 | OUT | dispositivo YY ← AC[15..8] | 16+ |
| 15 | RAL | rota el AC a la izquierda (AC ← 2·AC) | 8 |
| 16 | CSA | AC ← registro de llaves (SR) | 8 |
| 17 | NOP | no hace nada | 8 |

### 4.2 Cómo recordarlas (agrupadas)
- **Memoria:** LDA (06), STA (07).
- **Aritmética-lógica:** ADD (01), XOR (02), AND (03), IOR (04), NOT (05), RAL (15).
- **Control:** JMP (12), JMA (11), SRJ (10), HLT (00), NOP (17).
- **E/S:** INP (13), OUT (14).
- **Registros:** CSA (16).

### 4.3 Detalle de algunas
- **IOR** es la OR inclusiva (OR bit a bit). En la nota de la cátedra su microoperación aparece escrita como `AC + M[X]`, lo que es confuso porque se parece a la suma. En el final respondé: "IOR hace OR inclusiva bit a bit del AC con M[X]", y mencioná el detalle de la notación si te lo preguntan.
- **RAL** rota: el bit que sale por la izquierda vuelve por la derecha (rotación cíclica).
- **JMA** salta sólo si el bit de signo (A15) vale 1.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "BLUE tiene 16 instrucciones de 4 bits de opcode, en octal de 00 a 17."
2. **Tabla:** las 16 con su microoperación.
3. **Agrupación:** memoria, lógica, control, E/S.
4. **Cierre:** "Todas operan sobre el AC, excepto los saltos, que operan sobre el PC."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuál es el código de LDA en octal? | 06. |
| ¿Cuál es el código de HLT? | 00. |
| ¿Por qué el simulador tiene otros códigos? | Es una ayuda didáctica del TP16, no la tabla de la máquina. |
| Error común | Decir que BLUE tiene 16 opcodes de 5 bits. Eso es la BLUE indexada. |

## 7. Relacionado

- [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]
- [[TP20 Lenguaje máquina]] · [[P06 Ciclo de ejecución BLUE indexada y sin indexar]]
