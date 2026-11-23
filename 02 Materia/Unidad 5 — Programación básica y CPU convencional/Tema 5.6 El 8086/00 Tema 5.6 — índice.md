---
tipo: indice
unidad: 5
tema: "5.6"
---
# Tema 5.6 — El 8086

> [!abstract] Qué se estudia acá
> El primer microprocesador de 16 bits de Intel como **caso real** de la Unidad 5: la **segmentación** de 20 bits, la división **BIU / EU** que permite buscar la próxima instrucción mientras se ejecuta la actual (la semilla del *pipeline*), y los **modos de direccionamiento** concretos.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **5.6.1** BIU, EU y segmentación | cómo 16 bits direccionan 1 MB | [[5.6.1 BIU, EU y segmentación]] |
| **5.6.2** La pila y el registro SP | `PUSH`/`POP`, `CALL`/`RET` en el 8086 | [[5.6.2 La pila y el registro SP]] |

> [!important] Lo que hay que poder decir de memoria
> **20 bits = segmento × 16 + desplazamiento** (`CS:IP`, `DS:SI`, `SS:SP`, `ES:DI`). Segmento de 64 KB. La **BIU** trae las instrucciones a la **cola** de 6 bytes; la **EU** las ejecuta.

## Relacionado
[[00 Unidad 5 — temas y subtemas]] · [[00 Tema 5.5 — índice]] · [[TP21 intro al emu8086]] · [[5.5.2 Máscara, pila y RTI]]
