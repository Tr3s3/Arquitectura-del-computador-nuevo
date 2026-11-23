---
tp: 12
unidad: 2
tipo: tp
---
# TP12 — Memoria principal (RAM, ROM y caché)

> [!abstract] Consigna (cátedra)
> **Ej. 1** memoria principal y tipos de memoria · **Ej. 2** RAM y sus tipos · **Ej. 3** ROM y sus tipos ·
> **Ej. 4** caché · **Ej. 5** **cuadro comparativo RAM vs ROM**.

## 1) Memoria principal — características que se piden
- Es la memoria **interna** donde la CPU tiene el **programa y los datos en ejecución** (von Neumann).
- Está organizada en **celdas** de tamaño fijo, cada una con una **dirección única**; el acceso es
  **aleatorio** (mismo tiempo para cualquier dirección).
- Es **volátil** (la RAM pierde el contenido sin alimentación), **rápida** (ns) y de capacidad media.
- Parámetros que la describen: **capacidad**, **ancho de palabra/celda**, **tiempo de acceso**, **ciclo de
  memoria**, **ancho de banda** y **volatilidad**.
- Tipos: **RAM** (SRAM/DRAM), **ROM** (máscara, PROM, EPROM, EEPROM, Flash) y **caché**.

## 2) RAM
- **Lectura/escritura**, volátil. Se direcciona por fila/columna (matriz 2D o 3D).
- **SRAM (estática)**: celda de 6 transistores (latch), **no necesita refresco**, muy rápida y cara ⇒ se usa
  en **caché** y registros.
- **DRAM (dinámica)**: celda de 1 transistor + 1 capacitor, **necesita refresco** cada pocos ms, alta
  densidad y barata ⇒ **memoria principal**.
- Variantes DRAM: FPM, EDO, SDRAM, DDR (DDR2/3/4/5) — la evolución fue multiplicar la tasa de transferencia.

## 3) ROM
- **Sólo lectura** en operación normal, **no volátil**.
- Tipos: **máscara** (grabada en fábrica) · **PROM** (una sola vez) · **EPROM** (borrado con UV) ·
  **EEPROM** (borrado eléctrico) · **Flash** (EEPROM por bloques).
- Usos: firmware/BIOS, tablas de constantes y **memoria de control** de la UC microprogramada.

## 4) Caché
Memoria pequeña y rápida (SRAM) que guarda **copias de bloques** de la memoria principal; transparente al
programa. Funciona por **localidad**. Niveles L1/L2/L3. Se define por su **mapeo** (directo, asociativo,
por conjuntos), su **política de escritura** (write-through / write-back) y su **política de reemplazo**
(LRU/FIFO/aleatorio).

## 5) Cuadro comparativo RAM vs ROM (el que se entrega)
| | **RAM** | **ROM** |
|---|---|---|
| Operación | lectura y escritura | sólo lectura |
| Volatilidad | volátil | no volátil |
| Contenido | programa y datos en ejecución | firmware, tablas, microcódigo |
| Velocidad | muy alta | alta (suele ser algo más lenta que la RAM) |
| Modificación | permanente, por la CPU | no se modifica (o requiere grabador/borrado) |
| Costo por bit | mayor | menor |
| Tecnología | SRAM (latch) / DRAM (capacitor) | matriz fija / transistor flotante |
| Se puede ampliar | sí (módulos) | no (queda fija de fábrica) |

## Enlaces
Desarrollo: [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] · [[Memoria caché]] · [[Jerarquía de memorias]]
Siguiente: [[TP13 Componentes internos]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Memoria principal](https://www.youtube.com/watch?v=VPvVvy5ahAU) | HelderC |
| ▶️ | [RAM, ROM y caché](https://www.youtube.com/watch?v=YMR5IdezPv4) | Aprende conmigo Informática |
| ▶️ | [Memorias ROM y RAM explicadas](https://www.youtube.com/watch?v=swOCvouHeAg) | MindMachineTV |
| ▶️ | [Video complementario del TP](https://www.youtube.com/watch?v=ONa_M3bKX7A) | — |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo
> desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se
> toma en el parcial).

