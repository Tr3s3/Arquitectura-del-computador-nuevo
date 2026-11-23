---
tp: 4
unidad: 1
tipo: tp
---
# TP4 — De tabla de verdad a función: mintérminos, maxtérminos y Karnaugh

> [!abstract] Consigna (cátedra)
> **Ej. 1:** dada una tabla de verdad, encontrar la función booleana que la representa aplicando
> **mintérminos o maxtérminos** según convenga.
> **Ej. 2:** dada una función booleana, reducirla a su expresión mínima con **mapas de Karnaugh** y
> desarrollar su **circuito lógico**.

## Método: de la tabla a la función (mintérminos)
1. Contar variables ⇒ n ⇒ 2ⁿ filas.
2. Marcar las filas donde **F = 1**.
3. Cada fila con F = 1 es un **mintérmino**: producto con la variable **directa si vale 1** y **negada si vale 0**.
4. Unir con OR: `F = Σm(...)` ⇒ forma **SOP** (suma de productos).
5. Si hay **más unos que ceros**, conviene el camino inverso (maxtérminos / POS): la expresión queda más corta.

| A B C | F | mintérmino |
|---|---|---|
| 0 0 0 | 0 | — |
| 0 0 1 | 1 | A'B'C |
| 0 1 0 | 1 | A'BC' |
| 0 1 1 | 0 | — |
| 1 0 0 | 1 | AB'C' |
| 1 0 1 | 0 | — |
| 1 1 0 | 0 | — |
| 1 1 1 | 1 | ABC |

⇒ `F = Σm(1,2,4,7) = A'B'C + A'BC' + AB'C' + ABC`

## Método: mapa de Karnaugh (Ej. 2)
1. Dibujar el mapa de 2, 3 o 4 variables con **código Gray** en los bordes (00, 01, 11, 10): celdas
   adyacentes **difieren en un solo bit**.
2. Poner 1 en las celdas de los mintérminos.
3. Agrupar **1, 2, 4, 8…** unos en rectángulos, lo más grandes posible, pudiendo **envolver los bordes**.
4. Cada grupo elimina las variables que cambian dentro del grupo.
5. **OR** de los grupos = expresión mínima; después se dibuja el circuito (una AND por grupo + una OR).

> [!example] Ejemplo de 3 variables
> Si los unos están en 1, 3, 5 y 7 (toda la columna de C = 1), un solo grupo de 4 ⇒ `F = C`.
> Por álgebra habría que escribir cuatro términos y simplificarlos.

> [!tip] Reglas de oro del Karnaugh
> · Los grupos pueden **superponerse** y **envolver** los bordes (el mapa es un toroide).
> · Menos grupos y más grandes ⇒ expresión más simple.
> · Todo 1 debe quedar cubierto; los **indiferentes (X)** se usan sólo si conviene.
> · Un grupo que no aporta ningún 1 nuevo se elimina.

## Enlaces
Desarrollo: [[Mintérminos y maxtérminos]] · Práctica: [[Prácticas resueltas]]
Siguiente: [[TP5 Sumadores]]
