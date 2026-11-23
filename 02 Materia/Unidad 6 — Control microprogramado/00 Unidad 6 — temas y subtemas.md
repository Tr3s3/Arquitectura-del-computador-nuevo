---
tipo: indice
unidad: 6
---
# Unidad 6 — Control microprogramado

> [!abstract] Qué pide la unidad
> Cómo se construye la **Unidad de Control**: con **compuertas (cableada)** o con un **microprograma guardado en
> una ROM (microprogramada)**. La BLUE usa cableada; el 8088, microprogramada con una ROM de **504 × 21 bits**.

> [!tip] Para leer la unidad de corrido
> **[[00 Unidad 6 completa (lectura de corrido)]]**: los **5 subtemas** pegados en un solo archivo,
> con sus diagramas y figuras, sin abrir nada más. La síntesis ([[00 Síntesis — Unidad 6]]) es el
> resumen de una página; el archivo completo es el desarrollo entero.


## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 6 — Control microprogramado/
├── Tema 6.1 Control cableado/
│   └── 6.1.1 Circuito, compuertas y señales
├── Tema 6.2 Control microprogramado/
│   ├── 6.2.1 Memoria de control y microinstrucción
│   └── 6.2.2 Secuenciamiento y microPC
└── Tema 6.3 Comparación y caso real/
    ├── 6.3.1 Cableada vs microprogramada
    ├── 6.3.2 El 8088: ROM de control 504×21
    └── Unidad de control cableada y microprogramada   (nota de desarrollo de examen)
```

**3 temas y 5 subtemas.** Cada subtema es **una nota** dentro de la carpeta de su tema. La unidad está **cerrada**
y todo su contenido quedó reunido en **[[00 Síntesis — Unidad 6]]**.

| Tema | Subtemas | Estado |
|---|---|---|
| **6.1 Control cableado** | 6.1.1 Circuito, compuertas y señales | ✅ |
| **6.2 Control microprogramado** | 6.2.1 Memoria de control y microinstrucción · 6.2.2 Secuenciamiento y microPC | ✅ |
| **6.3 Comparación y caso real** | 6.3.1 Cableada vs microprogramada · 6.3.2 El 8088: ROM de control 504×21 | ✅ |

## Los 3 temas, de un vistazo

| Tema | Índice | La idea en una línea |
|---|---|---|
| **6.1** | [[00 Tema 6.1 — índice]] | `señal = estado · pulso · instrucción`, con AND y OR |
| **6.2** | [[00 Tema 6.2 — índice]] | el opcode **elige una dirección** de la ROM, no enciende compuertas |
| **6.3** | [[00 Tema 6.3 — índice]] | rápida y rígida vs lenta y flexible · 504 × 21 bits |

## Material de examen ya disponible de esta unidad
| Tema | Nota | Dónde está además |
|---|---|---|
| **Todo el tema** | [[Cómo se implementa la Unidad de Control]] | `Tanda 1/1.6` + `Apoyo a la pregunta/` |
| **Microprogramación** | [[Unidad de control cableada y microprogramada]] | `Tema 6.3 Comparación y caso real/` |
| **Control de la UC** | [[Unidad de Control]] | `Tanda 1/1.6/Apoyo a la pregunta/` |
| **CISC vs RISC** | [[CISC y RISC]] | `Tanda 2/2.6` |
| **El 8088 real** | [[El 8086 como CPU convencional (TP21)]] | Unidad 5 · `Tema 5.6 El 8086/` |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** el esquema de una UC cableada: decodificador + FF de estado + compuertas AND/OR.
2. **Escribir la ecuación** de una señal de control y explicar el papel de las familias `REF` / `ARITH` / `DTA`.
3. **Escribir** una microinstrucción con sus campos y explicar para qué sirve cada uno.
4. Explicar los **cuatro mecanismos de secuenciamiento** (incremento, condicional, mapeo, microsubrutina).
5. Decir **cuándo conviene** cada tipo y relacionarlo con **CISC y RISC**.
6. Manejar los **números del 8088**: 504 × 21 bits, ~90 microprocedimientos, microPC de 9 bits.

## TPs de la unidad
No tiene TP propio: se estudia con [[TP16 Ciclo de instrucción básico]] y el cierre del
[[TP21 intro al emu8086]].

## Fuente de la cátedra
Apuntes **Unidad 5** (sección del 8088: memoria de control, PLA, microMAR) · `blue.pdf`
(*Unidad de control* y *Circuitos de la unidad de control*, figs. 10-11 y 19-29) ·
[[00 Matriz del final — las 3 tandas|Matriz]] (CISC/RISC, peso 10).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 5 — temas y subtemas]] ·
[[00 Unidad 7 — temas y subtemas]] · [[00 Síntesis — Unidad 6]]
