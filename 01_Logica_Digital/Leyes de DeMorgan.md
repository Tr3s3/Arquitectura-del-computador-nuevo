---
unidad: 2
tipo: concepto
examen: practica
prioridad: maxima
---
# Leyes de DeMorgan

> [!abstract] En una frase
> **DeMorgan** son **dos teoremas** que dicen cómo se **niega** una operación:
> **`(A + B)' = A' · B'`** y **`(A · B)' = A' + B'`**. En palabras: **negar un "o" da un "y" de negaciones**, y
> **negar un "y" da un "o" de negaciones**. Regla práctica: **cuando una barra grande se rompe, cambia el signo y
> se niega todo lo que estaba abajo**.

> [!note] Si es la primera vez que ves esto
> Es lógica de todos los días. "**No** es cierto que (*llueva* **y** *haga frío*)" equivale a decir
> "**no** llueve **o** no hace frío". Y "**no** es cierto que (*tenga plata* **o** *tenga tiempo*)" equivale a
> "no tengo plata **y** no tengo tiempo".
>
> Fijate lo que pasó: al entrar la negación **adentro**, el **Y** se convirtió en **O** (y al revés) y **cada**
> condición quedó negada. Eso es exactamente DeMorgan. Suena obvio, pero es la herramienta que permite
> **cambiar un circuito de AND a OR sin cambiar lo que hace** y, sobre todo, **pasar todo a NAND** (o todo a
> NOR), que es como se fabrican los chips de verdad.

---

## 1. Los dos teoremas

| # | Teorema | Nombre | Lectura |
|---|---|---|---|
| 1 | **`(A + B)' = A' · B'`** | negación del OR | "no (A o B)" = "ni A ni B" |
| 2 | **`(A · B)' = A' + B'`** | negación del AND | "no (A y B)" = "falla al menos uno" |

Son **duales** entre sí (cambiando `·↔+`), como todo en Boole ([[Álgebra de Boole — postulados y teoremas]]).
Y **se generalizan a cualquier número de variables**:

```
   (A + B + C + D)' = A' · B' · C' · D'
   (A · B · C · D)' = A' + B' + C' + D'
```

> [!important] La regla de la barra larga (la que hay que decir en el oral)
> Para negar una expresión:
> 1. **Se rompe la barra grande**.
> 2. **Cambia el operador** (`·` ⇄ `+`).
> 3. **Se niega cada término** (si un término ya tenía barra, se le saca).
>
> `((A + B') · C)' = (A + B')' + C' = A'·B + C'`

---

## 2. Demostración por tabla de verdad (lo que se pide)

### Teorema 1 — `(A + B)' = A' · B'`
| A | B | A + B | **(A+B)'** | A' | B' | **A'·B'** |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | **1** | 1 | 1 | **1** |
| 0 | 1 | 1 | **0** | 1 | 0 | **0** |
| 1 | 0 | 1 | **0** | 0 | 1 | **0** |
| 1 | 1 | 1 | **0** | 0 | 0 | **0** |

Las dos columnas marcadas son **idénticas** en las 4 filas ⇒ los teoremas son equivalentes. ✔

### Teorema 2 — `(A · B)' = A' + B'`
| A | B | A · B | **(A·B)'** | A' | B' | **A' + B'** |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | **1** | 1 | 1 | **1** |
| 0 | 1 | 0 | **1** | 1 | 0 | **1** |
| 1 | 0 | 0 | **1** | 0 | 1 | **1** |
| 1 | 1 | 1 | **0** | 0 | 0 | **0** |

Idénticas ⇒ válido. ✔

> [!tip] Cómo se demuestra "elegante" sin tabla
> Por **dualidad y complemento**: `(A+B)·(A+B)' = 0` y `(A+B) + (A+B)' = 1`. Si probás que
> `(A+B)·(A'·B') = A·A'·B' + B·A'·B' = 0` y que `(A+B) + A'·B' = (A + A' + B')(B + A' + B') = 1·1 = 1`,
> entonces `A'·B'` cumple **exactamente** la definición de complemento de `(A+B)`, y el complemento es único.
> Con eso alcanza; la tabla es el camino corto y seguro.

---

## 3. Para qué sirve (los tres usos que se preguntan)

### Uso 1 — Simplificar y encontrar la función "más barata"
```
F = (A'·B)'                 = A + B'            ← DeMorgan 2
F = ((A + B)·C)'            = (A+B)' + C' = A'·B' + C'
F = (A·B' + C)'             = (A·B')' · C' = (A' + B)·C'
```
Fijate el patrón: al romper la barra, **los productos se vuelven sumas y las sumas, productos**, y **todas** las
variables cambian de estado de negación. Olvidarse de negar **una** variable es el error más común.

### Uso 2 — Pasar todo a NAND (o todo a NOR): por qué existe el chip real
Toda función en forma **suma de productos** (AND-OR) se implementa con **sólo compuertas NAND**:

```
   F = A·B + C·D
   F = ((A·B + C·D)')'                ← doble negación (involución)
     = ((A·B)' · (C·D)')'             ← DeMorgan sobre el OR interno
     = NAND( NAND(A,B) , NAND(C,D) )  ← dos NAND + un NAND final
```
Es decir: **NAND-NAND = AND-OR**. Lo mismo con NOR: **NOR-NOR = OR-AND**.

### Uso 3 — Pasar de mintérminos a maxterms (¡esto cae!)
El **complemento** de una función intercambia mintérminos y maxtérminos:

```
   Si  F(A,B) = Σm(0, 2)   ⇒   F' = Σm(1, 3) = ΠM(0, 2)
```
O sea: `F'` tiene los mintérminos que **faltaban**, y `F` escrita como producto de maxterms usa **esos mismos
índices**. Se ve en [[Mintérminos y maxtérminos]].

---

## 4. Ejemplo resuelto completo (el que conviene tener a mano)

Simplificar `F = (A + B·C)' + A·B'` y dibujar el circuito más chico.

```
Paso 1 — DeMorgan sobre el paréntesis grande:
   (A + B·C)' = A' · (B·C)'            ← barra larga: se rompe y cambia el signo
              = A' · (B' + C')         ← segunda barra: DeMorgan otra vez
Paso 2 — reemplazo:
   F = A'·(B' + C') + A·B'
Paso 3 — distributiva (saco B' de factor común):
   F = A'·B' + A'·C' + A·B'
Paso 4 — agrupo los que tienen B':
   F = B'·(A' + A) + A'·C'
     = B'·1 + A'·C'                     ← complemento
     = B' + A'·C'                       ← identidad
```

**Circuito simplificado**: 1 NOT (A'), 1 AND (A'·C') y 1 OR de 2 entradas ⇒ **3 compuertas**.
El original tenía 2 AND + 1 OR + 1 NOT + 1 OR = **5 compuertas**. Y si querés todo con NAND, se puede:
`F = B' + A'C'` ⇒ `F = (B · (A + C))'` (aplicando DeMorgan al revés) ⇒ **1 AND + 1 OR + 1 NAND**.

---

## 5. Errores típicos (los cuatro que anulan el punto)

| ❌ Mal | ✅ Bien | Por qué |
|---|---|---|
| `(A + B)' = A' + B'` | `(A + B)' = A'·B'` | Al romper la barra **cambia el operador** |
| `(A·B)' = A'·B'` | `(A·B)' = A' + B'` | Ídem |
| `(A + B·C)' = A' + B'·C'` | `= A'·(B' + C')` | La negación afecta **toda** la expresión, no término por término |
| `(A + B')' = A' + B` | `= A'·B` | Si el término ya estaba negado, al romper la barra **se le saca** la negación |

> [!warning] La versión con "ni"
> "**Ni** A **ni** B" se escribe `A'·B'` **y** es igual a `(A + B)'`. Si en el oral decís "no A o no B" para
> `(A·B)'`, está perfecto; si decís "no A y no B" para `(A·B)'`, es un error de operador.

---

## 6. Cómo responderlo en el final (2–3 minutos)

**Movimiento 1 — enunciado (20 s).** Las dos fórmulas, con el ejemplo del "llueve y hace frío".

**Movimiento 2 — demostración (50 s).** Tabla de verdad de 4 filas para `(A+B)' = A'·B'`, mostrando que las
columnas coinciden.

**Movimiento 3 — la regla (20 s).** "Barra larga se rompe: cambia el operador y se niega todo lo de adentro", y
generalización a n variables.

**Movimiento 4 — aplicación (40 s).** Simplificar `((A+B)·C)' = A'B' + C'` y decir que **DeMorgan permite pasar
toda función AND-OR a NAND-NAND** (o OR-AND a NOR-NOR), que es como se fabrica en la práctica.

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Cuántos teoremas son? | **Dos**, y son **duales** |
| Demostralo | Tabla de verdad: las columnas `(A+B)'` y `A'·B'` coinciden en las 4 filas |
| ¿Vale para 3 variables? | Sí, se generaliza: `(A+B+C)' = A'B'C'` |
| ¿Negar `A` y `B` por separado es lo mismo? | **No**: `(A+B)'` no es `A' + B'` |
| ¿Para qué sirve en la práctica? | Convertir a **NAND/NOR** (un solo tipo de compuerta en el chip) y simplificar funciones |
| ¿Qué relación tiene con los mintérminos? | `F'` usa los mintérminos que faltaban; eso da los maxterms de `F` |
| ¿Qué pasa si hay una barra sobre una barra? | Se cancelan (involución: `(A')' = A`) |

---

## 7. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **teoremas de DeMorgan** (dentro del álgebra de Boole) | el enunciado y la demostración tal como los da la cátedra | **Es la fuente exacta** de esta pregunta |
| **[[TP2 Álgebra de Boole]]** | el TP | las leyes a demostrar con tabla y con circuito equivalente | Lo que se entrega por escrito |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **álgebra booleana** (sección "teoremas de DeMorgan") | demostraciones y ejemplos de aplicación a simplificación | **La mejor ampliación**: ejercicios resueltos |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **álgebra de Boole** | DeMorgan y su uso en formas canónicas y en NAND/NOR | Formalización |
| **Tocci / Widmer, *Sistemas digitales*** | capítulo de **aplicaciones del álgebra booleana** | cómo convertir AND-OR a NAND-NAND paso a paso | Muy útil para el pizarrón |
| **[[Álgebra de Boole — postulados y teoremas]]** · **[[Mintérminos y maxtérminos]]** | notas de la bóveda | postulados y la relación mintérminos ↔ maxterms | El marco completo |
| **[[Compuertas lógicas]]** | nota de la bóveda | NAND y NOR como compuertas universales | Para el cierre práctico |

---

## Relacionado
[[Álgebra de Boole — postulados y teoremas]] · [[Mintérminos y maxtérminos]] · [[Compuertas lógicas]] ·
[[Multiplexor]] · [[Decodificador]] · [[Sumador completo]]
