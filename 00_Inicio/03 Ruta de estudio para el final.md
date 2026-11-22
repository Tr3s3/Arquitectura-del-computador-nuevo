---
tipo: guia
---
# Ruta de estudio para el final

> [!abstract] La regla
> El modelo de final tiene **8 preguntas principales** (valen la nota), **12 secundarias** (te las
> preguntan para subir o bajar) y **7 de práctica** (son las que se resuelven en el pizarrón).
> Estudiá en ese orden, no en el orden del programa.

## Bloque 0 — el esqueleto (2 h)
Sin esto, nada de lo demás se entiende.
1. [[Estructura básica de un computador]] — CPU, memoria, E/S y los tres buses.
2. [[Registros de la CPU]] — qué hace cada registro y **quién lo usa**.
3. [[Ciclo de máquina]] — búsqueda / ejecución, y el rol de RUN, STATE y CLOCK.

## Bloque 1 — las preguntas principales (2 días)
| # | Pregunta | Nota | Tiempo |
|---|---|---|---|
| 1 | Flujo de información (dato y direcciones) | [[Flujo de información en BLUE (datos y direcciones)]] | 1 h |
| 2 | Formato de la instrucción (las 4) | [[Formato de la instrucción (4 formatos)]] | 1 h |
| 3 | Ciclo de máquina | [[Ciclo de máquina]] | 1 h |
| 4 | Estructura básica (unidades y buses) | [[Estructura básica de un computador]] | 1 h |
| 5 | Memoria RAM 8×3 | [[Memoria RAM 8x3]] | 1,5 h |
| 6 | Ciclo de ejecución de BLUE indexada y sin indexar | [[BLUE indexada (RIF, RID, nuevo formato)]] + [[Ciclo de ejecución — todas las operaciones]] | 2 h |
| 7 | UC: funciones y señales de control | [[Unidad de Control]] | 1,5 h |
| 8 | Interrupciones | [[Interrupciones y entrada-salida]] | 1,5 h |

## Bloque 2 — secundarias (1 día)
Agrupadas por familia, así se estudian de a bloques:
- **Lógica y memoria interna:** [[Celda elemental de memoria]] · [[Memoria ROM y sus tipos]] · [[Jerarquía de memorias]] · [[Flip-Flops SR, D, JK y T]]
- **Direccionamiento:** [[Modos de direccionamiento]] (incluye *ventajas del indexado*)
- **Ciclos en detalle:** [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] · [[Ciclo de la instrucción LDA (24 pulsos)]]
- **ISA:** [[Máquina BLUE — arquitectura y conjunto de instrucciones]] (las 16 operaciones y qué hace cada una)
- **Arquitecturas:** [[Pipeline]] · [[CISC y RISC]]

## Bloque 3 — prácticas (1 día)
Se resuelven en el pizarrón, con tabla de verdad, funciones y gráfico:
[[Prácticas resueltas]] → sumador completo, decodificador, demultiplexor, multiplexor,
álgebra de Boole + DeMorgan, conjunto de instrucciones, celda elemental y caché.

## Bloque 4 — ensayo (medio día)
1. [[Guion de respuestas — preguntas principales]] → leelo en voz alta, cronometrado.
2. [[Autoevaluación]] → 30 preguntas cortas; las que fallás vuelven al Bloque 1 o 2.
3. Dibujá de memoria, en hoja en blanco: la estructura básica, la RAM 8×3, el ciclo de búsqueda
   con sus pulsos y el flujo de información de BLUE. Si los cuatro salen, estás listo.

> [!tip] Regla 20/80 del final
> Cuatro dibujos explican el 60% de la materia: **(1)** estructura básica con buses, **(2)** RAM 8×3,
> **(3)** ciclo de búsqueda pulso por pulso, **(4)** flujo de información de BLUE. Practicá dibujarlos
> hasta que salgan en 3 minutos cada uno.
