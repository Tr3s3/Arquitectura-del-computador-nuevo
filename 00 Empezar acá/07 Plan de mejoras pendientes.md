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
> **0 imágenes rotas** · **100 diagramas propios + 132 figuras de libro + 15 figuras de clase**. Todo lo de abajo es **mejora**, no
> reparación: la bóveda hoy se puede estudiar de punta a punta.

## La lista, de una

| # | Mejora | Tipo | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| ~~**M1**~~ | ~~**Glosario**: fichas desarrolladas por unidad~~ ✅ **hecho** (180 fichas) | — | — | — | **cerrado** |
| ~~**M2**~~ | ~~**Figuras de libro en los 34 subtemas que no tenían**~~ ✅ **hecho** (98 de 107 subtemas con figura) | mejora | alto | **1 sesión** | **cerrado** |
| **M3** | **Banco de autoevaluación**: 107 preguntas (hoy hay ~16) | mejora | **muy alto** | 3-4 sesiones | **P1** |
| ~~**M4**~~ | ~~**Figuras de los TPs y de los resúmenes**~~ ✅ **hecho con el resumen de Said**: 68 imágenes revisadas, **15 incorporadas** en 10 subtemas, **0 diagramas propios borrados** (detalle abajo). Los circuitos manuscritos de los 21 TPs siguen abiertos como **M4b** | mejora | alto | 1 sesión | **cerrado (Said)** |
| **M5** | **Recortar las 493 oraciones de más de 35 palabras** (U2 81, U1 60, U5 60, U9 53) | mejora | medio | 2-3 sesiones | P2 |
| **M6** | **30 ejercicios resueltos estilo examen** en `04 Práctica` (3 por unidad) | mejora | alto | 2 sesiones | P2 |
| **M7** | **Ficha de repaso de una página por unidad** (10 tarjetas) | mejora | medio | 1-2 sesiones | P2 |
| **M8** | **Test numérico automático** de los ejemplos (que las cuentas sigan cerrando) | arreglo | medio | 1 sesión | P2 |
| **M9** | **Ver los 25 videos** y anotar minuto a minuto qué aporta cada uno | mejora | bajo | 2 sesiones | P3 |
| **M10** | **Transcribir los 2 resúmenes manuscritos** (31 páginas) para poder auditarlos con texto | arreglo | bajo | 1-2 sesiones | P3 |
| **M11** | **Ampliar el modelo de final** con las preguntas de las unidades 8, 9 y 10 | mejora | medio | 2 sesiones | P3 |

## Detalle: cómo quedaría cada uno

### M1 · Glosario completo — ✅ HECHO
**Cómo quedó:** el glosario dejó de ser una tabla de 49 líneas y pasó a ser **180 fichas** repartidas en **diez
notas** (una por unidad, ver [[Glosario]]). Cada ficha tiene cuatro campos:
**Qué es** · **Para qué sirve** · **Características** · **Se estudia en** (enlace al subtema con el ejemplo y el
diagrama). El índice central es **alfabético**, con una línea por término, enlace directo a la ficha, y una tabla
final de **23 pares que se confunden** (`C` vs `V`, paridad vs Hamming, caché vs memoria virtual…).

| Unidad | Fichas | Unidad | Fichas |
|---|---|---|---|
| 1 — lógica digital | 31 | 6 — control microprogramado | 10 |
| 2 — memorias y secuenciales | 34 | 7 — CPU y arquitecturas | 15 |
| 3 — transferencia y microoperaciones | 12 | 8 — paralelismo | 16 |
| 4 — organización y diseño básico | 13 | 9 — hardware aritmético | 15 |
| 5 — programación y CPU convencional | 20 | 10 — entrada y salida | 14 |

**Si se quiere seguir:** los términos de la sección "Términos que se confunden" podrían tener ficha propia, y
faltaría un diagrama por ficha (hoy cada una remite al diagrama del subtema).

### M2 · Figuras de libro — ✅ HECHO (quedan 9 sin figura en los libros)
**Cómo quedó:** **98 de 107** subtemas tienen figura de libro (antes 73), con **132 figuras** pegadas (antes 100).
Se agregaron **25 subtemas** y **32 figuras**: decodificadores, codificadores, MUX/DEMUX, DeMorgan, códigos
(exceso 3 y Aiken), Karnaugh, biestable RS, conversión de biestables, formato de instrucción, Von Neumann y los
formatos de PDP-11, MIPS y las tres formas de programar.

| Lo que se agregó | Figuras |
|---|---|
| **Unidad 1** (8 subtemas) | Q 5.8, 5.9, 5.12, 6.7, 6.8, 6.10, 6.11, 6.13, 6.15, 6.18, 6.19, 6.20, 3.5, 3.6 + 2 mapas de Karnaugh recortados a mano |
| **Unidad 2** (3) | Q 6.27 (RS con NOR), Q 6.31 (conversión T→J-K), Q 7.9 (código de instrucción) |
| **Unidad 4** (3) | S 3.5 (ejecución paso a paso), Q 7.6 (formato 4+12), Q 8.2 (ciclo de las n instrucciones) |
| **Unidad 5** (3) | S 10.6 (bifurcación), S 10.15 (tres programas), S 13.8 (MIPS), S 11.6 (PDP-11) |
| **Unidades 7, 8 y 9** (5) | Q 1.3 (von Neumann), S 18.4 (multiprocesador), S 5.12 (SDRAM), S 5.14 (RDRAM), Q 4.1 y Q 5.16 (acarreo serie) |

**El descubrimiento de la sesión:** el extractor fallaba cuando **figura y epígrafe estaban pegados** en el mismo
bloque de tinta (por eso había 49 figuras de Quiroga). Corregido, Quiroga pasó de **49 a 122 figuras detectadas**:
ahí estaban todos los decodificadores, codificadores, MUX/DEMUX y códigos que faltaban.

**Los 9 que quedan sin figura de libro** (los libros no los traen, o el tema es propio de la cátedra):

| Subtema | Por qué no hay | De dónde podría salir |
|---|---|---|
| 1.6.2 Códigos continuos y cíclicos | Quiroga no trae Gray ni Johnson en figura | no hay fuente: queda el diagrama propio |
| 2.2.2 Registros SIPO y PISO | Quiroga sólo trae PIPO (Fig. 6.35) | **TP11 Registros SIPO-PISO** (es M4) |
| 2.4.2 PROM, EPROM, EEPROM y Flash | el libro trae ROM y PAL/PLA, no los tipos de ROM programable | **TP12 Memoria principal** (M4) |
| 5.4.1 RIF, RID y RB | la BLUE indexada es propia de la cátedra | ✅ **figura de clase del resumen de Said** (M4) |
| 8.2.1 SIMD, GPU | Stallings no cubre GPU | no hay fuente: queda el diagrama propio |
| 8.2.3 Multiplicación de matrices | no hay figura en ninguno de los dos libros | no hay fuente: queda el diagrama propio |
| 9.2.3 Arreglo multiplicador | Stallings trae el algoritmo (9.9-9.13), no el arreglo | no hay fuente: queda el diagrama propio |
| 9.3.2 Sobreflujo y división con signo | la figura de división (9.15/9.16) ya está en 9.3.1 | no hay fuente: queda el diagrama propio |
| 9.5.1 Suma decimal corregida | el libro no trae la suma BCD con corrección +6 | no hay fuente: queda el diagrama propio |

**Terminado cuando:** los que dependen de los TPs se resuelvan en **M4b**; 5.4.1 ya se cerró con la figura de
clase del resumen de Said y los 4 restantes no tienen fuente ni en la bibliografía ni en el resumen: quedan con el
diagrama propio.

### M3 · Banco de autoevaluación: 107 preguntas — P1, 3-4 sesiones
**Estado:** `04 Práctica/Autoevaluación.md` tiene **16 preguntas** para 107 subtemas.
**Falta:** una pregunta por subtema, con la respuesta en un `<details>` plegable, agrupadas por unidad y
enlazadas a la nota.
**Cómo:** 3 tandas de ~35 preguntas, cada una con respuesta de 2 líneas + "si no te salió, volvé a *este* subtema".
**Terminado cuando:** cada subtema tiene al menos una pregunta y el banco se puede rendir de corrido en ~40 min.

### M4 · Figuras de clase (resumen de Said) — ✅ HECHO
**Cómo se hizo:** `fitz` sobre el PDF del resumen (44 páginas) ⇒ **68 imágenes** extraídas a una carpeta de trabajo
con su página, su caja y su tamaño (`w·h ≥ 4000`, que descarta viñetas y logos), hoja de contactos de 12 por hoja y
**revisión una por una** contra el subtema que le correspondía.

**Resultado: 15 figuras incorporadas en 10 subtemas** (`assets/catedra-said-*.png`, con la página del PDF en el pie
y un `[!tip] Qué mirar`, igual que las del libro):

| Subtema | Figuras | Por qué entra |
|---|---|---|
| 1.4.3 Multiplexor | `mux-integrado` | el MUX como **integrado** (canales, selectores, una salida): el libro sólo trae el bloque |
| 2.1.1 Biestable RS | `clasificacion-biestables` | el **árbol asíncrono / sincrónico**, que no estaba dibujado en ningún lado |
| 4.1.2 IAS | `formato-palabra-ias` | los **dos formatos de la palabra de 40 bits** (dato contra instrucción) |
| 4.2.1 BLUE | `panel-frontal-blue` | la **consola** completa: 6 pulsadores, 16 leds, 16 llaves |
| 4.2.2 Opcodes | `formato-ri` · `16-instrucciones-nombres` | el corte 15..12 / 11..0 y los **nombres en castellano** del final |
| 4.3.3 Ejecución | `es-blue` | la **E/S con los 64 dispositivos**, `TRA` y `R`: la figura que confirma el dato de 6 bits |
| 5.2.1 Formatos | `formatos-comparacion` | **qué elimina** cada formato de 4 a 1 dirección |
| 5.4.1 RIF/RID/RB | `blue-indexada` | el **plano completo** de la indexada: era uno de los 9 subtemas sin figura |
| 5.4.2 24 pulsos | `formato-indexada` · `modos-modificador` · `lda3-ejecucion` · `ciclos-por-modo` · `original-vs-indexada` | la unidad entera: dos palabras, 4 modos, ciclos por modo y la comparación con la original |
| 7.1.1 Pipeline | `etapas-pipeline` | las etapas **IF-ID-EX-MEM-WB** con su función |

**Las otras 53 se descartaron**, y esto es lo importante del ítem: son **capturas de texto** (enunciados, listas,
definiciones) o **dibujos que el diagrama propio ya resolvía mejor** — compuertas, DeMorgan, semisumador, sumador
completo, los cuatro flip-flops, la pirámide de memorias, los mapeos de caché, el esquema con los tres buses, los
pulsos de la búsqueda, los cuatro formatos en bloque y CISC contra RISC. En esos casos se comparó la captura
(≈500 px, texto de 6 pt) contra el SVG propio (vectorial, con la explicación al lado en prosa) y **el SVG gana
siempre**: por eso **no se borró ningún diagrama propio**. El criterio de borrado quedó aplicado y el resultado fue
"no hay nada que borrar"; lo que sí faltaba era **agregar** las 15 que aportan algo nuevo.

**Lo que queda abierto (M4b):** los **circuitos manuscritos de los 21 TPs** (decodificadores, MUX, DEMUX, Karnaugh,
biestables resueltos a mano). No tienen epígrafe `Fig. N.N`: hay que recortar por página del ejercicio o por bloques
de tinta y revisar con hoja de contactos. Es de **prioridad baja**: los 9 subtemas que no tienen figura de libro ya
quedaron cubiertos con diagrama propio, y uno (5.4.1) se cubrió con la figura de clase de Said.

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

## Agregados de la comparación con el resumen de Said
Ver [[08 Comparación con el resumen de Said (qué agregarle)]]. De los 40 puntos que cubre ese resumen, la bóveda ya
tenía 35; se agregaron **4** (consola de la BLUE, punto fijo 15 + signo, SRAM 1024×1 — Intel 2102, tipos de acceso a
memoria), se aclaró la notación **3×8 / 8×3** y se **corrigió un error**: los dispositivos de E/S de la BLUE son
**64 (6 bits)**, no 256.

## Si tuvieras que elegir: el orden que yo seguiría

| Momento | Qué hacer | Para qué |
|---|---|---|
| ~~Una tarde~~ ✅ | ~~**M1 + M2**~~ · hechos: glosario de 180 fichas y figuras en 98 de 107 subtemas | el material quedó parejo |
| **Un fin de semana** | **M3** (banco de 107 preguntas) | es lo que más cambia la forma de estudiar: pasás de leer a **rendir** |
| **La semana antes del parcial** | **M7 + M8** (fichas de una página y test de cuentas) | repaso rápido y confianza en los números |
| **Después del parcial** | **M4 + M5 + M6** | completar figuras de TPs, aligerar el texto y sumar ejercicios |
| **Cuando haya tiempo** | **M9 + M10 + M11** | cierres de calidad, no de contenido |

## Lo que NO está pendiente
- Contenido de las **10 unidades**: cerrado (46 temas, 107 subtemas, 10 síntesis).
- Diagrama propio en cada subtema: **107/107**.
- Figura de libro: **98 de 107** subtemas (**132 figuras**); los 9 que faltan no están en los libros (5 podrían salir de los TPs en M4).
- Ejemplo resuelto y error típico en cada subtema: **107/107**.
- Enlaces e imágenes: **0 rotos**.
- Glosario: **180 fichas** en 10 notas, con índice alfabético (M1 cerrado).
- **Archivos de lectura de corrido:** `00 Unidad N completa` en cada una de las 10 unidades y
  **[[00 Materia completa (las 10 unidades en un archivo)]]** con los 107 subtemas en un solo archivo
  (85.000 palabras, diagramas y figuras incluidos).
- Videos de los TPs: listados y verificados (2 muertos quitados).
- Auditoría contra los resúmenes: hecha, con los 6 huecos cerrados.

## Relacionado
[[06 Validación de contenido (resúmenes, TPs y claridad)]] · [[00 Índice de la materia (las 10 unidades)]] ·
[[00 Mapa de diagramas (qué gráfico tiene cada subtema)]] · [[02 Plan de estudio — las 10 unidades]]
