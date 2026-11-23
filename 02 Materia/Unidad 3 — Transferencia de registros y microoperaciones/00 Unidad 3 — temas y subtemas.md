---
tipo: indice
unidad: 3
---
# Unidad 3 — Transferencia de registros y microoperaciones

> [!abstract] Qué pide la unidad
> Entender **cómo se mueve y se transforma un dato dentro de la CPU**: cada paso elemental es una
> **microoperación**, y todas viajan por **un bus** (con buffers de tres estados). Es la unidad que después hace
> posible entender el ciclo de instrucción.

| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **3.1 Transferencia entre registros** | bus único · buffers de 3 estados · una transferencia por pulso · `PC→MAR`, `MBR→IR` | [[Flujo de información en BLUE (datos y direcciones)]] · carpeta `Tanda 1/1.1` |
| **3.2 La ALU y sus microoperaciones** | aritméticas (suma, resta en A2, incremento) · lógicas (AND, OR, XOR, NOT) · desplazamiento y rotación | [[ALU]] · `Tema 3.1 La ALU/` |
| **3.3 Registros de la CPU** | AC, PC, IR, MAR, MBR · propósito general (base, índice, pila, estado) | [[Registros de la CPU]] · `Unidad 5/Tema 5.1` |
| **3.4 Buses** | interno vs externo · de datos, de direcciones, de control · bus común (comparación de costos) | [[Estructura básica de un computador]] · [[TP14 Buses]] · carpeta `Tanda 1/1.5` |
| **3.5 Hardware aritmético** | sumador-restador · acarreo anticipado · (se profundiza en la unidad 9) | [[Hardware aritmético (resumen)]] · `Unidad 9` |

---

## Qué hay que saber hacer al terminar la unidad
1. Escribir **microoperaciones** con notación de transferencia (`MAR ← PC`, `AC ← AC + M[X]`).
2. Explicar **por qué un bus único obliga a una transferencia por pulso**.
3. Justificar el **buffer de tres estados** (y por qué sin él todos los registros se pelearían por el cable).
4. Decir **qué hace la ALU** con G/P y con las señales de selección.

## TPs de la unidad
[[TP14 Buses]] · (apoyo: [[TP13 Componentes internos]] · [[TP5 Sumadores]])

## Fuente de la cátedra
Apuntes **Unidad 4 — Estructura básica de una computadora** · `blue.pdf` (capítulo de la máquina elemental:
bus común y flujo de información) · Hamacher (microoperaciones).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 2 — temas y subtemas]] ·
[[00 Unidad 4 — temas y subtemas]]
