---
tipo: indice
unidad: 7
---
# Unidad 7 — CPU y arquitecturas

> [!abstract] Qué pide la unidad
> Cómo se hace **rápido** un procesador: **pipeline** (y sus conflictos), las técnicas que lo empujan
> (**superscalar, superpipeline, SMT, multicore, caché, predicción**), las dos filosofías de repertorio
> (**CISC y RISC**) y la estructura de memoria y buses (**von Neumann/Harvard**, buses internos y externos).

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 7 completa (lectura de corrido)]]**: los **9 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 7]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.


> [!important] El hilo de la unidad
> `pipeline` → los conflictos que lo frenan → las técnicas que los tapan → **RISC** como arquitectura pensada para
> el pipeline → la **estructura** (memorias y buses) que lo hace posible.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 7 — CPU y arquitecturas/
├── Tema 7.1 Pipeline/
│   ├── 7.1.1 Etapas y diagrama en escalera
│   ├── 7.1.2 Hazards y sus soluciones
│   └── 7.1.3 Cálculo de speedup y límites
├── Tema 7.2 Técnicas para aumentar la velocidad/
│   ├── 7.2.1 Superscalar, superpipeline, SMT y multicore
│   ├── 7.2.2 Caché y predicción de saltos
│   └── Técnicas para aumentar la velocidad          (nota de desarrollo de examen)
├── Tema 7.3 CISC y RISC/
│   ├── 7.3.1 Tabla comparativa y ejemplos
│   └── 7.3.2 UC cableada vs microprogramada y load-store
└── Tema 7.4 Arquitecturas y buses/
    ├── 7.4.1 von Neumann vs Harvard
    └── 7.4.2 Buses internos y externos
```

**4 temas y 9 subtemas.** Cada subtema es **una nota** dentro de la carpeta de su tema. La unidad está **cerrada**
y todo su contenido quedó reunido en **[[00 Síntesis — Unidad 7]]**.

| Tema | Subtemas | Estado |
|---|---|---|
| **7.1 Pipeline** | 7.1.1 Etapas y diagrama en escalera · 7.1.2 Hazards y sus soluciones · 7.1.3 Cálculo de speedup y límites | ✅ |
| **7.2 Técnicas para aumentar la velocidad** | 7.2.1 Superscalar, superpipeline, SMT y multicore · 7.2.2 Caché y predicción de saltos | ✅ |
| **7.3 CISC y RISC** | 7.3.1 Tabla comparativa y ejemplos · 7.3.2 UC cableada vs microprogramada y load-store | ✅ |
| **7.4 Arquitecturas y buses** | 7.4.1 von Neumann vs Harvard · 7.4.2 Buses internos y externos | ✅ |

> [!note] Cómo creció el árbol
> El árbol original tenía **8 subtemas**. Se desdobló 7.1.2 ("Hazards y cálculo de speedup") en **dos**: los
> conflictos (7.1.2) y el cálculo del speedup **real** con penalidades (7.1.3), que es lo que más se toma.

## Los 4 temas, de un vistazo

| Tema | Índice | La idea en una línea |
|---|---|---|
| **7.1** | [[00 Tema 7.1 — índice]] | `k + (n − 1)` ciclos; tres conflictos recortan la ganancia |
| **7.2** | [[00 Tema 7.2 — índice]] | más ancho, más etapas, más hilos, más núcleos; y tapar esperas |
| **7.3** | [[00 Tema 7.3 — índice]] | CISC = pocas y complejas · RISC = muchas y simples, 1 ciclo |
| **7.4** | [[00 Tema 7.4 — índice]] | una memoria o dos · el bus y su ancho de banda |

## Material de examen ya disponible de esta unidad
| Tema | Nota | Dónde está además |
|---|---|---|
| **Pipeline** | [[Pipeline]] | `Tanda 2/2.7` + `Apoyo a la pregunta/` |
| **Técnicas de velocidad** | [[Técnicas para aumentar la velocidad]] | `Tema 7.2 …/` |
| **CISC y RISC** | [[CISC y RISC]] | `Tanda 2/2.6` |
| **Control cableado/microprogramado** | [[Cómo se implementa la Unidad de Control]] · [[Unidad de control cableada y microprogramada]] | Tanda 1 · Unidad 6 |
| **Caché y jerarquía** | [[Jerarquía de memorias]] · [[Memoria caché]] | Unidad 2 |
| **Bus** | [[3.1.2 Bus único y buffers de 3 estados]] | Unidad 3 |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** el diagrama en escalera y calcular ciclos y speedup ideal (`k + n − 1`).
2. Nombrar los **tres conflictos** con su ejemplo y su solución (caché I/D, forwarding, predicción).
3. Calcular el **speedup real** y el **CPI** sumando stalls y saltos.
4. Explicar **superscalar, superpipeline, SMT y multicore** y por qué no dan la ganancia teórica.
5. Calcular `AMAT` y el **costo de un salto mal predicho**.
6. Armar la **tabla CISC vs RISC** y justificar por qué RISC es cableado y `load/store`.
7. Distinguir **von Neumann de Harvard** (y el híbrido de las cachés).
8. Calcular **ancho de banda** de un bus y explicar el arbitraje.

## TPs de la unidad
No tiene TP propio: se apoya en [[TP21 intro al emu8086]] (BIU/EU y cola de instrucciones) y en
[[TP16 Ciclo de instrucción básico]].

## Fuente de la cátedra
Apuntes de la **Unidad 7** (CPU y arquitecturas) · Stallings (pipeline y arquitecturas) ·
Patterson & Hennessy (ILP, CISC/RISC, memoria) · Hamacher (buses y estructura) ·
`El_manual_del_Microprocesador.pdf`.

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 6 — temas y subtemas]] ·
[[00 Unidad 8 — temas y subtemas]] · [[00 Síntesis — Unidad 7]]
