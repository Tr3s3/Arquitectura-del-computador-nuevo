---
tipo: indice
unidad: 5
tema: "5.4"
---
# Tema 5.4 — La BLUE indexada

> [!abstract] Qué estudia
> La evolución de la BLUE: se le agregan **RIF** (índice de fuente), **RID** (índice de destino), **RB** (base), un **sumador de direcciones** y un **modificador de 2 bits**. Con eso aparecen los modos indexados… a cambio de **24 pulsos** por instrucción.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **5.4.1** RIF, RID y RB | qué suma cada registro a la dirección | [[5.4.1 RIF, RID y RB]] |
| **5.4.2** Modificador de 2 bits y los 24 pulsos | el formato nuevo y el costo en tiempo | [[5.4.2 Modificador de 2 bits y los 24 pulsos]] |

> [!important] La fórmula
> `EA = RB + campo [+ RIF o RID]`. El **base** se suma **siempre**; los índices, **sólo si la instrucción lo pide**.

## Relacionado
[[00 Unidad 5 — temas y subtemas]] · [[00 Tema 5.3 — índice]] · [[00 Tema 5.5 — índice]] · [[BLUE indexada (RIF, RID, nuevo formato)]]
