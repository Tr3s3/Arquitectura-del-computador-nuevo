---
tipo: indice
unidad: 6
---
# Unidad 6 — Control microprogramado

> [!abstract] Qué pide la unidad
> Cómo se construye la **Unidad de Control**: con **compuertas (cableada)** o con un **microprograma guardado en
> una ROM (microprogramada)**. La BLUE usa cableada; el 8088, microprogramada con una ROM de **504 × 21 bits**.

| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **6.1 Control cableado** | lógica combinacional · señales `estado·pulso·instrucción` · rápido pero rígido | [[Unidad de control cableada y microprogramada]] · [[Cómo se implementa la Unidad de Control]] · carpeta `Tanda 1/1.6` y su `Apoyo a la pregunta/` |
| **6.2 Control microprogramado** | memoria de control (**ROM**) · microinstrucción y sus campos · microprograma · secuenciamiento (microPC) · PLA vs ROM | [[Unidad de control cableada y microprogramada]] · [[Cómo se implementa la Unidad de Control]] |
| **6.3 Comparación** | velocidad · flexibilidad · costo · relación con **CISC y RISC** | [[CISC y RISC]] · carpeta `Tanda 2/2.6` |
| **6.4 El caso real** | el 8088: ROM de control 504×21 · ~90 microprocedimientos · microinstrucción de 5+5+3+4+3+1 | [[El 8086 como CPU convencional (TP21)]] · [[Cómo se implementa la Unidad de Control]] |

---

## Qué hay que saber hacer al terminar la unidad
1. **Dibujar** el esquema de una UC cableada: decodificador de opcode + FF de estado + compuertas OR.
2. **Escribir** una microinstrucción con sus campos y explicar para qué sirve cada uno.
3. Decir **cuándo conviene** cada tipo (complejo y cambiante → microprogramado; simple y rápido → cableado).
4. Relacionarlo con **CISC (microprogramado) y RISC (cableado)**.

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
[[00 Unidad 7 — temas y subtemas]]
