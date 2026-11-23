---
tipo: indice
---
# Plan de mejoras pendientes

> [!abstract] Qué es esta nota
> El **backlog** de la bóveda: lo que quedó abierto después de la validación de contenido, con **prioridad**,
> **esfuerzo** y **cómo se haría** cada cosa. Es la continuación de
> [[06 Validación de contenido (resúmenes, TPs y claridad)]], que dice qué **ya** está cerrado.

> [!success] Punto de partida (nada de esto bloquea el estudio)
> **107 subtemas** completos · **107/107** con ejemplo resuelto y error típico · **0 enlaces rotos** ·
> **0 imágenes rotas** · **100 diagramas propios + 100 figuras de libro**. Todo lo de abajo es **mejora**, no
> reparación: la bóveda hoy se puede estudiar de punta a punta.

## La lista, de una

| # | Mejora | Tipo | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| **M1** | **Glosario**: agregar los ~15 términos nuevos de la Fase 12 | arreglo | medio | **1 h** | **P1** |
| **M2** | **Figuras de libro en los 34 subtemas que no tienen** (usar las **108 ya extraídas** que quedaron sin usar) | mejora | alto | **1 sesión** | **P1** |
| **M3** | **Banco de autoevaluación**: 107 preguntas (hoy hay ~16) | mejora | **muy alto** | 3-4 sesiones | **P1** |
| **M4** | **Figuras de los TPs**: extraer los circuitos resueltos de los 21 PDF (es la única fuente para U1 combinacional) | mejora | alto | 1-2 sesiones | P2 |
| **M5** | **Recortar las 493 oraciones de más de 35 palabras** (U2 81, U1 60, U5 60, U9 53) | mejora | medio | 2-3 sesiones | P2 |
| **M6** | **30 ejercicios resueltos estilo examen** en `04 Práctica` (3 por unidad) | mejora | alto | 2 sesiones | P2 |
| **M7** | **Ficha de repaso de una página por unidad** (10 tarjetas) | mejora | medio | 1-2 sesiones | P2 |
| **M8** | **Test numérico automático** de los ejemplos (que las cuentas sigan cerrando) | arreglo | medio | 1 sesión | P2 |
| **M9** | **Ver los 25 videos** y anotar minuto a minuto qué aporta cada uno | mejora | bajo | 2 sesiones | P3 |
| **M10** | **Transcribir los 2 resúmenes manuscritos** (31 páginas) para poder auditarlos con texto | arreglo | bajo | 1-2 sesiones | P3 |
| **M11** | **Ampliar el modelo de final** con las preguntas de las unidades 8, 9 y 10 | mejora | medio | 2 sesiones | P3 |

## Detalle: cómo quedaría cada uno

### M1 · Glosario completo — P1, 1 hora
**Estado:** el glosario tiene **49 entradas / 768 palabras** y **no** incluye nada de lo agregado en la Fase 12.
**Falta:** `AIKEN`, `exceso 3`, `exceso 64`, `Gray`, `Johnson`, `BCD empaquetado`, `paridad`, `LRC`, `CRC`,
`Hamming`, `síndrome`, `DIMM`, `SODIMM`, `DDR`, `FSB`, `NOP`, `secuenciamiento`, `microPC`.
**Cómo:** una fila por término (`| término | definición de una línea | nota donde se desarrolla |`), ordenadas
alfabéticamente dentro de las letras que ya existen.
**Terminado cuando:** cualquier término que aparece en un `[!abstract]` está en el glosario.

### M2 · Figuras de libro en los 34 subtemas que no tienen — P1, 1 sesión
**Estado:** **73 de 107** subtemas tienen figura de libro; **34** no. De las **208 figuras extraídas**, **108
quedaron sin usar** en `_figs/`.
**Falta:** asignarlas. Propuesta concreta (las que ya tienen candidato claro):

| Subtema sin figura | Figura disponible |
|---|---|
| 1.2.2 DeMorgan | Quiroga **6.27** (diagrama con compuertas NOR) |
| 1.2.3 Simplificación | Quiroga **6.17** (diagrama de lógica) |
| 1.3.1 Mintérminos | Quiroga **6.11** (diagrama de lógica de F3) |
| 2.1.1 Biestable RS | Quiroga **6.31** (diagramas de bloque) |
| 2.1.4 Conversión de biestables | Quiroga **6.2** (semisumador, otra opción) |
| 2.7.2 CodOp vs dirección | Stallings **11.6** (formatos del PDP-11) |
| 4.2.1 Especificación de la BLUE | Stallings **3.5** (ejecución de un programa) |
| 4.2.2 Los 16 opcodes | Stallings **11.7** (ejemplos de instrucciones del VAX) |
| 4.2.3 Programar en BLUE | Stallings **10.15** (tres programas equivalentes) |
| 5.1.2 Clasificación de instrucciones | Stallings **10.6** (instrucciones de bifurcación) |
| 5.2.1 Los 4 formatos | Stallings **13.8** (formatos del MIPS) |
| 5.2.2 Cálculo del CodOp | Stallings **13.13** (formatos del SPARC) |
| 7.4.1 von Neumann vs Harvard | Stallings **1.4** (estructura del nivel superior) |
| 8.2.1 SIMD y registros vectoriales | Stallings **15.7** (registros de aplicación IA-64) |
| 8.2.2 Flynn | Stallings **18.4** (multiprocesador genérico) |
| 8.3.1 Bancos de memoria | Stallings **5.12** (SDRAM) |
| 8.3.2 Entrelazado | Stallings **5.14** (estructura RDRAM) |
| 9.2.3 Arreglo multiplicador | Stallings **9.9** (flujo de la multiplicación) |
| 9.5.1 Suma decimal corregida | Quiroga **6.8** (convertidor de código) |
| 2.4.2 PROM/EPROM/Flash | Quiroga **9.11** (inserción de chip y módulo) |

**Los 14 que quedan sin candidato** (1.3.2 Karnaugh, 1.3.3 don't care, 1.4.1 a 1.4.4, 1.6.1, 1.6.2, 2.2.2,
5.4.1, 8.2.3, 9.1.2, 9.3.2) **no tienen figura en los libros**: son temas que en la bibliografía están resueltos
con ejemplos resueltos, no con láminas. Para ésos va **M4**.

### M3 · Banco de autoevaluación: 107 preguntas — P1, 3-4 sesiones
**Estado:** `04 Práctica/Autoevaluación.md` tiene **16 preguntas** para 107 subtemas.
**Falta:** una pregunta por subtema, con la respuesta en un `<details>` plegable, agrupadas por unidad y
enlazadas a la nota.
**Cómo:** 3 tandas de ~35 preguntas, cada una con respuesta de 2 líneas + "si no te salió, volvé a *este* subtema".
**Terminado cuando:** cada subtema tiene al menos una pregunta y el banco se puede rendir de corrido en ~40 min.

### M4 · Figuras de los TPs — P2, 1-2 sesiones
**Estado:** los 19 TPs resueltos (PDF) tienen los **circuitos hechos a mano** de decodificadores, MUX, DEMUX,
Karnaugh y biestables: la única fuente real para esos subtemas.
**Cómo:** correr `tools/extraer_figuras.py` adaptado (los TPs no tienen epígrafe `Fig. N.N`: hay que recortar por
**página completa del ejercicio** o por bloques de tinta) y guardar como `tp-fNN-pXX.png`.
**Riesgo:** son manuscritos ⇒ algunos recortes salen torcidos; hay que revisar con hoja de contactos como se hizo
con los libros.

### M5 · Recortar 493 oraciones largas — P2, 2-3 sesiones
**Estado:** **493 de 2 505** oraciones pasan de 35 palabras (**20 %**), repartidas así: U2 **81**, U1 **60**,
U5 **60**, U9 **53**, U4 **49**, U7 **49**, U8 **42**, U3 **37**, U10 **35**, U6 **27**.
**Cómo:** partir en dos por coma o punto y coma; mantener el número y el verbo al principio. Se puede hacer con un
script que liste las oraciones (ya está el criterio) y corregirlas a mano de a 40 por sesión.
**Cuidado:** no tocar los `[!abstract]` (están pensados cortos) ni los bloques de código.

### M6 · 30 ejercicios resueltos estilo examen — P2, 2 sesiones
**Estado:** `04 Práctica/Prácticas resueltas.md` tiene **1 914 palabras** (muy poco para 10 unidades).
**Falta:** 3 ejercicios por unidad con enunciado, resolución paso a paso y "qué se evalúa con esto".
**Prioridad dentro del ítem:** U9 (aritmética con trazas), U5 (24 pulsos), U4 (pulsos de la BLUE), U2 (dimensionar
memorias), U10 (cálculo de tiempos de E/S).

### M7 · Ficha de una página por unidad — P2, 1-2 sesiones
**Estado:** las `00 Síntesis` tienen 1 500-2 500 palabras: buenas para estudiar, largas para repasar el día antes.
**Falta:** una **tarjeta** por unidad con: 5 definiciones, 3 fórmulas, 2 dibujos, 1 cuenta modelo.
**Cómo:** dentro de cada `00 Síntesis`, un bloque `> [!summary] En una página` arriba; nada nuevo que aprender.

### M8 · Test numérico automático de los ejemplos — P2, 1 sesión
**Estado:** las cuentas de los ejemplos están verificadas a mano (AMAT, speedup, ciclos, 143, −15, 62, 6 µs…),
pero nada impide que un cambio futuro las rompa.
**Cómo:** `tools/verificar_cuentas.py` con ~30 asserts (`1 + 0,05×100 == 6`, `S(100) ≈ 4,81`,
`13×11 == 143`, `11110001 == −15`, `0101 1100 + 0110 == 0110 0010`, …). Se corre antes de cada commit.
**Terminado cuando:** `python3 tools/verificar_cuentas.py` imprime `30 ok`.

### M9 · Ver los 25 videos y anotarlos — P3, 2 sesiones
**Estado:** están los **37 recursos** con título y canal, pero **sin veredicto**: no se sabe cuáles sirven.
**Cómo:** tabla por TP con columnas `video | minuto | qué aporta | qué ignora | ¿reemplaza la nota? (no)`.

### M10 · Transcribir los 2 resúmenes manuscritos — P3, 1-2 sesiones
**Estado:** `Resumen2` (20 p.) y `Resumen3` (11 p.) **no tienen capa de texto**; se revisaron como imagen.
**Cómo:** transcribir a mano (o con OCR externo) y correr la misma auditoría de términos de la Fase 12.
**Impacto real:** bajo — su temario ya está cubierto y de ahí salió el único hueco grande (códigos).

### M11 · Ampliar el modelo de final — P3, 2 sesiones
**Estado:** el modelo de final tiene **3 tandas**; las unidades **8, 9 y 10** están flojas de preguntas.
**Falta:** 2 preguntas por unidad nueva, con la carpeta `Apoyo a la pregunta/` como las demás.

## Si tuvieras que elegir: el orden que yo seguiría

| Momento | Qué hacer | Para qué |
|---|---|---|
| **Una tarde** | **M1 + M2** (glosario + figuras que ya están extraídas) | deja el material **parejo**: ningún subtema sin figura |
| **Un fin de semana** | **M3** (banco de 107 preguntas) | es lo que más cambia la forma de estudiar: pasás de leer a **rendir** |
| **La semana antes del parcial** | **M7 + M8** (fichas de una página y test de cuentas) | repaso rápido y confianza en los números |
| **Después del parcial** | **M4 + M5 + M6** | completar figuras de TPs, aligerar el texto y sumar ejercicios |
| **Cuando haya tiempo** | **M9 + M10 + M11** | cierres de calidad, no de contenido |

## Lo que NO está pendiente
- Contenido de las **10 unidades**: cerrado (46 temas, 107 subtemas, 10 síntesis).
- Diagrama propio en cada subtema: **107/107**.
- Ejemplo resuelto y error típico en cada subtema: **107/107**.
- Enlaces e imágenes: **0 rotos**.
- Videos de los TPs: listados y verificados (2 muertos quitados).
- Auditoría contra los resúmenes: hecha, con los 6 huecos cerrados.

## Relacionado
[[06 Validación de contenido (resúmenes, TPs y claridad)]] · [[00 Índice de la materia (las 10 unidades)]] ·
[[00 Mapa de diagramas (qué gráfico tiene cada subtema)]] · [[02 Plan de estudio — las 10 unidades]]
