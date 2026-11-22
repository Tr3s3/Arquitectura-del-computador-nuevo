---
unidad: 2
tipo: concepto
examen: practica
prioridad: maxima
---
# Flip-Flops SR, D, JK y T

> [!abstract] En una frase
> Un **flip-flop** es una **memoria de 1 bit**: guarda un valor (`Q`) hasta que una entrada se lo cambia. Cada
> tipo se define por su **ecuación característica**:
> **SR:** `Q⁺ = S + R'·Q` (con `S·R = 0`) · **D:** `Q⁺ = D` · **JK:** `Q⁺ = J·Q' + K'·Q` · **T:** `Q⁺ = T ⊕ Q`.
> Todas se deducen de su **tabla característica** con un **mapa de Karnaugh**.

> [!note] Si es la primera vez que ves esto
> Todo lo que viste hasta acá era **combinacional**: la salida depende **sólo** de las entradas de ahora. Si
> soltás la entrada, la salida se va.
>
> Un flip-flop hace algo nuevo: **recuerda**. El truco es una **realimentación**: la salida vuelve a la entrada
> (dos inversores en un círculo se sostienen mutuamente, como dos personas que se dan la mano y no se pueden
> caer). A eso se le agregan compuertas para poder **cambiar** el valor cuando querés. Resultado: un bit que
> **se queda** guardado.
>
> Ese bit es la base de **todo**: los registros de la CPU (AC, PC, IR…), las celdas de una **SRAM**, los
> **contadores**, y los **flip-flops de estado** de la Unidad de Control de la BLUE (RUN, STATE, TRA). Sin
> flip-flops no hay memoria ni secuencia: sólo compuertas que reaccionan.

---

## 1. La tabla que hay que saber leer: `Q` y `Q⁺`

- **`Q`** = el estado **actual** (lo que el flip-flop tenía guardado).
- **`Q⁺`** = el estado **siguiente** (lo que va a quedar después del pulso de reloj).
- La tabla característica **incluye a `Q` como una entrada** (por eso tiene el doble de filas que una tabla
  combinacional con las mismas entradas).

> [!warning] La confusión nº 1 del tema
> `Q` **no** es una entrada que vos manejás: es lo que el flip-flop **ya tenía**. Vos manejás `S`, `R`, `J`, `K`,
> `D`, `T` y el **reloj**; `Q` es la memoria.

---

## 2. Flip-flop **SR** (Set–Reset)

**Construcción:** dos compuertas **NOR** cruzadas (cada salida vuelve a la entrada de la otra). Eso es todo: la
realimentación es el circuito.

| S | R | Q⁺ | Nombre |
|---|---|---|---|
| 0 | 0 | **Q** | **mantener** (memoriza) |
| 0 | 1 | **0** | **reset** (borrar) |
| 1 | 0 | **1** | **set** (poner en 1) |
| 1 | 1 | **X** | **estado prohibido** |

**El problema:** con `S = R = 1` las dos salidas van a 0 a la vez y, cuando se sueltan las dos entradas, el
resultado queda **indefinido** (depende de quién gane la carrera). Por eso ese estado está **prohibido** y se
marca con **X**. Ése es el motivo por el que existe el JK.

### Ecuación característica, paso a paso (con Karnaugh)

| S | R | Q | Q⁺ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | **X** |
| 1 | 1 | 1 | **X** |

Mapa (filas `S`, columnas `RQ` en Gray: 00, 01, 11, 10):
```
          RQ
         00   01   11   10
   S=0 │ 0 │  1 │  X │  0 │
   S=1 │ 1 │  1 │  X │  1 │
```
- Un grupo de **4** en la fila `S = 1` (usando las X como comodín) ⇒ **`S`**
- Un grupo de **2**: `R = 0`, `Q = 1` (la columna 01 en las dos filas) ⇒ **`R'·Q`**

**`Q⁺ = S + R'·Q`**, con la **condición `S·R = 0`** (¡siempre hay que decirla!).

---

## 3. Flip-flop **D** (Data / Delay)

**Idea:** una sola entrada de dato y nada más. Al pulso, `Q⁺ = D`. Es el flip-flop **más usado del mundo**,
porque es el que forma los **registros**.

| D | Q⁺ |
|---|---|
| 0 | 0 |
| 1 | 1 |

**Ecuación:** **`Q⁺ = D`**. No hay mapa que hacer: la salida copia la entrada (la tabla ni siquiera necesita a
`Q`).

**Cómo se construye con un SR:** `S = D`, `R = D'` (un inversor). Así nunca se cae en `S = R = 1`.
```
        ┌───┐
   D ───┤S  │
      ┌─┤R  │── Q
      │ └───┘
      └──NOT──  (R = D')
```
- **Latch (transparente):** mientras el habilitador está en 1, la salida **sigue** a la entrada.
- **Flip-flop disparado por flanco:** sólo copia en el **flanco** (subida o bajada) del reloj. Es lo que se usa
  en los registros, porque evita problemas de carrera.

---

## 4. Flip-flop **JK** (el SR arreglado)

**Idea:** se toma el SR y se **realimenta la salida** para que `S = R = 1` ya no sea un problema: en ese caso el
flip-flop **conmuta** (toggle).

| J | K | Q⁺ | Nombre |
|---|---|---|---|
| 0 | 0 | **Q** | mantener |
| 0 | 1 | **0** | reset |
| 1 | 0 | **1** | set |
| 1 | 1 | **Q'** | **toggle** (conmuta) |

### Ecuación característica con Karnaugh (el ejercicio que piden)

Tabla completa (J, K como entradas; Q como estado):

| J | K | Q | Q⁺ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | **1** |
| 1 | 1 | 1 | 0 |

Mapa (filas `J`, columnas `KQ` en Gray):
```
          KQ
         00   01   11   10
   J=0 │ 0 │  1 │  0 │  0 │
   J=1 │ 1 │  1 │  0 │  1 │
```
Dos grupos de **2**:
- fila `J = 1` con `Q = 0` (columnas 00 y 10, **que son vecinas porque el mapa cierra**) ⇒ **`J·Q'`**
- columna `K = 0, Q = 1` (las dos filas) ⇒ **`K'·Q`**

**`Q⁺ = J·Q' + K'·Q`**

**Lectura de la ecuación:** "si `J = 1` y estaba en 0, se pone en 1; si `K = 0`, **conserva** lo que tenía".
Y con `J = K = 1`: `Q⁺ = Q' + Q` … no: `Q⁺ = 1·Q' + 0·Q = Q'` ⇒ **conmuta**. ✔ (Por eso el JK resuelve el
problema del SR.)

---

## 5. Flip-flop **T** (Toggle)

**Idea:** una sola entrada: si `T = 1`, **conmuta** en cada pulso; si `T = 0`, se queda.

| T | Q⁺ |
|---|---|
| 0 | **Q** |
| 1 | **Q'** |

**Ecuación:** **`Q⁺ = T⊕Q = T'·Q + T·Q'`**.
**Circuito:** es un **JK con `J = K = T`**. Y con `T = 1` fijo, cada pulso divide la frecuencia por 2 ⇒ es la
base de los **contadores** y de los divisores de reloj.

---

## 6. Las cuatro ecuaciones juntas (cuadro para el pizarrón)

| Tipo | Entradas | Ecuación característica | Se usa para |
|---|---|---|---|
| **SR** | S, R | `Q⁺ = S + R'·Q` (con `S·R = 0`) | memoria básica; base didáctica |
| **D** | D | `Q⁺ = D` | **registros** (AC, PC, IR, MAR…), SRAM |
| **JK** | J, K | `Q⁺ = J·Q' + K'·Q` | contadores, control (sin estado prohibido) |
| **T** | T | `Q⁺ = T ⊕ Q` | **contadores** / divisores de frecuencia |

> [!tip] Cómo recordarlas sin memorizar
> Todas salen de **mirar la columna `Q⁺` y agrupar en el mapa**. Si te olvidás una, hacé la tabla de 8 filas
> (4 combinaciones de entradas × 2 de `Q`) y el mapa: en 2 minutos la tenés.

---

## 7. Sincrónico, asíncrono y reloj

| Concepto | Qué significa |
|---|---|
| **Reloj (CLK)** | señal que marca **cuándo** se permite cambiar de estado |
| **Asíncrono** | cambia en cuanto cambian las entradas (sin reloj): SR básico, latch |
| **Sincrónico** | cambia sólo con el **flanco** del reloj ⇒ todo el sistema avanza junto |
| **Preset / Clear** | entradas asíncronas que ponen el flip-flop en 1 o en 0 **sin esperar el reloj** (para inicializar) |
| **Flanco** | el instante de subida (0→1) o de bajada (1→0); "disparado por flanco" evita carreras |

> [!example] En la materia
> - **Registros de la BLUE**: cada uno (`AC`, `PC`, `IR`, `MAR`, `MBR`, `SW`) es un conjunto de flip-flops **D**
>   con entrada de **LOAD**: cargan sólo cuando su señal de control está activa en el pulso correcto
>   ([[Registros de la CPU]]).
> - **Unidad de Control**: los flip-flops **RUN**, **STATE** y **TRA** guardan el estado de la máquina; el pulso
>   avanza la secuencia ([[Cómo se implementa la Unidad de Control]]).
> - **SRAM**: la celda elemental es un **biestable** (dos inversores realimentados) ⇒ 1 bit que se sostiene solo
>   ([[Celda elemental de memoria]]).

---

## 8. Cómo responderlo en el final (4 minutos)

**Movimiento 1 — definición (20 s).** "Un flip-flop es una memoria de 1 bit construida con realimentación; tiene
un estado actual `Q` y uno siguiente `Q⁺`."

**Movimiento 2 — SR (60 s).** Tabla de 4 filas (mantener, reset, set, prohibido) y la ecuación `Q⁺ = S + R'Q` con
la condición `S·R = 0`; explicar por qué existe el JK.

**Movimiento 3 — D (40 s).** `Q⁺ = D`, se arma con `S = D` y `R = D'`; es el que forma los registros.

**Movimiento 4 — JK con Karnaugh (70 s).** Hacer la tabla de 8 filas, el **mapa** y llegar a
`Q⁺ = JQ' + K'Q`; remarcar que con `J = K = 1` **conmuta**.

**Movimiento 5 — T y cierre (30 s).** `Q⁺ = T⊕Q`; es un JK con `J = K`; con `T = 1` divide la frecuencia por 2 ⇒
contadores. Cerrar: "los registros de la BLUE son flip-flops D con LOAD, y la UC guarda su estado en RUN/STATE".

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Por qué memoriza? | Por la **realimentación**: la salida vuelve a la entrada y se sostiene |
| ¿Qué es el estado prohibido del SR? | `S = R = 1`: las dos salidas a 0 y resultado indefinido al soltar |
| ¿Cómo lo resuelve el JK? | Realimentando `Q`: con `J = K = 1` **conmuta** en vez de quedar indefinido |
| ¿Diferencia entre latch y flip-flop? | El **latch** es transparente con el nivel; el **FF** cambia sólo en el **flanco** |
| ¿Qué es `Q⁺`? | El estado **siguiente**, después del pulso de reloj |
| ¿Cuál es el más usado? | **D**: es la celda de los registros y de la SRAM |
| ¿Qué es T? | Un JK con `J = K = T`: conmuta con `T = 1` |
| ¿Para qué sirve preset/clear? | Para **inicializar** el flip-flop sin esperar el reloj |
| ¿Cuántos flip-flops tiene un registro de 16 bits? | **16** (uno por bit) |

---

## 9. Errores típicos
- Olvidar la **condición `S·R = 0`** en el SR (sin ella la ecuación no vale).
- Confundir `Q` (estado actual, es **memoria**) con una entrada de control.
- Decir que el JK "no tiene estado prohibido porque sí": se elimina por la **realimentación** `Q → S/R`.
- Escribir `Q⁺ = J + K'Q` (falta el `Q'` en el término del J).
- Confundir **T** con **toggle permanente**: sólo conmuta si `T = 1`.
- Decir que un flip-flop **D** "retiene el dato anterior" siempre: `Q⁺ = D` (no hay retención salvo que se agregue
  un enable).

---

## 10. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **biestables / flip-flops** | las tablas características **como las da la cátedra** (ojo con la convención de S y R activos) | **Es la fuente exacta** |
| **[[TP8 Biestables RS]]** · **[[TP9 Biestables D, JK y T]]** | los TPs | los circuitos, las tablas y las conversiones pedidas | Lo que se entrega y se corrige |
| **[[Conversión entre biestables (RS, JK, D, T)]]** | nota de la bóveda | el método de **tabla de excitación** y los mapas de cada conversión | El otro ítem de la tanda |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **circuitos secuenciales**: latches y flip-flops | diagramas de tiempo, flanco, preset/clear, tablas características | **La mejor ampliación**: tiene los cronogramas |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **circuitos secuenciales** | ecuaciones características, análisis y diseño | Formalización |
| **[[Celda elemental de memoria]]** | nota de la bóveda | el biestable como celda de SRAM | Conexión con la 2.ª tanda |
| **[[Registros de la CPU]]** · **[[Cómo se implementa la Unidad de Control]]** | notas de la bóveda | registros con LOAD y los FF de estado de la BLUE | Dónde se usa en la máquina |

---

## Relacionado
[[Conversión entre biestables (RS, JK, D, T)]] · [[Celda elemental de memoria]] · [[Registros de la CPU]] ·
[[Cómo se implementa la Unidad de Control]] · [[Compuertas lógicas]] · [[Álgebra de Boole — postulados y teoremas]]
