# Bóveda de estudio — Arquitectura de Computadoras (UCASAL)

Bóveda de Obsidian para preparar el final de **Arquitectura / Organización de Computadoras**
(plan de 10 unidades, cátedra UCASAL). Está armada a partir del **plan de estudios** y del
**modelo de final** entregados por la cátedra: cada pregunta del modelo tiene su nota de
desarrollo, con los conceptos previos, los gráficos y el guion de respuesta.

## Cómo abrirla

1. Descargá o cloná este repositorio.
2. En Obsidian: **Abrir carpeta como bóveda** → elegí esta carpeta.
3. Empezá por `00_Inicio/00 Cómo usar esta bóveda.md`.

No necesita plugins. Los diagramas son SVG dentro de `assets/` (se ven en Obsidian y en
GitHub); algunos esquemas usan **Mermaid**, que Obsidian renderiza de forma nativa.

## Estructura

```
00_Inicio/                  portada, mapa de la materia, ruta de estudio, glosario
01_Logica_Digital/          Unidad 1 — compuertas, Boole, DeMorgan, sumadores, MUX/DEMUX
02_Memorias_Secuenciales/   Unidad 2 y 3 — flip-flops, registros, contadores, RAM/ROM, caché
03_CPU_Blue/                Unidades 4 a 6 — estructura, UC, BLUE, ciclos, formato, modos, interrupciones
04_Arquitecturas_Avanzadas/ Unidades 7 a 9 — pipeline, CISC/RISC, microprogramación, paralelismo
05_Examen/                  banco de preguntas del final + guion de respuestas
06_Practica/                prácticas resueltas y autoevaluación
assets/                     diagramas SVG (generados con tools/diagramas.py)
```

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
