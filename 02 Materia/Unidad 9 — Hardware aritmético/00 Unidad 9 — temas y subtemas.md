---
tipo: indice
unidad: 9
---
# Unidad 9 — Hardware aritmético

> [!abstract] Qué pide la unidad
> Cómo se construyen **con compuertas** las cuatro operaciones: **suma/resta** (un sumador y acarreo anticipado),
> **multiplicación** (sumas y desplazamientos, Booth, arreglo), **división** (restas y desplazamientos) y **punto
> flotante** (alinear, normalizar, redondear). Cierra con la aritmética **decimal (BCD)**.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 9 completa (lectura de corrido)]]**: los **10 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 9]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.


> [!important] El hilo de toda la unidad
> **Todo es un sumador.** La resta es una suma (`B' + 1`); la multiplicación son sumas desplazadas; la división son
> restas desplazadas; el punto flotante es una suma de mantisas más lógica de exponentes. Si entendés 9.1, el resto
> es organización.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 9 — Hardware aritmético/
├── Tema 9.1 Suma y resta/
│   ├── 9.1.1 Complemento a 2 y desbordamiento
│   ├── 9.1.2 Acarreo anticipado (G y P)
│   └── Hardware aritmético (resumen)              (nota de desarrollo de examen)
├── Tema 9.2 Multiplicación/
│   ├── 9.2.1 Sumas y desplazamientos
│   ├── 9.2.2 Algoritmo de Booth
│   └── 9.2.3 Arreglo multiplicador
├── Tema 9.3 División/
│   ├── 9.3.1 Restauración y no restauración
│   └── 9.3.2 Sobreflujo y división con signo
├── Tema 9.4 Punto flotante/
│   ├── 9.4.1 Formato, normalización y operaciones
│   └── 9.4.2 IEEE 754
└── Tema 9.5 Aritmética BCD/
    └── 9.5.1 Suma decimal corregida
```

**5 temas y 10 subtemas.** Cada subtema es **una nota** dentro de la carpeta de su tema. La unidad está **cerrada**
y todo su contenido quedó reunido en **[[00 Síntesis — Unidad 9]]**.

| Tema | Subtemas | Estado |
|---|---|---|
| **9.1 Suma y resta** | 9.1.1 Complemento a 2 y desbordamiento · 9.1.2 Acarreo anticipado (G y P) | ✅ |
| **9.2 Multiplicación** | 9.2.1 Sumas y desplazamientos · 9.2.2 Algoritmo de Booth · 9.2.3 Arreglo multiplicador | ✅ |
| **9.3 División** | 9.3.1 Restauración y no restauración · 9.3.2 Sobreflujo y división con signo | ✅ |
| **9.4 Punto flotante** | 9.4.1 Formato, normalización y operaciones · 9.4.2 IEEE 754 | ✅ |
| **9.5 Aritmética BCD** | 9.5.1 Suma decimal corregida | ✅ |

> [!note] Cómo creció el árbol
> El árbol original tenía **8 subtemas**. Al desarrollar se agregaron **dos**: el **arreglo multiplicador** (9.2.3)
> y **sobreflujo y división con signo** (9.3.2), que estaban en el material de la cátedra pero no tenían nota propia.

## Los 5 temas, de un vistazo

| Tema | Índice | La idea en una línea |
|---|---|---|
| **9.1** | [[00 Tema 9.1 — índice]] | `A − B = A + B' + 1` · `V = Cin ⊕ Cout` · `C(i+1) = G + P·C(i)` |
| **9.2** | [[00 Tema 9.2 — índice]] | sumar y desplazar · Booth (pares y signo) · `n²` celdas |
| **9.3** | [[00 Tema 9.3 — índice]] | restar y desplazar · restaurar o no · divisor 0 y cociente que no entra |
| **9.4** | [[00 Tema 9.4 — índice]] | `1.M × 2^e`: alinear, normalizar, redondear |
| **9.5** | [[00 Tema 9.5 — índice]] | si pasa de 9 o hay acarreo: **sumar 6** |

## Material de examen ya disponible de esta unidad
| Tema | Nota | Dónde está además |
|---|---|---|
| **Todo el tema** | [[Hardware aritmético (resumen)]] | `Tema 9.1 Suma y resta/` |
| **Sumadores** | [[Sumador completo]] · [[3.2.1 Estructura, G-P y señales de selección]] | Unidades 1 y 3 · [[TP5 Sumadores]] |
| **Flags** | [[3.2.2 Operaciones aritméticas, lógicas y flags]] | Unidad 3 |
| **Complemento a 2** | [[1.5.2 Sumador de n bits y resta en complemento a 2]] | Tanda 1 |

---

## Qué hay que saber hacer al terminar la unidad
1. **Restar** con complemento a 2 y detectar `V` mirando los **dos** acarreos del MSB.
2. Escribir las **ecuaciones de acarreo anticipado** con `G` y `P` y explicar el retardo.
3. **Multiplicar** con sumas y desplazamientos (y con **Booth** sobre complemento a 2).
4. **Dividir** con el método restaurativo y el no restaurativo, y decir cuál es más rápido.
5. Detectar **sobreflujo** al dividir y manejar los **signos** (signo del resto = signo del dividendo).
6. Sumar en **punto flotante**: alinear, normalizar, redondear, con un ejemplo numérico.
7. Codificar y decodificar un número en **IEEE 754** simple.
8. Corregir una suma **BCD** con la regla del `+6`.

## TPs de la unidad
[[TP5 Sumadores]] (sumador completo, semisumador y acarreo).

## Fuente de la cátedra
Apuntes de la **Unidad 9** (hardware aritmético) · Hamacher (capítulo de aritmética) ·
Stallings (aritmética del computador) · Mano (*Lógica digital*) · Patterson & Hennessy (ALU y FPU).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 8 — temas y subtemas]] ·
[[00 Unidad 10 — temas y subtemas]] · [[00 Síntesis — Unidad 9]]
