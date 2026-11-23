---
tp: 8
unidad: 2
tipo: tp
prioridad: alta
---
# TP8 — Biestables RS (asincrónico y sincrónico)

> [!abstract] Consigna (cátedra)
> **Ej. 1:** construir un biestable **RS asincrónico** (sin reloj) con su tabla de verdad y circuito secuencial. Graficar el **circuito reducido** para cada valor permitido de las entradas. **Ej. 2:** lo mismo con el biestable **RS sincrónico** (con reloj).

## Qué hay que saber para resolverlo

1. Un biestable es **secuencial**: Q(t+1) depende de S, R y del **estado anterior** Q(t). Por eso la tabla tiene una columna `Q(t)` (o se escribe "mantiene").

2. El biestable se arma con **dos compuertas cruzadas** (realimentación): dos **NOR** (entradas activas por nivel alto) o dos **NAND** (activas por nivel bajo).

3. "Circuito reducido" = dibujar el circuito con los valores de entrada del caso (por ejemplo S=1, R=0) y **simplificar las compuertas** para ver cómo queda Q forzado.

> [!warning] Las dos convenciones del RS (esto se pregunta)
> | | Con **NOR** (activo alto) | Con **NAND** (activo bajo) |
> |---|---|---|
> | Estado de reposo | S = 0, R = 0 ⇒ **mantiene** | S = 1, R = 1 ⇒ **mantiene** |
> | Prohibido | S = 1, R = 1 | S = 0, R = 0 |
> | Set | S = 1, R = 0 ⇒ Q = 1 | S = 0, R = 1 ⇒ Q = 1 |
> | Reset | S = 0, R = 1 ⇒ Q = 0 | S = 1, R = 0 ⇒ Q = 0 |
>
> Decí siempre **qué convención estás usando**. Con la tabla del TP8 (donde 0 0 figura como indefinible) se está trabajando con la versión **NAND** (activa por nivel bajo).

## RS asincrónico (sin reloj) — versión NOR

| S | R | Q(t+1) | Observación |
|---|---|---|---|
| 0 | 0 | Q(t) | mantiene (memoria) |
| 1 | 0 | 1 | **set** |
| 0 | 1 | 0 | **reset** |
| 1 | 1 | — | **prohibido** (Q = Q' = 0) |

Ecuación característica: `Q(t+1) = S + R'·Q` Circuito: dos NOR cruzadas — la salida de cada una entra a la otra.

```
        ┌───────┐
   S ──→│  NOR  │──→ Q
        │   ↑   │
        └───┼───┘
            │ (realimentación)
        ┌───┼───┐
   R ──→│  NOR  │──→ Q'
        └───────┘
```

## RS sincrónico (con reloj)
Se agregan dos compuertas AND a la entrada, habilitadas por el **reloj (C)**:
```
  S ──AND──┐
  C ───────┤  (la entrada sólo llega al biestable cuando C = 1)
  R ──AND──┘
```
Ahora el biestable **sólo cambia cuando hay reloj**; si C = 0, las AND se bloquean y el estado se mantiene. El problema del 1-1 prohibido sigue existiendo.

> [!tip] Por qué esto importa
> El RS sincrónico es el paso previo al **D**: si conectás `S = D` y `R = D'`, el 1-1 nunca ocurre y el biestable copia el dato. Ese es el camino RS → D (ver [[TP9 Biestables D, JK y T]]).

## Enlaces
Desarrollo: [[Flip-Flops SR, D, JK y T]] · Dibujo: [[Cómo dibujar los circuitos (checklist de pizarrón)]] Siguiente: [[TP9 Biestables D, JK y T]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Flip-flop RS con reloj](https://www.youtube.com/watch?v=ShQwsahdLOc&t=322s) | Les Ingenieurs |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
