---
tipo: indice
---
# Validación de contenido: resúmenes, TPs y claridad

> [!abstract] Qué es esta nota
> El resultado de **auditar la bóveda contra los resúmenes de la cátedra y los TPs**: qué faltaba (y cómo se
> cerró), qué tan parejo es el material para estudiar, el estado de los videos de los TPs y una lista honesta de
> lo que todavía queda flojo. Fecha de la revisión: **22/11/2026**.

> [!success] Resultado en una línea
> **107 subtemas** cubiertos, **107/107 con ejemplo resuelto y con caja de error típico**, **100 diagramas propios
> + 100 figuras de libro**, **0 enlaces y 0 imágenes rotas**, y **6 temas que sólo estaban en los resúmenes** que se
> agregaron como contenido nuevo.

## 1. Método

| Paso | Qué se hizo |
|---|---|
| **1. Extraer** | Se sacó el texto de los 6 resúmenes/apuntes de la cátedra (`apuntes`, `Resumen final`, `2do intento FINAL`, `memorias`) y se inventariaron los TPs |
| **2. Comparar** | Un script extrajo **todos los acrónimos y términos técnicos** de los resúmenes (**2 616 candidatos**, **608 acrónimos distintos**) y buscó cada uno en las 298 notas |
| **3. Aislar los huecos** | Se quedaron los **133 acrónimos ausentes** y se los leyó en contexto para descartar ruido (inflexiones, erratas del OCR, nombres de pines) |
| **4. Cerrar** | Los temas reales que faltaban se escribieron como contenido nuevo en la jerarquía `Unidad → Tema → Subtema` |
| **5. Uniformar** | Se verificó que **todos** los subtemas tengan la misma estructura de estudio (resumen en una frase, analogía, definición, diagrama, ejemplo resuelto, error típico, relacionado) |

## 2. Lo que faltaba y ya está

| Tema ausente | Dónde aparecía | Dónde se agregó |
|---|---|---|
| **Códigos ponderados** (BCD natural, **AIKEN 2-4-2-1**) | `apuntes` U1, `Resumen 3` p. 1 (era una tabla de examen) | **nuevo subtema [[1.6.1 Códigos ponderados y no ponderados]]** |
| **Códigos no ponderados** (exceso 3), **BCD empaquetado/desempaquetado** | `apuntes` U1 | idem 1.6.1 + diagrama `codigos_ponderados` |
| **Códigos continuos y cíclicos**: **Gray** y **Johnson** | `apuntes` U1 | **nuevo subtema [[1.6.2 Códigos continuos y cíclicos]]** + diagrama `codigos_continuos` |
| **Detección y corrección de errores**: **paridad, LRC, CRC, Hamming** | `apuntes` U1 (CRC/LRC), Stallings cap. 5 | **nuevo subtema [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]]** + diagrama `deteccion_errores` |
| **Escalas de integración SSI / MSI / LSI / VLSI** | `apuntes` U1, `Resumen final` U1 | sección nueva en [[1.1.3 Compuertas universales]] |
| **Módulos de memoria**: SIMM / **DIMM** / **SODIMM**, **DDR2 a DDR5**, pines | `apuntes` U2 (`memorias.pdf`) | sección nueva en [[2.3.2 SRAM y DRAM]] |
| **FSB, puente norte y DMI** | `apuntes` U2 | sección nueva en [[7.4.2 Buses internos y externos]] |
| **Exceso 64 / Exceso 128** (la convención de la cátedra) y las fórmulas `Ep = E1 + E2 − 64 − K`, `Ed = E1 − E2 + 64 + K` | `apuntes` U9 | sección nueva en [[9.4.1 Formato, normalización y operaciones]] |
| **Inserción de NOP** para resolver hazards | `apuntes` U7 | sección nueva en [[7.1.2 Hazards y sus soluciones]] |

> [!info] Por qué impresionaba el de códigos y el de errores
> En `Resumen 3` la **primera página** es la tabla `decimal / binario natural / AIKEN / exceso 3`, y el CRC/LRC
> ocupa dos páginas de los apuntes: son temas que la cátedra **da y toma**, y no estaban en la bóveda.

## 3. Claridad: cómo quedó cada subtema

Los **107 subtemas** tienen ahora la misma estructura, para que estudiar sea siempre el mismo recorrido:

| Sección | Para qué | Cobertura |
|---|---|---|
| `[!abstract] En una frase` | la respuesta mínima, la que se dice primero en el oral | **107 / 107** |
| `[!note] Si es la primera vez` | analogía cotidiana antes de la definición | **107 / 107** |
| Definición + tablas | el contenido formal | **107 / 107** |
| **Diagrama** | el dibujo que hay que poder reproducir | **107 / 107** (109 propios + 100 de libro) |
| **Ejemplo resuelto** | un caso con números, paso a paso | **107 / 107** |
| `[!warning]` error típico | lo que se pierde por escribir mal | **107 / 107** |
| `## Relacionado` | a dónde ir después | **107 / 107** |

**Tamaño:** mediana de **627 palabras** por subtema (mínimo 354, máximo ~1 100). Cada subtema entra en **una**
pantalla de lectura de 4-5 minutos; la unidad completa, en 15-25 minutos.

**Extensión de las oraciones:** 493 de 2 505 oraciones pasan de 35 palabras (**20 %**). Están concentradas en los
temas con mucha fórmula (U9 y U5); no impiden estudiar, pero son lo primero a recortar si se quiere un texto más
liviano.

## 4. TPs y videos

| Qué | Estado |
|---|---|
| Notas de TP | **21 TPs** con su nota en `03 Material de cátedra (TPs)/` |
| Videos de la consigna | **16 TPs** tienen ahora una sección `## Videos del TP` con el **título real** y el canal de cada video |
| Recursos listados | **37** (videos de YouTube, listas de reproducción y material en Drive) |
| Enlaces muertos | **2 encontrados y quitados**: un PDF de Scalahed (404) y una lista de reproducción (404) |
| TPs sin videos en el PDF | **TP6, TP14, TP18, TP19, TP20**: la consigna venía sin enlaces |

> [!warning] Lo que los videos NO reemplazan
> Los videos son de canales externos y a veces usan otra convención (por ejemplo, IEEE 754 en lugar de exceso 64,
> o máquinas de 8 bits con otro juego de instrucciones). **Para el parcial manda la nota**, que está alineada con la
> cátedra. El video es para ver el circuito moverse.

## 5. Los resúmenes: qué se pudo leer y qué no

| Resumen | Páginas | Estado |
|---|---|---|
| `apuntes-arquitectura de computadores` | 111 | **texto completo** (37 576 palabras) — base principal de la auditoría |
| `2do intento FINAL ARQUITECTURA` | 38 | **texto completo** (14 370 palabras) — formato pregunta/respuesta |
| `Resumen final arqui` | 30 | **texto completo** (8 095 palabras) — recorrido unidad por unidad |
| `memorias` | 32 | **texto completo** (6 987 palabras) — específico de U2 |
| `Resumen2-20pag` | 20 | **escaneado a mano, sin capa de texto** ⇒ se revisó **página por página como imagen**: compuertas, Boole, Karnaugh, MUX/DEMUX, biestables, registros (todo ya cubierto) |
| `Resumen3-13pags` | 11 | **escaneado a mano** ⇒ revisado como imagen: tabla de códigos, ciclo de instrucción, microoperaciones, interrupciones (de acá salió el hueco de códigos) |

## 6. Lo que todavía queda flojo (honesto)

| Punto flojo | Impacto | Plan |
|---|---|---|
| Los dos resúmenes manuscritos no se pudieron leer con OCR | bajo: su temario coincide con lo ya cubierto | si aparece la versión digital, se vuelve a correr la auditoría |
| 20 % de oraciones largas | medio | pasar oración por oración en U5 y U9 |
| Los 25 videos no se vieron completos | medio | verlos y anotar, en cada nota, **minuto a minuto** qué aporta cada uno |
| No hay banco de preguntas de final por subtema | medio | armar 107 preguntas de autoevaluación (una por subtema) con respuesta |
| El resumen de cada unidad (`00 Síntesis`) no tiene versión "de una página" | bajo | agregar una tarjeta de repaso de 10 líneas por unidad |

## 7. Cómo estudiar con esto

1. **Primera pasada (por unidad):** leer `00 Síntesis — Unidad N`. Son 15-25 minutos y dan el mapa.
2. **Segunda pasada:** entrar a los subtemas que no cerraron, en orden. En cada uno: leer el `[!abstract]`,
   **tapar** el resto y decirlo en voz alta; después leer la definición y comparar.
3. **Dibujo:** copiar a mano el **diagrama propio** de cada subtema (el de la figura del libro es la fuente, no el
   que se rinde).
4. **Números:** resolver el **ejemplo resuelto** sin mirar y comparar. Si no sale, ése es el subtema a repetir.
5. **Cierre:** `04 Práctica/Autoevaluación` y el `01 Modelo de final resuelto` para las preguntas orales.

## Relacionado
[[07 Plan de mejoras pendientes]] (el backlog con prioridades) · [[00 Índice de la materia (las 10 unidades)]] · [[00 Mapa de diagramas (qué gráfico tiene cada subtema)]] ·
[[00 Figuras de los libros (índice)]] · [[00 Índice de TPs y qué aporta cada uno]] · [[02 Plan de estudio — las 10 unidades]]
