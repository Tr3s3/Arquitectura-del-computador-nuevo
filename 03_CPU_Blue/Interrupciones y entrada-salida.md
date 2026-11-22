---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# Interrupciones y entrada/salida

> [!abstract] En una frase
> Una **interrupción** es un pedido de atención que **rompe la secuencia normal** del programa: la CPU
> termina la instrucción en curso, **guarda el contexto**, salta a una **rutina de servicio**, y al
> terminar **restaura** el contexto y sigue como si nada. Sirve para atender periféricos sin que la CPU se
> quede esperando (polling).

## El problema: la CPU es 10⁶ veces más rápida que el periférico
| Técnica | Cómo funciona | Costo |
|---|---|---|
| **Polling (consulta)** | la CPU pregunta en un lazo "¿tenés un dato?" | **desperdicia** toda la CPU esperando |
| **Interrupción** | el periférico **avisa** cuando tiene un dato | la CPU trabaja mientras tanto |
| **DMA** | el periférico escribe directo en memoria sin la CPU | óptimo para bloques grandes |

## Secuencia de una interrupción (la respuesta completa)
1. El periférico activa la línea **INT**.
2. La CPU **termina la instrucción en curso** (no se interrumpe a mitad de una microoperación).
3. Comprueba que **las interrupciones están habilitadas** (flag `I` / señal `SI`).
4. **Guarda el contexto**: el PC (y los flags/registros que la rutina vaya a usar) en la **pila** o en
   registros de respaldo.
5. **Identifica la fuente**: por *polling* (consultando a cada periférico) o **vectorizada** (el periférico
   o el controlador entrega el número de vector).
6. Carga en el PC la **dirección de la rutina de servicio** (ISR) y salta.
7. La rutina atiende el periférico (leer/escribir el registro de datos, bajar la señal de pedido).
8. **Restaura el contexto** y ejecuta la instrucción de retorno (`RETI` / `IRET`), que además **habilita de
   nuevo** las interrupciones.

> [!important] Por qué hay que guardar el PC
> Porque el PC ya apunta a la instrucción **siguiente**; si no se guarda, al volver se perdería el hilo del
> programa. Ese es el objetivo central de una interrupción: **ser transparente**.

## Polling vs vectorizadas
| | **Polling** (consultada) | **Vectorizada** |
|---|---|---|
| Identificación | la CPU recorre los periféricos preguntando quién pidió | el periférico entrega su **número de vector** |
| Velocidad de atención | lenta (proporcional al nº de dispositivos) | rápida (directa) |
| Hardware | simple: una línea INT común | más complejo: bus de datos/controlador de interrupciones |
| Dirección de la ISR | fija, una sola rutina que discrimina | sale de una **tabla de vectores** indexada por el número de vector |

**Tabla de vectores:** en memoria hay una tabla donde la entrada *i* contiene la dirección de la rutina del
dispositivo *i*. La CPU toma el número de vector, lo usa como índice y carga el PC con esa entrada.

## Clasificación de las interrupciones
| Tipo | Origen | Ejemplos |
|---|---|---|
| **De hardware (externas)** | un dispositivo | teclado, fin de transferencia de disco, timer |
| **De software (internas)** | una instrucción | `INT n` (llamada al sistema operativo) |
| **Excepciones / traps** | un error o evento del procesador | división por cero, fallo de página, instrucción ilegal, desbordamiento |
| **Enmascarables (INTR)** | se pueden **deshabilitar** por software (flag I) | periféricos |
| **No enmascarables (NMI)** | no se pueden deshabilitar | falla de alimentación, error de memoria |
| **Reiniciable / no reiniciable** | según se pueda retomar la instrucción | fallo de página (sí) vs error grave (no) |

## Prioridades
Cuando hay **varios pedidos a la vez**, hay que decidir el orden:
- **Prioridad por hardware:** un codificador con prioridad (ver [[Codificador]]) o un controlador de
  interrupciones (PIC/APIC) que entrega el vector de mayor prioridad.
- **Prioridad por software:** la rutina de polling consulta en orden de prioridad.
- **Reglas habituales:** las no enmascarables ganan a todo; los errores graves ganan a los periféricos;
  las de mayor velocidad (disco) suelen ganar a las lentas (teclado).
- **Anidamiento:** una interrupción de mayor prioridad puede interrumpir a la rutina de una de menor
  prioridad (**interrupción anidada**), si las interrupciones se habilitan dentro de la rutina.

## El sistema de interrupciones que agrega la cátedra a la BLUE indexada
> [!note] Dato que conviene decir primero
> **La BLUE original no tiene interrupciones** (el apunte de Foster lo dice explícitamente: no tiene registros
> índice, ni direccionamiento indirecto, ni interrupciones). La cátedra las **agrega** sobre la BLUE indexada,
> con un sistema elemental. Decir esto en el oral muestra que sabés de dónde sale cada cosa.

| Elemento | Función |
|---|---|
| **SI** (flip-flop del sistema de interrupción) | **1 = habilitado**, 0 = deshabilitado. Se maneja con las instrucciones **ION** (habilita) e **IOF** (inhabilita) |
| **IRQ** | línea única de pedido: es la **OR** de las "banderas de dispositivo" (cada periférico pone la suya en 1 cuando necesita atención) |
| **I** (biestable auxiliar) | genera la señal de reconocimiento; su salida indica que **se está atendiendo** una interrupción |
| **Estados F / E / I** | búsqueda, ejecución e **interrupción** |
| **ACK** | reconocimiento de interrupción, en las **vectorizadas** (se encadena de un dispositivo al siguiente: prioridad por cercanía) |
| **SKF / EMR / RTI** | instrucciones nuevas: **SKF X** omite la próxima instrucción si la bandera X es 0 · **EMR valor** carga el registro máscara · **RTI** retorno de interrupción |
| **RM** (registro máscara) | permite **enmascarar** (no dar curso a) determinados pedidos |
| **SP** (puntero de pila) | permite **interrupciones anidadas** guardando el contexto en una pila LIFO |

**Cuándo se acepta**: con `IRQ = 1`, `SI = 1` y **CP8 estando en estado E**. O sea: **siempre después de
terminar la instrucción en curso** (nunca en el medio).

**Ciclo de interrupción (8 pulsos, el de la cátedra):**
| Pulso | Acción |
|---|---|
| CP1 | **SI ← 0** (se deshabilita el sistema: evita que otra interrupción lo interrumpa) |
| CP2 | Envíe PC, **Cargue MBR** (se guarda el PC) |
| CP3 | Envíe 0, **Cargue MAR**, **Orden de escritura** ⇒ el PC queda guardado en la **posición CERO** |
| CP4 | Envíe 1, **Cargue PC** ⇒ la rutina de atención empieza en la posición **1** |
| CP5-CP7 | — (se ejecuta la rutina: guardar contexto, determinar quién interrumpió) |
| CP8 | **I ← 0** (termina el reconocimiento) |

**La rutina de atención hace tres cosas**: (1) **salva el contexto** (todos los registros menos el PC, que ya
está en la posición 0), (2) **determina quién interrumpió** —el *polling* con `SKF`/`JMP`— y (3) atiende al
dispositivo. Al final, **RTI** recupera el PC desde la posición CERO y **vuelve a poner SI = 1**.

**Polling (identificación por software)**: la rutina pregunta bandera por bandera
```
SKF 1            ; ¿está la bandera 1 en 1? si está en 0, omite la próxima
JMP Rutina1      ; atiende al dispositivo 1
SKF 2
JMP Rutina2
...
```
**El orden en que se consultan las banderas ES la prioridad.**

**Vectorizadas (identificación por hardware)**: cada dispositivo tiene una **dirección (vector)**; cuando la
CPU da **ACK**, el dispositivo **pone su vector en el bus** y se hace un **salto indirecto** a través de él. Es
**más rápido** que el polling (no hay que preguntar bandera por bandera) y la prioridad la resuelve el
**encadenado de ACK** (el primero de la cadena gana).

**Anidamiento**: con el esquema de la posición CERO no se puede interrumpir una interrupción (se perdería la
dirección de retorno). Con **pila (SP)** sí: se apila el contexto, se incrementa/decrementa el puntero y el
`SI` se vuelve a poner en 1 al empezar la rutina. Para que un dispositivo de menor prioridad no interrumpa a
uno de mayor, se usa el **registro máscara**.

**Ciclo de interrupción (esquema):**
```
fin de una ejecución
   │
   ├── ¿INT = 1 y SI = 1? ──no──→ STATE ← F (búsqueda normal)
   │            sí
   ▼
STATE ← I  (estado de interrupción)
   1) guardar PC (y flags)        → pila / registro de respaldo
   2) identificar la fuente       → polling: saltar a rutina que consulta
                                  → vectorizada: leer vector de la tabla
   3) PC ← dirección de la ISR
   4) ejecutar la rutina; al final RETI: restaurar PC y flags, SI ← 1
   5) STATE ← F  (vuelve la búsqueda normal)
```
En la versión indexada de BLUE este sistema es una de las **novedades** (ver
[[BLUE indexada (RIF, RID, nuevo formato)]]).

## Entrada/Salida: lo mínimo que se pregunta
- **Transmisión paralela:** todos los bits a la vez, un cable por bit (+ líneas de control). Rápida, corto
  alcance (impresora, bus interno).
- **Transmisión serie:** los bits uno tras otro por un par de hilos. Lenta, largo alcance y barata
  (RS-232, USB, Ethernet). Sincrónica (con reloj) o asíncrona (con bits de arranque/parada).
- **Puerta (port) de E/S:** registro de **datos** + registro de **estado** (¿listo?) + registro de
  **control**, con líneas de datos y de control.
- **Interfaz / controlador:** adapta velocidades y niveles entre el bus y el periférico; avisa por
  interrupción o por DMA.
- **Direccionamiento de E/S:** mapeada en memoria (como en BLUE: `IN`/`OUT` con número de puerto) o en
  espacio separado.

## Cómo responderlo en el final (pregunta principal #8)
1. Definir interrupción y por qué existe (evitar el polling).
2. Describir la secuencia completa: terminar instrucción → comprobar habilitación → guardar contexto →
   identificar fuente → saltar a la ISR → atender → restaurar y retornar.
3. Comparar **polling vs vectorizada** (con la tabla de vectores).
4. Clasificar: hardware/software, enmascarables/NMI, excepciones.
5. Explicar **prioridades** y anidamiento.
6. Aterrizar en **BLUE**: SI, INT, INTACK, estados F/E/I y el ciclo.
7. Cerrar con E/S serie/paralela y el rol de la interfaz.

## Errores típicos
- Interrumpir **a mitad de una instrucción** (se termina la actual; si no, el estado queda inconsistente).
- Olvidar **guardar el PC** al entrar y **restaurarlo** al salir.
- Confundir **vector** (número/índice) con la **rutina** (el código).
- Decir que polling y vectorizada son "lo mismo con otro nombre".
- Olvidar que hay que **habilitar** las interrupciones (flag/`SI`) y que la NMI no se puede enmascarar.

## Relacionado
[[Unidad de Control]] · [[Ciclo de máquina]] · [[BLUE indexada (RIF, RID, nuevo formato)]] · [[Técnicas para aumentar la velocidad]]
