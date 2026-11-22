# Bóveda de estudio — Arquitectura de Computadoras (UCASAL)

Bóveda de Obsidian para preparar el final de **Arquitectura / Organización de Computadoras**
(plan de 10 unidades, cátedra UCASAL). Está armada a partir del **plan de estudios**, del
**modelo de final** y de los **20 trabajos prácticos** entregados por la cátedra: cada pregunta del
modelo tiene su nota de desarrollo, con los conceptos previos, los gráficos y el guion de respuesta.

**El final es oral** y, en la práctica, se rinde **dibujando circuitos y explicando sus tablas de
verdad**. Por eso todas las notas de examen son *habladas* (definición → dibujo → desarrollo →
cierre) y los diagramas están pensados para reproducirse a mano en el pizarrón.

**Estado:** 77 notas · 16 diagramas SVG · ~59.000 palabras · 857 enlaces internos, 0 rotos.

## Cómo abrirla

1. Descargá o cloná este repositorio.
2. En Obsidian: **Abrir carpeta como bóveda** → elegí esta carpeta.
3. Empezá por `00_Inicio/00 Cómo usar esta bóveda.md`.

No necesita plugins. Los diagramas son SVG dentro de `assets/` (se ven en Obsidian y en
GitHub); algunos esquemas usan **Mermaid**, que Obsidian renderiza de forma nativa.

## Estructura

```
00_Inicio/                  portada, mapa (MOC), plan de estudio, ruta para el final,
                            resumen integrador de la materia y glosario
01_Logica_Digital/          Unidad 1 — compuertas, Boole, DeMorgan, sumadores, MUX/DEMUX
02_Memorias_Secuenciales/   Unidad 2 y 3 — flip-flops, registros, contadores, RAM/ROM, caché
03_CPU_Blue/                Unidades 4 a 6 — estructura, UC, BLUE, ciclos, formato, modos, interrupciones
04_Arquitecturas_Avanzadas/ Unidades 7 a 9 — pipeline, CISC/RISC, microprogramación, paralelismo
01_Material_Catedra/        los 20 TPs: consigna, qué hay que saber y respuesta sintetizada
05_Examen/                  banco de preguntas del final + guion oral de las 8 principales
06_Practica/                prácticas resueltas, cómo dibujar los circuitos, tablas de verdad, autoevaluación
assets/                     diagramas SVG (generados con tools/diagramas.py)
```

## Por dónde empezar

| Objetivo | Nota |
|---|---|
| Ver la materia completa en 20 minutos | `00_Inicio/04 Resumen integrador de la materia.md` |
| Saber qué pide la cátedra, TP por TP | `01_Material_Catedra/00 Índice de TPs y qué aporta cada uno.md` |
| Entrenar el oral | `05_Examen/Guion de respuestas — preguntas principales.md` |
| Practicar el pizarrón | `06_Practica/Cómo dibujar los circuitos (checklist de pizarrón).md` |
| Repasar tablas de verdad | `06_Practica/Tablas de verdad de memoria.md` |

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
