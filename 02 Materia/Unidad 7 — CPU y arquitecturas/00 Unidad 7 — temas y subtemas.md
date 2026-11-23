---
tipo: indice
unidad: 7
---
# Unidad 7 — CPU y arquitecturas

> [!abstract] Qué pide la unidad
> Cómo se hace **más rápida** una computadora sin cambiar el programa: **solapando** (pipeline), **acercando los
> datos** (caché) y **simplificando el repertorio** (RISC). Y qué tipos de **bus** y de arquitectura existen.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 7 — CPU y arquitecturas/
├── 7.1 Pipeline/
│   ├── 7.1.1 Etapas y diagrama en escalera
│   └── 7.1.2 Hazards y cálculo de speedup
├── 7.2 Técnicas para aumentar la velocidad/
│   ├── 7.2.1 Superscalar, superpipeline, SMT y multicore
│   └── 7.2.2 Caché y predicción de saltos
├── 7.3 CISC y RISC/
│   ├── 7.3.1 Tabla comparativa y ejemplos
│   └── 7.3.2 UC cableada vs microprogramada y load/store
└── 7.4 Arquitecturas y buses/
    ├── 7.4.1 von Neumann vs Harvard
    └── 7.4.2 Buses internos y externos
```

**4 temas y 8 subtemas.** Cada subtema va a ser **una nota** dentro de la carpeta de su tema,
y al terminar la unidad se genera **`00 Síntesis — Unidad 7`** con todo el contenido junto (como ya está hecho en
[[00 Síntesis — Unidad 1|la Unidad 1]]).

| Tema | Subtemas | Estado |
|---|---|---|
| **7.1 Pipeline** | 7.1.1 Etapas y diagrama en escalera · 7.1.2 Hazards y cálculo de speedup | ⏳ a desarrollar |
| **7.2 Técnicas para aumentar la velocidad** | 7.2.1 Superscalar, superpipeline, SMT y multicore · 7.2.2 Caché y predicción de saltos | ⏳ a desarrollar |
| **7.3 CISC y RISC** | 7.3.1 Tabla comparativa y ejemplos · 7.3.2 UC cableada vs microprogramada y load/store | ⏳ a desarrollar |
| **7.4 Arquitecturas y buses** | 7.4.1 von Neumann vs Harvard · 7.4.2 Buses internos y externos | ⏳ a desarrollar |

> [!note] Qué hay ya de esta unidad
> El **desarrollo de examen** de casi todos estos temas ya está escrito (está enlazado más abajo, en la tabla de
> material disponible). Lo que falta es la **versión de programa**: el subtema desarrollado en la carpeta de su
> tema, con el detalle de la cursada y los TPs.

## Material ya disponible de esta unidad
| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **7.1 Pipeline** | 5 etapas · diagrama en escalera · `k+(n−1)` vs `k·n` · 3 hazards y sus soluciones | [[Pipeline]] · carpeta `Tanda 2/2.7` |
| **7.2 Técnicas para aumentar la velocidad** | pipeline · superpipeline · superscalar · caché · multicore · predicción | [[Técnicas para aumentar la velocidad]] · `Unidad 7 — CPU y arquitecturas/` |
| **7.3 CISC y RISC** | repertorio · longitud fija vs variable · load/store · UC cableada vs microprogramada · híbridos | [[CISC y RISC]] · carpeta `Tanda 2/2.6` |
| **7.4 Memoria caché (repaso)** | localidad · mapeos · políticas | [[Memoria caché]] · carpeta `Tanda 2/2.3` |
| **7.5 Buses** | interno/externo · datos, direcciones, control · bus común vs dedicado | [[Estructura básica de un computador]] · [[TP14 Buses]] · carpeta `Tanda 1/1.5` |
| **7.6 Tipos de arquitectura** | von Neumann vs Harvard · 1 dirección (BLUE) vs 3 operaciones (RISC) | [[Estructura básica de un computador]] · [[Formato de la instrucción (4 formatos)]] |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** el pipeline de 3 instrucciones y calcular el speedup con `k` y `n`.
2. Nombrar los **3 conflictos** y su solución (forwarding/stall, predicción, cachés I-D).
3. Completar la **tabla comparativa CISC/RISC** de memoria y dar el ejemplo de instrucción de cada uno.
4. Explicar por qué **RISC nació para poder hacer pipeline**.

## TPs de la unidad
[[TP20 Lenguaje máquina]] (comparación CISC/RISC) · (apoyo: [[TP14 Buses]] · [[TP12 Memoria principal]])

## Fuente de la cátedra
`Resumen final arqui.pdf` (secciones *Pipeline* y *Arquitectura CISC / RISC*) · Apuntes **Unidad 5** ·
Patterson & Hennessy · Stallings.

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 6 — temas y subtemas]] ·
[[00 Unidad 8 — temas y subtemas]] · [[00 Tanda 2 — índice]]
