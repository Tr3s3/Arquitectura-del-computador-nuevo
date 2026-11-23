# Bóveda de estudio — Arquitectura de Computadoras (UCASAL)

Bóveda de Obsidian para preparar el final de **Arquitectura / Organización de Computadoras**
(plan de 10 unidades, cátedra UCASAL). Está armada a partir del **plan de estudios**, del
**modelo de final** y de los **20 trabajos prácticos** entregados por la cátedra: cada pregunta del
modelo tiene su nota de desarrollo, con los conceptos previos, los gráficos y el guion de respuesta.

**El final es oral** y, en la práctica, se rinde **dibujando circuitos y explicando sus tablas de
verdad**. Por eso todas las notas de examen son *habladas* (definición → dibujo → desarrollo →
cierre) y los diagramas están pensados para reproducirse a mano en el pizarrón.

**Estado:** 311 notas · **100 SVG propios + 132 figuras de libro + 15 figuras de clase** · ~295.000 palabras · 0 enlaces e imágenes rotas.
**Cobertura gráfica:** los **107 subtemas** de `02 Materia/` tienen su diagrama propio ([[00 Mapa de diagramas (qué gráfico tiene cada subtema)]]) y **99 de los 107** suman además figura externa: **132 figuras extraídas de la bibliografía** ([[00 Figuras de los libros (índice)]]) y **15 del resumen de cátedra**.
**Materia en detalle:** las **10 unidades completas** (46 temas, **107 subtemas**), con una `00 Síntesis` por unidad.
**Para leer de corrido:** cada unidad tiene un `00 Unidad N completa (lectura de corrido)` —todos sus subtemas pegados
en un archivo, con diagramas y figuras— y está **[[00 Materia completa (las 10 unidades en un archivo)]]** con las 10
unidades en un solo archivo (85.000 palabras).

**Organización:** `01 Modelo de final resuelto/` → `Tanda 1|2|3` → `N. Pregunta/` → **los archivos de esa
pregunta** (desarrollo + subtemas juntos) · `02 Materia/` → `Unidad N — nombre/` → `Tema N.M/` → **subtemas**.
Cada unidad tiene su nota índice `00 Unidad N — temas y subtemas`.

## Cómo abrirla

1. Descargá o cloná este repositorio.
2. En Obsidian: **Abrir carpeta como bóveda** → elegí esta carpeta.
3. Empezá por `00 Empezar acá/00 Cómo usar esta bóveda.md`.

No necesita plugins. Los diagramas son SVG dentro de `assets/` (se ven en Obsidian y en
GitHub); algunos esquemas usan **Mermaid**, que Obsidian renderiza de forma nativa.

## Estructura

Dos carpetas grandes, con jerarquía **explícita en carpetas** (no hay que abrir un índice para saber qué hay
adentro: el nombre de la carpeta lo dice).

```
01 Modelo de final resuelto/      las 27 preguntas del final, cada una resuelta
├── 00 Índice — el final resuelto.md
├── 00 Guías/                    matriz, chequeo de los 12 temas, qué leer, banco, guion
├── Tanda 1 — La máquina/        00 Tanda 1 — índice
│   ├── 1.1 Flujo de información (direcciones y datos)/
│   │   ├── Flujo de información en BLUE (datos y direcciones).md   ← nota principal
│   │   └── Apoyo a la pregunta/   00 Apoyos — 1.1 … (+ los archivos de apoyo de esa pregunta)
│   ├── 1.2 BLUE vs BLUE indexada/                        → nota + «BLUE indexada (RIF, RID)»
│   ├── 1.3 Ciclo de LDA indexada (24 pulsos)/
│   ├── 1.4 Memoria RAM 8x3/
│   ├── 1.5 Estructura básica del computador/
│   ├── 1.6 Implementación de la Unidad de Control/
│   ├── 1.7 Formato de la instrucción (4 formatos)/
│   └── 1.8 Ciclo de máquina y ciclo de instrucción/       → ciclo de máquina + búsqueda + ejecución
├── Tanda 2 — Memorias y arquitectura/   2.1 … 2.10 (una carpeta por pregunta)
└── Tanda 3 — Circuitos con tablas de verdad/   3.0 … 3.9 (incluye el RI)
02 Materia/                       la materia completa, las 10 unidades (Unidad → Tema → Subtema)
├── 00 Índice de la materia (las 10 unidades).md
├── Unidad 1 — Circuitos de lógica digital/        ✅ desarrollada (5 temas / 15 subtemas)
│   ├── 00 Unidad 1 — temas y subtemas
│   ├── 00 Síntesis — Unidad 1            ← toda la unidad en un solo archivo
│   ├── Tema 1.1 Compuertas lógicas/  1.1.1 … 1.1.3   (una nota por subtema)
│   └── Tema 1.2 … Tema 1.5
├── Unidad 2 — Memorias y circuitos secuenciales/  ✅ desarrollada (7 temas / 19 subtemas)
│   ├── 00 Síntesis — Unidad 2
│   └── Tema 2.1 … Tema 2.7
├── Unidad 3 — Transferencia de registros y microoperaciones/  ✅ desarrollada (3 temas / 7 subtemas)
│   ├── 00 Síntesis — Unidad 3
│   └── Tema 3.1 Microoperaciones y bus/ · Tema 3.2 La ALU/ · Tema 3.3 Registros de la CPU/
├── Unidad 4 — Organización y diseño básico/   ✅ desarrollada (4 temas / 10 subtemas)
│   ├── 00 Síntesis — Unidad 4
│   └── Tema 4.1 … Tema 4.4 (BLUE, ciclo de instrucción, UC)
├── Unidad 5 — Programación básica y CPU convencional/  ✅ desarrollada (6 temas / 13 subtemas)
│   ├── 00 Síntesis — Unidad 5
│   └── Tema 5.1 Lenguaje máquina/ · Tema 5.2 Formato de la instrucción/ · … · Tema 5.6 El 8086/
├── Unidad 6 — Control microprogramado/   ✅ desarrollada (3 temas / 5 subtemas)
│   ├── 00 Síntesis — Unidad 6
│   └── Tema 6.1 Control cableado/ · Tema 6.2 Control microprogramado/ · Tema 6.3 Comparación y caso real/
├── Unidad 7 — CPU y arquitecturas/        ✅ desarrollada (4 temas / 9 subtemas)
│   ├── 00 Síntesis — Unidad 7
│   └── Tema 7.1 Pipeline/ · … · Tema 7.4 Arquitecturas y buses/
├── Unidad 8 — Paralelismo/               ✅ desarrollada (4 temas / 9 subtemas)
│   ├── 00 Síntesis — Unidad 8
│   └── Tema 8.1 Pipeline aritmético/ · … · Tema 8.4 Multiprocesadores/
├── Unidad 9 — Hardware aritmético/       ✅ desarrollada (5 temas / 10 subtemas)
│   ├── 00 Síntesis — Unidad 9
│   └── Tema 9.1 Suma y resta/ · … · Tema 9.5 Aritmética BCD/
└── Unidad 10 — Entrada y Salida/          ✅ desarrollada (4 temas / 7 subtemas)
    ├── 00 Síntesis — Unidad 10
    └── Tema 10.1 Entrada y salida programada/ · Tema 10.2 Interrupciones/ · Tema 10.3 DMA/ ·
        Tema 10.4 Dispositivos y almacenamiento/
00 Empezar acá/                  cómo usar, mapa (MOC), plan de las 10 unidades, ruta para el final,
                                 resumen integrador, fuentes y glosario
03 Material de cátedra (TPs)/    los 21 TPs: consigna, qué hay que saber y respuesta sintetizada
04 Práctica/                     prácticas resueltas, checklist de dibujo, tablas de verdad, autoevaluación
assets/                          100 SVG propios + 132 PNG de los libros + 15 PNG de clase
tools/                           diagramas.py, diagramas_2.py (SVG) y extraer_figuras.py (figuras de PDF)
```

> **La regla:** en `01 Modelo de final resuelto/` cada carpeta es **una pregunta**: adentro está la
> **nota principal** y la carpeta **`Apoyo a la pregunta/`** con su nota `00 Apoyos — N.M …` (qué archivos hacen
> falta, **para qué sirve cada uno** y el enlace a los apoyos que viven en otras tandas) más los archivos de
> apoyo propios de esa pregunta. La nota principal **abre diciendo qué apoyos necesita**. En `02 Materia/` la
> cadena es `Unidad → Tema → Subtemas`. Cada nota vive en un solo lugar: lo que sirve a dos preguntas se
> enlaza, no se duplica.

## Escrita para aprender desde cero

Las notas troncales arrancan con un bloque **"Si es la primera vez que ves esto"**: la analogía y el problema
que resuelve el concepto, antes de cualquier definición. Después vienen el desarrollo con tablas y diagramas,
el **guion oral** y los **errores típicos**. La idea es que puedas estudiar sin otro material al lado.

## Por dónde empezar

| Objetivo | Nota |
|---|---|
| **Preparar el final** (empezar acá) | `01 Modelo de final resuelto/00 Índice — el final resuelto.md` |
| **Estudiar la materia completa** (las 10 unidades) | `02 Materia/00 Índice de la materia (las 10 unidades).md` |
| Ver **qué cae y con qué peso** (foto del profesor) | `01 Modelo de final resuelto/00 Guías/00 Matriz del final — las 3 tandas.md` |
| Ver la materia completa en 20 minutos | `00 Empezar acá/04 Resumen integrador de la materia.md` |
| Saber qué pide la cátedra, TP por TP | `03 Material de cátedra (TPs)/00 Índice de TPs y qué aporta cada uno.md` |
| Entrenar el oral | `01 Modelo de final resuelto/00 Guías/Guion de respuestas — preguntas principales.md` |
| Practicar el pizarrón | `04 Práctica/Cómo dibujar los circuitos (checklist de pizarrón).md` |
| Repasar tablas de verdad | `04 Práctica/Tablas de verdad de memoria.md` |
| Saber de dónde sale cada dato | `00 Empezar acá/05 Fuentes y qué aporta cada una.md` |
| Saber **qué leer para ampliar** cada tema | `01 Modelo de final resuelto/00 Guías/01 Qué leer para cada pregunta principal.md` |
| **Chequear la cobertura de la lista de 12 temas** | `01 Modelo de final resuelto/00 Guías/02 Chequeo de los 12 temas.md` |

## Fuentes

La bóveda está construida sobre el material de la cátedra: el apunte base (**Foster, *Computer
Architecture***, capítulo de la máquina elemental "BLUE"), los **apuntes de las Unidades 1 a 5**, la **matriz
del final**, los **21 TPs**, los resúmenes de clase y el material de memorias semiconductoras. El detalle de
qué aporta cada fuente (y cómo se resolvieron los conflictos entre ellas) está en
`00 Empezar acá/05 Fuentes y qué aporta cada una.md`.

## Avisos sobre el material de cátedra

Algunos TPs tienen **desarrollos sólo en imágenes**, errores de tipeo o números que no cierran. La
bóveda respeta la consigna original, marca la diferencia con un `> [!warning]` y explica el criterio
correcto (por ejemplo: `1101 + 0111 = 1 0100`, no `1 1100`; 1 GB con celdas de 4 B = 2²⁸ celdas ⇒ 28
bits de dirección). También queda documentada la **discrepancia de códigos de operación** entre el
simulador de los TPs y el mapa de 16 opcodes de la máquina BLUE: se muestran ambos y se explica cuál
usar según la fuente.

## Aviso importante sobre los números de pulsos

Los **ciclos de la máquina BLUE** (búsqueda de 7/8 pulsos, LDA de 24 pulsos, etc.) están
desarrollados con un esquema **coherente y razonado**: se explica *qué* microoperación debe
ocurrir en cada pulso y *por qué*. La cuenta exacta de pulsos puede variar un poco según la
versión del apunte de la cátedra; lo que se evalúa es que puedas **justificar la cuenta**.
Las notas marcan con `> [!warning]` los puntos a contrastar con el apunte.

## Regenerar los diagramas

```bash
python3 tools/diagramas.py     # reescribe assets/*.svg
```
