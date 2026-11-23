---
tipo: indice
unidad: 2
---
# Unidad 2 — Memorias y circuitos secuenciales

> [!abstract] Qué pide la unidad
> Pasar de lo **combinacional** a lo que **recuerda**: biestables y flip-flops → registros y contadores → la
> memoria (celda, chip, jerarquía). Es la unidad más larga del programa y la que más circuitos hace dibujar.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 2 completa (lectura de corrido)]]**: los **20 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 2]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.

> [!success] Unidad desarrollada
> Los **7 temas** y sus **20 subtemas** están escritos, y hay **dos archivos con toda la unidad junta**:
> el resumen de una página (**[[00 Síntesis — Unidad 2]]**) y el desarrollo completo para leer de corrido
> (**[[00 Unidad 2 completa (lectura de corrido)]]**). Estado: ✅ completa.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 2 — Memorias y circuitos secuenciales/
├── 00 Unidad 2 — temas y subtemas   (esta nota)
├── 00 Síntesis — Unidad 2           (toda la unidad en un solo archivo)
├── 00 Unidad 2 completa (lectura de corrido)   ← los subtemas pegados, para leer de corrido
├── Tema 2.1 Biestables y flip-flops/
│   ├── 2.1.1 Biestable RS (NOR y NAND)
│   ├── 2.1.2 Flip-flops D y T
│   ├── 2.1.3 Flip-flop JK y ecuaciones características
│   └── 2.1.4 Conversión entre biestables
├── Tema 2.2 Registros y contadores/
│   ├── 2.2.1 Registros PIPO y SISO
│   ├── 2.2.2 Registros SIPO y PISO
│   └── 2.2.3 Contadores binarios y módulo N
├── Tema 2.3 La celda y el chip de memoria/
│   ├── 2.3.1 Celda elemental de memoria
│   ├── 2.3.2 SRAM y DRAM
│   ├── 2.3.3 Matriz, expansión y RAM 8x3
│   └── 2.3.4 Detección y corrección de errores
├── Tema 2.4 ROM y memorias no volátiles/
│   ├── 2.4.1 ROM = decodificador + OR
│   └── 2.4.2 PROM, EPROM, EEPROM y Flash
├── Tema 2.5 Jerarquía y caché/
│   ├── 2.5.1 Jerarquía y localidad
│   ├── 2.5.2 Caché: mapeos y políticas
│   └── 2.5.3 AMAT y cálculo de mejora
├── Tema 2.6 Memorias complementarias/
│   ├── 2.6.1 Memoria virtual y paginación
│   └── 2.6.2 Memoria auxiliar y memoria asociativa
└── Tema 2.7 Dimensionar memorias/
    ├── 2.7.1 Bits de dirección = log2 de celdas
    └── 2.7.2 CodOp vs campo de dirección
```

## Tema por tema

| Tema | Subtemas (notas) | Índice |
|---|---|---|
| **2.1 Biestables y flip-flops** | [[2.1.1 Biestable RS (NOR y NAND)]] · [[2.1.2 Flip-flops D y T]] · [[2.1.3 Flip-flop JK y ecuaciones características]] · [[2.1.4 Conversión entre biestables]] | [[00 Tema 2.1 — índice]] |
| **2.2 Registros y contadores** | [[2.2.1 Registros PIPO y SISO]] · [[2.2.2 Registros SIPO y PISO]] · [[2.2.3 Contadores binarios y módulo N]] | [[00 Tema 2.2 — índice]] |
| **2.3 La celda y el chip de memoria** | [[2.3.1 Celda elemental de memoria]] · [[2.3.2 SRAM y DRAM]] · [[2.3.3 Matriz, expansión y RAM 8x3]] · [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]] | [[00 Tema 2.3 — índice]] |
| **2.4 ROM y memorias no volátiles** | [[2.4.1 ROM = decodificador + OR]] · [[2.4.2 PROM, EPROM, EEPROM y Flash]] | [[00 Tema 2.4 — índice]] |
| **2.5 Jerarquía y caché** | [[2.5.1 Jerarquía y localidad]] · [[2.5.2 Caché: mapeos y políticas]] · [[2.5.3 AMAT y cálculo de mejora]] | [[00 Tema 2.5 — índice]] |
| **2.6 Memorias complementarias** | [[2.6.1 Memoria virtual y paginación]] · [[2.6.2 Memoria auxiliar y memoria asociativa]] | [[00 Tema 2.6 — índice]] |
| **2.7 Dimensionar memorias** | [[2.7.1 Bits de dirección igual a log2 de celdas]] · [[2.7.2 CodOp vs campo de dirección]] | [[00 Tema 2.7 — índice]] |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar un biestable** y escribir su **ecuación característica** con el mapa.
2. **Convertir** un flip-flop en otro (RS → JK con dos compuertas).
3. **Dibujar una celda de memoria** con sus 4 bloques y explicar SRAM vs DRAM.
4. **Dimensionar**: cuántas celdas, cuántos bits de dirección, cuántos chips, cuántas instrucciones.
5. **Calcular el AMAT** y comparar dos cachés.
6. **Dibujar una ROM** como decodificador + OR.

## TPs de la unidad
[[TP8 Biestables RS]] · [[TP9 Biestables D, JK y T]] · [[TP10 Registros PIPO y SISO]] · [[TP11 Registros SIPO y PISO]] ·
[[TP12 Memoria principal]] · [[TP13 Componentes internos]]

## Fuente de la cátedra
Apuntes **Unidad 3 — Memorias electrónicas** · `memorias.pdf` (ROM, SRAM, DRAM, refresco) · Floyd (secuenciales) ·
Hamacher (jerarquía). Resúmenes de clase: `Resumen final arqui.pdf`.

## Desarrollo de examen de estos temas
[[00 Tanda 2 — índice]]: [[Celda elemental de memoria]] · [[Memoria ROM y sus tipos]] · [[Memoria caché]] ·
[[Jerarquía de memorias]] · [[Registros base e índice]] · [[Modos de direccionamiento]] ·
y en la Tanda 1: [[Memoria RAM 8x3]] · [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] ·
en la Tanda 3: [[Flip-Flops SR, D, JK y T]] · [[Conversión entre biestables (RS, JK, D, T)]]

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Síntesis — Unidad 2]] ·
[[00 Unidad 1 — temas y subtemas]] · [[00 Unidad 3 — temas y subtemas]]
