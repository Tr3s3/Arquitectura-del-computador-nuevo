---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Las 16 instrucciones de BLUE — ciclo completo pulso por pulso

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[Ciclo de búsqueda (7 y 8 pulsos)]] (Tanda 1 · 1.8 Ciclo de máquina y ciclo de instrucción) · [[Ciclo de ejecución — todas las operaciones]] (Tanda 1 · 1.8 Ciclo de máquina y ciclo de instrucción) · [[Ciclo de máquina]] (Tanda 1 · 1.8 Ciclo de máquina y ciclo de instrucción) · [[Máquina BLUE — arquitectura y conjunto de instrucciones]] (Tanda 3 · 3.9 El RI y 3 ejemplos de instrucciones) · [[Cómo se implementa la Unidad de Control]] (Tanda 1 · 1.6 Implementación de la Unidad de Control) · [[Programar en BLUE — ejemplos]] (Materia · Unidad 4)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 2.5 Las 16 instrucciones]].


> [!abstract] En una frase
> **Todas** las instrucciones comparten el mismo **ciclo de búsqueda de 8 pulsos**. Lo que cambia es lo que
> pasa después: **8 instrucciones terminan dentro de esos mismos 8 pulsos** (HLT, NOP, JMP, JMA, SRJ, CSA,
> NOT, RAL), **6 necesitan un segundo ciclo** (LDA, STA, ADD, XOR, AND, IOR) y **2 esperan al periférico**
> (INP, OUT), que pueden repetir el ciclo de ejecución indefinidamente. Total: **8, 16 o más pulsos**.

## Partamos de cero: qué se entiende por "los pulsos"
El reloj de la BLUE divide el tiempo en **pulsos** y agrupa 8 pulsos en un **ciclo de máquina**. En cada pulso
la Unidad de Control activa un conjunto de microórdenes: **"Envíe X"** (un registro pone su contenido en el
bus) y **"Cargue Y"** (un registro toma el contenido del bus). Como en cada pulso **uno habla y los demás
escuchan**, cada línea de la tabla es una transferencia.

Para memorizar esto no hay que estudiar 16 tablas: hay que ver que son **un tronco común (la búsqueda) + una
cola corta distinta**. Las 16 instrucciones se separan en tres familias por **cuánto tardan**:

| Familia | Instrucciones | Ciclos de máquina | Pulsos |
|---|---|---|---|
| **Se resuelven solas** | HLT, NOP, JMP, JMA, SRJ, CSA, NOT, RAL | 1 (sólo búsqueda) | **8** |
| **Van a memoria por el operando** | LDA, STA, ADD, XOR, AND, IOR | 2 | **16** |
| **Hablan con un periférico** | INP, OUT | 2 + n (espera) | **16 o más** |

## El tronco común: ciclo de búsqueda (los 8 primeros pulsos, iguales para las 16)

| Pulso | Acción | Para qué |
|---|---|---|
| **CP1** | Envíe PC, Cargue MAR, Cargue Z · **Orden de lectura** | el PC entrega la dirección de la instrucción |
| **CP2** | Envíe +1, Cargue Y | prepara el incremento del PC en la ALU |
| **CP3** | — | la memoria y la ALU trabajan |
| **CP4** | Envíe SUMA, Cargue PC | `PC ← PC + 1` (apunta a la próxima instrucción) |
| **CP5** | Strobe MBR | el dato de memoria se copia al MBR |
| **CP6** | Envíe MBR, Cargue IR | la instrucción entra al IR y **se decodifica** |
| **CP7** | (según instrucción) | decodificación / primer paso de ejecución |
| **CP8** | (según instrucción) o `E → STATE` | ejecución o pasar a ejecución |

> [!tip] El truco para no olvidarse la búsqueda
> "**PC→MAR** (busco), **+1** (aviso dónde sigo), **espero**, **PC+1**, **guardo** (MBR), **MBR→IR**
> (ya sé qué es), y los dos últimos pulsos son para lo que sobre". Cuatro ideas y siempre las mismas.

## Las 8 que terminan en el mismo ciclo (CP7 y CP8)

| Instrucción (octal) | Qué hace | **CP7** | **CP8** |
|---|---|---|---|
| **HLT** (00) | detiene la máquina | — | **Reset FF RUN** (se apaga RUN) |
| **NOP** (17) | no hace nada | — | — |
| **JMP** (12) | salto incondicional | — | **Envíe IR, Cargue PC** (la dirección va al PC) |
| **JMA** (11) | salto si AC < 0 | — | **Envíe IR, Cargue PC** sólo si **A15 = 1** |
| **SRJ** (10) | salto a subrutina | **Envíe PC, Cargue A** (guarda el retorno en AC) | **Envíe IR, Cargue PC** |
| **CSA** (16) | copia llaves al AC | **Envíe SR, Cargue A** | — |
| **NOT** (05) | complemento a uno del AC | **Envíe A, Cargue Z** | **Envíe Z' (Zbar), Cargue A** |
| **RAL** (15) | rota el AC a la izquierda | **Envíe A, Cargue Z** | **Envíe 2·Z, Cargue A** |

Estas 8 **no cambian el biestable STATE**: se quedan en F (búsqueda), así que el ciclo siguiente es otra
búsqueda. Ninguna va a la memoria a buscar operandos (por eso entran en un solo ciclo).

> [!note] Por qué NOT y RAL usan el par Z → A
> La ALU sólo trabaja sobre **Y** y **Z**. Entonces el dato tiene que pasar del acumulador a Z (CP7), la ALU
> calcula (`Z'` o `2·Z` = desplazamiento) y en CP8 el resultado vuelve al acumulador. Es el mismo truco del
> CP2/CP4: **la ALU siempre recibe por Y o Z y entrega por el bus**.

## Las 6 que necesitan un segundo ciclo (16 pulsos)

Terminan la búsqueda con `CP8: E → STATE` (pasar a ejecución) y hacen un ciclo de ejecución completo:

### LDA — cargar el acumulador
| Fase | CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 |
|---|---|---|---|---|---|---|---|---|
| Búsqueda | PC→MAR, Z, lectura | +1→Y | — | SUMA→PC | Strobe MBR | MBR→IR | — | **E→STATE** |
| Ejecución | **IR→MAR**, lectura | — | — | Strobe MBR | **MBR→A** | — | — | **F→STATE** |

### STA — almacenar el acumulador
| Fase | CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 |
|---|---|---|---|---|---|---|---|---|
| Búsqueda | PC→MAR, Z, lectura | +1→Y | — | SUMA→PC | Strobe MBR | MBR→IR | — | **E→STATE** |
| Ejecución | **IR→MAR** | — | — | **A→MBR**, orden de **escritura** | — | — | — | **F→STATE** |

### ADD / XOR / AND / IOR — las cuatro aritmético-lógicas
| Fase | CP1 | CP2 | CP3 | CP4 | CP5 | CP6 | CP7 | CP8 |
|---|---|---|---|---|---|---|---|---|
| Búsqueda | PC→MAR, Z, lectura | +1→Y | — | SUMA→PC | Strobe MBR | MBR→IR | — | **E→STATE** |
| Ejecución | **IR→MAR**, lectura | **A→Z** | — | — | Strobe MBR | **MBR→Y** | — | **SUMA/XOR/AND/OR → A**, `F→STATE` |

> [!important] La lógica de las cuatro
> En CP2 se guarda el **acumulador en Z**, y en CP6 el **dato de memoria en Y**: la ALU queda con los dos
> operandos en sus dos entradas y en **CP8** hace la operación y el resultado cae en el acumulador. La única
> diferencia entre ADD, XOR, AND e IOR es **qué salida de la ALU se habilita** en CP8.

## Las 2 de entrada/salida (16 pulsos o más)

Usan dos biestables auxiliares: **TRA** (transferencia: indica a los periféricos que hay una operación de E/S
en curso) y la señal **R** (ready: el periférico está listo).

| Fase | CP7 | CP8 |
|---|---|---|
| Búsqueda | **TRA = 1** (se envía IR5-0 por las líneas de selección de dispositivo) | **E → STATE** |
| Ejecución | si **R = 1** → copiar el dato (INP: líneas de entrada → A) y **TRA = 0** | si **TRA = 0** → **F → STATE**; si no, **se repite el ciclo de ejecución** |

- **INP** (13): los 8 bits bajos del AC ← dato del dispositivo `YY`; los 8 altos se ponen en 0.
- **OUT** (14): los 8 bits altos del AC → dispositivo `YY`.
- Si el periférico **no está listo**, la máquina **repite el ciclo de ejecución** hasta que R = 1: la
  instrucción puede tardar **16, 24, 32…** pulsos. Ese es el gran defecto de la E/S por consulta y la razón de
  ser de las **interrupciones** ([[Interrupciones y entrada-salida]]).

## Tabla maestra (la que conviene dibujar en el pizarrón)

| # | Mnem. | Octal | Qué hace | Ciclos | Pulsos | CP7 / CP8 propios |
|---|---|---|---|---|---|---|
| 1 | HLT | 00 | detiene | 1 | 8 | CP8: reset RUN |
| 2 | ADD | 01 | `AC ← AC + M[X]` | 2 | 16 | CP8: SUMA→A |
| 3 | XOR | 02 | `AC ← AC ⊕ M[X]` | 2 | 16 | CP8: XOR→A |
| 4 | AND | 03 | `AC ← AC · M[X]` | 2 | 16 | CP8: AND→A |
| 5 | IOR | 04 | `AC ← AC + M[X]` (lógica) | 2 | 16 | CP8: OR→A |
| 6 | NOT | 05 | `AC ← AC'` | 1 | 8 | CP7: A→Z · CP8: Z'→A |
| 7 | LDA | 06 | `AC ← M[X]` | 2 | 16 | CP5: MBR→A |
| 8 | STA | 07 | `M[X] ← AC` | 2 | 16 | CP4: A→MBR, escritura |
| 9 | SRJ | 10 | subrutina: `AC ← PC`, `PC ← X` | 1 | 8 | CP7: PC→A · CP8: IR→PC |
| 10 | JMA | 11 | salto si `A15 = 1` | 1 | 8 | CP8: IR→PC condicional |
| 11 | JMP | 12 | salto | 1 | 8 | CP8: IR→PC |
| 12 | INP | 13 | entrada de 8 bits | 2+n | 16+ | CP7 búsqueda: TRA=1 · espera R |
| 13 | OUT | 14 | salida de 8 bits | 2+n | 16+ | ídem |
| 14 | RAL | 15 | rota a la izquierda | 1 | 8 | CP7: A→Z · CP8: 2Z→A |
| 15 | CSA | 16 | llaves → AC | 1 | 8 | CP7: SR→A |
| 16 | NOP | 17 | nada | 1 | 8 | — |

> [!tip] Contar de un vistazo
> **8 de 8 · 6 de 16 · 2 de 16+**. Suma de todas: 8×8 + 6×16 + 2×16 = 64 + 96 + 32 = **192 pulsos** para
> ejecutar el juego completo una vez (sin contar las esperas de E/S).

> [!warning] Sobre los códigos de operación
> Esta tabla usa los códigos **octales del apunte de la cátedra** (Foster, *Computer Architecture*):
> `00 HLT, 01 ADD, 02 XOR, 03 AND, 04 IOR, 05 NOT, 06 LDA, 07 STA, 10 SRJ, 11 JMA, 12 JMP, 13 INP, 14 OUT,
> 15 RAL, 16 CSA, 17 NOP`. Es la fuente que usan los apuntes y la versión indexada.
> Ojo: **el simulador del [[TP16 Ciclo de instrucción básico|TP16]] usa números decimales simples** (`1` cargar,
> `5` sumar, `2`/`3` almacenar). Si en el oral aparece esa numeración, aclaralo: "según el simulador del TP…
> / según la tabla octal de la máquina…". **Lo que se evalúa es la secuencia de pulsos, no el número.**

## BLUE indexada: cuántos pulsos cambian
En la BLUE indexada la instrucción ocupa **2 palabras**, así que las que **referencian memoria** suman un ciclo
(y en el indirecto, dos). Recorrido completo en [[Ciclo de LDA indexada (los 24 pulsos)]].

| Instrucción | BLUE | BLUE indexada |
|---|---|---|
| LDA / STA (directo o indexado) | 16 | **24** |
| LDA / STA (indirecto) | — | **32** |
| ADD / XOR / AND / IOR | 16 | 24 (32 indirecto) |
| HLT, NOP, JMP, JMA, SRJ, CSA, NOT, RAL | 8 | 8 |
| INP / OUT | 16+ | 16+ |

## Cómo responderlo en el final (5–6 minutos)
1. **Encuadre**: "todas comparten el ciclo de búsqueda de 8 pulsos; la diferencia es cuántos ciclos de
   ejecución necesitan".
2. **Dibujo**: la barra de 8 pulsos de la búsqueda con las 6 microórdenes clave, y debajo tres columnas:
   *1 ciclo / 2 ciclos / 2+n*.
3. **La tabla de las 8 de un ciclo** (CP7 y CP8), que es la que demuestra que entendiste el bus: **la ALU
   recibe por Y y Z, y el resultado vuelve por el bus**.
4. **Las 6 de dos ciclos**: LDA y STA en detalle (son las que se piden), y las cuatro aritméticas con su
   `CP2: A→Z` / `CP6: MBR→Y` / `CP8: operación→A`.
5. **Las de E/S**: explicar TRA y R, y que pueden repetir el ciclo: eso motiva las **interrupciones**.
6. **Cierre**: "8, 16 o más: el número sale de contar ciclos de máquina de 8 pulsos".

## Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **`blue.pdf`** (Foster, *Una máquina elemental*) | **Tabla 2** ("El ciclo de búsqueda"), y las secciones "Instrucciones de E/S" e "Instrucciones de dos ciclos" | la tabla pulso por pulso de **cada** instrucción, con el nombre exacto de las señales de control | **Es la fuente literal** de esta pregunta: si sabés leer la tabla, sabés la respuesta |
| **Apuntes de cátedra**, *Unidad 5* | sección de la **BLUE** y de la **unidad de control** | el repertorio y la lógica de `estado · pulso · instrucción` | Alineación con el vocabulario de la cátedra |
| **[[Máquina BLUE — arquitectura y conjunto de instrucciones]]** | nota de la bóveda | el repertorio completo con opcodes octales y qué hace cada instrucción | La referencia rápida antes de los pulsos |
| **[[Ciclo de búsqueda (7 y 8 pulsos)]]** · **[[Ciclo de máquina]]** | notas de la bóveda | el tronco común de CP1-CP8 y por qué son 8 pulsos de 125 ns | Prerrequisito: sin esto, los pulsos no significan nada |
| **[[Cómo se implementa la Unidad de Control]]** | nota de la bóveda | cómo de `estado · pulso · instrucción` salen las señales | El "por qué" detrás de cada pulso |
| **[[Ciclo de la instrucción LDA (24 pulsos)]]** y **[[Ciclo de LDA indexada (los 24 pulsos)]]** | notas de la bóveda | el detalle fino de la instrucción que más se pregunta | Para bajar al caso concreto |
| **[[TP16 Ciclo de instrucción básico]]** · **[[TP17 Formato básico de instrucciones]]** | los TPs | los diagramas de pulsos y el formato que se entregaron | Modelo de lo que se espera dibujar |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **unidad de control** | el esquema de señales por paso y por instrucción | Formaliza el método |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **control cableado** | implementación con señales temporizadas | Ejercicios equivalentes |

## Errores típicos
- Poner `A → Z` en ADD en CP2 **y** en CP6 (son pulsos distintos, Z y Y).
- Darle ciclo de ejecución a JMP: el salto se resuelve en **CP8 de la búsqueda** (`IR → PC`).
- Decir que HLT apaga el reloj: **resetea el FF RUN**.
- Olvidar que **LDA y STA** son las únicas que *cargan/guardan* el acumulador contra memoria sin operar.
- Confundir **SRJ** (guarda el PC en el AC) con **JMP** (no guarda nada).

## Relacionado
[[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] ·
[[Ciclo de ejecución — todas las operaciones]] · [[Ciclo de LDA indexada (los 24 pulsos)]] ·
[[Cómo se implementa la Unidad de Control]] · [[Programar en BLUE — ejemplos]]
