---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T06 · Conjunto de instrucciones, registro de instrucción y 3 ejemplos

> [!question] Pregunta
> Describa el conjunto de instrucciones de BLUE, qué es el registro de instrucción (IR) y explique tres ejemplos de instrucciones paso a paso.

## 1. Teoría previa

**Conjunto de instrucciones (ISA).** Es el repertorio de operaciones que la CPU entiende. En BLUE son **16 instrucciones**, con un opcode de 4 bits.

**Registro de instrucción (IR).** Es el registro de 16 bits donde queda la instrucción que se está ejecutando. La UC **decodifica** el IR:
- **IR15…IR12**: opcode (4 bits). Es lo que la UC mira para decidir qué hacer.
- **IR11…IR0**: dirección (12 bits). Es lo que va al MAR en la ejecución, o al PC en un salto.

**Formato de instrucción de BLUE.** `opcode 4 + dirección 12`, una palabra de 16 bits.

**Notación octal.** La tabla de la cátedra usa octal: `06` = LDA, `07` = STA, `01` = ADD, `12` = JMP, `00` = HLT. Como 06 octal = 6 decimal = 0110 binario, el opcode de LDA es `0110`.

## 2. Contexto

Esta pregunta une el IR (registro), el conjunto de instrucciones (16 operaciones) y los ejemplos paso a paso. Es la práctica donde se ve que sabés **leer** una instrucción en binario, en hexadecimal y en su significado.

## 3. Gráfico

![[T06-registro-instruccion.svg]]

*Lectura:* arriba, el IR dividido en opcode (4 bits, rosa) y dirección (12 bits, celeste). Abajo, tres ejemplos en binario, hexadecimal y microoperación.

## Figuras reales (libros y resumen de cátedra)

![[catedra-said-formato-ri.png]]

*Corte del registro de instrucción: opcode 15..12 y dirección 11..0.* · Resumen de cátedra (Said)

![[catedra-said-16-instrucciones-nombres.png]]

*Los 16 nombres de instrucción de la BLUE.* · Resumen de cátedra (Said)

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Ejemplo 1: `LDA 500` (dirección hexadecimal 500)

- Opcode LDA = 06 octal = `0110`.
- Dirección 500 hexadecimal = `0101 0000 0000`.
- Instrucción completa: `0110 0101 0000 0000` = **6500 hex**.
- Microoperaciones: `IR(dir) → MAR`, lectura, `MBR → AC`. Es decir, `AC ← M[500]`.

### 4.2 Ejemplo 2: `ADD 501`

- Opcode ADD = 01 octal = `0001`.
- Dirección 501 = `0101 0000 0001`.
- Instrucción: `0001 0101 0000 0001` = **1501 hex**.
- Microoperación: `AC ← AC + M[501]`.

### 4.3 Ejemplo 3: `STA 502`

- Opcode STA = 07 octal = `0111`.
- Dirección 502 = `0101 0000 0010`.
- Instrucción: `0111 0101 0000 0010` = **7502 hex**.
- Microoperación: `M[502] ← AC`.

### 4.4 Ejemplo extra: `JMP 100`

- Opcode JMP = 12 octal = `1010`.
- Dirección 100 hex = `0001 0000 0000`.
- Instrucción: `1010 0001 0000 0000` = **A100 hex**.
- Microoperación: `PC ← 100`. No pasa por el AC.

### 4.5 Cómo se usa el IR en el ciclo
1. En CP6 de la búsqueda, `MBR → IR`.
2. En CP7, la UC decodifica IR15…IR12.
3. En la ejecución, `IR11…IR0 → MAR` (o `→ PC` si es un salto).

## 5. Cómo se responde (4 minutos)

1. **Definición:** "El conjunto de instrucciones es el repertorio de 16 operaciones; el IR guarda la instrucción actual."
2. **Dibujo:** el IR con opcode y dirección.
3. **Ejemplos:** LDA, ADD, STA paso a paso, con su microoperación.
4. **Cierre:** "El opcode dice qué hacer; la dirección dice dónde."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántos bits tiene el IR? | 16. |
| ¿Qué bits decodifica la UC? | Los 4 del opcode (IR15…IR12). |
| ¿Cuál es el opcode de STA? | 07 octal = 0111. |
| Error común | Confundir el octal de la tabla con el decimal. 07 octal es 7 decimal. |

## 7. Relacionado

- [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Programar en BLUE — ejemplos]] · [[Registros de la CPU]]
- [[S12 Operaciones de máquina BLUE]] · [[P01 Flujo de información (datos y direcciones)]]
