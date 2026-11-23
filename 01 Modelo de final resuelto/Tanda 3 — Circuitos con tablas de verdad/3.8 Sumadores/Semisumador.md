---
unidad: 1
tipo: concepto
examen: practica
prioridad: maxima
---
# Semisumador (half adder)

> [!abstract] En una frase
> El **semisumador** suma **dos bits** (A y B) y entrega **la suma `S`** y **el acarreo `C`**:
> **`S = A ⊕ B = A'B + AB'`** y **`C = A·B`**. Es el circuito aritmético más simple: **1 XOR + 1 AND**.

> [!note] Si es la primera vez que ves esto
> Sumá en papel:
> ```
>    1
>  + 1
>  ────
>   10
> ```
> Cuando sumás 1 + 1 no podés escribir "2" en una columna binaria: escribís **0 y te llevás 1** a la columna
> siguiente. Ese "me llevo uno" es el **acarreo** (*carry*). El semisumador es exactamente eso: **dos bits entran,
> un bit de suma sale y un bit de acarreo sale**.
>
> ¿Por qué "semi"? Porque **no recibe** el acarreo que viene de la columna anterior. Sirve para la **primera
> columna** (la de los bits menos significativos), donde no hay nada que arrastrar. Para las demás columnas, que
> sí reciben acarreo, hace falta el **sumador completo** ([[Sumador completo]]).

---

## 1. La tabla de verdad (4 filas, la suma binaria de dos bits)

| A | B | **S** (suma) | **C** (acarreo) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | **1** | 0 |
| 1 | 0 | **1** | 0 |
| 1 | 1 | **0** | **1** |

Se lee de un vistazo:
- **S = 1** cuando las entradas son **distintas** ⇒ ésa es la definición de **XOR**.
- **C = 1** sólo cuando las **dos** son 1 ⇒ ésa es la **AND**.

> [!important] Lo que hay que decir de la tabla
> "La columna de suma es **exactamente** la XOR, y la del acarreo es **exactamente** la AND. Por eso el circuito
> es de dos compuertas."

---

## 2. Las funciones (de la tabla al álgebra)

```
   S = Σm(1,2) = A'·B + A·B'  =  A ⊕ B
   C = Σm(3)   = A·B
```

**Verificación por Karnaugh** (2 variables, mapa de 2×2):

```
        B=0   B=1                  B=0   B=1
  A=0 │  0  │  1  │          A=0 │  0  │  0  │
  A=1 │  1  │  0  │  → S      A=1 │  0  │  1  │  → C
```
- En el mapa de **S** los unos están en **diagonal**: no hay vecinos que agrupar ⇒ **no se puede simplificar**
  (queda `A'B + AB'` = XOR).
- En el mapa de **C** hay un único 1 ⇒ el término completo: **`A·B`**.

> [!tip] Por qué S no se simplifica (dato que sube nota)
> La XOR es la función de 2 variables que **no tiene forma más simple**: su mapa tiene los unos en diagonal y no
> hay dos unos vecinos. Por eso la XOR tiene **compuerta propia**. En cambio, si se permite usar NAND: 
> `S = NAND( NAND(A, NAND(A,B)) , NAND(B, NAND(A,B)) )` = **4 NAND**.

---

## 3. El circuito (2 compuertas)

```
   A ──┬──────────┤XOR├──── S = A ⊕ B
       │          └───┘
   B ──┼──────────┤AND├──── C = A · B
       │          └───┘
```

![Semisumador](../../../assets/semisumador.svg)

**Compuertas: 1 XOR + 1 AND.** (Si sólo hay NAND: 5 compuertas; si sólo hay AND-OR-NOT: 2 NOT + 2 AND + 1 OR.)

**Cómo dibujarlo en el pizarrón (orden que no falla):**
1. Dos líneas de entrada a la izquierda: `A` y `B`.
2. Arriba, un **XOR** con A y B ⇒ salida **S**.
3. Abajo, una **AND** con A y B ⇒ salida **C**.
4. Rotular las salidas y, si se encadena, marcar que `C` va al **Cin** del siguiente.

---

## 4. Ejemplo numérico (verificación)

| Suma | A | B | S | C | Resultado (C S) | En decimal |
|---|---|---|---|---|---|---|
| 0 + 0 | 0 | 0 | 0 | 0 | 00 | 0 |
| 0 + 1 | 0 | 1 | 1 | 0 | 01 | 1 |
| 1 + 0 | 1 | 0 | 1 | 0 | 01 | 1 |
| 1 + 1 | 1 | 1 | 0 | 1 | **10** | **2** |

O sea: **el par (C, S) es el número A + B en binario de 2 bits**. Ésa es la mejor forma de explicar el circuito:
*"la salida de dos bits es la suma aritmética"*. Con eso, `1 + 1 = 10₂ = 2`. ✔

---

## 5. Para qué sirve (y por qué no alcanza)

| Situación | ¿Sirve el semisumador? |
|---|---|
| Sumar los **bits menos significativos** (columna 0) | **Sí** (no hay acarreo de entrada) |
| Sumar las **columnas siguientes** | **No**: hay que recibir el acarreo ⇒ [[Sumador completo]] |
| Contar unos (paridad) | Sí: encadenar XOR da la paridad |
| Detectar igualdad de dos bits | Sí: la XNOR (`(A⊕B)'`) da 1 si son iguales |

**Y el dato que cierra:** **un sumador completo = dos semisumadores + una OR**.
```
   Semi 1 (A, B) → S1 (suma parcial) y C1 = A·B
   Semi 2 (S1, Cin) → S (suma final) y C2 = S1·Cin
   Cout = C1 + C2
```
Por eso el semisumador **no es un circuito de juguete**: es la mitad del sumador real, que está en la
[[ALU]], en el incrementador del PC y en el sumador de direcciones de
[[BLUE indexada (RIF, RID, nuevo formato)|BLUE indexada]].

---

## 6. Cómo responderlo en el final (2–3 minutos)

**Movimiento 1 — definición (20 s).** "Suma dos bits y da suma y acarreo; es la celda de la primera columna."

**Movimiento 2 — tabla (30 s).** Las 4 filas, y decir en voz alta: "la suma es la XOR, el acarreo es la AND".

**Movimiento 3 — funciones y mapa (40 s).** `S = A'B + AB' = A⊕B`, `C = A·B`; mostrar el mapa de S con los unos
en diagonal (no simplifica) y el de C con un solo 1.

**Movimiento 4 — dibujo (40 s).** La XOR arriba y la AND abajo, con `A` y `B` a la izquierda; `S` y `C` a la
derecha. Cerrar con `1 + 1 = 10`.

**Movimiento 5 — límite (20 s).** "No recibe acarreo, así que no se puede encadenar: para eso está el **sumador
completo**, que es **dos semisumadores + una OR**."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Por qué se llama "semi"? | Porque **no tiene `Cin`**: no puede recibir el acarreo de la columna anterior |
| ¿Cuál es la función de la suma? | `S = A ⊕ B = A'B + AB'` |
| ¿Y la del acarreo? | `C = A · B` |
| ¿Cuántas compuertas? | **2**: una XOR y una AND |
| ¿Se puede simplificar `S`? | **No** por Karnaugh (los unos están en diagonal); es la forma mínima |
| ¿Se puede hacer sin XOR? | Sí: con NAND (4) o con AND-OR-NOT (5) |
| ¿Sirve para 4 bits? | Solo para el **bit 0**; los demás necesitan sumador completo |
| ¿Dónde está en la computadora? | En la **ALU**, en el incrementador del PC y en el sumador de direcciones |

---

## 7. Errores típicos
- Escribir `S = A + B` (eso es un OR: con `1 + 1` daría 1, cuando la suma es **0** con acarreo 1).
- Poner `C = A + B` (el acarreo sólo aparece con **los dos** bits en 1).
- Decir que el semisumador "suma números": suma **un bit** de cada número.
- Olvidar el acarreo en el dibujo (la tabla tiene **dos** salidas, no una).
- Usarlo en la columna 1 pensando que el acarreo no importa.

---

## 8. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **circuitos aritméticos**: semisumador y sumador completo | la tabla y las funciones tal como las da la cátedra | **Es la fuente exacta** |
| **[[TP5 Sumadores]]** | el TP | los sumadores de 4 y 8 bits a construir y las sumas a verificar | Lo que se entrega |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **funciones aritméticas** (suma binaria) | semisumador, sumador completo, acarreo en cascada | **La mejor ampliación**: figuras y ejercicios |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **circuitos combinacionales** (sumadores) | semisumador y sumador completo con mapas | Formalización con Karnaugh |
| **[[Sumador completo]]** | nota de la bóveda | el paso siguiente: la celda que sí recibe acarreo | Continuidad obligatoria |
| **[[Mintérminos y maxtérminos]]** | nota de la bóveda | cómo se arma `Σm` y se simplifica el mapa | La herramienta de la tanda |
| **[[ALU]]** · **[[Ciclo de máquina]]** | notas de la bóveda | dónde se usa el sumador en la BLUE (PC + 1, sumador de direcciones) | Aplicación en la máquina |

---

## Relacionado
[[Sumador completo]] · [[ALU]] · [[Compuertas lógicas]] · [[Mintérminos y maxtérminos]] ·
[[Álgebra de Boole — postulados y teoremas]] · [[Hardware aritmético (resumen)]]
