---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T01 · Sumador completo (tabla de verdad, funciones y gráfico)

> [!question] Pregunta
> Diseñe un sumador completo: tabla de verdad, funciones simplificadas y gráfico.

## 1. Teoría previa

**Suma binaria.** Sumar dos bits `A` y `B` da un bit de suma `S` y un bit de **acarreo** `C`. Con un acarreo de entrada `Cin` (que viene de la columna anterior), la suma tiene tres bits de entrada.

**Semisumador (half adder).** Suma sólo dos bits:
- `S = A ⊕ B` (XOR)
- `C = A · B` (AND)

**Sumador completo (full adder).** Suma tres bits: `A`, `B` y `Cin`. Tiene dos salidas: `S` y `Cout`.

**Dato clave.** El semisumador no alcanza para sumar varios bits, porque no recibe el acarreo de la columna anterior. El sumador completo sí, y se encadenan para sumar palabras (sumador de n bits).

## 2. Contexto

El sumador es el **ejemplo estrella** de un circuito combinacional: tiene tabla de verdad, función y dibujo. Es la práctica que más se toma en el final porque reúne todo lo de las unidades 1 y 2: compuertas, mintérminos, simplificación y dibujo. Lo mismo vale para el resto de las prácticas.

## 3. Gráfico

![[T01-sumador-completo.svg]]

*Lectura:* dos semisumadores en cascada y una OR para el acarreo de salida. La tabla de la izquierda cubre las entradas con acarreo 0 y la de la derecha, con A = 1.

## 4. Desarrollo detallado

### 4.1 Tabla de verdad (8 filas)

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

### 4.2 Funciones (sumas de mintérminos)

Con `A` como bit más significativo (fila 0 = `000`):
- `S = Σ m(1, 2, 4, 7)` → `S = A'B'Cin + A'BCin' + AB'Cin' + ABCin`
- `Cout = Σ m(3, 5, 6, 7)` → `Cout = A'BCin + AB'Cin + ABCin' + ABCin`

### 4.3 Forma simplificada (la que se dibuja)

- `S = A ⊕ B ⊕ Cin`
- `Cout = A·B + Cin·(A ⊕ B)`

Se verifica: si `A ⊕ B = 1`, `Cout = Cin`; si `A = B = 1`, `Cout = 1`; si `A = B = 0`, `Cout = 0`. Eso coincide con la tabla.

### 4.4 Circuito

1. **Semisumador 1**: entradas A y B → `S1 = A ⊕ B`, `C1 = A · B`.
2. **Semisumador 2**: entradas `S1` y `Cin` → `S = S1 ⊕ Cin`, `C2 = S1 · Cin`.
3. **OR**: `Cout = C1 + C2`.

Es el mismo resultado que la forma simplificada: `C2 = Cin·(A ⊕ B)`.

## 5. Cómo se responde (4–5 minutos)

1. **Tabla de verdad**: 8 filas, de `000` a `111`.
2. **Funciones**: S y Cout como sumas de mintérminos.
3. **Simplificación**: `S = A⊕B⊕Cin`, `Cout = AB + Cin(A⊕B)`.
4. **Gráfico**: dos semisumadores y una OR.
5. **Cierre**: "Con dos semisumadores y una OR se hace un sumador completo; encadenados, suman palabras."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántas filas tiene la tabla? | 8 = 2³. |
| ¿Por qué no sirve un semisumador en la columna 2? | Porque no recibe el acarreo de entrada. |
| ¿Cuánto vale Cout para A=1, B=0, Cin=1? | 1 (1 + 0 + 1 = 10₂). |
| Error común | Escribir `Cout = A + B`. Es `AB + Cin(A⊕B)`. |

## 7. Relacionado

- [[Sumador completo]] · [[Semisumador]] · [[1.5.1 Semisumador y sumador completo]] · [[1.5.2 Sumador de n bits y resta en complemento a 2]]
- [[Mintérminos y maxtérminos]] · [[T05 Álgebra de Boole, postulados y teoremas de DeMorgan]]
