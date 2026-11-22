---
unidad: 2
tipo: concepto
examen: practica
prioridad: maxima
---
# Multiplexor (MUX)

> [!abstract] En una frase
> Un **multiplexor de 2ⁿ a 1** tiene **2ⁿ entradas de dato**, **n entradas de selección** y **una sola salida**:
> la salida **copia** la entrada cuyo número indican las líneas de selección. `Y = S1'·S0'·I0 + S1'·S0·I1 +
> S1·S0'·I2 + S1·S0·I3` (para 4 a 1).

> [!note] Si es la primera vez que ves esto
> Es una **llave de paso de 4 caños con una sola canilla de salida**: girás la palanca (las líneas de selección)
> y elegís **cuál** de los cuatro caños pasa. O, mejor: es el **selector de canales del control remoto** — hay
> muchas señales entrando y **una** sale hacia la pantalla, la que elegiste.
>
> ¿Para qué sirve? Para **compartir un solo cable** entre varios que hablan de a uno: un **bus**. En la BLUE, el
> bus común lleva el contenido de **un** registro por vez, y eso lo decide un multiplexor. Además tiene un uso
> elegante que siempre cae en el final: **un multiplexor puede implementar cualquier función lógica** (se pone la
> tabla de verdad en las entradas de dato).

---

## 1. Multiplexor 2 → 1 (el mínimo)

| S | Y |
|---|---|
| 0 | I0 |
| 1 | I1 |

**Función:** `Y = S'·I0 + S·I1` ⇒ **2 AND + 1 OR + 1 NOT** (o 3 compuertas si se arma con NAND).

**Lectura:** si `S = 0`, el primer AND deja pasar `I0` (porque `S' = 1`) y el segundo queda en 0; el OR deja
pasar el que sobrevivió. Con `S = 1`, al revés. Los AND son "**puertas**" que se abren o cierran con la
selección.

---

## 2. Multiplexor 4 → 1 (el que se dibuja en el final)

| S1 | S0 | Y |
|---|---|---|
| 0 | 0 | **I0** |
| 0 | 1 | **I1** |
| 1 | 0 | **I2** |
| 1 | 1 | **I3** |

**Función canónica:**
```
Y = S1'·S0'·I0 + S1'·S0·I1 + S1·S0'·I2 + S1·S0·I3
```
Cada término es un **mintérmino de la selección multiplicado por el dato** correspondiente.

**Circuito (estructura AND-OR):**
```
 I0 ──┤AND├──┐
 I1 ──┤AND├──┤
 I2 ──┤AND├──┼──┤OR├── Y
 I3 ──┤AND├──┘
        ▲
   S1,S0 (y sus negados) abren un solo AND a la vez
```
**Compuertas:** 2 inversores (S1', S0') + **4 AND de 3 entradas** + **1 OR de 4 entradas** = **7 compuertas**.
(En un chip real se implementa más chico, pero **así se dibuja**.)

![Multiplexor 4 a 1](../assets/mux_4x1.svg)

> [!tip] La fórmula general
> MUX de **2ⁿ a 1** ⇒ **n líneas de selección**, **2ⁿ AND de (n+1) entradas** (n selecciones + 1 dato) y
> **1 OR de 2ⁿ entradas**. Y el dato: **2ⁿ a 1 es lo mismo que "un decodificador de n → 2ⁿ que habilita el AND
> de cada entrada"**.

---

## 3. El MUX como generador de funciones (el uso que impresiona)

Un MUX puede **implementar cualquier función lógica** de n variables: se pone la **tabla de verdad en las
entradas de dato** y las **variables en la selección**.

> [!example] Implementar `F(A,B,C) = Σm(1,2,5,7)` con un MUX 8→1
> ```
>        A B C  →  selección (A=S2, B=S1, C=S0)
>   I0 = 0   (m0 no está)
>   I1 = 1   (m1 sí)
>   I2 = 1   (m2 sí)
>   I3 = 0
>   I4 = 0
>   I5 = 1   (m5 sí)
>   I6 = 0
>   I7 = 1   (m7 sí)
> ```
> Listo: **no hace falta simplificar ni dibujar compuertas**. El MUX **es** la tabla de verdad.
>
> **Versión con menos hardware (4→1 y dos variables en la selección):** se usan A y B como selección y cada
> entrada de dato se conecta a `0`, `1`, `C` o `C'` según la columna:
> | A B | F en función de C | I |
> |---|---|---|
> | 0 0 | `C` | `I0 = C` |
> | 0 1 | `C'` | `I1 = C'` |
> | 1 0 | `C` | `I2 = C` |
> | 1 1 | `1` | `I3 = 1` |
>
> Así una función de 3 variables se hace con **un MUX 4→1** (más barato que 8→1). Éste es el ejercicio que
> combina Karnaugh + MUX y que suele estar en el TP.

---

## 4. Expansión: armar MUX más grandes

- **8 → 1 con dos 4 → 1**: las dos salidas entran a un **MUX 2 → 1** final, gobernado por el bit de mayor peso
  (S2). Es el mismo truco de expansión del decodificador ([[Decodificador]]).
- **MUX en árbol**: 16 → 1 con cinco 4 → 1 en dos niveles. El retardo crece con los **niveles**, no con la
  cantidad de entradas.

---

## 5. Aplicaciones (las que se nombran en la materia)

| Uso | Cómo |
|---|---|
| **Bus común** | todos los registros vuelcan en el bus y el MUX elige **cuál**; en la BLUE, el contenido del registro seleccionado va al bus ([[Flujo de información en BLUE (datos y direcciones)]]) |
| **Selección de operando de la ALU** | la ALU recibe `A` o `B` del banco de registros según la selección ([[ALU]]) |
| **Multiplexar direcciones** | en la BLUE, el MAR recibe el PC, el IR o el sumador según el pulso ⇒ un MUX de direcciones |
| **Serie / paralelo** | un MUX recorre las líneas de un bus y arma una salida serie (transmisión) |
| **Generador de funciones** | tabla de verdad dentro del MUX (lo de arriba) |
| **Selección de fuente de reloj / de señal** | elegir entre dos relojes o dos sensores |

> [!example] El dato de la BLUE
> En cada pulso, **quién** pone la información en el bus lo decide un **multiplexor** (o un conjunto de buffers
> de 3 estados con decodificador). El par **MUX (salida) + DEMUX (destino)** es el modelo conceptual del **bus
> común**: uno elige quién habla, el otro a quién le llega.

---

## 6. MUX vs DECODIFICADOR vs DEMUX (cuadro que se pregunta)

| | **Decodificador** | **Multiplexor** | **Demultiplexor** |
|---|---|---|---|
| Entradas | n (selección) | 2ⁿ (datos) + n (selección) | 1 dato + n (selección) |
| Salidas | 2ⁿ | **1** | 2ⁿ |
| Qué hace | activa **una** línea | **elige una entrada** y la manda a la salida | **manda el dato** a una salida |
| Función | `Yi = mi` | `Y = Σ mi · Ii` | `Yi = D · mi` |
| Dirección del flujo | de código a línea | **muchos → uno** | **uno → muchos** |

**Frase para el oral:** "el decodificador **señala**, el multiplexor **elige**, el demultiplexor **reparte**".

---

## 7. Cómo responderlo en el final (3–4 minutos)

**Movimiento 1 — definición (20 s).** "2ⁿ entradas de dato, n de selección, una salida; la salida copia la
entrada seleccionada."

**Movimiento 2 — tabla y función (60 s).** Tabla del **4→1** y la función
`Y = S1'S0'I0 + S1'S0I1 + S1S0'I2 + S1S0I3`.

**Movimiento 3 — el circuito (60 s).** Dibujar los **4 AND que se abren de a uno** + el **OR**; contar compuertas
y explicar que las selecciones funcionan como "llaves".

**Movimiento 4 — el uso fuerte (60 s).** "Cualquier función se implementa con un MUX: la tabla de verdad va en las
entradas de dato." Dar el ejemplo de `Σm(1,2,5,7)` con un 8→1, y mencionar la versión con 4→1 usando `C` y `C'`.

**Movimiento 5 — cierre (20 s).** "Es el bloque que permite **compartir un bus**: en la BLUE, el bus común lleva
a un solo registro por vez, y eso lo decide un MUX."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Cuántas líneas de selección para 16 entradas? | **4** (2⁴ = 16) |
| ¿Cuántas salidas tiene? | **Una** (por eso es multiplexor) |
| ¿Qué pasa con las entradas no seleccionadas? | Se ignoran: su AND está cerrado |
| ¿Se puede hacer una función con un MUX? | **Sí**, cualquier función: la tabla va en los datos |
| ¿Y con 4→1 una función de 3 variables? | Sí: dos variables en la selección, la tercera (o su negada) en los datos |
| ¿Cómo se agranda un MUX? | En **árbol**: 8→1 con dos 4→1 y un 2→1 final |
| ¿Diferencia con el decodificador? | El decodificador **activa una de 2ⁿ salidas**; el MUX **elige una de 2ⁿ entradas** |
| ¿Y con el DEMUX? | El MUX concentra (muchos→uno); el DEMUX reparte (uno→muchos) |
| ¿Dónde está en la BLUE? | En el bus común: selecciona qué registro vuelca en el bus |

---

## 8. Errores típicos
- Confundir **entradas de dato** con **entradas de selección** (y por lo tanto dibujar mal el número de AND).
- Escribir `Y = I0 + I1 + I2 + I3` (eso sería un OR de todo, no un MUX).
- Olvidar que cada AND necesita **todas** las selecciones (negadas o no) ⇒ AND de `n+1` entradas.
- Decir que el MUX "tiene 2ⁿ salidas" (tiene **una**; el que tiene 2ⁿ salidas es el demultiplexor).
- Al usarlo como generador de funciones, equivocar el **orden** de la selección (S2 = bit más significativo).

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **multiplexores** | el 4→1 con su tabla, función y circuito | **Es la fuente exacta** |
| **[[TP7 Codificadores y multiplexores]]** | el TP | los MUX a resolver y el uso como generador de funciones | Lo que se entrega |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **funciones combinacionales** (multiplexores) | 74LS151 (8→1), expansión, aplicaciones | **La mejor ampliación**: chip real con EN y selección |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **circuitos combinacionales** | MUX y su uso para implementar funciones booleanas | El método "tabla dentro del MUX" con formalización |
| **[[Decodificador]]** · **[[Demultiplexor]]** · **[[Codificador]]** | notas de la bóveda | los otros bloques de la tanda | Estudiarlos juntos |
| **[[Mintérminos y maxtérminos]]** | nota de la bóveda | la forma canónica que se pone en el MUX | Justificación de la fórmula |
| **[[Flujo de información en BLUE (datos y direcciones)]]** · **[[ALU]]** | notas de la bóveda | el bus común y la selección de operandos | La aplicación en la máquina |

---

## Relacionado
[[Decodificador]] · [[Codificador]] · [[Demultiplexor]] · [[Mintérminos y maxtérminos]] · [[Compuertas lógicas]] ·
[[ALU]] · [[Flujo de información en BLUE (datos y direcciones)]]
