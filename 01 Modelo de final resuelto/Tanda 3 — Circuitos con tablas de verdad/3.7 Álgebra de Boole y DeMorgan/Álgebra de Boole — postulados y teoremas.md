---
unidad: 1
tipo: concepto
examen: practica
prioridad: maxima
---
# Álgebra de Boole — postulados y teoremas

> [!important] Qué necesitás para responder esta pregunta
> **En `Apoyo a la pregunta/`:** [[Leyes de DeMorgan]] **En otra tanda o unidad:** [[Compuertas lógicas]] (Tanda 3 · 3.0 Herramientas (Karnaugh y compuertas)) · [[Mintérminos y maxtérminos]] (Tanda 3 · 3.0 Herramientas (Karnaugh y compuertas)) · [[Flip-Flops SR, D, JK y T]] (Tanda 3 · 3.6 Flip-flops D, T y RS) El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 3.7 Boole y DeMorgan]].

> [!abstract] En una frase
> El **álgebra de Boole** es el "idioma" de los circuitos digitales: trabaja con **dos valores (0 y 1)** y tres operaciones (**OR `+`**, **AND `·`**, **NOT `'`**). Con un puñado de **postulados** (que se aceptan sin demostrar) y de **teoremas** (que se deducen) se reescribe una función **sin cambiar su tabla de verdad**, para **gastar menos compuertas**: menos costo, menos retardo, menos consumo.

> [!note] Si es la primera vez que ves esto
> Olvidate de los números. Pensá en **interruptores**:
>
> | Operación | Qué significa con interruptores | Resultado |
> |---|---|---|
> | **A · B** (AND) | dos interruptores **en serie**: la lamparita prende sólo si están **los dos** cerrados | 1 sólo si A = 1 **y** B = 1 |
> | **A + B** (OR) | dos interruptores **en paralelo**: prende si **alguno** está cerrado | 1 si A = 1 **o** B = 1 |
> | **A'** (NOT) | un interruptor **normalmente cerrado** (inversor): si A = 1, no pasa corriente | el opuesto |
>
> Eso es todo. El resto de esta nota son **reglas para reescribir** combinaciones de esos interruptores. ¿Por qué molestarse? Porque un circuito con 6 compuertas es **más caro, más grande y más lento** (la señal pasa por más compuertas) que el mismo circuito con 2. Y como **dos circuitos distintos pueden hacer exactamente lo mismo**, conviene encontrar el más chico. Simplificar es **ahorrar plata y ganar velocidad**.

---

## 1. Lo mínimo que hay que saber de memoria

| Operación | Símbolo | Se lee | Vale 1 cuando… | Tabla |
|---|---|---|---|---|
| **AND** | `A · B` | "A y B" | **ambas** valen 1 | 00→0 · 01→0 · 10→0 · **11→1** |
| **OR** | `A + B` | "A o B" | **alguna** vale 1 | 00→0 · **01→1 · 10→1 · 11→1** |
| **NOT** | `A'` (o `Ā`) | "no A" | A vale 0 | 0→1 · 1→0 |

**Jerarquía de operaciones** (como en la matemática): primero `'`, después `·`, al final `+`. Así `A + B·C` es `A + (B·C)`, **no** `(A+B)·C`.

> [!warning] Cuidado con el `+`
> El `+` del álgebra de Boole **no es la suma**: `1 + 1 = 1` (no 2). Es un "o". La suma aritmética es otra cosa ([[Semisumador]] · [[Sumador completo]]), y se escribe distinto (⊕ o el sumador).

---

## 2. Los postulados (se aceptan, definen el álgebra)

| # | Postulado | Forma OR | Forma AND |
|---|---|---|---|
| 1 | **Identidad** (elemento neutro) | `A + 0 = A` | `A · 1 = A` |
| 2 | **Conmutativa** | `A + B = B + A` | `A · B = B · A` |
| 3 | **Asociativa** | `A + (B + C) = (A + B) + C` | `A·(B·C) = (A·B)·C` |
| 4 | **Distributiva** | `A + (B·C) = (A+B)·(A+C)` | `A·(B+C) = A·B + A·C` |
| 5 | **Complemento** | `A + A' = 1` | `A · A' = 0` |
| 6 | **Dominancia** (elemento nulo) | `A + 1 = 1` | `A · 0 = 0` |

> [!important] El postulado que confunde a todos
> La distributiva del **OR sobre el AND** — `A + B·C = (A+B)·(A+C)` — **no existe** en el álgebra común (`2 + 3·4 = 14`, pero `(2+3)(2+4) = 30`). En Boole **sí vale**, porque sólo hay 0 y 1. Se demuestra con tabla de verdad en 8 filas (o mirando que si `A = 1` los dos lados dan 1, y si `A = 0` los dos lados dan `B·C`). Este es el postulado que más se pregunta.

---

## 3. Los teoremas (se deducen de los postulados)

| Teorema | Forma OR | Forma AND |
|---|---|---|
| **Idempotencia** | `A + A = A` | `A · A = A` |
| **Involución** (doble negación) | `(A')' = A` | — |
| **Absorción** | `A + A·B = A` | `A·(A + B) = A` |
| **Absorción (variante)** | `A + A'·B = A + B` | `A·(A' + B) = A·B` |
| **Combinación** | `A·B + A·B' = A` | `(A+B)·(A+B') = A` |
| **DeMorgan** | `(A + B)' = A'·B'` | `(A·B)' = A' + B'` |
| **Consenso** | `A·B + A'·C + B·C = A·B + A'·C` | `(A+B)(A'+C)(B+C) = (A+B)(A'+C)` |

**El principio de dualidad** (esto sube nota): si en una identidad válida cambiás `0↔1`, `·↔+` y dejás las variables igual, la identidad que queda **también es válida**. Por eso la tabla tiene dos columnas: **no hay que memorizar el doble**, sólo saber dualizar.

> [!example] Demostración de la absorción (por tabla, 4 filas)
> | A | B | A·B | A + A·B |
> |---|---|---|---|
> | 0 | 0 | 0 | 0 |
> | 0 | 1 | 0 | 0 |
> | 1 | 0 | 0 | 1 |
> | 1 | 1 | 1 | 1 |
>
> La columna `A + A·B` es **idéntica** a la columna `A` ⇒ `A + A·B = A`. ✔ (Si A ya vale 1, agregar A·B no cambia nada; y si A vale 0, A·B vale 0.)

---

## 4. Simplificar analíticamente (lo que corrige el TP3)

> [!warning] La regla del TP3
> En el [[TP3 Simplificación analítica]] **no alcanza con llegar al resultado**: hay que **citar la ley, regla o teorema aplicado en cada paso**. Un renglón sin justificar no se corrige como correcto.

### Ejemplo 1 — el clásico
```
F = A·B + A·B' + A'·B
  = A·(B + B')  + A'·B        ← distributiva (saco A de factor común)
  = A·1         + A'·B        ← complemento (B + B' = 1)
  = A           + A'·B        ← identidad (A·1 = A)
  = (A + A')·(A + B)          ← distributiva (OR sobre AND)
  = 1·(A + B)                 ← complemento
  = A + B                     ← identidad
```
**Atajo con la misma validez:** `A + A'·B = A + B` es directamente el **teorema de absorción (variante)**. Pasamos de **3 AND + 1 OR de 3 entradas** a **1 OR de 2 entradas**.

### Ejemplo 2 — dos variables que se cancelan
```
F = A'·B'·C + A'·B·C + A·B'·C + A·B·C
  = A'·C·(B' + B) + A·C·(B' + B)     ← distributiva (dos veces)
  = A'·C + A·C                       ← complemento
  = C·(A' + A)                       ← distributiva
  = C                                ← complemento
```
Moraleja: si una variable aparece **con y sin negación** en todos los términos, **desaparece**.

### Ejemplo 3 — con paréntesis
```
F = (A + B)·(A + C)
  = A + B·C                          ← distributiva (dual, "al revés")
```
Y al revés: `A + B·C = (A+B)·(A+C)`. Las dos formas son válidas: se elige la que use **menos compuertas** (`A + B·C` = 1 AND + 1 OR + 1 NOT; `(A+B)(A+C)` = 2 OR + 1 AND).

### Ejemplo 4 — éste es el que más se equivoca
```
F = A·B + A'·B + A·B'      ← ¡ojo, hay un término repetido lógico!
  = B·(A + A') + A·B'      ← distributiva
  = B + A·B'               ← complemento
  = B + A                  ← absorción (variante)
```

---

## 5. Cómo se cuenta el "ahorro" (para el cierre de la respuesta)

| Función original | Compuertas | Función simplificada | Compuertas |
|---|---|---|---|
| `A·B + A·B' + A'·B` | 3 AND + 1 OR(3) = **4** | `A + B` | **1** OR |
| `A'·B'·C + A'·B·C + A·B'·C + A·B·C` | 4 AND(3) + 1 OR(4) = **5** | `C` | **0** (un cable) |
| `(A+B)·(A+C)` | 3 | `A + B·C` | 2 (+1 NOT) |

Contar compuertas es la forma de **demostrar que simplificar sirve**: menos compuertas ⇒ menos área, menos consumo y **menos retardo de propagación** (la señal atraviesa menos niveles).

---

## 6. Las compuertas universales (bonus que impresiona)

Con **NAND** o con **NOR** solas se puede armar todo:
```
   A'  = NAND(A, A)                 A'  = NOR(A, A)
   A·B = NAND(NAND(A,B), NAND(A,B)) A+B = NOR(NOR(A,B), NOR(A,B))
   A+B = NAND(A', B')  (DeMorgan)   A·B = NOR(A', B')  (DeMorgan)
```
Por eso los chips reales se fabrican casi todos con NAND/NOR: **es más barato fabricar un solo tipo de compuerta**. Ver [[Compuertas lógicas]] y [[Leyes de DeMorgan]].

---

## 7. Cómo responderlo en el final (3–4 minutos)

**Movimiento 1 — definición (20 s).** "Álgebra de Boole: conjunto {0, 1} con tres operaciones (+, ·, ') que cumple los postulados de identidad, conmutatividad, distributividad y complemento. Es el lenguaje de los circuitos combinacionales."

**Movimiento 2 — la tabla de compuertas (30 s).** OR, AND, NOT con su tabla y la analogía serie/paralelo. Aclarar que `1 + 1 = 1`.

**Movimiento 3 — los postulados y los teoremas (60 s).** Nombrar los 6 postulados y los teoremas principales; **demostrar la absorción con 4 filas** (es rápido y muestra método). Mencionar **dualidad**.

**Movimiento 4 — DeMorgan y una simplificación (60 s).** Enunciar DeMorgan y hacer el ejemplo `AB + AB' + A'B = A + B` citando cada ley.

**Movimiento 5 — cierre (20 s).** "Simplificar es reescribir la función sin cambiar la tabla de verdad, para gastar menos compuertas: menos costo, menos consumo y menos retardo. Cuando no se ve el camino analítico, se usa **Karnaugh** ([[Mintérminos y maxtérminos]])."

### Repreguntas típicas

| Repregunta | Respuesta corta |
|---|---|
| ¿Cuántos valores tiene el álgebra? | **Dos**: 0 y 1 (binaria) |
| ¿Qué diferencia hay entre postulado y teorema? | El postulado **se acepta** (define el álgebra); el teorema **se demuestra** a partir de ellos |
| Demostrame que `A + A·B = A` | Tabla de verdad de 4 filas, o "si A = 1 ya es 1; si A = 0, A·B = 0" |
| ¿Vale `A + B·C = (A+B)(A+C)`? | **Sí** (distributiva del OR sobre el AND); en el álgebra común no valdría |
| ¿Para qué sirve todo esto? | Para **minimizar** funciones: menos compuertas, menos costo y menos retardo |
| ¿Qué es dualizar? | Cambiar `·↔+` y `0↔1`; si la identidad valía, la dual también |
| ¿Qué es una compuerta universal? | La que sola permite armar cualquier función: **NAND** y **NOR** |
| ¿Y si la función es de 5 variables? | Se simplifica con **Karnaugh** (hasta 4–5) o con **Quine-McCluskey** |

---

## 8. Errores típicos

- Sumar como en aritmética: `1 + 1 = 1`, no 2; y `A + A = A` (idempotencia), no `2A`.

- Aplicar `(A + B)' = A' + B'` (falso: es **DeMorgan**, `(A+B)' = A'·B'`).

- Simplificar **sin justificar** los pasos (en el TP3 y en el oral se corrige el método).

- Olvidar el orden de operaciones (`'` primero, después `·`, después `+`).

- Creer que "más simplificado" siempre significa "con menos literales": lo que importa es **menos compuertas** y, a igual compuertas, **menos niveles** (retardo).

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2 — Circuitos lógicos y digitales* | comienzo de la unidad: **álgebra de Boole, postulados y teoremas** | la lista exacta de postulados y teoremas **que usa la cátedra**, en su notación | **Es la fuente exacta** de esta pregunta |
| **[[TP2 Álgebra de Boole]]** · **[[TP3 Simplificación analítica]]** | los TPs | demostrar las leyes con tabla **y** con circuito; simplificar **citando la ley** en cada paso | Lo que se corrige: el método, no sólo el resultado |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **álgebra booleana y simplificación** | teoremas con su demostración y ejemplos de simplificación paso a paso | **La mejor ampliación**: muchísimos ejercicios resueltos |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **álgebra de Boole** | postulados, formas canónicas, mapas de Karnaugh | Formalización y ejercicios |
| **Tocci / Widmer, *Sistemas digitales*** (si lo tenés) | capítulos de **operaciones booleanas** y **simplificación** | tablas de teoremas y método de simplificación con conteo de compuertas | Muy didáctico |
| **[[Compuertas lógicas]]** · **[[Leyes de DeMorgan]]** · **[[Mintérminos y maxtérminos]]** | notas de la bóveda | las tres herramientas que se usan con el álgebra | Encadenar el estudio |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | apéndice de **lógica digital** | repaso formal (si querés lenguaje de ingeniería) | Contexto de arquitectura |

---

## Relacionado
[[Leyes de DeMorgan]] · [[Mintérminos y maxtérminos]] · [[Compuertas lógicas]] · [[Decodificador]] · [[Multiplexor]] · [[Semisumador]] · [[Sumador completo]] · [[Flip-Flops SR, D, JK y T]]
