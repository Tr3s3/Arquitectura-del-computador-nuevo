---
tp: 10
unidad: 2
tipo: tp
prioridad: alta
---
# TP10 — Registros PIPO y SISO

> [!abstract] Consigna (cátedra)
> **Ej. 1:** ¿qué es y cómo funciona un registro **PIPO**? Construir uno de **1 byte (8 bits)** y mostrar su funcionamiento ingresando **10101010**. **Ej. 2:** ¿qué es y cómo funciona un registro **SISO**? Construir uno de **8 bits** y mostrar su funcionamiento ingresando **11001100**.

## PIPO (Parallel In – Parallel Out)
**Qué es:** 8 flip-flops **D** con el **mismo reloj** y una señal de **habilitación (LOAD/EN)**. Los 8 bits entran y salen **a la vez**.

```
 D7..D0 ──→ [FF7]…[FF0] ──→ Q7..Q0
                 ↑
              CLK común  +  LOAD
```

**Funcionamiento con 10101010:** en el flanco de reloj con `LOAD = 1`, los 8 FF copian su bit:

| FF | Q antes | D | Q después |
|---|---|---|---|
| 7 | x | 1 | 1 |
| 6 | x | 0 | 0 |
| 5 | x | 1 | 1 |
| 4 | x | 0 | 0 |
| 3 | x | 1 | 1 |
| 2 | x | 0 | 0 |
| 1 | x | 1 | 1 |
| 0 | x | 0 | 0 |

⇒ el registro pasa a valer **10101010 en un solo pulso** (esa es la diferencia con el SISO).

## SISO (Serial In – Serial Out)
**Qué es:** 8 flip-flops D **en cadena**: la salida de uno entra al siguiente. El dato entra **bit a bit** y sale **bit a bit**, un bit por pulso de reloj ⇒ funciona como **retardo de 8 pulsos** y como registro de desplazamiento.

```
 entrada serie → [FF7] → [FF6] → [FF5] → … → [FF0] → salida serie
                   ↑       ↑       ↑            ↑
                          CLK común (todos en el mismo flanco)
```

**Funcionamiento con 11001100** (entrando el MSB primero, un bit por pulso):

| Pulso | Entrada | Contenido del registro |
|---|---|---|
| 0 | — | 0000 0000 |
| 1 | 1 | 1000 0000 |
| 2 | 1 | 1100 0000 |
| 3 | 0 | 0110 0000 |
| 4 | 0 | 0011 0000 |
| 5 | 1 | 0001 1000 |
| 6 | 1 | 0000 1100 |
| 7 | 0 | 0000 0110 |
| 8 | 0 | 0000 0011 |

Después de 8 pulsos el dato quedó dentro (y sale por el otro extremo con 8 pulsos más). **Para mostrarlo en el pizarrón, la tabla pulso a pulso es la respuesta**: se ve el corrimiento.

> [!tip] La frase que ordena todo
> **PIPO = entra todo junto, sale todo junto · SISO = entra de a uno, sale de a uno.** Y la regla general: la primera palabra es la **entrada** y la segunda la **salida**.

## Enlaces
Desarrollo: [[Registros]] · Siguiente: [[TP11 Registros SIPO y PISO]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Registros paralelo-paralelo (9.1)](https://www.youtube.com/watch?v=bqQJoTB6P4Q) | Diego Sales Lérida |
| ▶️ | [Registros serie-serie (9.2)](https://www.youtube.com/watch?v=3sJe6I9-L5E) | Diego Sales Lérida |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
