---
tipo: indice
unidad: 4
---
# Unidad 4 — Organización y diseño básico

> [!abstract] Qué pide la unidad
> Armar la computadora completa: **estructura** (CPU + memoria + E/S con buses), el modelo **von Neumann** con la
> **máquina BLUE**, y el **ciclo de instrucción** gobernado por la **Unidad de Control**. Es el corazón de la
> 1.ª tanda del final.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 4 — Organización y diseño básico/
├── 4.1 Estructura y modelo von Neumann/
│   ├── 4.1.1 Unidades funcionales de una computadora
│   └── 4.1.2 IAS y el programa almacenado
├── 4.2 La máquina BLUE/
│   ├── 4.2.1 Especificación, registros y 4096×16
│   ├── 4.2.2 Los 16 opcodes octales
│   └── 4.2.3 Programar en BLUE
├── 4.3 El ciclo de instrucción/
│   ├── 4.3.1 Ciclo de reloj, de máquina y de instrucción
│   ├── 4.3.2 Búsqueda: los 8 pulsos
│   └── 4.3.3 Ejecución instrucción por instrucción
└── 4.4 Unidad de Control/
    ├── 4.4.1 Funciones y señales de control
    └── 4.4.2 estado·pulso·instrucción y el decodificador 1-16
```

**4 temas y 10 subtemas.** Cada subtema va a ser **una nota** dentro de la carpeta de su tema,
y al terminar la unidad se genera **`00 Síntesis — Unidad 4`** con todo el contenido junto (como ya está hecho en
[[00 Síntesis — Unidad 1|la Unidad 1]]).

| Tema | Subtemas | Estado |
|---|---|---|
| **4.1 Estructura y modelo von Neumann** | 4.1.1 Unidades funcionales de una computadora · 4.1.2 IAS y el programa almacenado | ⏳ a desarrollar |
| **4.2 La máquina BLUE** | 4.2.1 Especificación, registros y 4096×16 · 4.2.2 Los 16 opcodes octales · 4.2.3 Programar en BLUE | ⏳ a desarrollar |
| **4.3 El ciclo de instrucción** | 4.3.1 Ciclo de reloj, de máquina y de instrucción · 4.3.2 Búsqueda: los 8 pulsos · 4.3.3 Ejecución instrucción por instrucción | ⏳ a desarrollar |
| **4.4 Unidad de Control** | 4.4.1 Funciones y señales de control · 4.4.2 estado·pulso·instrucción y el decodificador 1-16 | ⏳ a desarrollar |

> [!note] Qué hay ya de esta unidad
> El **desarrollo de examen** de casi todos estos temas ya está escrito (está enlazado más abajo, en la tabla de
> material disponible). Lo que falta es la **versión de programa**: el subtema desarrollado en la carpeta de su
> tema, con el detalle de la cursada y los TPs.

## Material ya disponible de esta unidad
| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **4.1 Estructura de una computadora** | von Neumann · unidades funcionales · IAS · buses | [[Estructura básica de un computador]] · carpeta `Tanda 1/1.5` |
| **4.2 La máquina BLUE** | especificación (4096×16) · registros · 16 opcodes · señales RUN/STATE/CLOCK | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · carpeta `Tanda 3/3.9` |
| **4.3 Programar la BLUE** | ensamblador de la cátedra · lazos · arreglos · ejemplos resueltos | [[Programar en BLUE — ejemplos]] · `Tema 4.2 La máquina BLUE/` |
| **4.4 Ciclo de instrucción** | ciclo de reloj / de máquina / de instrucción · los 8 pulsos · búsqueda y ejecución | [[Ciclo de máquina]] · [[Proceso de manejo de una instrucción]] · carpeta `Tanda 1/1.8` y su `Apoyo a la pregunta/` |
| **4.5 Unidad de Control** | 4 funciones · señales de control · `estado·pulso·instrucción` · implementación con decodificador | [[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]] · carpeta `Tanda 1/1.6` y su `Apoyo a la pregunta/` |
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
