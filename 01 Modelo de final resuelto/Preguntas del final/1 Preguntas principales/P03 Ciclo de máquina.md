---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P03 · Ciclo de máquina

> [!question] Pregunta
> Explique el ciclo de máquina: qué fases tiene, cómo se controla con RUN y STATE, y cuánto tarda.

## 1. Teoría previa: tres ciclos que no son lo mismo

Antes de responder hay que distinguir tres términos. Es el error número uno del tema.

| Término | Qué es | Duración en BLUE |
|---|---|---|
| **Ciclo de reloj (pulso)** | un tic del reloj; en cada tic se ejecuta **una** microoperación | 125 ns |
| **Ciclo de máquina** | 8 pulsos seguidos: una **búsqueda** o una **ejecución** | 8 × 125 ns = 1 µs |
| **Ciclo de instrucción** | todo lo que tarda una instrucción: 1 búsqueda + 1 o más ejecuciones | de 8 a 24 pulsos |

**Los biestables que gobiernan todo:**

| Biestable | Significado | Se pone en 1 | Se pone en 0 |
|---|---|---|---|
| **RUN** | la máquina está andando | START | STOP, HLT, overflow |
| **STATE** | F = búsqueda, E = ejecución | al final de una búsqueda que necesita ejecución | al final de una ejecución |
| **TRA** | hay una E/S en curso | CP7 de INP/OUT | el periférico terminó |

**Microoperación.** Es una transferencia o una operación elemental (`MAR ← PC`, `AC ← AC + M`). Cada pulso ejecuta una.

## 2. Contexto

El ciclo de máquina es **la unidad de trabajo** de la CPU. Todo lo que hace el procesador se descompone en pulsos. Si esta pregunta sale, el profesor quiere ver si podés conectar **reloj, estado y control** en una sola explicación. Es la base de P06 (LDA indexada), S09 (pulsos de búsqueda) y S10 (ciclos por familia).

## 3. Gráfico

![[P03-ciclo-de-maquina.svg]]

*Lectura:* mientras RUN = 1, la máquina repite búsqueda → decodificación → ejecución. Si la instrucción no necesita ejecución (por ejemplo JMP), vuelve directamente a la búsqueda. HLT pone RUN = 0 y la máquina se detiene.

## Figuras reales (libros y resumen de cátedra)

![[libro-stallings-f3-3.png]]

*Fig. 3.3 — Ciclo de instrucción básico.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 84

![[libro-stallings-f3-6.png]]

*Fig. 3.6 — Diagrama de estados del ciclo de instrucción.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 87

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 La búsqueda (fetch), siempre igual

| Pulso | Microoperación | Por qué |
|---|---|---|
| CP1 | PC → MAR, PC → Z, orden de lectura | la memoria tarda: hay que pedir cuanto antes |
| CP2 | 1 → Y | prepara el incremento del PC en la ALU |
| CP3 | (espera) | la memoria y la ALU trabajan |
| CP4 | SUMA → PC | PC ← PC + 1: apunta a la siguiente instrucción |
| CP5 | strobe MBR | el dato ya está estable en el bus |
| CP6 | MBR → IR | la instrucción entra al IR y empieza la decodificación |
| CP7 | decodificación | la UC identifica el opcode |
| CP8 | E → STATE (si hace falta ejecutar) | pasa a ejecución o queda en F |

### 4.2 La ejecución, depende del opcode

- **LDA:** IR(dir) → MAR, lectura, MBR → AC. Dos pulsos de ejecución (ver P06 y S11).
- **ADD:** operando → Y, SUMA → AC, flags.
- **JMP:** IR(dir) → PC en CP8. No hay ejecución extra, por eso dura 8 pulsos.
- **HLT:** RUN ← 0 en CP8. El reloj se detiene.

### 4.3 El reloj y el control

- Si RUN = 0, el reloj no avanza. La máquina queda congelada en el estado en que estaba. Con START se reanuda.
- Cada registro tiene un retardo de carga (10–15 ns) para que el dato esté estable antes de copiarse.
- Al final de los 8 pulsos, si RUN = 1, arranca un nuevo ciclo.

### 4.4 Ejemplo resuelto

Un programa con `LDA 500`, `ADD 501`, `STA 502`:
- Cada instrucción tiene una búsqueda (8 pulsos) y una ejecución (8 o 16 pulsos).
- Como LDA, ADD y STA necesitan memoria, cada una cuesta 2 ciclos (16 pulsos).
- Total: 3 × (8 + 8) = 48 pulsos, o 6 ciclos de máquina.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Es la unidad de trabajo de la CPU: búsqueda, decodificación y ejecución, repetidas mientras RUN = 1."
2. **Dibujo:** el lazo búsqueda ↔ ejecución con STATE F/E.
3. **Desarrollo:** los 8 pulsos de la búsqueda y la diferencia de la ejecución según el opcode.
4. **Control:** RUN, STATE, CLOCK.
5. **Cierre:** "La búsqueda es igual para todas las instrucciones, por eso se puede cablear en la UC."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué pasa si aprieto STOP en medio de un ciclo? | RUN = 0, el reloj se congela. Con START sigue y no se corrompe nada. |
| ¿Quién pone RUN en 0? | STOP, la instrucción HLT (en CP8) y el overflow de la ALU. |
| ¿Cuándo se incrementa el PC? | En la búsqueda, CP4, usando la ALU. |
| ¿Por qué 8 pulsos y no 7? | Porque el pulso 5 es de espera de memoria; el trabajo real son 7 pasos. |
| Error común | Decir que HLT "apaga el reloj". Apaga RUN; el oscilador sigue. |
| Error común | Decir que LDA dura 8 pulsos. En BLUE son 16 sin indexar y 24 indexada. |

## 7. Relacionado

- [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]
- [[P07 Unidad de Control (funciones, señales e importancia)]] · [[S09 Pulsos del ciclo de búsqueda (7 y 8 pulsos)]] · [[S11 Ciclo LDA (24 pulsos)]]
