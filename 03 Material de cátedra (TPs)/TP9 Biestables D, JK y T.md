---
tp: 9
unidad: 2
tipo: tp
prioridad: alta
---
# TP9 — Biestables D, JK y T

> [!abstract] Consigna (cátedra)
> Por cada biestable: **a)** ¿qué es y cómo funciona? **b)** construirlo con su **tabla de verdad** y
> **circuito secuencial**, y graficar el **circuito reducido** para cada valor permitido de las entradas.

## La respuesta "a)" que espera la cátedra
| Biestable | Qué es / cómo funciona | Ecuación |
|---|---|---|
| **D** (Data/Delay) | almacena **el dato** que hay en su entrada en el flanco de reloj. Es el biestable de memoria: `Q` copia a `D`. Se obtiene de un RS con `S = D`, `R = D'` | `Q(t+1) = D` |
| **JK** | es un RS **sin estado prohibido**: cuando J = K = 1 **conmuta** (toggle). Se usa en contadores | `Q(t+1) = J·Q' + K'·Q` |
| **T** (Toggle) | conmuta si T = 1 y mantiene si T = 0. Es el J-K con `J = K = T`; con T = 1 divide la frecuencia por 2 | `Q(t+1) = T ⊕ Q` |

## Tablas de verdad
**D**
| C | D | Q(t+1) |
|---|---|---|
| ↑ | 0 | 0 |
| ↑ | 1 | 1 |
| 0 | X | Q(t) (mantiene) |

**J-K**
| J | K | Q(t+1) |
|---|---|---|
| 0 | 0 | Q(t) mantiene |
| 1 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 1 | Q'(t) conmuta |

**T**
| T | Q(t+1) |
|---|---|
| 0 | Q(t) mantiene |
| 1 | Q'(t) conmuta |

## Circuitos (cómo se dibujan)
- **D**: un RS sincrónico con un inversor: `S = D` y `R = D'`. En la práctica, un **latch D** con dos
  compuertas y realimentación, más un **maestro-esclavo** para que sea disparado por flanco.
- **J-K**: un RS sincrónico **realimentado** con la salida: `S = J·Q'` y `R = K·Q`. Esa realimentación es la
  que hace que con J = K = 1 conmute en lugar de quedar prohibido.
- **T**: un J-K con `J = K = T` (o un D con `D = T ⊕ Q`).

> [!example] "Circuito reducido" (lo que pide el inciso b)
> Para cada combinación permitida, se reemplazan las entradas por su valor y se ve qué le queda a las
> compuertas. Ejemplo con J-K:
> - `J = 1, K = 0` ⇒ `S = 1·Q' = Q'` y `R = 0` ⇒ la rama de reset se anula y queda **Q = 1** (set).
> - `J = 0, K = 1` ⇒ `S = 0` y `R = Q` ⇒ **Q = 0** (reset).
> - `J = K = 1` ⇒ `S = Q'`, `R = Q` ⇒ el biestable se invierte en cada flanco (**toggle**).
> - `J = K = 0` ⇒ `S = R = 0` ⇒ **mantiene**.
> Dibujar los cuatro casos reducidos es exactamente lo que pide el TP.

## Enlaces
Desarrollo: [[Flip-Flops SR, D, JK y T]] · Aplicación: [[Registros]] · [[Contadores]]
Siguiente: [[TP10 Registros PIPO y SISO]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Flip-flop D en 6 minutos](https://www.youtube.com/watch?v=Gpliq_1qxh0&t=24s) | Les Ingenieurs |
| ▶️ | [Flip-flop JK: cómo funciona](https://www.youtube.com/watch?v=M9toqPQghaA&t=13s) | Les Ingenieurs |
| ▶️ | [Flip-flop T: funcionamiento y diseño](https://www.youtube.com/watch?v=QIs4lorH3G4) | Les Ingenieurs |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo
> desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se
> toma en el parcial).

