---
tipo: moc
prioridad: maxima
---
# Bloque EXAMEN — desarrollo del modelo de final

> [!abstract] Qué hay en este bloque
> **Todo lo que se pregunta en el final**, desarrollado como respuesta oral: las **27 preguntas de las 3 tandas**
> de la matriz (más los apoyos que cada una necesita), con **tabla de verdad / dibujo / guion / repreguntas /
> qué leer para ampliar**. Si estás preparando el final, **empezás y terminás acá**.

> [!tip] Las tres puertas, en orden
> 1. [[00 Matriz del final — las 3 tandas]] — **qué cae y con qué peso** (foto del profesor).
> 2. [[02 Chequeo de los 12 temas]] — la lista de la cátedra con **lo que hay que poder decir** de cada tema.
> 3. Las notas de cada tanda (abajo) — el desarrollo completo.

---

## Cómo está organizado

```
10_Examen_Final/
├── 00 Índice — bloque examen (esta nota)
├── 01 Primera tanda — la máquina/              8 preguntas + apoyos
├── 02 Segunda tanda — memorias y arquitectura/ 10 preguntas
├── 03 Tercera tanda — circuitos con tablas/    8 ítems + herramientas
└── 04 Guías del examen/                        matriz, chequeo, fuentes, banco, guion
```

> [!important] La regla de esta reorganización
> **Cada nota vive en un solo bloque** (el lugar donde más se usa), pero **se llega a ella desde los dos**.
> El bloque **Programa** ([[00 Índice — bloque programa (las 10 unidades)]]) te lleva a estas mismas notas
> cuando la unidad del programa las necesita. No hay contenido duplicado.

---

## 1.ª tanda — la máquina (8 preguntas, peso 6-10)

| Pregunta | Nota | Apoyos |
|---|---|---|
| **BLUE vs BLUE indexada** | [[BLUE vs BLUE indexada — qué cambia y por qué]] | [[BLUE indexada (RIF, RID, nuevo formato)]] |
| **Ciclo de LDA indexada (24 pulsos)** | [[Ciclo de LDA indexada (los 24 pulsos)]] | [[Ciclo de la instrucción LDA (24 pulsos)]] |
| **Flujo de direcciones y datos** | [[Flujo de información en BLUE (datos y direcciones)]] | [[Estructura básica de un computador]] |
| **Memoria RAM 8×3** | [[Memoria RAM 8x3]] | [[Celda elemental de memoria]] |
| **Estructura básica del computador** | [[Estructura básica de un computador]] | [[Registros de la CPU]] |
| **Cómo se implementa la UC** | [[Cómo se implementa la Unidad de Control]] | [[Unidad de Control]] |
| **Formato de la instrucción (4 → 1 campo)** | [[Formato de la instrucción (4 formatos)]] | [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] |
| **Ciclo de máquina** | [[Ciclo de máquina]] | [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] |

**Y las cuatro que se preguntan como apoyo de la 1.ª tanda:** [[Proceso de manejo de una instrucción]] (las 5
fases y en qué unidad se usa) · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]].

## 2.ª tanda — memorias y arquitectura (10 preguntas, peso 4-10)

| Pregunta | Peso | Nota |
|---|---|---|
| Celda elemental de memoria | 4 | [[Celda elemental de memoria]] |
| **CISC y RISC** | **10** | [[CISC y RISC]] |
| **Pipeline** | **10** | [[Pipeline]] |
| **Interrupciones** | **9** | [[Interrupciones y entrada-salida]] |
| Las 16 instrucciones, todos los pulsos | 6-7 | [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] |
| Memoria ROM y sus tipos | 4 | [[Memoria ROM y sus tipos]] |
| Memoria caché | 4 | [[Memoria caché]] |
| **Registros base e índice** | 8 | [[Registros base e índice]] |
| Jerarquía de memorias | 4 | [[Jerarquía de memorias]] |
| **Modos de direccionamiento (los 4 de la indexada)** | 8 | [[Modos de direccionamiento]] (+ [[BLUE indexada (RIF, RID, nuevo formato)]]) |

## 3.ª tanda — circuitos con tabla de verdad (peso 12)

> [!warning] El orden obligatorio de cada ítem
> **tabla de verdad → función → Karnaugh → circuito dibujado**. Si falta el circuito o la función, la tabla sola
> no alcanza.

| # | Ítem | Nota |
|---|---|---|
| — | **Herramienta base (Karnaugh)** | [[Mintérminos y maxtérminos]] |
| 1 | Decodificadores | [[Decodificador]] |
| 2 | Codificadores | [[Codificador]] |
| 3 | Multiplexores | [[Multiplexor]] |
| 4 | Demultiplexores | [[Demultiplexor]] |
| 5 | RS → JK con Karnaugh | [[Conversión entre biestables (RS, JK, D, T)]] |
| 6 | Flip-flops D, T y RS | [[Flip-Flops SR, D, JK y T]] |
| 7 | Álgebra de Boole y DeMorgan | [[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] |
| 8 | Sumadores | [[Semisumador]] · [[Sumador completo]] |
| + | El RI y 3 ejemplos de instrucciones | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] |
| — | Compuertas (base de dibujo) | [[Compuertas lógicas]] |

## 4. Guías del examen

| Nota | Para qué |
|---|---|
| [[00 Matriz del final — las 3 tandas]] | los pesos reales y el plan de 5 días |
| [[02 Chequeo de los 12 temas]] | la lista de la cátedra, tema por tema, con "lo decisivo" |
| [[01 Qué leer para cada pregunta principal]] | qué fuente abrir para cada tema (cátedra + libros) |
| [[Guion de respuestas — preguntas principales]] | el oral ensayado, movimiento por movimiento |
| [[Banco de preguntas del final]] | preguntas sueltas para practicar al azar |

---

## Cómo se estudia este bloque (3 pasadas)

1. **Decir sin mirar (60-90 s por pregunta).** Usá la columna "lo decisivo" del [[02 Chequeo de los 12 temas]].
2. **Dibujar.** Celda de memoria, mapa de Karnaugh, pipeline, ciclo de búsqueda, LDA 24 pulsos, los 4 modos de la
   indexada. Práctica: [[Cómo dibujar los circuitos (checklist de pizarrón)]].
3. **Cruzar con la cátedra.** De cada nota, leer su sección **"Para ampliar"** y abrir la fuente indicada.

> [!tip] Los cinco temas que definen la nota
> **3.ª tanda (12)** · **CISC/RISC (10)** · **pipeline (10)** · **RAM 8×3 (10)** · **interrupciones (9)**.
> Con esos cinco sólidos ya estás arriba de la mitad del examen.

---

## Relacionado
[[00 Índice — bloque programa (las 10 unidades)]] · [[00 Cómo usar esta bóveda]] ·
[[03 Ruta de estudio para el final]] · [[04 Resumen integrador de la materia]]
