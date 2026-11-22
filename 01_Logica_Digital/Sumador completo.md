---
unidad: 1
tipo: concepto
examen: practica
prioridad: maxima
---
# Sumador completo (full adder)

> [!abstract] En una frase
> El **sumador completo** suma **tres bits** (A, B y el acarreo de entrada **Cin**) y entrega **suma `S`** y
> **acarreo `Cout`**: **`S = A ⊕ B ⊕ Cin`** · **`Cout = A·B + Cin·(A⊕B)`**. Es la celda que, repetida n veces y
> encadenando los acarreos, suma palabras de n bits.

> [!note] Si es la primera vez que ves esto
> La computadora **sólo sabe sumar**: restar es sumar el complemento, multiplicar es sumar varias veces, dividir
> es restar varias veces. Así que la pieza más importante de la máquina es **la que suma**.
>
> El [[Semisumador]] suma dos bits, pero **no recibe** el "me llevo uno" de la columna anterior. Cuando en papel
> sumás
> ```
>    1 0 1 1
>  + 0 1 1 0
>  ───────────
> ```
> la segunda columna recibe el acarreo de la primera. Entonces la celda real necesita **tres entradas**: A, B y
> el acarreo que viene. Eso es el **sumador completo**. Con 4 de ellos encadenados se suma un nibble; con 32, la
> palabra de una computadora de 32 bits.

---

## 1. Tabla de verdad (8 filas)

| A | B | Cin | **S** | **Cout** |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | **1** | 0 |
| 0 | 1 | 0 | **1** | 0 |
| 0 | 1 | 1 | **0** | **1** |
| 1 | 0 | 0 | **1** | 0 |
| 1 | 0 | 1 | **0** | **1** |
| 1 | 1 | 0 | **0** | **1** |
| 1 | 1 | 1 | **1** | **1** |

**Lectura rápida (memorizala así):**
- **S = 1** cuando hay un **número impar de unos** (1 o 3).
- **Cout = 1** cuando hay **dos o tres unos** (es decir: "la suma dio 2 o más").

> [!tip] Verificación mental en 3 segundos
> `A = 1, B = 1, Cin = 1` ⇒ 1+1+1 = **3** ⇒ binario `11` ⇒ **S = 1, Cout = 1**. ✔
> Con eso podés reconstruir la tabla entera sin memorizarla: cada fila es una suma aritmética de tres bits.

---

## 2. Funciones: canónicas, mapa de Karnaugh y simplificación

**Por mintérminos:**
```
   S    = Σm(1,2,4,7) = A'B'Cin + A'BCin' + AB'Cin' + ABCin
   Cout = Σm(3,5,6,7) = A'BCin + AB'Cin + ABCin' + ABCin
```

**Mapa de Karnaugh de S** (filas AB en Gray, columnas Cin):
```
            Cin=0  Cin=1
   AB=00  │  0  │  1  │   ← m1
   AB=01  │  1  │  0  │   ← m2, m3
   AB=11  │  0  │  1  │   ← m7
   AB=10  │  1  │  0  │   ← m4, m5
```
Los unos quedan **en damero**: **ningún par es vecino** ⇒ **no se puede simplificar** ⇒ `S = A ⊕ B ⊕ Cin`.
(La S se reconoce como "paridad de 3 bits": la XOR de los tres.)

**Mapa de Karnaugh de Cout:**
```
            Cin=0  Cin=1
   AB=00  │  0  │  0  │
   AB=01  │  0  │  1  │   ← m3
   AB=11  │  1  │  1  │   ← m6, m7
   AB=10  │  0  │  1  │   ← m5
```
Tres grupos de 2:
- `AB = 11`, con Cin cualquiera ⇒ **`A·B`**
- `AB = 01` y `Cin = 1` ⇒ **`A'·B·Cin`**
- `AB = 10` y `Cin = 1` ⇒ **`A·B'·Cin`**

`Cout = A·B + A'BCin + AB'Cin = A·B + Cin·(A'B + AB')` ⇒ **`Cout = A·B + Cin·(A ⊕ B)`**

> [!important] Los dos nombres que hay que decir
> - **`G = A·B`** es el acarreo **generado**: lo producen los dos bits solos.
> - **`P = A ⊕ B`** es el acarreo **propagado**: si exactamente uno de los bits es 1, el acarreo de entrada
>   **pasa** hacia la salida.
> - **`Cout = G + P·Cin`**. Con esta forma se explica el **acarreo anticipado** (más abajo).

---

## 3. El circuito (5 compuertas: 2 XOR, 2 AND, 1 OR)

![Sumador completo](../assets/sumador_completo.svg)

Estructura interna, con los cables intermedios **nombrados** (esto es lo que hace que el dibujo se entienda):

| Paso | Compuerta | Salida | Significado |
|---|---|---|---|
| 1 | XOR (A, B) | `S1 = A ⊕ B` | suma parcial / acarreo propagado |
| 2 | AND (A, B) | `C1 = A·B` | acarreo generado |
| 3 | XOR (S1, Cin) | **`S = S1 ⊕ Cin`** | **suma final** |
| 4 | AND (S1, Cin) | `C2 = S1·Cin` | acarreo propagado que se activa |
| 5 | OR (C1, C2) | **`Cout = C1 + C2`** | **acarreo de salida** |

> [!example] La otra forma de dibujarlo (muy usada en el final)
> **Un sumador completo = dos semisumadores + una OR.**
> ```
>   Semi 1 (A, B)     →  S1 , C1 = A·B
>   Semi 2 (S1, Cin)  →  S  , C2 = S1·Cin
>   OR                →  Cout = C1 + C2
> ```
> Es la misma función y, si te piden "armá un sumador completo con semisumadores", es la respuesta directa.

---

## 4. Sumador de n bits: acarreo en cascada

Se conectan n sumadores completos y **el `Cout` de cada uno va al `Cin` del siguiente**:

```
  A3 B3        A2 B2        A1 B1        A0 B0
   │  │         │  │         │  │         │  │
  ┌FA3┐──C3────┌FA2┐──C2────┌FA1┐──C1────┌FA0┐◄── Cin = 0
  │S3 │        │S2 │        │S1 │        │S0 │
```

- Se llama **sumador con acarreo en cascada** (*ripple carry*).
- **Retardo**: el bit más significativo tiene que esperar a que el acarreo atraviese **todas** las etapas ⇒ el
  retardo crece **linealmente** con n (n × retardo de un FA).
- **Solución**: **acarreo anticipado** (*carry look-ahead*): con los `G` y `P` de cada etapa se calculan **todos**
  los Ci en paralelo (`C1 = G0 + P0·C0`, `C2 = G1 + P1·G0 + P1·P0·C0`, …). Más compuertas, **mucho menos**
  retardo.

> [!example] Ejercicio resuelto (el típico del TP5)
> Sumar **1101 + 0111** con un sumador de 4 bits (Cin = 0):

| Bit | A | B | Cin | S | Cout |
|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | **0** | 1 |
| 1 | 0 | 1 | 1 | **0** | 1 |
| 2 | 1 | 1 | 1 | **1** | 1 |
| 3 | 1 | 0 | 1 | **0** | 1 |

> Resultado: `Cout S3 S2 S1 S0` = **1 0100** = **20**.
> Verificación decimal: 13 + 7 = 20. ✔ (¡Ojo con el error clásico de escribir `1 1100`!)

---

## 5. Dos derivados que se preguntan seguido

### Resta con el mismo circuito: complemento a 2
`A − B = A + (B' + 1)`. Entonces un **sumador/restador** es un sumador con **XOR en las entradas de B**:
```
   B ──XOR◄── Sub/Sum   ⇒ si Sub = 1, entran B' y Cin = 1  ⇒  A + B' + 1  =  A − B
```
**Un solo circuito suma y resta**, y eso es exactamente lo que hace la [[ALU]].

### Desbordamiento (overflow)
Con números **con signo** (complemento a 2), hay desbordamiento cuando **el acarreo que entra al último bit es
distinto del que sale**:
```
   Overflow = Cout(n−1) ⊕ Cin(n−1)      (o, equivalentemente, si dos positivos dan negativo)
```
En un sumador **sin signo**, en cambio, `Cout = 1` del último bit es simplemente el **acarreo** (bit 33 de la
suma).

---

## 6. Cómo responderlo en el final (4 minutos)

**Movimiento 1 — definición (20 s).** "Suma tres bits (A, B, Cin) y entrega S y Cout; es la celda del sumador de
n bits."

**Movimiento 2 — tabla (50 s).** Dibujar las 8 filas, leyendo "S = impar de unos, Cout = dos o más unos", y
verificar una fila en voz alta (1+1+1 = 11).

**Movimiento 3 — funciones (60 s).** `S = Σm(1,2,4,7) = A⊕B⊕Cin` (justificando con el **mapa en damero** que no
simplifica) y `Cout = A·B + Cin(A⊕B)`, presentando **G** y **P**.

**Movimiento 4 — circuito (70 s).** Los 5 pasos con los cables nombrados, o la versión **dos semisumadores + OR**.
Marcar de dónde sale cada salida.

**Movimiento 5 — cierre (40 s).** "n sumadores encadenados por el acarreo = sumador de n bits; el retardo se
arregla con **carry look-ahead**; y con un **XOR** en B el mismo circuito **resta** (complemento a 2). Ésa es la
ALU."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Cuántas filas tiene la tabla? | **8** (2³, tres entradas) |
| ¿Por qué `S` es una XOR triple? | Porque da 1 con un **número impar de unos** (paridad) |
| ¿Por qué `Cout` no es `A·B·Cin`? | Porque hay acarreo con **dos** unos también (filas 3, 5, 6) |
| ¿Se puede simplificar `S`? | **No** por Karnaugh (unos en damero); es la forma mínima |
| ¿Qué es G y qué es P? | **Generado** `A·B` y **propagado** `A⊕B` ⇒ `Cout = G + P·Cin` |
| ¿Cómo se suma 4 bits? | 4 FA encadenados: `Cout` de uno al `Cin` del siguiente |
| ¿Cuál es el problema del ripple carry? | El **retardo** crece con n ⇒ se usa **carry look-ahead** |
| ¿Cómo se resta? | `A + B' + 1` con XOR en B y `Cin = 1` (complemento a 2) |
| ¿Qué es el desbordamiento? | `Cout` del último ≠ `Cin` del último (en complemento a 2) |
| ¿Cuántas compuertas tiene? | **5** (2 XOR, 2 AND, 1 OR) |

---

## 7. Errores típicos
- Escribir `S = A + B + Cin` (eso es un OR: `1+1+1` daría 1 en vez de 1 con acarreo… y en `A=1,B=1,Cin=0` daría 1
  cuando la suma es 0).
- Poner `Cout = A·B·Cin` ⇒ se pierden los acarreos de "dos unos".
- Encadenar al revés: el `Cout` va al `Cin` del **siguiente** (el de más peso).
- Decir que el acarreo del último bit siempre es error: en **sin signo** es el bit n; en **con signo** es
  desbordamiento.
- Olvidar nombrar los cables intermedios en el dibujo (después no se puede explicar).

---

## 8. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **sumadores** (semisumador y sumador completo) | la tabla, las funciones y el circuito tal como los da la cátedra | **Es la fuente exacta** |
| **[[TP5 Sumadores]]** | el TP | sumadores de **4 y 8 bits** y las sumas `1101 + 0111`, `1101 0101 + 1010 0111` | Lo que se entrega y se corrige |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **funciones aritméticas** | sumador completo, ripple carry, carry look-ahead, resta en complemento a 2 | **La mejor ampliación** |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **circuitos combinacionales** (sumadores) | sumador–restador, detección de desbordamiento | Formalización |
| **[[Semisumador]]** | nota de la bóveda | la celda anterior: dos bits, sin Cin | Prerrequisito |
| **[[ALU]]** · **[[Hardware aritmético (resumen)]]** | notas de la bóveda | cómo el sumador se convierte en la ALU con compuertas de selección | Dónde se usa |
| **[[Ciclo de máquina]]** · **[[BLUE indexada (RIF, RID, nuevo formato)]]** | notas de la bóveda | el `PC + 1` de CP2-CP4 y el sumador de direcciones | El sumador dentro de la máquina |

---

## Relacionado
[[Semisumador]] · [[ALU]] · [[Hardware aritmético (resumen)]] · [[Compuertas lógicas]] ·
[[Mintérminos y maxtérminos]] · [[Álgebra de Boole — postulados y teoremas]]
