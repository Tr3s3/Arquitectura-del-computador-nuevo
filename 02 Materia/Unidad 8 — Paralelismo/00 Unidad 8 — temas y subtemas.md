---
tipo: indice
unidad: 8
---
# Unidad 8 — Paralelismo

> [!abstract] Qué pide la unidad
> Las formas de hacer **varias cosas a la vez**: pipeline aritmético, procesamiento **vectorial**, **SIMD**,
> **multiprocesadores** y **memoria entrelazada**. Es la continuación natural del pipeline de la unidad 7.

| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **8.1 Pipeline aritmético** | etapas de la ALU segmentada · suma de vectores solapada · límites por dependencias | [[Paralelismo y procesamiento vectorial]] · `Unidad 8 — Paralelismo/` |
| **8.2 Procesamiento vectorial y SIMD** | un instruction, muchos datos · registros vectoriales · GPU como caso extremo | [[Paralelismo y procesamiento vectorial]] |
| **8.3 Memoria entrelazada** | bancos de memoria · acceso solapado · ancho de banda | [[Paralelismo y procesamiento vectorial]] · [[Jerarquía de memorias]] |
| **8.4 Multiprocesadores y multihilo** | multicore · SMT · coherencia de caché · speedup y ley de Amdahl | [[Paralelismo y procesamiento vectorial]] · [[Técnicas para aumentar la velocidad]] |
| **8.5 Pipeline de instrucciones (repaso)** | solapamiento a nivel de instrucción | [[Pipeline]] · carpeta `Tanda 2/2.7` |

---

## Qué hay que saber responder
1. **Diferencia** entre paralelismo de **instrucciones** (pipeline) y de **datos** (vectorial/SIMD).
2. **Dibujar** un pipeline aritmético sumando dos vectores.
3. Explicar **memoria entrelazada** y por qué aumenta el ancho de banda.
4. Decir **por qué no se gana linealmente** con más procesadores (dependencias, comunicación).
5. Nombrar **SIMD** con un ejemplo real (procesar 4 enteros con una instrucción).

## TPs de la unidad
No tiene TP propio: se apoya en [[TP5 Sumadores]] (ALU segmentada) y en [[Pipeline]].

## Fuente de la cátedra
Apuntes de la **Unidad 8** (paralelismo) · Stallings (capítulo de paralelismo y multiprocesadores) ·
Patterson & Hennessy (ILP y procesadores vectoriales).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 7 — temas y subtemas]] ·
[[00 Unidad 9 — temas y subtemas]]
