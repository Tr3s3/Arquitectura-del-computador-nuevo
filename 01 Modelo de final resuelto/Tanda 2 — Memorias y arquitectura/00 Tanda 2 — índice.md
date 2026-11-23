---
tipo: indice
prioridad: maxima
---
# Tanda 2 — Memorias y arquitectura (10 preguntas)

> [!abstract] Cómo está armada esta tanda
> Una **carpeta por pregunta**, con el **desarrollo principal** y sus **subtemas** adentro. Los pesos son los de
> la [[00 Matriz del final — las 3 tandas|matriz]]: acá están las dos preguntas de **peso 10** (CISC/RISC y
> pipeline) y la de **peso 9** (interrupciones).

| # | Pregunta | Peso | Carpeta | Archivos que corresponden |
|---|---|---|---|---|
| 2.1 | **Celda elemental de memoria** | 4 | `2.1 Celda elemental de memoria/` | [[Celda elemental de memoria]] |
| 2.2 | **Memoria ROM y sus tipos** | 4 | `2.2 Memoria ROM y sus tipos/` | [[Memoria ROM y sus tipos]] |
| 2.3 | **Memoria caché** | 4 | `2.3 Memoria caché/` | [[Memoria caché]] |
| 2.4 | **Jerarquía de memorias** | 4 | `2.4 Jerarquía de memorias/` | [[Jerarquía de memorias]] |
| 2.5 | **Las 16 instrucciones, pulso por pulso** | 6-7 | `2.5 Las 16 instrucciones, pulso por pulso/` | [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] |
| 2.6 | **CISC y RISC** | **10** | `2.6 CISC y RISC/` | [[CISC y RISC]] |
| 2.7 | **Pipeline** | **10** | `2.7 Pipeline/` | [[Pipeline]] |
| 2.8 | **Interrupciones** | **9** | `2.8 Interrupciones/` | [[Interrupciones y entrada-salida]] |
| 2.9 | **Registros base e índice** | 8 | `2.9 Registros base e índice/` | [[Registros base e índice]] |
| 2.10 | **Modos de direccionamiento** | 8 | `2.10 Modos de direccionamiento/` | [[Modos de direccionamiento]] |

> [!note] Un subtema que vive en la Tanda 1
> [[BLUE indexada (RIF, RID, nuevo formato)]] es el **hardware** que hace posibles los modos 2 y 3 de la pregunta
> 2.10 y los registros de la 2.9. Está guardado en `Tanda 1 → 1.2 BLUE vs BLUE indexada/`, porque ahí es donde
> más se usa.

> [!note] La carpeta `Apoyo a la pregunta/` (está dentro de cada pregunta)
> Cada pregunta tiene adentro **`Apoyo a la pregunta/`** con la nota **`00 Apoyos — N.M …`**:
> qué archivos hacen falta para responderla, **para qué sirve cada uno** y el enlace a los apoyos
> que viven en otras tandas. Es lo primero que muestra la nota principal.


---

## El orden en que conviene estudiarla

**Bloque memorias (2.1 → 2.4):** primero la **celda**, después cómo se organiza en un chip (RAM/ROM), después
cómo se ordenan los chips (jerarquía) y por último el nivel rápido (caché).

**Bloque arquitectura (2.5 → 2.10):** las 16 instrucciones como repaso de la máquina, después **pipeline** y
**CISC/RISC** (que se explican uno con otro), después **interrupciones** y al final los **modos** con sus dos
registros índice.

> [!tip] Los dibujos de esta tanda
> Celda elemental (los 4 bloques) · pirámide de la jerarquía · mapa de Karnaugh no hace falta acá, pero sí el
> **diagrama de etapas del pipeline** y el **diagrama de tiempos** de las 3 operaciones en 8 pulsos.

---

## Ficha rápida (para repasar en 8 minutos)

| Pregunta | Lo que no se puede omitir |
|---|---|
| 2.1 | Biestable + selección + L/E + buffer de 3 estados; **SRAM** = 2 inversores realimentados, **DRAM** = 1 T + capacitor con **refresco** |
| 2.2 | No volátil; **ROM = decodificador + m OR**; máscara → PROM → EPROM (UV) → EEPROM → Flash |
| 2.3 | Localidad; **etiqueta / índice / desplazamiento**; 3 mapeos; write-through vs write-back; `AMAT = 1 + 0,05·100` |
| 2.4 | Pirámide registros → L1 → L2/L3 → RAM → disco; mejora el **promedio**, no un acceso |
| 2.5 | 8 pulsos (1 ciclo) sin memoria · 16 pulsos (2 ciclos) con memoria · el RI en CP6 |
| 2.6 | Tabla comparativa + `ADD [BX+SI+4],AX` vs `LW+ADD+SW` + UC microprogramada vs cableada |
| 2.7 | 5 etapas, diagrama en escalera, `k+(n−1)`, 3 hazards y sus soluciones |
| 2.8 | `IRQ·SI·CP8`; rutina en la posición 1 con **polling**; EMR, pila con SP, RTI |
| 2.9 | RIF (fuente) y RID (destino) al sumador de direcciones; RB reubica el programa |
| 2.10 | Los 7 modos con su EA y accesos; los 4 del modificador (0, 1, 2, 3) |

---

## Relacionado
[[00 Índice — el final resuelto]] · [[00 Tanda 1 — índice]] · [[00 Tanda 3 — índice]] ·
[[00 Matriz del final — las 3 tandas]]
