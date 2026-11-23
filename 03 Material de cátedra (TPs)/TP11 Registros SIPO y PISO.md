---
tp: 11
unidad: 2
tipo: tp
prioridad: alta
---
# TP11 — Registros SIPO y PISO

> [!abstract] Consigna (cátedra)
> **Ej. 1:** ¿qué es y cómo funciona un registro **SIPO**? Construir uno de 8 bits y mostrar su
> funcionamiento ingresando **10101010**.
> **Ej. 2:** ¿qué es y cómo funciona un registro **PISO**? Construir uno de 8 bits y mostrar su
> funcionamiento ingresando **11001100**.

## SIPO (Serial In – Parallel Out)
Entra **bit a bit** y se lee **todo junto**. Es la estructura de un ** receptor serie**: los bits llegan por
una línea y, cuando se completan 8, se leen en paralelo.

**Funcionamiento con 10101010** (MSB primero):
| Pulso | Entrada | Registro | ¿Se puede leer? |
|---|---|---|---|
| 1 | 1 | 1000 0000 | no (falta) |
| 2 | 0 | 0100 0000 | no |
| 3 | 1 | 1010 0000 | no |
| 4 | 0 | 0101 0000 | no |
| 5 | 1 | 1010 1000 | no |
| 6 | 0 | 0101 0100 | no |
| 7 | 1 | 1010 1010 | no |
| 8 | 0 | 0101 0101 | **sí** (dato completo) |

> [!note] Detalle de orden
> Si entrás los bits **LSB primero**, el registro termina con el número "al revés". Por eso en la práctica se
> define siempre **qué bit entra primero**; decilo en el examen.

## PISO (Parallel In – Serial Out)
Se **carga todo junto** (como un PIPO) y después se **transmite bit a bit**. Es la estructura de un
**transmisor serie**: la CPU escribe un byte completo y el registro lo saca por una sola línea.

**Funcionamiento con 11001100:**
1. `LOAD = 1` → en un pulso el registro toma `11001100`.
2. `LOAD = 0` y se habilita el desplazamiento: en cada pulso sale un bit por la salida serie y entra 0:
| Pulso | Contenido | Bit que sale |
|---|---|---|
| carga | 1100 1100 | — |
| 1 | 0110 0110 | 1 (MSB) |
| 2 | 0011 0011 | 1 |
| 3 | 0001 1001 | 0 |
| 4 | 0000 1100 | 0 |
| 5 | 0000 0110 | 1 |
| 6 | 0000 0011 | 1 |
| 7 | 0000 0001 | 0 |
| 8 | 0000 0000 | 0 |

⇒ salió la secuencia **11001100**, un bit por pulso.

## Los cuatro registros, en una tabla (respuesta de examen)
| Tipo | Entrada | Salida | Para qué sirve |
|---|---|---|---|
| **PIPO** | paralela | paralela | almacenar una palabra (registros de la CPU) |
| **SISO** | serie | serie | retardar n pulsos / almacenamiento serie |
| **SIPO** | serie | paralela | **recepción** serie → bus (teclado, modem, red) |
| **PISO** | paralela | serie | **transmisión** bus → serie (UART) |

Y el **bidireccional con carga en paralelo** (el más completo) agrega dos modos más: desplazar a izquierda y
a derecha, con un [[Multiplexor]] de 4 canales por cada flip-flop.

## Enlaces
Desarrollo: [[Registros]] · Aplicación: [[Interrupciones y entrada-salida]] (transmisión serie)
Siguiente: [[TP12 Memoria principal]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Registros serie-paralelo (9.3)](https://www.youtube.com/watch?v=Ghns0mXBPgw) | Diego Sales Lérida |
| ▶️ | [Registros paralelo-serie (9.4)](https://www.youtube.com/watch?v=3l9zZpWqADE) | Diego Sales Lérida |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo
> desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se
> toma en el parcial).

