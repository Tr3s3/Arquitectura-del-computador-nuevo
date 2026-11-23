---
tipo: indice
unidad: 3
tema: "3.1"
---
# Tema 3.1 — Microoperaciones y bus

> [!abstract] Qué se estudia acá
> El **idioma** con el que se describe lo que hace la máquina pulso por pulso: la **notación de transferencia entre registros** (RTL), y el medio físico por el que circulan los datos: el **bus** con sus **buffers de tres estados**. Es la base para leer el ciclo de instrucción de cualquier máquina.

| Subtema | Qué resuelve | Nota |
|---|---|---|
| **3.1.1** Notación de transferencia entre registros | escribir `MAR ← PC` y saber qué significa cada símbolo | [[3.1.1 Notación de transferencia entre registros]] |
| **3.1.2** Bus único y buffers de 3 estados | por qué hay **una sola** transferencia por pulso | [[3.1.2 Bus único y buffers de 3 estados]] |
| **3.1.3** Buses de datos, de direcciones y de control | qué lleva cada bus y de qué tamaño es | [[3.1.3 Buses de datos, de direcciones y de control]] |

> [!important] La regla de oro de la unidad
> Con **un solo bus**, en cada pulso se puede hacer **una** transferencia. Todo lo demás (sumar un 1 al PC, traer un dato y sumarlo) son **varias** microoperaciones, es decir, varios pulsos.

## TPs y práctica
[[TP14 Buses]] · (apoyo) [[TP13 Componentes internos]]

## Relacionado
[[00 Unidad 3 — temas y subtemas]] · [[00 Tema 3.2 — índice]] · [[Flujo de información en BLUE (datos y direcciones)]]
