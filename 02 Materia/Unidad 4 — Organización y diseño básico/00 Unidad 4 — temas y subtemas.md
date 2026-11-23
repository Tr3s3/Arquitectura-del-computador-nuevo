---
tipo: indice
unidad: 4
---
# Unidad 4 — Organización y diseño básico

> [!abstract] Qué pide la unidad
> Armar la computadora completa: **estructura** (CPU + memoria + E/S con buses), el modelo **von Neumann** con la
> **máquina BLUE**, el **ciclo de instrucción** en 8 pulsos gobernado por la **Unidad de Control**. Es el corazón de
> la 1.ª tanda del final.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 4 completa (lectura de corrido)]]**: los **10 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 4]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.

> [!success] Unidad desarrollada
> Los **4 temas** y sus **10 subtemas** están escritos, y hay **dos archivos con toda la unidad junta**:
> el resumen de una página (**[[00 Síntesis — Unidad 4]]**) y el desarrollo completo para leer de corrido
> (**[[00 Unidad 4 completa (lectura de corrido)]]**). Estado: ✅ completa.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 4 — Organización y diseño básico/
├── 00 Unidad 4 — temas y subtemas   (esta nota)
├── 00 Síntesis — Unidad 4           (toda la unidad en un solo archivo)
├── 00 Unidad 4 completa (lectura de corrido)   ← los subtemas pegados, para leer de corrido
├── Tema 4.1 Estructura y modelo von Neumann/
│   ├── 4.1.1 Unidades funcionales de una computadora
│   └── 4.1.2 IAS y el programa almacenado
├── Tema 4.2 La máquina BLUE/              (+ la nota ampliada Programar en BLUE — ejemplos)
│   ├── 4.2.1 Especificación, registros y 4096x16
│   ├── 4.2.2 Los 16 opcodes octales
│   └── 4.2.3 Programar en BLUE
├── Tema 4.3 El ciclo de instrucción/
│   ├── 4.3.1 Ciclo de reloj, de máquina y de instrucción
│   ├── 4.3.2 Búsqueda, los 8 pulsos
│   └── 4.3.3 Ejecución instrucción por instrucción
└── Tema 4.4 Unidad de Control/
    ├── 4.4.1 Funciones y señales de control
    └── 4.4.2 estado·pulso·instrucción y el decodificador 1-16
```

## Tema por tema

| Tema | Subtemas (notas) | Índice |
|---|---|---|
| **4.1 Estructura y von Neumann** | [[4.1.1 Unidades funcionales de una computadora]] · [[4.1.2 IAS y el programa almacenado]] | [[00 Tema 4.1 — índice]] |
| **4.2 La máquina BLUE** | [[4.2.1 Especificación, registros y 4096x16]] · [[4.2.2 Los 16 opcodes octales]] · [[4.2.3 Programar en BLUE]] | [[00 Tema 4.2 — índice]] |
| **4.3 El ciclo de instrucción** | [[4.3.1 Ciclo de reloj, de máquina y de instrucción]] · [[4.3.2 Búsqueda, los 8 pulsos]] · [[4.3.3 Ejecución instrucción por instrucción]] | [[00 Tema 4.3 — índice]] |
| **4.4 Unidad de Control** | [[4.4.1 Funciones y señales de control]] · [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] | [[00 Tema 4.4 — índice]] |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** el diagrama de bloques con el bus único y las cinco unidades.
2. Decir los **cuatro números** de la BLUE (4096×16, 8×125 ns = 1 µs, 16 instrucciones, 12 bits).
3. **Codificar y decodificar** una instrucción en octal y decir cuántos pulsos tarda.
4. Escribir la **tabla de los 8 pulsos** de la búsqueda y explicar por qué el 8.º existe.
5. Explicar **por qué 8 instrucciones son de 1 ciclo y 6 de 2 ciclos**.
6. Escribir la señal de control de cualquier microoperación (`F·CP5`, `E·CP8·ADD`).

## TPs de la unidad
[[TP15 Arquitectura de Von Neumann (IAS)]] · [[TP16 Ciclo de instrucción básico]] ·
(apoyo) [[TP14 Buses]] · [[TP17 Formato básico de instrucciones]]

## Fuente de la cátedra
`blue.pdf` (Foster, *Una máquina elemental*: especificación, Tabla 2 del ciclo de búsqueda, instrucciones de dos
ciclos, unidad de control) · Apuntes **Unidad 4** y **Unidad 5**.

## Desarrollo de examen de estos temas
[[00 Tanda 1 — índice]]: [[Estructura básica de un computador]] · [[Flujo de información en BLUE (datos y direcciones)]] ·
[[Memoria RAM 8x3]] · [[Cómo se implementa la Unidad de Control]] · [[Unidad de Control]] · [[Ciclo de máquina]] ·
[[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] ·
Tanda 2: [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] ·
Tanda 3: [[Máquina BLUE — arquitectura y conjunto de instrucciones]]

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Síntesis — Unidad 4]] ·
[[00 Unidad 3 — temas y subtemas]] · [[00 Unidad 5 — temas y subtemas]]
