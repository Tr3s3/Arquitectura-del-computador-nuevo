---
tipo: indice
unidad: 6
tema: "6.1"
---
# Tema 6.1 — Control cableado

> [!abstract] Qué se estudia acá
> La UC hecha **con compuertas**: los biestables de estado, la cadena de retardos que fabrica los 8 pulsos, el
> decodificador del opcode y las compuertas que arman **cada señal** con la fórmula `estado · pulso · instrucción`.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **6.1.1** Circuito, compuertas y señales | el esquema completo: estado, reloj, decodificador y las familias `REF`/`ARITH`/`DTA` | [[6.1.1 Circuito, compuertas y señales]] |

> [!important] Lo que hay que poder dibujar de memoria
> ```
> IR(4) ─► 1→16 ─┐
> FF STATE      ├─► AND (estado · pulso · instrucción) ─► OR ─► señales
> FF RUN/TRA    │
> reloj CP1..CP8 ┘
> ```

> [!note] Relación con la Unidad 4
> En [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]] está la **fórmula**; acá está el **circuito** con el
> que se construye: los biestables, el reloj y el cableado de las compuertas.

## Relacionado
[[00 Unidad 6 — temas y subtemas]] · [[00 Tema 6.2 — índice]] · [[00 Tema 4.4 — índice]] ·
[[Cómo se implementa la Unidad de Control]]
