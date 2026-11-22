---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# Interrupciones y entrada/salida

> [!abstract] En una frase
> Una **interrupción** es un pedido de atención que **rompe la secuencia** del programa: la CPU **termina la
> instrucción en curso**, **guarda el contexto**, salta a una **rutina de servicio**, la ejecuta y **retorna**
> como si nada hubiera pasado. Existe porque la CPU es **millones de veces más rápida** que un periférico:
> esperarlo (E/S por consulta, *polling*) es desperdiciarla.

> [!note] Si es la primera vez que ves esto
> Imaginá que estás estudiando (tu programa) y suena el timbre (el periférico). Tenés dos maneras de atender:
> **(a)** cada dos renglones levantás la cabeza y mirás la puerta —eso es *polling*: no te perdés nada, pero
> perdés medio estudio—; **(b)** seguís estudiando y cuando suena el timbre dejás el marcador en el libro, abrís,
> volvés y seguís desde el marcador —eso es **interrupción**: no perdés tiempo, pero necesitás el marcador (el
> **contexto**) y una regla para que no te interrumpan dos veces a la vez (la **máscara** y las **prioridades**).
> Ese marcador es el **PC**; la rutina que atendés es la **ISR**; volver al libro es el **RTI**.

---

## 1. El problema que resuelve (con números)

| Situación | Tiempo |
|---|---|
| Una instrucción de la CPU | ~1 µs (8 pulsos de 125 ns) |
| Un periférico lento (teclado, cinta, disco) | milisegundos |
| Diferencia | **~1000 a 1 000 000 veces** |

Si la CPU espera al periférico con una instrucción `INP` que no termina hasta que el dispositivo esté listo
(como hace la BLUE, ver [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]), **se queda
inmovilizada** miles de ciclos haciendo nada. Y peor: si el periférico se rompe, **espera para siempre**.

**La solución**: que el periférico **avise** cuando esté listo, y que la CPU siga trabajando mientras tanto.
Eso es una interrupción.

> [!important] La diferencia clave con la E/S por consulta
> | | **E/S por consulta (polling)** | **E/S por interrupción** |
> |---|---|---|
> | Quién inicia | la CPU, y **espera** | la CPU inicia y **sigue**; el periférico avisa |
> | Tiempo perdido | mucho (espera activa) | casi nulo |
> | ¿Quién pregunta? | la **CPU** pregunta una y otra vez | el **periférico** avisa |
> | Si el dispositivo falla | la CPU espera eternamente | no pasa nada (nunca llega el pedido) |
> | Hardware necesario | mínimo | líneas de pedido, biestables, prioridades |

---

## 2. Tipos de interrupción

| Criterio | Tipos | Ejemplo |
|---|---|---|
| **Origen** | **de hardware** (externas) | teclado, disco, timer |
| | **de software** | la instrucción `INT n` |
| | **internas** (excepciones) | división por cero, desborde, **código de operación inválido**, fallo de página, desborde de pila |
| **¿Se pueden deshabilitar?** | **enmascarables** | las de los periféricos (se tapan con la máscara) |
| | **no enmascarables (NMI)** | falla de alimentación, error de memoria: **no se pueden** tapar |
| **¿Se pueden anidar?** | normales | una interrupción que interrumpe a otra |
| **Identificación** | **polling** (preguntar bandera por bandera) | la BLUE de la cátedra |
| | **vectorizadas** (el dispositivo entrega su vector) | el 8086, las PCs |

---

## 3. La secuencia de atención, paso a paso (la respuesta que se espera)

1. **El periférico pide**: pone su línea de pedido en 1 (en la BLUE, la bandera del dispositivo va a la **OR**
   que produce `IRQ`).
2. **La CPU termina la instrucción en curso**: la interrupción se acepta **al final** de la instrucción, nunca
   en el medio (si no, se perdería un estado intermedio).
3. **Verifica que esté habilitada**: hace falta que el flip-flop de habilitación esté en 1 (`SI` en la BLUE, el
   flag **IF** en el 8086).
4. **Reconoce el pedido**: genera la señal de reconocimiento (`INTACK` / `ACK`).
5. **Guarda el contexto**: al menos el **PC** (la dirección de la próxima instrucción, que ya está calculada) y,
   en máquinas reales, los **flags** y los registros que la rutina vaya a usar.
6. **Identifica la fuente**: por *polling* (la rutina pregunta bandera por bandera) o por **vector** (el
   dispositivo entrega un número que indexa una **tabla de vectores**; hay un salto **indirecto**).
7. **Salta a la rutina de servicio (ISR)**.
8. **La rutina atiende**: lee o escribe el registro de datos del periférico y **baja el pedido**.
9. **Restaura el contexto** y ejecuta el **retorno de interrupción** (`RTI` / `IRET`), que vuelve a habilitar las
   interrupciones.
10. **El programa sigue** exactamente donde estaba.

> [!tip] La frase que resume por qué es "transparente"
> "La interrupción es útil **sólo si es invisible**: el programa principal no puede notar que lo interrumpieron.
> Por eso lo crítico es guardar y restaurar **el PC, que ya apunta a la instrucción siguiente**."

---

## 4. Prioridades, máscara y anidamiento

**Prioridad** — si dos periféricos piden a la vez, hay que decidir a quién atender primero. Dos formas:
- **Por software**: el **orden en que la rutina consulta las banderas ES la prioridad** (el que se pregunta
  primero gana).
- **Por hardware**: un **codificador con prioridad** o el **encadenado de ACK** (el dispositivo más cercano a la
  CPU en la cadena tiene prioridad).

**Máscara** — un registro donde cada bit habilita o tapa un pedido. Sirve para:
- que ciertas interrupciones no molesten en momentos críticos,
- **cambiar dinámicamente la prioridad**,
- que una rutina de mayor prioridad no sea interrumpida por una de menor.

**Anidamiento** — atender una interrupción **dentro** de otra. Requiere guardar el contexto en una **pila (LIFO)**
con un **puntero de pila (SP)**: sin pila, la segunda interrupción **pisaría** la dirección de retorno de la
primera. Con pila: se apila todo, se atiende, y cada retorno va desapilando.

---

## 5. El sistema de interrupciones que agrega la cátedra a la BLUE indexada

> [!note] Dato que conviene decir primero
> **La BLUE original no tiene interrupciones** (el apunte de Foster lo dice expresamente: no tiene registros
> índice, ni direccionamiento indirecto, ni interrupciones). La cátedra las **agrega** sobre la BLUE indexada.

| Elemento | Función |
|---|---|
| **SI** | flip-flop que **habilita/inhabilita** el sistema (1 = habilitado). Se maneja con **ION** e **IOF** |
| **IRQ** | pedido único: es la **OR** de las "banderas de dispositivo" |
| **I** | biestable auxiliar que marca que **se está atendiendo** una interrupción |
| **Estados F / E / I** | búsqueda, ejecución e **interrupción** |
| **SKF X** | "omitir la próxima instrucción si la bandera X es 0" (sirve para el *polling*) |
| **EMR** | carga el **registro máscara** |
| **RTI** | retorno de interrupción: recupera el PC y vuelve a poner `SI = 1` |
| **SP** | puntero de pila (permite **anidamiento**) |
| **ACK** | reconocimiento, encadenado entre dispositivos (vectorizadas) |

**Cuándo se acepta**: con `IRQ = 1`, `SI = 1` y **CP8 estando en estado E**. Es decir: **al final de la
instrucción**, nunca en el medio.

**El ciclo de interrupción (8 pulsos)**:
| Pulso | Acción | Para qué |
|---|---|---|
| CP1 | **SI ← 0** | se deshabilita: evita que otra interrupción lo interrumpa |
| CP2 | Envíe PC, Cargue MBR | se guarda la dirección de retorno |
| CP3 | Envíe 0, Cargue MAR, **orden de escritura** | el PC queda guardado en la **posición CERO** |
| CP4 | Envíe 1, Cargue PC | la rutina de servicio empieza en la **posición 1** |
| CP5-CP7 | — | la rutina ya corre (guardar contexto, identificar la fuente) |
| CP8 | **I ← 0** | termina el reconocimiento |

**La rutina hace tres cosas**: guarda el contexto, **determina quién interrumpió** (polling con `SKF`/`JMP`),
atiende al dispositivo. Al final, **RTI**: `PC ← M[0]` y `SI ← 1`.

**Polling en la rutina**:
```
SKF 1          ; ¿bandera 1 en 1? si está en 0, omite la próxima
JMP Rutina1    ; atiende al dispositivo 1
SKF 2
JMP Rutina2
...
```
**El orden de las consultas es la prioridad.**

**Vectorizadas**: cada dispositivo tiene un **vector** (dirección); cuando la CPU da **ACK**, el dispositivo
**pone el vector en el bus** y se hace un **salto indirecto** a través de la tabla de vectores. Es **más rápido**
que el polling, y la prioridad la resuelve el **encadenado de ACK**.

---

## 6. E/S: lo mínimo que se pregunta

| Concepto | Qué es |
|---|---|
| **E/S programada (por consulta)** | la CPU inicia la operación y **espera**; inmoviliza el procesador |
| **E/S por interrupción** | la CPU inicia, sigue trabajando y el periférico avisa al terminar |
| **DMA** (acceso directo a memoria) | un controlador mueve bloques entre memoria y periférico **sin la CPU**; al terminar, interrumpe |
| **E/S mapeada en memoria** | los registros del periférico se direccionan como si fueran celdas de memoria |
| **E/S aislada (puertos)** | hay un espacio de direcciones aparte para los puertos (instrucciones `IN`/`OUT`) |
| **Transmisión paralela vs serie** | todos los bits a la vez (rápida, corta distancia) o bit a bit (lenta, larga distancia) |

En la BLUE: **E/S aislada**, por acumulador, con `INP` (8 bits al AC) y `OUT` (8 bits altos del AC), **6 líneas
de selección de dispositivo** (hasta 64 periféricos) y la línea **R** (ready).

---

## 7. Cómo responderlo en el final (3–4 minutos)

**Movimiento 1 — el porqué (20 s).** "La CPU es miles de veces más rápida que el periférico. Esperar
(polling) es desperdiciarla; la interrupción permite que el periférico avise cuando terminó."

**Movimiento 2 — el dibujo (60 s).** La línea `IRQ` entrando a la CPU; el flip-flop `SI`; la caja "guardar
contexto"; la rutina; el `RTI`. Y los tres estados **F / E / I**.

**Movimiento 3 — la secuencia (90 s).** Los 10 pasos, recalcando: **se acepta al final de la instrucción**,
**se guarda el PC**, **se identifica la fuente** (polling o vector), **se atiende**, **se restaura**, **`RTI`**.

**Movimiento 4 — los extras que suben nota (40 s).**
1. **Prioridades**: por orden de consulta (software) o por codificador/ACK encadenado (hardware).
2. **Máscara**: permite tapar pedidos y cambiar prioridades.
3. **Anidamiento**: requiere **pila**; sin pila se pierde la dirección de retorno.
4. **En la BLUE de la cátedra**: `SI`, `IRQ`, posición CERO para el PC, rutina en 1, `SKF`, `EMR`, `RTI`,
   ciclo de interrupción de 8 pulsos.
5. **En el 8086**: flag `IF`, vector de interrupciones, `IRET`, NMI.

**Movimiento 5 — cierre (20 s).** "Lo que hace útil a la interrupción es ser **transparente**: el programa
principal no se entera. Y lo que la hace posible es guardar y restaurar el **contexto**."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Puede interrumpirse en medio de una instrucción? | **No**: se acepta al final (CP8 del estado E). Si no, se perdería un estado intermedio |
| ¿Qué se guarda exactamente? | Como mínimo el **PC** (ya incrementado); en máquinas reales, también **flags** y registros usados |
| ¿Por qué el PC ya apunta a la siguiente instrucción? | Porque se incrementó en la búsqueda (CP4). Al retornar, hay que volver **ahí** |
| ¿Cómo se identifica el dispositivo? | **Polling** (preguntar banderas) o **vectorizado** (el dispositivo entrega su vector) |
| ¿Qué pasa si llegan dos pedidos a la vez? | Se resuelve por **prioridad** (orden de polling o cadena de ACK) |
| ¿Diferencia entre interrupción y excepción? | La interrupción viene **de afuera**; la excepción es **interna** (división por cero, opcode inválido, fallo de página) |
| ¿Y el DMA? | El controlador transfiere **sin la CPU** y avisa al terminar con una interrupción |
| ¿En qué se diferencia de una subrutina? | La subrutina la llama **el programa** (`CALL`, `SRJ`); la interrupción la dispara **un evento externo**, en un momento impredecible |

---

## 8. Errores típicos
- Decir que la interrupción "corta" la instrucción en el medio.
- Olvidar **guardar el PC** (o guardar el PC **antes** de incrementarlo).
- Confundir **polling** (la CPU pregunta) con **interrupción** (el periférico avisa); y confundir el *polling de
  identificación* dentro de la rutina con la *E/S por consulta*.
- Decir que la máscara "elimina" la interrupción: la **posterga / no le da curso**.
- Pensar que en la BLUE original hay interrupciones: **no las tiene**, las agrega la cátedra.
- Confundir **RTI** (retorno de interrupción, restaura flags y habilita) con **RET** (retorno de subrutina).

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 5* | secciones **"Interrupciones"**, **"Manejo de E/S bajo control del procesador"**, **"Sistema elemental de interrupciones para BLUE indexada"** e **"Interrupciones vectorizadas"** | SI, IRQ, estados F/E/I, el ciclo de interrupción de 8 pulsos, `SKF`/`EMR`/`RTI`, el encadenado de ACK, el registro máscara | **Es la fuente exacta** de esta pregunta |
| **`blue.pdf`** (Foster) | **"Instrucciones de entrada y salida"** (Tabla 4 y fig. 12) y las **Conclusiones** | cómo funciona la E/S por consulta con `TRA` y `R`; la frase "no existen interrupciones" en la BLUE | El punto de partida: entender **qué problema** resuelve la interrupción |
| **[[TP14 Buses]]** | el TP | las líneas de control: **petición de interrupción**, petición/cesión de bus | Vocabulario de la cátedra |
| **[[TP16 Ciclo de instrucción básico]]** | el TP | el ciclo con `INP`/`OUT` y la espera del periférico | Ver el problema en concreto |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **entrada/salida** (interrupciones, DMA, canales, prioridades) | el ciclo de interrupción completo, el hardware de prioridades (8259), DMA | **La mejor ampliación**: cubre todo lo que el apunte deja en "sistema elemental" |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **entrada/salida** | interrupciones, vectores, anidamiento y buses | Formalización con ejercicios |
| **Tanenbaum, *Estructura de computadores*** | capítulos de **E/S** e **interrupciones** | tipos, reconocimiento, máscaras, DMA | Explicaciones claras y comparaciones |
| **Brey, *Los microprocesadores Intel 8086/8088*** | capítulo de **interrupciones del 8086** | `IF`, `INTR`/`NMI`, `INTA`, tabla de vectores, `IRET`, el 8259 | El ejemplo concreto que menciona el TP21 |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo de **excepciones e interrupciones** | excepciones, `EPC`, causas, cuándo se acepta | El punto de vista moderno (excepciones) |
| **[[El 8086 como CPU convencional (TP21)]]** | la nota de la bóveda | el flag IF y los vectores del 8086 | Conectar con la CPU real |

---

## Relacionado
[[Estructura básica de un computador]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] ·
[[Ciclo de máquina]] · [[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Unidad de Control]] ·
[[El 8086 como CPU convencional (TP21)]] · [[Técnicas para aumentar la velocidad]]
