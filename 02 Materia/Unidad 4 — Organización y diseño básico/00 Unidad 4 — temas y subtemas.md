---
tipo: indice
unidad: 4
---
# Unidad 4 — Organización y diseño básico

> [!abstract] Qué pide la unidad
> Armar la computadora completa: **estructura** (CPU + memoria + E/S con buses), el modelo **von Neumann** con la
> **máquina BLUE**, y el **ciclo de instrucción** gobernado por la **Unidad de Control**. Es el corazón de la
> 1.ª tanda del final.

| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **4.1 Estructura de una computadora** | von Neumann · unidades funcionales · IAS · buses | [[Estructura básica de un computador]] · carpeta `Tanda 1/1.5` |
| **4.2 La máquina BLUE** | especificación (4096×16) · registros · 16 opcodes · señales RUN/STATE/CLOCK | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · carpeta `Tanda 3/3.9` |
| **4.3 Programar la BLUE** | ensamblador de la cátedra · lazos · arreglos · ejemplos resueltos | [[Programar en BLUE — ejemplos]] · `Tema 4.3 Programar la BLUE/` |
| **4.4 Ciclo de instrucción** | ciclo de reloj / de máquina / de instrucción · los 8 pulsos · búsqueda y ejecución | [[Ciclo de máquina]] · [[Proceso de manejo de una instrucción]] · carpeta `Tanda 1/1.8` |
| **4.5 Unidad de Control** | 4 funciones · señales de control · `estado·pulso·instrucción` · implementación con decodificador | [[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]] · carpeta `Tanda 1/1.6` |
| **4.6 Las 16 instrucciones** | microoperaciones de cada una · 1 ciclo vs 2 ciclos · E/S | [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · carpeta `Tanda 2/2.5` |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** el diagrama de bloques con el bus único.
2. **Contar los pulsos** de cualquier instrucción (8 o 16) y decir por qué.
3. Escribir la **señal de control** de una microoperación (`E·CP8·LDA`).
4. **Explicar** por qué la búsqueda tarda 7 pulsos y el ciclo tiene 8.

## TPs de la unidad
[[TP15 Arquitectura de Von Neumann (IAS)]] · [[TP16 Ciclo de instrucción básico]] ·
(apoyo: [[TP14 Buses]] · [[TP17 Formato básico de instrucciones]])

## Fuente de la cátedra
`blue.pdf` (Foster, *Una máquina elemental*: ciclo de búsqueda, Tabla 2, unidad de control) ·
Apuntes **Unidad 4** y **Unidad 5**.

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 3 — temas y subtemas]] ·
[[00 Unidad 5 — temas y subtemas]] · [[00 Tanda 1 — índice]]
