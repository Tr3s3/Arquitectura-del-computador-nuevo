---
tp: 18
unidad: 3
tipo: tp
prioridad: maxima
---
# TP18 — Direccionamiento de memoria (cálculo de CodOp y Dirección)

> [!abstract] Consigna (cátedra)
> Dada una **memoria principal** de cierta capacidad y un **tamaño de celda (palabra)**, se pide:
> **a)** graficar la memoria dividida en celdas · **b)** calcular su **espacio de direccionamiento** ·
> **c)** determinar **cuántos bits corresponden al CodOp** y **cuántos a la Dirección**.

> [!important] Es el cálculo más "de examen" de toda la materia
> Aparece en TP17, TP18 y en el final. La receta son tres cuentas y una resta. Está desarrollada paso a paso
> en [[Espacio de direccionamiento y cálculo de CodOp-Dirección]].

## La receta (3 pasos)
```
1) nº de celdas  = capacidad de memoria / tamaño de celda
2) bits de dirección = log₂(nº de celdas)
3) bits de CodOp = (bits de la palabra) − (bits de dirección)
```

## Ejercicio ejemplo (resuelto en el TP)
Memoria 512 MB, celdas de 4 bytes:
1. 512 MB / 4 B = 128 M celdas = 2²⁷
2. Dirección = **27 bits**
3. Palabra = 4 B = 32 bits ⇒ CodOp = 32 − 27 = **5 bits**

| CodOp | Dirección |
|---|---|
| 5 bits | 27 bits |

## Los cuatro ejercicios del TP (con la cuenta verificada)
| Ej. | Memoria | Celda | Nº de celdas | Bits de dirección | Palabra | **CodOp** |
|---|---|---|---|---|---|---|
| 1 | 2 GB | 8 B | 2³¹/2³ = 2²⁸ | **28** | 64 bits | **36** |
| 2 | 1 GB | 4 B | 2³⁰/2² = 2²⁸ | **28** | 32 bits | **4** |
| 3 | 128 MB | 2 B | 2²⁷/2 = 2²⁶ | **26** | 16 bits | **imposible (−10)** |
| 4 | 64 MB | 1 B | 2²⁶ | **26** | 8 bits | **imposible (−18)** |

**Los dos últimos son la parte conceptual del TP:** con celdas de 2 o 1 byte no hay bits suficientes para
direccionar tanta memoria (haría falta un CodOp "negativo"). Conclusión: **hay que aumentar el tamaño de la
celda** (o usar varios niveles/varios accesos), porque **la palabra instrucción tiene que contener la
dirección del operando**.

> [!warning] Un detalle del PDF del TP
> En el Ej. 2 (1 GB con celdas de 4 B) el TP escribe "128 MB de celdas ⇒ 2²⁷", pero 1 GB / 4 B = **256 M
> celdas = 2²⁸**. Con 2²⁸ la dirección son **28 bits** y el CodOp queda en **4** bits. En el examen conviene
> hacer la cuenta en voz alta: "1 GB son 2³⁰ bytes; dividido 2² son 2²⁸ celdas, o sea 28 bits".

## Enlaces
Desarrollo (con más ejemplos y atajos): [[Espacio de direccionamiento y cálculo de CodOp-Dirección]]
Siguiente: [[TP19 Modos de direccionamiento]]
