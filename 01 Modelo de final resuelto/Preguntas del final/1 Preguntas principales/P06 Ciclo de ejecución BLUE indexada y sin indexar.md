---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P06 · Ciclo de ejecución de BLUE indexada y BLUE sin indexar

> [!question] Pregunta
> Describa el ciclo de ejecución de una instrucción en BLUE indexada y en BLUE sin indexar. Explique cómo se calcula la dirección efectiva y cuántos pulsos cuesta el LDA.

## 1. Teoría previa

**Dirección efectiva (EA).** Es la dirección real del operando, después de aplicar el modo de direccionamiento. En BLUE sin indexar, `EA = campo de dirección`. En BLUE indexada, la EA se calcula con el **sumador de direcciones**.

**BLUE sin indexar.** Formato `opcode 4 + dirección 12` (16 bits). Un solo modo: directo. Cada instrucción de memoria tiene 2 ciclos: búsqueda y ejecución, es decir, 16 pulsos.

**BLUE indexada.** Formato `opcode 5 + dirección 16 + modificador 2`, en una o dos palabras. Tiene **cuatro modos** según el modificador:

| Modificador | Modo | EA | Ejemplo |
|---|---|---|---|
| 0 | directo | `EA = D` | LDA 0, D |
| 1 | indirecto | `EA = M[D]` (dos accesos) | LDA 1, D |
| 2 | indexado por RIF | `EA = D + RIF` | LDA 2, D |
| 3 | indexado por RID | `EA = D + RID` | LDA 3, D |

**Registros nuevos.**
- **RIF** (índice fuente) y **RID** (índice destino): 16 bits, los carga el programador (`ENI`, `INI`).
- **RB** (registro base): desplazamiento global, lo carga el sistema. Se suma siempre.
- **W** y **X**: entradas del sumador de direcciones. No los ve el programador.

**Sumador de direcciones.** Dispositivo dedicado que calcula `Σ = W + X` sin usar la ALU. El campo de dirección entra por W, el índice por X, y el resultado va al MAR.

**Pulso.** Cada CP (CP1…CP8) es un pulso de reloj. Cada ciclo de máquina son 8 pulsos.

## 2. Contexto

Esta pregunta es el **núcleo** del final: une formato, registros, modos y pulsos. El profesor la pide como "ciclo de ejecución de BLUE indexada y sin indexar" y, como la matriz la marca como principal, espera que dibujes el camino de datos y expliques el LDA pulso por pulso. Es donde se nota si entendiste la máquina o si sólo memorizaste.

## 3. Gráfico

![[P06-blue-indexada.svg]]

*Lectura:* arriba, el formato nuevo (5 + 16 + 2 + 9 sin uso). En el medio, el sumador de direcciones recibe el campo de dirección (por W) y el índice (por X) y entrega la EA. Abajo, la tabla de los 3 ciclos del LDA con modo indexado.

## 4. Desarrollo detallado

### 4.1 BLUE base (sin indexar): LDA en 16 pulsos

En la BLUE base (formato 4 + 12), LDA ocupa **2 ciclos**: búsqueda y ejecución.

| Fase | Microoperaciones |
|---|---|
| Búsqueda (CP1–CP8) | PC → MAR, lectura, MBR → IR, PC + 1, E → STATE |
| Ejecución (CP1–CP8) | IR(dir) → MAR, lectura, MBR → AC, F → STATE |

Total: **8 + 8 = 16 pulsos**. La tabla de la nota 2.5 cuenta así a la familia "operando en memoria" (LDA, STA, ADD, XOR, AND, IOR).

> [!warning] Ojo con el número 24
> Varias notas de estudio dicen "LDA = 24 pulsos (8 de búsqueda + 16 de ejecución)" sin aclarar la máquina. La cifra correcta depende de cuál BLUE:
> - **BLUE base**: LDA = 16 pulsos.
> - **BLUE indexada, modo directo**: LDA = 24 pulsos, porque la instrucción ocupa dos palabras y el ciclo extra lee la segunda (ver 4.2).
> En el final, aclarar siempre a qué máquina se refiere la respuesta.

### 4.2 Indexada: LDA 3, X (RID) en tres ciclos de ocho pulsos

Esta es la tabla que hay que dibujar:

| Ciclo | Pulso | Acción |
|---|---|---|
| **1. Búsqueda** | CP1 | Envíe PC, cargue MAR, Z, orden de lectura |
| | CP2 | Envíe 1, cargue Y |
| | CP4 | Envíe SUMA, cargue PC (apunta a la siguiente) |
| | CP6 | Envíe MBR, cargue IR (la instrucción está en el IR) |
| | CP8 | Pasar a ejecución |
| **2. Ejecución 1** | CP1 | Envíe PC, cargue MAR, orden de lectura (**segunda palabra**) |
| | CP4 | PC + 1 |
| | CP5 | **Envíe RID, cargue X** (el índice entra al sumador) |
| | CP6 | **Envíe MBR, cargue W** (el campo de dirección entra al sumador) |
| | CP8 | Seguir en ejecución |
| **3. Ejecución 2** | CP1 | **Envíe Σ, cargue MAR**, orden de lectura |
| | CP6 | **Envíe MBR, cargue Acc** (el dato entra al acumulador) |
| | CP8 | Estado búsqueda |

**Total: 3 ciclos × 8 pulsos = 24 pulsos.**

### 4.3 Cuántos pulsos cuesta cada modo

| Instrucción | Modo | Ciclos | Pulsos |
|---|---|---|---|
| `LDA 0, X` | directo | 3 | 24 |
| `LDA 1, X` | indirecto | 4 | 32 (un ciclo extra: leer el puntero y después el dato) |
| `LDA 2, X` | indexado RIF | 3 | 24 (en CP5 se carga RIF en X) |
| `LDA 3, X` | indexado RID | 3 | 24 (en CP5 se carga RID en X) |

En el modo directo, en CP5 se carga **0** en X: el índice no participa.

### 4.4 Qué cambia respecto de la BLUE sin indexar

- La búsqueda es **igual**. Lo que cambia es la ejecución: antes el MAR se cargaba desde IR; ahora se carga desde el **sumador**.
- La indexada tiene una ejecución más, porque la dirección se arma en dos pasos: primero se trae el campo, después se suma el índice.
- El **sumador de direcciones** no gasta pulsos de ALU: el resultado está listo cuando el MBR entra por W.

## 5. Cómo se responde (4 minutos)

1. **Definición:** "En BLUE indexada, la búsqueda es igual, y la ejecución calcula la dirección efectiva con el sumador de direcciones."
2. **Dibujo:** formato 5+16+2 y el sumador con W y X, con las flechas MBR → W y RID → X.
3. **Desarrollo:** los tres ciclos del LDA 3 con sus pulsos clave (CP5, CP6, CP1 del tercer ciclo).
4. **Pulsos:** 3 × 8 = 24. Indirecto: 32.
5. **Cierre:** "La indexada no cambia la estructura del ciclo: cambia quién calcula la dirección."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Por qué 24 y no 16? | En la indexada el LDA lee dos palabras: son 3 ciclos de 8 pulsos (búsqueda + 2 de ejecución). En la BLUE base son 2 ciclos = 16. |
| ¿Cuál es la diferencia entre RIF y RB? | RIF lo maneja el programador y sólo se suma con los modos 2 y 3; RB lo carga el sistema y se suma siempre. |
| ¿Cuánto cuesta el indirecto? | 32 pulsos: un acceso extra a memoria. |
| Error común | Decir que el sumador es la ALU. Es un sumador dedicado. |
| Error común | Olvidar que en el modo directo X = 0. |

## 7. Relacionado

- [[Ciclo de LDA indexada (los 24 pulsos)]] · [[BLUE vs BLUE indexada — qué cambia y por qué]] · [[BLUE indexada (RIF, RID, nuevo formato)]]
- [[P03 Ciclo de máquina]] · [[S11 Ciclo LDA (24 pulsos)]] · [[S10 Ciclo de ejecución para todas las operaciones]]
