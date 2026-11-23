---
tipo: indice
unidad: 2
---
# Unidad 2 — Memorias y circuitos secuenciales

> [!abstract] Qué pide la unidad
> Pasar de lo **combinacional** a lo que **recuerda**: biestables y flip-flops → registros y contadores → la
> memoria (celda, chip, jerarquía). Es la unidad más larga del programa y la que más circuitos hace dibujar.

| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **2.1 Biestables y flip-flops** | SR (estado prohibido) · D · JK (toggle) · T · sincrónico vs asíncrono · ecuaciones características con Karnaugh | [[Flip-Flops SR, D, JK y T]] · carpeta `Tanda 3/3.6` |
| **2.2 Conversión entre flip-flops** | tabla de excitación · RS→JK (`S=JQ'`, `R=KQ`) · JK→D · T | [[Conversión entre biestables (RS, JK, D, T)]] · carpeta `Tanda 3/3.5` |
| **2.3 Registros** | PIPO · SISO · SIPO · PISO · carga paralela · desplazamiento | [[Registros]] · `Tema 2.4 Registros y contadores/` |
| **2.4 Contadores** | binario · con carga en paralelo · módulo N | [[Contadores]] · `Tema 2.4 Registros y contadores/` |
| **2.5 Celda de memoria y chip RAM** | celda elemental (biestable, selección, L/E, 3 estados) · SRAM vs DRAM · matriz 2D/3D · RAM 8×3 | [[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · carpetas `Tanda 2/2.1` y `Tanda 1/1.4` |
| **2.6 Memoria ROM** | decodificador + OR · máscara, PROM, EPROM, EEPROM, Flash | [[Memoria ROM y sus tipos]] · carpeta `Tanda 2/2.2` |
| **2.7 Jerarquía y caché** | localidad · pirámide · mapeos · políticas · AMAT | [[Jerarquía de memorias]] · [[Memoria caché]] · carpetas `Tanda 2/2.3 y 2.4` |
| **2.8 Memorias complementarias** | memoria virtual y paginación · TLB · memoria asociativa | [[Memoria virtual y administración de memoria]] · [[Memoria auxiliar y memoria asociativa]] · `Tema 2.5 Memorias complementarias/` |
| **2.9 Memorias grandes** | `bits dir = log₂ celdas` · CodOp vs dirección | [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] · carpeta `Tanda 1/1.7` |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar un biestable** y escribir su **ecuación característica** desde la tabla con Karnaugh.
2. **Convertir** un flip-flop en otro con dos compuertas y justificarlo.
3. **Dibujar una celda de memoria** con sus 4 bloques y explicar SRAM vs DRAM.
4. **Dimensionar una memoria**: cuántas celdas, cuántos bits de dirección, cuántos chips.
5. **Explicar el promedio** de la jerarquía (`AMAT`).

## TPs de la unidad
[[TP6 Decodificadores y demultiplexores]] · [[TP7 Codificadores y multiplexores]] · [[TP8 Biestables RS]] ·
[[TP9 Biestables D, JK y T]] · [[TP10 Registros PIPO y SISO]] · [[TP11 Registros SIPO y PISO]] ·
[[TP12 Memoria principal]] · [[TP13 Componentes internos]]

## Fuente de la cátedra
Apuntes **Unidad 3 — Memorias electrónicas** · `memorias.pdf` (Tema 7: ROM, SRAM, DRAM) · Floyd ·
Fernández Ramos et al. (tema 7).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 1 — temas y subtemas]] ·
[[00 Unidad 3 — temas y subtemas]] · [[00 Tanda 2 — índice]]
