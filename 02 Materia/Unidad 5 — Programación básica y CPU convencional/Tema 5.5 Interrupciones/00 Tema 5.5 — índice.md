---
tipo: indice
unidad: 5
tema: "5.5"
---
# Tema 5.5 — Interrupciones

> [!abstract] Qué se estudia acá
> Cómo un periférico **avisa** que necesita atención sin que la CPU esté preguntando todo el tiempo: la señal
> **`IRQ · SI · CP8`**, el **polling** del flag, la **máscara**, la **pila** para guardar el contexto y la vuelta con
> **`RTI`**.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **5.5.1** IRQ·SI·CP8 y polling del flag | cómo entra una interrupción | [[5.5.1 IRQ, SI y CP8]] |
| **5.5.2** Máscara, pila y RTI | cómo se atiende sin perder nada | [[5.5.2 Máscara, pila y RTI]] |

> [!important] La diferencia con la E/S por consulta
> **Consulta (polling):** la CPU **pregunta** en un lazo (`INP` con `TRA` repitiéndose). **Interrupción:** el
> periférico **avisa**. La primera desperdicia tiempo; la segunda lo aprovecha.

## Relacionado
[[00 Unidad 5 — temas y subtemas]] · [[00 Tema 5.4 — índice]] · [[00 Tema 5.6 — índice]] ·
[[Interrupciones y entrada-salida]]
