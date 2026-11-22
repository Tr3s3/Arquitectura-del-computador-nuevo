---
unidad: 1
tipo: concepto
examen: practica
prioridad: alta
---
# Sumador completo (full adder)

> [!abstract] En una frase
> Suma **tres bits** (A, B y el acarreo de entrada Cin) y entrega **suma S** y **acarreo de salida Cout**:
> `S = A ⊕ B ⊕ Cin`  ·  `Cout = A·B + Cin·(A⊕B)`. Es la celda que, repetida n veces, suma palabras de n bits.

## Contexto: por qué hace falta
El [[Semisumador]] no acepta acarreo de entrada, así que no se puede encadenar. Para sumar 1011 + 0110 hay
que sumar **columna por columna**, y cada columna recibe el acarreo de la anterior: eso exige una celda de
3 entradas. El sumador completo es **el circuito aritmético más importante del computador**: está en la ALU,
en el incrementador del PC, en el sumador de direcciones de [[BLUE indexada (RIF, RID, nuevo formato)|BLUE indexada]]
y en los contadores.

## Tabla de verdad
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

**Lectura rápida:** S = 1 cuando hay **un número impar de unos**; Cout = 1 cuando hay **dos o tres unos**.

## Funciones (canónicas y simplificadas)
- `S = Σm(1,2,4,7) = A'B'Cin + A'BCin' + AB'Cin' + ABC`  → simplificado: **`S = A ⊕ B ⊕ Cin`**
- `Cout = Σm(3,5,6,7) = A'BCin + AB'Cin + ABCin' + ABC`  → simplificado: **`Cout = A·B + Cin·(A⊕B)`**

La demostración de la simplificación de Cout: `A'BCin + AB'Cin + ABCin' + ABC` = `Cin(A'B + AB') + AB(Cin' + Cin)`
= `Cin(A⊕B) + AB`. Es el clásico "acarreo generado + acarreo propagado":

- **generado** `G = A·B` (los dos bits ya producen acarreo),
- **propagado** `P = A⊕B` (el acarreo de entrada pasa si exactamente uno de los bits es 1),
- `Cout = G + P·Cin`.

## Circuito (2 XOR + 2 AND + 1 OR)
![sumador_completo](assets/sumador_completo.svg)

Estructura interna, de izquierda a derecha:
1. `X1`: `S1 = A ⊕ B`
2. `A1`: `A·B` (acarreo generado)
3. `X2`: `S = S1 ⊕ Cin` ← **la suma final**
4. `A2`: `S1 · Cin` (acarreo propagado)
5. `O1`: `Cout = A·B + S1·Cin`

Otra forma de verlo (muy usada en el final): **un sumador completo = dos semisumadores + una OR**.
Semisumador 1 (A,B) da S1 y C1 = A·B; semisumador 2 (S1,Cin) da S y C2 = S1·Cin; la OR combina C1 y C2 en Cout.

## Sumador de n bits (acarreo en cascada)
Se conectan n sumadores completos y **el Cout de cada uno va al Cin del siguiente**:

```
     A3 B3        A2 B2        A1 B1        A0 B0
      │  │         │  │         │  │         │  │
Cout← FA ──C3── FA ──C2── FA ──C1── FA ←Cin = 0
```
Se llama **sumador con acarreo en cascada (ripple carry)**: el retardo crece linealmente con n porque el
último bit tiene que esperar la propagación de todos los acarreos. La solución (mencionarla de memoria) es
el **acarreo anticipado (carry look-ahead)**, que calcula todos los Ci en paralelo a partir de los G y P de
cada etapa: más compuertas, mucho menos retardo.

> [!example] Ejercicio típico
> Sumar 0110 + 0101 con un sumador de 4 bits (Cin = 0 del bit 0).
> - bit 0: 0+1+0 ⇒ S = 1, C = 0
> - bit 1: 1+0+0 ⇒ S = 1, C = 0
> - bit 2: 1+1+0 ⇒ S = 0, C = 1
> - bit 3: 0+0+1 ⇒ S = 1, C = 0
> Resultado: 1011 (= 11). ✔  (6 + 5 = 11)
> Si hubiera Cout = 1 en el último bit, eso es **desbordamiento** de la palabra.

## Cómo responderlo en el final (práctica, vale nota)
1. **Definición**: suma 3 bits, produce S y Cout; es la celda del sumador de n bits.
2. **Tabla de verdad** completa (8 filas) — dibujarla prolija.
3. **Funciones**: por mintérminos y simplificadas (`S = A⊕B⊕Cin`, `Cout = A·B + Cin(A⊕B)`).
4. **Gráfico**: las 5 compuertas, con los nombres de las señales intermedias (S1, A·B, S1·Cin).
5. **Cierre**: n sumadores completos encadenados por el acarreo = sumador de n bits; el retardo por
   propagación se resuelve con carry look-ahead.

## Errores típicos
- Escribir `S = A+B+Cin` (es la suma módulo 2, no la aritmética: hay que usar XOR).
- Poner `Cout = A·B·Cin` (con AND de los tres, la mayoría de los acarreos desaparece).
- Confundir **Cin** (entrada) con **Cout** (salida) al encadenar: se conecta Cout → Cin del **siguiente**.

## Relacionado
[[Semisumador]] · [[ALU]] · [[Hardware aritmético (resumen)]] · [[Compuertas lógicas]]
