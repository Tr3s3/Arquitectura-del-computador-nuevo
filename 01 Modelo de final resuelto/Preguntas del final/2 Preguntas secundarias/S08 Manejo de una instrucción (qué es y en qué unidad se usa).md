---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S08 · Proceso de manejo de una instrucción

> [!question] Pregunta
> Describa el proceso de manejo de una instrucción: qué es, en qué unidad se usa y qué pasos tiene.

## 1. Teoría previa

**Instrucción.** Es una palabra de bits que indica una operación y, en general, dónde están sus operandos.

**Manejo de una instrucción.** Es el proceso completo que la CPU sigue desde que la busca en memoria hasta que la ejecuta. Son tres fases:
1. **Búsqueda (fetch):** traer la instrucción de memoria al IR.
2. **Decodificación:** identificar el opcode y los operandos.
3. **Ejecución (execute):** realizar la operación y guardar el resultado.

**Dónde se usa cada fase.**

| Fase | Unidad principal | Registros que intervienen |
|---|---|---|
| Búsqueda | UC (genera las señales) | PC, MAR, MBR, IR |
| Decodificación | UC | IR (el opcode) |
| Ejecución | ALU y UC | AC, Z, Y, MAR, MBR y, en su caso, la memoria |

## 2. Contexto

Esta pregunta es un **resumen de la CPU**: pide que digas qué hace cada unidad en el proceso completo. Se pregunta como "resumen de todo" y el profesor la usa para ver si podés conectar UC, ALU y registros en una sola secuencia.

## 3. Gráfico

![[S08-manejo-instruccion.svg]]

*Lectura:* tres bloques en secuencia: búsqueda, decodificación y ejecución. Debajo de cada bloque, la unidad que lo maneja.

## Figuras reales (libros y resumen de cátedra)

![[libro-stallings-f3-3.png]]

*Fig. 3.3 — Ciclo de instrucción básico.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 84

![[libro-quiroga-f7-10.png]]

*Fig. 7.10 — Fase fetch.* · Quiroga, *Arquitectura de computadoras*, p. 178

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Búsqueda
- `PC → MAR`: la dirección de la instrucción va al MAR.
- Lectura de memoria: la instrucción llega al MBR.
- `MBR → IR`: la instrucción queda en el registro de instrucción.
- `PC + 1`: el PC apunta a la siguiente.

### 4.2 Decodificación
- La UC lee los bits del opcode (IR15…IR12) y decide qué microprograma o qué compuertas activar.
- Si la instrucción necesita un operando de memoria, la UC sabe que tiene que hacer un acceso.

### 4.3 Ejecución
- Según el opcode:
  - **LDA**: `IR(dir) → MAR`, lectura, `MBR → AC`.
  - **ADD**: el operando va a Y, la ALU suma con AC, el resultado va a AC, se actualizan los flags.
  - **JMP**: `IR(dir) → PC`.
  - **HLT**: `RUN ← 0`.
- La UC genera las señales en cada pulso; la ALU y los registros las cumplen.

### 4.4 Quién hace qué (el punto que se pregunta)
- **La UC manda y no calcula.** Genera las señales.
- **La ALU calcula.** Suma, resta, lógica.
- **Los registros guardan.** PC, MAR, MBR, IR, AC.
- **La memoria guarda programa y datos.**

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Es el proceso de búsqueda, decodificación y ejecución de una instrucción."
2. **Dibujo:** tres bloques en secuencia con la unidad debajo.
3. **Desarrollo:** el LDA como ejemplo, con la búsqueda y la ejecución.
4. **Cierre:** "La UC ordena y la ALU ejecuta; la búsqueda es igual para todas."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Quién decodifica? | La UC, a partir del opcode del IR. |
| ¿Quién suma? | La ALU, no la UC. |
| ¿Por qué la búsqueda es igual para todas? | Porque antes de decodificar no se sabe qué instrucción es. |
| Error común | Poner la decodificación como un pulso aparte. Ocurre en CP6–CP7, al cargarse el IR. |

## 7. Relacionado

- [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Proceso de manejo de una instrucción]] · [[Unidad de Control]]
- [[P03 Ciclo de máquina]] · [[P07 Unidad de Control (funciones, señales e importancia)]]
