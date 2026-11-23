---
tp: 5
unidad: 1
tipo: tp
prioridad: alta
---
# TP5 — Sumadores

> [!abstract] Consigna (cátedra)
> **Ej. 1:** construir un **semisumador** con su tabla de verdad y circuito combinacional. **Ej. 2:** construir un **sumador completo** (2 bits) con su tabla de verdad y circuito combinacional. **Ej. 3:** construir un **sumador de 4 bits** y resolver `1101 + 0111`. **Ej. 4:** construir un **sumador de 8 bits** y resolver `1101 0101 + 1010 0111`.

## Qué hay que saber para resolverlo
Es **el** TP del final práctico. La secuencia que espera la cátedra, en los cuatro ejercicios, es siempre la misma: **tabla de verdad → funciones (mintérminos y simplificación) → circuito**. Y en los de 4 y 8 bits se agrega la **verificación con la suma binaria columna por columna**.

## Ejercicio 1 — Semisumador

| A | B | S | C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

`S = A'B + AB' = A ⊕ B`  ·  `C = A·B`  → **1 XOR + 1 AND**

![semisumador.svg](../assets/semisumador.svg)

## Ejercicio 2 — Sumador completo

| A | B | Cin | S | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

`S = A⊕B⊕Cin`  ·  `Cout = A·B + Cin·(A⊕B)`  → **2 XOR + 2 AND + 1 OR**

![sumador_completo.svg](../assets/sumador_completo.svg)

## Ejercicio 3 — Sumador de 4 bits
Cuatro sumadores completos **encadenados** (el `Cout` de cada uno va al `Cin` del siguiente, y el primero entra con `Cin = 0`).

**Verificación de `1101 + 0111`:**
```
  acarreos →  1 1 1 0
              1 1 0 1   (13)
           +  0 1 1 1   (7)
           ───────────
            1 0 1 0 0   = 20
```
bit 0: 1+1 = 0 y llevo 1 · bit 1: 0+1+1 = 0 y llevo 1 · bit 2: 1+1+1 = 1 y llevo 1 · bit 3: 1+0+1 = 0 y llevo 1 ⇒ **resultado 1 0100 (20)**, con acarreo de salida 1.

> [!warning] Dato del TP5 que conviene chequear
> En la consigna figura `1101 + 0111 = 1 1100`. Verificá la suma: 1101 + 0111 = **1 0100** (= 20). El resultado `1 1100` (= 28) corresponde a **1101 + 1111**. En el oral conviene resolverlo con el resultado correcto y, si aparece la discrepancia, decir con naturalidad "acá hay un error de tipeo en el TP: 13 + 7 = 20 = 1 0100". Demuestra que verificás lo que hacés.

## Ejercicio 4 — Sumador de 8 bits
Ocho sumadores completos encadenados.

**Verificación de `1101 0101 + 1010 0111`** (= 213 + 167 = 380):
```
   1 1 1 1 1 1
   1 1 0 1 0 1 0 1
 + 1 0 1 0 0 1 1 1
 ───────────────────
 1 0 1 1 1 1 1 0 0    = 380  ✔
```
⇒ resultado **1 0111 1100** (9 bits: acarreo de salida + 8 bits de suma), que coincide con la consigna.

> [!tip] Cómo dibujar el sumador de n bits en el pizarrón
> Dibujá **un bloque por bit** (un rectángulo rotulado FA) en fila, con `A3 B3 … A0 B0` arriba y `S3 … S0` abajo, y la línea de acarreo pasando de izquierda a derecha: `C0 = 0 → FA0 → C1 → FA1 → C2 …` y `C4 = Cout`. Con eso explicás la propagación del acarreo, que es lo que se evalúa.

## Enlaces
Desarrollo: [[Semisumador]] · [[Sumador completo]] · Dibujo: [[Cómo dibujar los circuitos (checklist de pizarrón)]] Siguiente: [[TP6 Decodificadores y demultiplexores]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Semisumador y sumador completo](https://www.youtube.com/watch?v=pZfp3wuIirY) | Clases en Línea |
| ▶️ | [Sumador de 4 bits en paralelo y en cascada](https://www.youtube.com/watch?v=Ak_uHvpquJI&t=112s) | Clases en Línea |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
