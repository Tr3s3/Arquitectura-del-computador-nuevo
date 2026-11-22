---
unidad: 2
tipo: concepto
examen: secundario
prioridad: alta
---
# Flip-Flops SR, D, JK y T

> [!abstract] En una frase
> Un flip-flop (biestable) es un circuito **secuencial** capaz de **memorizar 1 bit**: su salida Q
> depende de las entradas **y** de su estado anterior, y sólo cambia en el **flanco** del reloj.
> Es la celda con la que se construyen registros, contadores y memorias.

## Combinacional vs secuencial
| Combinacional | Secuencial |
|---|---|
| salida = f(entradas actuales) | salida = f(entradas, estado anterior) |
| no tiene memoria | **tiene memoria** (realimentación) |
| sumador, MUX, decodificador | flip-flop, registro, contador, RAM |

El flip-flop se obtiene **realimentando** compuertas (dos NOR o dos NAND cruzadas). Esa realimentación
es lo que le permite "quedarse" con un valor: si Q = 1 y no se lo cambia, sigue en 1 indefinidamente.

## Los cuatro tipos
![flipflops](../assets/flipflops.svg)

### 1) S-R (Set-Reset)
| S | R | Q(t+1) |
|---|---|---|
| 0 | 0 | Q (mantiene) |
| 1 | 0 | 1 (set) |
| 0 | 1 | 0 (reset) |
| 1 | 1 | **prohibido** |

Ecuación: `Q(t+1) = S + R'·Q`. La combinación S=R=1 se prohíbe porque fuerza Q = Q' = 1 (estado
inconsistente) y al soltar las entradas el estado queda indefinido.

> [!warning] Las dos convenciones del RS (esto se pregunta en el TP8)
> | | Con **NOR** (activo alto) | Con **NAND** (activo bajo) |
> |---|---|---|
> | Reposo | S = 0, R = 0 ⇒ **mantiene** | S = 1, R = 1 ⇒ **mantiene** |
> | Prohibido | S = 1, R = 1 | S = 0, R = 0 |
> | Set | S = 1, R = 0 ⇒ Q = 1 | S = 0, R = 1 ⇒ Q = 1 |
> | Reset | S = 0, R = 1 ⇒ Q = 0 | S = 1, R = 0 ⇒ Q = 0 |
>
> En la tabla del [[TP9 Biestables D, JK y T|TP9]] y del [[TP8 Biestables RS|TP8]] conviene **decir cuál usás**;
> si la tabla trae "0 0 indefinible", está en la versión **NAND** (activa por nivel bajo).Ecuación: `Q(t+1) = S + R'·Q`. La combinación S=R=1 se prohíbe porque fuerza Q = Q' = 1 (estado
inconsistente) y al soltar las entradas el estado queda indefinido.

### 2) D (Data / Delay)
| D | Q(t+1) |
|---|---|
| 0 | 0 |
| 1 | 1 |

Ecuación: `Q(t+1) = D`. Es el biestable **de memoria por excelencia**: en el flanco copia lo que hay en D.
Se obtiene de un S-R con `S = D` y `R = D'` (nunca se da S=R=1). **Es el que usa la materia** para
celdas de memoria, registros y contadores.

### 3) J-K
| J | K | Q(t+1) |
|---|---|---|
| 0 | 0 | Q (mantiene) |
| 1 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 1 | Q' (conmuta) |

Ecuación: `Q(t+1) = J·Q' + K'·Q`. Es un S-R **sin estado prohibido**: el 1-1 se define como "toggle".
Muy usado en contadores porque con J=K=1 divide la frecuencia por 2.
(Se arma con un S-R y realimentación: `S = J·Q'`, `R = K·Q`.)

### 4) T (Toggle)
| T | Q(t+1) |
|---|---|
| 0 | Q (mantiene) |
| 1 | Q' (conmuta) |

Ecuación: `Q(t+1) = T ⊕ Q`. Es el J-K con J=K=T. Con T=1 permanente es un **divisor por 2**: la base de
los [[Contadores]] asíncronos.

## Sincrónico vs asíncrono
- **Asíncrono**: cambia apenas cambian las entradas (latch). Tiene problemas de carrera (*race*) y de
  sensibilidad al ancho del pulso.
- **Sincrónico**: además de las entradas tiene **reloj (C)** y sólo cambia en el **flanco** (de subida o
  de bajada, según el modelo). Esto hace todo el sistema predecible: el estado se actualiza una vez por
  pulso, y el [[Ciclo de máquina]] se puede contar en pulsos.
- **Maestro-esclavo**: dos latches en serie con relojes opuestos; la salida sólo se actualiza en un flanco
  y el dato se "congela" durante el resto del pulso.
- Entradas **asincrónicas** PRESET (Q=1) y CLEAR (Q=0): actúan sin reloj; se usan para inicializar
  registros y contadores (el RESET del sistema).

## Para qué se usan en la materia
| Aplicación | Se arma con |
|---|---|
| Registro de n bits | n flip-flops D con el mismo reloj y la misma señal LOAD ([[Registros]]) |
| Contador | flip-flops T/J-K encadenados o D + sumador ([[Contadores]]) |
| Celda de RAM | 1 flip-flop (o latch) por bit ([[Celda elemental de memoria]]) |
| Registro de estado de la UC | flip-flops RUN, STATE (F/E), CLOCK ([[Máquina BLUE — arquitectura y conjunto de instrucciones]]) |
| Divisor de frecuencia | T=1 o J=K=1 |

## Cómo responderlo en el final
1. Definir biestable = elemento de memoria de 1 bit, secuencial, disparado por flanco.
2. Recorrer los cuatro tipos con su tabla de estados y su ecuación (con el gráfico del símbolo).
3. Marcar el problema del S-R (1,1 prohibido) y cómo J-K y D lo resuelven.
4. Cerrar con el uso: registro = n FF D; contador = FF T/J-K; RAM = celdas de 1 bit.

## Errores típicos
- Decir que el FF es combinacional (¡tiene memoria!).
- Confundir **nivel** con **flanco**: los biestables de la cátedra son disparados por flanco.
- Olvidar que S=R=1 es **prohibido** y no "mantiene".
- Confundir T (conmuta siempre con T=1) con D (copia el dato).

## Relacionado
[[Registros]] · [[Contadores]] · [[Celda elemental de memoria]] · [[Compuertas lógicas]]
