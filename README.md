# Bóveda de estudio — Arquitectura de Computadoras (UCASAL)

Bóveda de Obsidian para preparar el final de **Arquitectura / Organización de Computadoras**
(plan de 10 unidades, cátedra UCASAL). Está armada a partir del **plan de estudios**, del
**modelo de final** y de los **20 trabajos prácticos** entregados por la cátedra: cada pregunta del
modelo tiene su nota de desarrollo, con los conceptos previos, los gráficos y el guion de respuesta.

**El final es oral** y, en la práctica, se rinde **dibujando circuitos y explicando sus tablas de
verdad**. Por eso todas las notas de examen son *habladas* (definición → dibujo → desarrollo →
cierre) y los diagramas están pensados para reproducirse a mano en el pizarrón.

**Estado:** 92 notas · 22 diagramas SVG · ~123.000 palabras · 1.560 enlaces internos, 0 rotos.

## Cómo abrirla

1. Descargá o cloná este repositorio.
2. En Obsidian: **Abrir carpeta como bóveda** → elegí esta carpeta.
3. Empezá por `00_Inicio/00 Cómo usar esta bóveda.md`.

No necesita plugins. Los diagramas son SVG dentro de `assets/` (se ven en Obsidian y en
GitHub); algunos esquemas usan **Mermaid**, que Obsidian renderiza de forma nativa.

## Estructura

```
00_Inicio/                        portada, mapa (MOC), plan de las 10 unidades, ruta para el final,
                                  resumen integrador, fuentes y glosario
10_Examen_Final/                  BLOQUE 1 — desarrollo del MODELO DE FINAL
├── 01 Primera tanda — la máquina/            8 preguntas + apoyos (ciclos, UC, formatos)
├── 02 Segunda tanda — memorias y arquitectura/ 10 preguntas (caché, ROM, RISC/CISC, pipeline…)
├── 03 Tercera tanda — circuitos con tablas/   8 ítems (Karnaugh, MUX/DEMUX, FF, sumadores) + RI
└── 04 Guías del examen/                       matriz, chequeo de los 12 temas, fuentes, banco, guion
20_Programa_Materia/              BLOQUE 2 — desarrollo del PROGRAMA (las 10 unidades)
├── 01 Memorias, registros y contadores/
├── 02 La CPU y su control/
└── 03 Arquitecturas avanzadas/
01_Material_Catedra/              los 21 TPs: consigna, qué hay que saber y respuesta sintetizada
30_Practica/                      prácticas resueltas, checklist de dibujo, tablas de verdad, autoevaluación
assets/                           diagramas SVG (generados con tools/diagramas.py)
tools/                            generador de los diagramas
```

> Los dos bloques están **indexados** y se cruzan: `10_Examen_Final/00 Índice…` y
> `20_Programa_Materia/00 Índice…`. Cada nota vive en un bloque y se llega a ella desde los dos.

## Escrita para aprender desde cero

Las notas troncales arrancan con un bloque **"Si es la primera vez que ves esto"**: la analogía y el problema
que resuelve el concepto, antes de cualquier definición. Después vienen el desarrollo con tablas y diagramas,
el **guion oral** y los **errores típicos**. La idea es que puedas estudiar sin otro material al lado.

## Por dónde empezar

| Objetivo | Nota |
|---|---|
| **Preparar el final** (empezar acá) | `10_Examen_Final/00 Índice — bloque examen (las 3 tandas).md` |
| **Estudiar la materia completa** (las 10 unidades) | `20_Programa_Materia/00 Índice — bloque programa (las 10 unidades).md` |
| Ver **qué cae y con qué peso** (foto del profesor) | `10_Examen_Final/04 Guías del examen/00 Matriz del final — las 3 tandas.md` |
| Ver la materia completa en 20 minutos | `00_Inicio/04 Resumen integrador de la materia.md` |
| Saber qué pide la cátedra, TP por TP | `01_Material_Catedra/00 Índice de TPs y qué aporta cada uno.md` |
| Entrenar el oral | `10_Examen_Final/04 Guías del examen/Guion de respuestas — preguntas principales.md` |
| Practicar el pizarrón | `30_Practica/Cómo dibujar los circuitos (checklist de pizarrón).md` |
| Repasar tablas de verdad | `30_Practica/Tablas de verdad de memoria.md` |
| Saber de dónde sale cada dato | `00_Inicio/05 Fuentes y qué aporta cada una.md` |
| Saber **qué leer para ampliar** cada tema | `10_Examen_Final/04 Guías del examen/01 Qué leer para cada pregunta principal.md` |
| **Chequear la cobertura de la lista de 12 temas** | `10_Examen_Final/04 Guías del examen/02 Chequeo de los 12 temas.md` |

## Fuentes

La bóveda está construida sobre el material de la cátedra: el apunte base (**Foster, *Computer
Architecture***, capítulo de la máquina elemental "BLUE"), los **apuntes de las Unidades 1 a 5**, la **matriz
del final**, los **21 TPs**, los resúmenes de clase y el material de memorias semiconductoras. El detalle de
qué aporta cada fuente (y cómo se resolvieron los conflictos entre ellas) está en
`00_Inicio/05 Fuentes y qué aporta cada una.md`.

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
