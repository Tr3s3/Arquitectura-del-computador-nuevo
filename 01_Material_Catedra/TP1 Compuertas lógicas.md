---
tp: 1
unidad: 1
tipo: tp
---
# TP1 — Compuertas lógicas

> [!abstract] Consigna (cátedra)
> **"Compuertas lógicas: NOT, AND, NAND, OR, NOR, XOR y NXOR. ¿Qué operación corresponde a cada una de
> ellas? Desarrolle tabla de verdad y gráfico."**

## Qué hay que saber para resolverlo
Es el TP más "de pizarrón" de todos: por cada compuerta hay que entregar **tres cosas**:
1. **Símbolo** normalizado (D para AND, escudo curvo para OR, triángulo + círculo para NOT, etc.).
2. **Tabla de verdad** (2 entradas ⇒ 4 filas; NOT tiene 2 filas).
3. **Expresión booleana** y una frase diciendo qué operación representa.

> [!warning] Ojo con el nombre "NXOR"
> La cátedra escribe **NXOR** para la XOR negada (en los libros aparece como **XNOR**). Usá el nombre de la
> cátedra y aclaralo: "NXOR o XNOR, la negación de la XOR".

## Respuesta sintetizada (lo que hay que decir)
| Compuerta | Expresión | Operación en palabras |
|---|---|---|
| **NOT** | `Y = A'` | invierte: vale 1 si A = 0 |
| **AND** | `Y = A·B` | 1 sólo si **todas** las entradas son 1 |
| **NAND** | `Y = (A·B)'` | AND negada: 0 sólo si todas son 1 |
| **OR** | `Y = A + B` | 1 si **alguna** entrada es 1 |
| **NOR** | `Y = (A+B)'` | OR negada: 1 sólo si todas son 0 |
| **XOR** | `Y = A⊕B = A'B + AB'` | 1 cuando las entradas son **distintas** |
| **NXOR** | `Y = (A⊕B)' = AB + A'B'` | 1 cuando las entradas son **iguales** (comparador) |

**Cierre que suma:** NAND y NOR son **universales** (con una sola de ellas se arma cualquier función) — se
demuestra con [[Leyes de DeMorgan]] — y por eso son las que se fabrican como circuito integrado.
XOR/NXOR son la base de la **suma sin acarreo** ([[Semisumador]]) y de los **comparadores**.

## Tabla de verdad completa (para copiar en el pizarrón)
| A | B | AND | NAND | OR | NOR | XOR | NXOR |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |

## Enlaces
Desarrollo: [[Compuertas lógicas]] · Para el oral: [[Tablas de verdad de memoria]] ·
Siguiente: [[TP2 Álgebra de Boole]]
