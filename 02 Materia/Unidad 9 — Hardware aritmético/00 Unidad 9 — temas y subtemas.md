---
tipo: indice
unidad: 9
---
# Unidad 9 — Hardware aritmético

> [!abstract] Qué pide la unidad
> Cómo la ALU hace **cuentas**: suma y resta en **complemento a 2**, acarreo anticipado, multiplicación
> (**Booth**), división, **punto flotante** y aritmética **BCD**. Nada de esto es magia: son los circuitos de la
> unidad 1 encadenados.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 9 — Hardware aritmético/
├── 9.1 Suma y resta/
│   ├── 9.1.1 Complemento a 2 y desbordamiento
│   └── 9.1.2 Acarreo anticipado (G y P)
├── 9.2 Multiplicación/
│   ├── 9.2.1 Sumas y desplazamientos
│   └── 9.2.2 Algoritmo de Booth
├── 9.3 División/
│   └── 9.3.1 Restauración y no restauración
├── 9.4 Punto flotante/
│   ├── 9.4.1 Formato, normalización y operaciones
│   └── 9.4.2 IEEE 754
└── 9.5 Aritmética BCD/
    └── 9.5.1 Suma decimal corregida
```

**5 temas y 8 subtemas.** Cada subtema va a ser **una nota** dentro de la carpeta de su tema,
y al terminar la unidad se genera **`00 Síntesis — Unidad 9`** con todo el contenido junto (como ya está hecho en
[[00 Síntesis — Unidad 1|la Unidad 1]]).

| Tema | Subtemas | Estado |
|---|---|---|
| **9.1 Suma y resta** | 9.1.1 Complemento a 2 y desbordamiento · 9.1.2 Acarreo anticipado (G y P) | ⏳ a desarrollar |
| **9.2 Multiplicación** | 9.2.1 Sumas y desplazamientos · 9.2.2 Algoritmo de Booth | ⏳ a desarrollar |
| **9.3 División** | 9.3.1 Restauración y no restauración | ⏳ a desarrollar |
| **9.4 Punto flotante** | 9.4.1 Formato, normalización y operaciones · 9.4.2 IEEE 754 | ⏳ a desarrollar |
| **9.5 Aritmética BCD** | 9.5.1 Suma decimal corregida | ⏳ a desarrollar |

> [!note] Qué hay ya de esta unidad
> El **desarrollo de examen** de casi todos estos temas ya está escrito (está enlazado más abajo, en la tabla de
> material disponible). Lo que falta es la **versión de programa**: el subtema desarrollado en la carpeta de su
> tema, con el detalle de la cursada y los TPs.

## Material ya disponible de esta unidad
| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **9.1 Suma y resta** | semisumador · sumador completo · sumador de n bits · `A − B = A + B' + 1` · desbordamiento | [[Hardware aritmético (resumen)]] · [[Semisumador]] · [[Sumador completo]] · carpeta `Tanda 3/3.8` |
| **9.2 Acarreo anticipado** | `G` y `P` · `Cout = G + P·Cin` · calculadora de acarreos en paralelo | [[Hardware aritmético (resumen)]] · [[Sumador completo]] |
| **9.3 Multiplicación** | sumas y desplazamientos · algoritmo de **Booth** (complemento a 2) | [[Hardware aritmético (resumen)]] |
| **9.4 División** | restauración · no restauración · desplazamientos | [[Hardware aritmético (resumen)]] |
| **9.5 Punto flotante** | signo, exponente, mantisa · normalización · suma y multiplicación · IEEE 754 | [[Hardware aritmético (resumen)]] |
| **9.6 Aritmética BCD** | suma decimal corregida (sumar 6 si > 9) | [[Hardware aritmético (resumen)]] |
| **9.7 La ALU** | señales de selección · flags (Z, C, N, V) | [[ALU]] · `Unidad 3/Tema 3.2 La ALU/` |

---

## Qué hay que saber hacer
1. **Sumar en binario** con acarreo y detectar **desbordamiento** en complemento a 2.
2. Explicar **por qué un sumador resta** (`XOR` en B y `Cin = 1`).
3. Describir **Booth** en una frase ("mira el bit y el anterior: 01 suma, 10 resta, 00/11 no hace nada").
4. Decir **por qué el punto flotante necesita normalizar**.

## TPs de la unidad
[[TP5 Sumadores]] (la base) · no hay TP específico de la unidad 9.

## Fuente de la cátedra
Apuntes de la **Unidad 9** · Hamacher (capítulo de aritmética) · Stallings (aritmética de computadores) ·
Floyd (sumadores).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 8 — temas y subtemas]] ·
[[00 Unidad 10 — temas y subtemas]]
