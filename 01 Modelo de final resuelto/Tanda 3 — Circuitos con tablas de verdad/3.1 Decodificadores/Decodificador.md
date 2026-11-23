---
unidad: 2
tipo: concepto
examen: practica
prioridad: maxima
---
# Decodificador

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[Mintérminos y maxtérminos]] (Tanda 3 · 3.0 Herramientas (Karnaugh y compuertas)) · [[Compuertas lógicas]] (Tanda 3 · 3.0 Herramientas (Karnaugh y compuertas)) · [[Memoria RAM 8x3]] (Tanda 1 · 1.4 Memoria RAM 8x3) · [[Cómo se implementa la Unidad de Control]] (Tanda 1 · 1.6 Implementación de la Unidad de Control) · [[Memoria ROM y sus tipos]] (Tanda 2 · 2.2 Memoria ROM y sus tipos) El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 3.1 Decodificadores]].

> [!abstract] En una frase
> Un **decodificador de n a 2ⁿ** tiene **n entradas** y **2ⁿ salidas**, y activa **una sola salida**: la que corresponde al número binario de la entrada. Cada salida es un **mintérmino** de las entradas: **`Yi = mi`** ⇒ `Y0 = A1'A0'`, `Y1 = A1'A0`, `Y2 = A1A0'`, `Y3 = A1A0`.

> [!note] Si es la primera vez que ves esto
> Pensá en el **portero de un edificio con 8 departamentos**. Le decís "departamento 5" y **sólo suena el timbre del 5**; los otros siete no se enteran. Eso es un decodificador: entra un **número** (la dirección) y se enciende **una sola línea** entre muchas.
>
> ¿Para qué sirve? Para **elegir**. Cuando la CPU quiere leer la celda 1 234 de la memoria, tiene que activar **esa** celda y ninguna otra: el decodificador convierte el número del bus de direcciones en "activo esta línea". Y también lo usa la Unidad de Control: el opcode de la instrucción entra a un decodificador y activa la línea de esa instrucción. **Un mismo circuito, dos usos centrales**: por eso está siempre en el final.

---

## 1. Decodificador 2 → 4 (el que se dibuja primero)

| A1 | A0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| 0 | 0 | **1** | 0 | 0 | 0 |
| 0 | 1 | 0 | **1** | 0 | 0 |
| 1 | 0 | 0 | 0 | **1** | 0 |
| 1 | 1 | 0 | 0 | 0 | **1** |

**Funciones (cada salida = un mintérmino):**
```
   Y0 = A1'·A0'      Y1 = A1'·A0      Y2 = A1·A0'      Y3 = A1·A0
```

**Cómo se lee la tabla al revés (el paso que se suele saltear):** cada fila tiene **un solo 1**. Si miro la columna `Y2`, vale 1 **sólo** en la fila `A1=1, A0=0` ⇒ `Y2 = A1·A0'`. Es decir: **las columnas de un decodificador son los mintérminos en orden**. Por eso `Yi = mi`.

**Circuito: 2 inversores + 4 AND de 2 entradas.** (En total, 6 compuertas; y con NAND, el mismo bloque.)

![Decodificador 2 a 4](../../../assets/decodificador_2x4.svg)

---

## 2. Decodificador 3 → 8 (el de las memorias)

| A2 A1 A0 | salida activa |
|---|---|
| 0 0 0 | Y0 |
| 0 0 1 | Y1 |
| 0 1 0 | Y2 |
| 0 1 1 | Y3 |
| 1 0 0 | Y4 |
| 1 0 1 | Y5 |
| 1 1 0 | Y6 |
| 1 1 1 | Y7 |

**Funciones:**
```
   Y0 = A2'A1'A0'   Y1 = A2'A1'A0   Y2 = A2'A1A0'   Y3 = A2'A1A0
   Y4 = A2 A1'A0'   Y5 = A2 A1'A0   Y6 = A2 A1A0'   Y7 = A2 A1A0
```
**Circuito: 3 inversores + 8 AND de 3 entradas.** Cada AND "mira" los tres bits y sólo da 1 con **su** combinación exacta.

![Decodificador 3 a 8](../../../assets/decodificador_3x8.svg)

> [!tip] La fórmula general (esto es lo que se pregunta)
> Un decodificador de **n** entradas necesita:
> - **2ⁿ compuertas AND de n entradas**
> - **n inversores** (para generar las variables negadas)
>
> | Entradas | Salidas | Qué representa en la materia |
> |---|---|---|
> | 2 | 4 | ejercicio de pizarrón |
> | 3 | 8 | **memoria RAM 8×3** (una línea por palabra) |
> | 4 | 16 | **opcode de la BLUE** (16 instrucciones) |
> | 12 | **4 096** | bus de direcciones de la **BLUE** (4 K palabras) |
>
> **El decodificador es lo que fija el tamaño de la memoria**: 12 bits de dirección ⇒ 4 096 líneas ⇒ 4 096 palabras.

---

## 3. Habilitación (EN) y expansión en cascada

- **EN** (*enable* / *chip select*): si está en 0, **todas** las salidas quedan en 0 aunque las entradas digan otra cosa. Es lo que permite tener **varios** decodificadores en el mismo bus sin que se peleen.

- **Expansión 4 → 16 con dos 3 → 8**: el **bit más significativo** (A3) va a `EN` de un decodificador y **negado** al `EN` del otro; los otros tres bits (A2 A1 A0) entran a **los dos**.

  - `A3 = 0` ⇒ habilita el primero ⇒ salidas Y0…Y7.

  - `A3 = 1` ⇒ habilita el segundo ⇒ salidas Y8…Y15.

- **Expansión de memoria con el mismo truco**: varios chips RAM comparten los buses de datos y de dirección y cada uno se habilita con **una salida distinta** del decodificador de banco ([[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]]).

> [!warning] Activas por nivel bajo
> En los chips comerciales (74LS138, el 3→8) las salidas son **activas por nivel bajo**: la línea seleccionada va a **0** y las demás a **1** (se escriben `Ȳ0`, `Ȳ1`…). Si en el apunte aparecen negadas, **no es un error**: es la convención del fabricante. En el pizarrón conviene aclarar cuál usás: "activo alto" (un solo 1) o "activo bajo" (un solo 0).

---

## 4. Aplicaciones (las cuatro que se nombran)

| Uso | Cómo se usa el decodificador |
|---|---|
| **Selección de palabra en memoria** | la dirección entra al decodificador y activa **una** línea de palabra |
| **Selección de registro** | la UC pone un código de 3–4 bits y se activa el `LOAD` de **un** registro |
| **Decodificación de instrucciones** | los bits de opcode del **IR** entran al decodificador y activan la línea de esa instrucción ([[Unidad de Control]]) |
| **Selección de periférico (E/S)** | la dirección del puerto activa el chip de E/S que corresponde ([[Interrupciones y entrada-salida]]) |

> [!example] En la BLUE, con números
> El opcode de la BLUE es de **4 bits** ⇒ decodificador **4 → 16** ⇒ 16 líneas, una por instrucción. La línea activa se combina después con el **estado** y el **pulso** para formar las señales de control (la famosa expresión `estado · pulso · instrucción`). Sin decodificador, la UC no sabría qué instrucción llegó. Ver [[Cómo se implementa la Unidad de Control]].

---

## 5. Decodificador vs demultiplexor (la comparación que se pregunta)

| | **Decodificador** | **Demultiplexor** |
|---|---|---|
| Entradas | n bits de **selección** | n bits de **selección** + **1 dato** |
| Salidas | 2ⁿ | 2ⁿ |
| Qué hace | activa **una** salida (siempre en 1) | **envía el dato** a **una** salida (las demás en 0) |
| Relación | `Y = sel` | `Y = dato · sel` ⇒ **es un decodificador con EN = dato** |

O sea: el demultiplexor **es** un decodificador usado al revés, con el dato como habilitación ([[Demultiplexor]]). Y el decodificador es el **inverso** del [[Codificador]].

---

## 6. Cómo responderlo en el final (3–4 minutos)

**Movimiento 1 — definición (20 s).** "n entradas, 2ⁿ salidas, una sola activa; cada salida es un mintérmino."

**Movimiento 2 — tabla y funciones (60 s).** Dibujar la tabla del **2→4** y escribir `Y0 = A1'A0'` … `Y3 = A1A0`, mostrando que **cada columna es un mintérmino**.

**Movimiento 3 — el circuito (60 s).** 2 inversores + 4 AND de 2 entradas; generalizar a **3→8** (3 inversores + 8 AND de 3) y decir la fórmula `2ⁿ AND de n entradas`.

**Movimiento 4 — EN y expansión (40 s).** Para qué sirve el *enable* y cómo se hace un **4→16** con dos 3→8 (bit de mayor peso al EN de uno y negado al otro).

**Movimiento 5 — cierre (20 s).** "Es lo que **elige**: una palabra de memoria (12 bits ⇒ 4 096 líneas), un registro, o la instrucción en la UC (4 bits ⇒ 16)."

### Repreguntas típicas

| Repregunta | Respuesta corta |
|---|---|
| ¿Cuántas salidas tiene un decodificador de 4 entradas? | **16** (2⁴) |
| ¿Cuántas salidas están activas a la vez? | **Exactamente una** (si está habilitado) |
| ¿Qué pasa si EN = 0? | **Todas** las salidas quedan en 0 (o en 1, si son activas bajas) |
| ¿Para qué sirve el EN? | Para habilitar un chip entre varios y para **expandir** en cascada |
| ¿Cómo se hace un 4→16? | Dos 3→8: el bit más significativo al EN de uno y negado al otro |
| ¿Diferencia con el codificador? | El codificador va al revés: **2ⁿ entradas → n salidas** |
| ¿Diferencia con el MUX? | El MUX **elige una entrada y la manda a la única salida**; el decodificador **activa una salida** |
| ¿Y con el DEMUX? | El DEMUX **manda un dato** a la salida elegida (es un decodificador con el dato en EN) |
| ¿Cómo se relaciona con los mintérminos? | Cada salida **es** un mintérmino ⇒ un decodificador + OR = cualquier función (una ROM) |

---

## 7. Errores típicos

- Decir que se activan **varias** salidas (siempre una; si hay varias, el circuito está mal o es un demultiplexor).

- Confundir **entradas** (n) con **salidas** (2ⁿ) — y por lo tanto dibujar 4 entradas para el 2→4.

- Olvidar los **inversores** en el dibujo: sin `A1'` y `A0'` no se pueden armar los mintérminos.

- Contar mal las AND: son **2ⁿ**, no n.

- Ignorar que el 74LS138 tiene salidas **activas por nivel bajo**.

---

## 8. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **decodificadores** | el 2→4 y el 3→8 con su tabla y su circuito tal como los da la cátedra | **Es la fuente exacta** de esta pregunta |
| **[[TP6 Decodificadores y demultiplexores]]** | el TP | los circuitos a construir y las tablas pedidas | Lo que se entrega por escrito |
| **Apuntes / `memorias.pdf`** | sección de **memoria RAM** ([[Memoria RAM 8x3]]) | el decodificador de filas y el de banco dentro de la memoria | La aplicación que más se pregunta |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **funciones lógicas combinacionales** (decodificadores) | 74LS138, expansión en cascada, aplicaciones | **La mejor ampliación**: diagramas de chips reales |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **circuitos combinacionales** | decodificador, implementación de funciones con decodificador + OR | Formalización (y la idea de la ROM) |
| **[[Codificador]]** · **[[Multiplexor]]** · **[[Demultiplexor]]** | notas de la bóveda | los otros tres bloques de la misma tanda | Estudiarlos juntos: se preguntan juntos |
| **[[Mintérminos y maxtérminos]]** | nota de la bóveda | por qué la salida de un decodificador es un mintérmino | Justificación matemática |
| **[[Cómo se implementa la Unidad de Control]]** | nota de la bóveda | el decodificador de instrucciones de la BLUE (4→16) | Conexión con la 1.ª tanda |

---

## Relacionado
[[Codificador]] · [[Multiplexor]] · [[Demultiplexor]] · [[Mintérminos y maxtérminos]] · [[Compuertas lógicas]] · [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] · [[Unidad de Control]]
