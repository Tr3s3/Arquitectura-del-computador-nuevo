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

## El sistema de interrupciones en BLUE
| Elemento | Función |
|---|---|
| **SI** | flip-flop que **habilita/inhabilita** las interrupciones (equivale al flag I) |
| **INT** | línea de pedido del periférico |
| **INTACK / INTA** | la CPU **reconoce** el pedido |
| **Estados F / E / I** | F = búsqueda, E = ejecución, **I = atención de la interrupción** |
| **Rutina de servicio** | dirección fija (polling) o tomada de la tabla de vectores |

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
