---
unidad: 3
tipo: concepto
examen: secundario
---
# ALU (Unidad Aritmética-Lógica)

> [!abstract] En una frase
> La ALU es el bloque combinacional que hace **las cuentas y las operaciones lógicas** de la CPU: recibe
> dos operandos y un **código de operación**, y entrega el resultado más los **flags** (Z, C, N, V).

## Qué operaciones hace
| Grupo | Operaciones | Hardware que la implementa |
|---|---|---|
| **Aritméticas** | suma, resta, incremento, decremento | [[Sumador completo]] / sumador-restador |
| **Lógicas** | AND, OR, XOR, NOT (complemento a 1) | [[Compuertas lógicas]] |
| **Desplazamiento** | shl (×2), shr (÷2), rotación | registro de desplazamiento / barrel shifter |
| **Comparación** | igual, mayor, menor | resta + flags |

## Estructura
```
        A (16) ──┐
                 ├──→ ┌───────────────┐
        B (16) ──┘    │     ALU       │──→ resultado (16)
                     │               │
   op (4 bits) ─────→│  selector     │──→ flags: Z C N V
                     └───────────────┘
```
- El **selector de operación** activa el camino de compuertas correspondiente (es un
  [[Multiplexor]]/decodificador interno).
- Los operandos vienen del **AC** y del **MBR** (o del bus), en BLUE.
- El resultado vuelve al **AC** (o al bus).

## Los flags (registro de estado)
| Flag | Significado | Para qué se usa |
|---|---|---|
| **Z** (zero) | el resultado fue 0 | saltos condicionales (`JZ`) |
| **C** (carry) | hubo acarreo/borrow en el bit más alto | `JC`, aritmética extendida |
| **N** (negative) | el bit de signo del resultado es 1 | comparaciones con signo |
| **V** (overflow) | desbordamiento con signo | detectar resultado inválido |

En BLUE hay un [[Flip-Flops SR, D, JK y T|flip-flop]] por flag; el `JZ` consulta Z y el `JC` consulta C
(ver [[Máquina BLUE — arquitectura y conjunto de instrucciones]]).

## Sumador-restador (microoperación aritmética)
Para restar se usa el mismo sumador: `A - B = A + (-B)` y en complemento a 2 `-B = B' + 1`.
- Se invierte B con compuertas XOR controladas por una señal `SUB`: `B ⊕ SUB`.
- Se inyecta `SUB` como acarreo de entrada: si SUB = 1, el sumador hace `A + B' + 1 = A - B`.
⇒ **Un solo circuito suma y resta**, con una señal de control. Esa es la microoperación `A ← A ± B`.

## Incrementador
`A + 1` es un sumador con una entrada fija en 1; se usa para el **PC** (`PC ← PC + 1`) y para los
[[Contadores]]. En BLUE el incremento del PC es una microoperación del [[Ciclo de búsqueda (7 y 8 pulsos)|ciclo de búsqueda]].

## Microoperaciones lógicas y de desplazamiento
- Lógicas: se aplican bit a bit (no hay acarreo). El complemento a 1 es `A ← A'`.
- Desplazamiento: `shl` multiplica por 2 (entra 0 por la derecha), `shr` divide por 2 (entra 0 por la
  izquierda); el desplazamiento **aritmético** conserva el bit de signo; la **rotación** reinyecta el bit
  que sale. El hardware es el [[Registros|registro de desplazamiento]] o un *barrel shifter* (desplaza n
  bits en un paso, con MUX en cascada).

> [!tip] Instrucciones MMX / SIMD
> Conjuntos como MMX/SSE empaquetan varios datos chicos en un registro ancho (p. ej. 4 bytes en 32 bits) y
> la ALU hace la misma operación sobre todos a la vez: es **paralelismo de datos (SIMD)**, la misma idea del
> [[Paralelismo y procesamiento vectorial|procesamiento vectorial]].

## Cómo responderlo en el final
1. Definir ALU y su lugar (dentro de la CPU, alimentada por registros/bus).
2. Enumerar los grupos de operaciones y con qué hardware se hacen.
3. Explicar cómo se resta con el mismo sumador (complemento a 2 + SUB).
4. Describir los flags y su uso en saltos condicionales.
5. Cerrar: la ALU no decide; la [[Unidad de Control]] le dice qué operación hacer.

## Errores típicos
- Decir que la ALU guarda resultados: los guarda el AC/registro; la ALU es combinacional.
- Confundir acarreo (C) con desbordamiento (V): C es para sin signo, V para con signo.
- Olvidar que las operaciones lógicas **no** generan acarreo.

## Relacionado
[[Sumador completo]] · [[Unidad de Control]] · [[Registros de la CPU]] · [[Hardware aritmético (resumen)]]
