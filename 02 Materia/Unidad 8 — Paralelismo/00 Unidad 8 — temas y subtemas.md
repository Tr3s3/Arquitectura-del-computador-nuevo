---
tipo: indice
unidad: 8
---
# Unidad 8 — Paralelismo

> [!abstract] Qué pide la unidad
> Las formas de hacer **varias cosas a la vez**: pipeline **aritmético**, procesamiento **vectorial**, **SIMD**,
> **memoria entrelazada** y **multiprocesadores**. Es la continuación del pipeline de instrucciones de la Unidad 7,
> pero acá el paralelismo es por **datos** y por **unidades**.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 8 completa (lectura de corrido)]]**: los **9 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 8]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.


> [!important] Cómo se lee la unidad
> Hay **tres** formas de paralelismo y cada tema es una:
> **tiempo** (pipeline aritmético, 8.1) · **ancho** (vectorial/SIMD, 8.2) · **unidades** (bancos y núcleos, 8.3-8.4).

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 8 — Paralelismo/
├── Tema 8.1 Pipeline aritmético/
│   ├── 8.1.1 Etapas segmentadas y suma de vectores
│   └── 8.1.2 Encadenamiento y speedup
├── Tema 8.2 Procesamiento vectorial y SIMD/
│   ├── 8.2.1 SIMD, registros vectoriales y GPU
│   ├── 8.2.2 Flynn, arreglos SIMD y conectados
│   └── 8.2.3 Multiplicación de matrices
├── Tema 8.3 Memoria entrelazada/
│   ├── 8.3.1 Bancos de memoria y ancho de banda
│   └── 8.3.2 Patrón de entrelazado y conflictos de banco
└── Tema 8.4 Multiprocesadores/
    ├── 8.4.1 Multicore, coherencia de caché y ley de Amdahl
    ├── 8.4.2 Monousuario vs multiusuario
    └── Paralelismo y procesamiento vectorial   (nota de desarrollo de examen)
```

**4 temas y 9 subtemas.** Cada subtema es **una nota** dentro de la carpeta de su tema. La unidad está **cerrada**
y todo su contenido quedó reunido en **[[00 Síntesis — Unidad 8]]**.

| Tema | Subtemas | Estado |
|---|---|---|
| **8.1 Pipeline aritmético** | 8.1.1 Etapas segmentadas y suma de vectores · 8.1.2 Encadenamiento y speedup | ✅ |
| **8.2 Procesamiento vectorial y SIMD** | 8.2.1 SIMD, registros vectoriales y GPU · 8.2.2 Flynn, arreglos SIMD y conectados · 8.2.3 Multiplicación de matrices | ✅ |
| **8.3 Memoria entrelazada** | 8.3.1 Bancos de memoria y ancho de banda · 8.3.2 Patrón de entrelazado y conflictos de banco | ✅ |
| **8.4 Multiprocesadores** | 8.4.1 Multicore, coherencia de caché y ley de Amdahl · 8.4.2 Monousuario vs multiusuario | ✅ |

> [!note] Cómo creció el árbol
> El árbol original tenía **4 subtemas** (uno por tema). Al desarrollar se desdoblaron en **9**: el encadenamiento
> salió de 8.1, Flynn y la multiplicación de matrices de 8.2, el conflicto de banco de 8.3 y monousuario/multiusuario
> de 8.4.

## Los 4 temas, de un vistazo

| Tema | Índice | La idea en una línea |
|---|---|---|
| **8.1** | [[00 Tema 8.1 — índice]] | `k + (n − 1)` ciclos: sale un elemento por ciclo |
| **8.2** | [[00 Tema 8.2 — índice]] | una instrucción, muchos datos |
| **8.3** | [[00 Tema 8.3 — índice]] | bancos en paralelo: más ancho de banda, misma latencia |
| **8.4** | [[00 Tema 8.4 — índice]] | varios flujos + coherencia + ley de Amdahl |

## Material de examen ya disponible de esta unidad
| Tema | Nota | Dónde está además |
|---|---|---|
| **Todo el tema** | [[Paralelismo y procesamiento vectorial]] | `Tema 8.2 …/` |
| **Pipeline (repaso de la 7)** | [[Pipeline]] | `Tanda 2/2.7` |
| **Técnicas de velocidad** | [[Técnicas para aumentar la velocidad]] | Unidad 7 |
| **Bancos y caché** | [[Jerarquía de memorias]] · [[Memoria caché]] | Unidad 2 |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** un pipeline aritmético y calcular ciclos, tiempo y speedup con `k + (n−1)`.
2. Explicar el **encadenamiento** y cuantificar lo que se gana.
3. Nombrar las **cuatro clases de Flynn** con un ejemplo de cada una y ubicar el pipeline (es **SISD**).
4. Calcular **cuántas instrucciones** ahorra un registro vectorial (`n / ancho`).
5. Explicar **memoria entrelazada**, calcular el ancho de banda y detectar un **conflicto de banco**.
6. Aplicar la **ley de Amdahl** con `S = 1/((1−f) + f/n)` y decir el techo.
7. Explicar **coherencia de caché** (MESI, falso compartido) y distinguir **latencia de productividad**.

## TPs de la unidad
No tiene TP propio: se apoya en [[TP5 Sumadores]] (ALU segmentada) y en [[Pipeline]].

## Fuente de la cátedra
Apuntes de la **Unidad 8** (paralelismo) · Stallings (paralelismo y multiprocesadores) ·
Patterson & Hennessy (ILP y procesadores vectoriales) · Hamacher (memoria entrelazada).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 7 — temas y subtemas]] ·
[[00 Unidad 9 — temas y subtemas]] · [[00 Síntesis — Unidad 8]]
