---
tipo: guia
prioridad: maxima
---
# Chequeo: los 12 temas de la lista del profesor

> [!abstract] Para qué sirve esta nota
> Es el **control de cobertura** de la lista de 12 temas que pasó la cátedra. Cada tema tiene su nota maestra
> (desarrollo desde cero + tabla + dibujo + guion oral + repreguntas + "Para ampliar"), su **peso** en la matriz
> y **lo que hay que poder decir** en 60-90 segundos. Si podés explicar la columna "decisivo", el tema está
> aprobado.

| # | Tema de la lista | Nota maestra | Peso / tanda | Lo decisivo (lo que no se puede omitir) |
|---|---|---|---|---|
| 1 | **Memoria RAM (celda elemental)** | [[Celda elemental de memoria]] (+ [[Memoria RAM 8x3]]) | 4 · 2.ª | Los **4 bloques** de la celda (biestable, selección, L/E, buffer 3 estados) y **SRAM (biestable) vs DRAM (1 T + capacitor + refresco)** |
| 2 | **Flip Flops** | [[Flip-Flops SR, D, JK y T]] (+ [[Conversión entre biestables (RS, JK, D, T)]]) | 12 · 3.ª (ítems 5 y 6) | Las **4 ecuaciones características** (`Q⁺ = S+R'Q`, `D`, `JQ'+K'Q`, `T⊕Q`) y su **mapa de Karnaugh** |
| 3 | **Modos de direccionamiento (BLUE indexada ¿ventajas?)** | [[Modos de direccionamiento]] + [[BLUE indexada (RIF, RID, nuevo formato)]] | 8 · 2.ª | Los **7 modos** con la EA y los **accesos a memoria**, los **4 modos del modificador** y las **ventajas de la indexada** (lazos, 64 K, 32 instrucciones, RB) **pagando 24 pulsos** |
| 4 | **Memoria ROM** | [[Memoria ROM y sus tipos]] | 4 · 2.ª | No volátil; **ROM = decodificador + m compuertas OR**; máscara → PROM → EPROM (UV) → EEPROM → Flash |
| 5 | **Jerarquía de memorias** | [[Jerarquía de memorias]] (+ [[Memoria caché]]) | 4 · 2.ª | La **pirámide** con tiempos, **localidad**, y que mejora el **promedio** (`1 + 0,05·100 = 6 ns`), no un acceso |
| 6 | **Defina y ejemplifique el proceso pipeline** | [[Pipeline]] | **10** · 2.ª | Las **etapas**, el diagrama en escalera, `k+(n−1)` vs `k·n` y el ejemplo de la cátedra (**3 operaciones en 8 pulsos**); los **3 hazards** |
| 7 | **Arquitectura CISC y RISC** | [[CISC y RISC]] | **10** · 2.ª | La tabla comparativa (largo, modos, memoria, registros, **UC**), el ejemplo `ADD [BX+SI+4],AX` vs `LW+ADD+SW` y el **híbrido** actual |
| 8 | **Proceso de manejo de una instrucción: qué son y en qué unidad se usa** | [[Proceso de manejo de una instrucción]] | 6-7 · 1.ª/4.ª | Las **5 fases** (búsqueda → decodificación → operandos → ejecución → escritura), la distinción **instrucción / microoperación / señal**, y que **lo dirige la UC** (ALU ejecuta, memoria guarda) |
| 9 | **7 y 8 pulsos del ciclo de búsqueda** | [[Ciclo de búsqueda (7 y 8 pulsos)]] | 6 · 1.ª | `PC→MAR` · `PC+1` (CP2-CP4) · `strobe MBR` (CP5) · `MBR→IR` (CP6) · `E→State` (CP8), y **por qué 8**: el octavo era la **reescritura de la ferrita** |
| 10 | **Ciclo de ejecución para todas las operaciones** | [[Ciclo de ejecución — todas las operaciones]] | 6-8 · 1.ª | Las **4 familias** (transferencia, ALU, control, E/S) con sus microoperaciones, y que `JMP/NOP/NOT/RAL/CSA/HLT/SRJ/JMA` **terminan en la búsqueda** |
| 11 | **Ciclo LDA (24 pulsos)** | [[Ciclo de LDA indexada (los 24 pulsos)]] (+ [[Ciclo de la instrucción LDA (24 pulsos)]]) | 8 · 1.ª | Los **3 ciclos**: `RID→X`/`MBR→W` (2.º) y `Σ→MAR+Read` → `MBR→AC` (3.º); **24 pulsos = 3 ciclos**, y el indirecto **32** |
| 12 | **Las operaciones de máquina BLUE y qué hacía cada una** | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] + [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | 6-7 · 1.ª | La tabla de los **16 opcodes en octal**, el **RI** (4+12, carga en CP6) y **3 ejemplos** (LDA 16, ADD 16, JMP 8) |

---

## Cómo usar este chequeo

**Método en 3 pasadas (2 h por tanda):**
1. **Pasada 1 — decir sin mirar.** Para cada tema, contá en voz alta 60-90 segundos con la columna "decisivo" a
   la vista. Si te trabás, marcá el tema.
2. **Pasada 2 — dibujar.** Sólo los temas con dibujo: celda, mapa de Karnaugh, pipeline, ciclo de búsqueda,
   LDA 24 pulsos, los 4 modos de la indexada. **El final es oral pero se rinde dibujando.**
3. **Pasada 3 — cruzar.** Abrí la nota maestra **sólo** de los temas marcados y leé su sección
   **"Para ampliar"** (qué fuente y qué parte) para tapar el hueco con la cátedra.

> [!tip] Los 4 temas que hay que tener perfectos
> Por peso y por frecuencia: **pipeline (10)**, **CISC/RISC (10)**, **los circuitos de la 3.ª tanda (12)** y
> **LDA 24 pulsos / modos en la indexada (8)**. Esos cuatro son el 40 % de la nota.

---

## Notas de contexto que se usan en varios temas

| Si te preguntan… | Apoyo |
|---|---|
| el esquema general de la máquina | [[Estructura básica de un computador]] · [[Flujo de información en BLUE (datos y direcciones)]] |
| registros y sus tamaños | [[Registros de la CPU]] · [[Registros base e índice]] |
| cómo se arma una señal de control | [[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]] |
| interrupciones (no está en la lista, pero se pregunta) | [[Interrupciones y entrada-salida]] |
| qué fuente abrir para cada pregunta | [[01 Qué leer para cada pregunta principal]] |
| la matriz completa con los pesos | [[00 Matriz del final — las 3 tandas]] |

---

## Relacionado
[[00 Matriz del final — las 3 tandas]] · [[01 Qué leer para cada pregunta principal]] ·
[[Banco de preguntas del final]] · [[Guion de respuestas — preguntas principales]] ·
[[03 Ruta de estudio para el final]]
