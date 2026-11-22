---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# Formato de la instrucción (los 4 formatos)

> [!abstract] En una frase
> El **formato** es cómo se reparten los bits de una instrucción entre el `opcode` y sus **direcciones**
> (operandos y resultado). Hay cuatro formatos clásicos —**4, 3, 2 y 1 dirección**— y son un compromiso:
> más direcciones = instrucción más larga pero menos instrucciones por programa; menos direcciones =
> instrucción corta pero más instrucciones y un registro implícito (el acumulador).

## Los cuatro formatos
![formatos_instruccion](assets/formatos_instruccion.svg)

| Formato | Campos | Operación típica | Comentario |
|---|---|---|---|
| **4 direcciones** | `OP A1 A2 A3 A4` | `A1 ← A2 OP A3`, luego salta a `A4` | no toca el PC: no hay instrucción de salto separada. Instrucción larguísima |
| **3 direcciones** | `OP A1 A2 A3` | `A1 ← A2 OP A3` | el más "legible"; base de las máquinas **RISC** |
| **2 direcciones** | `OP A1 A2` | `A1 ← A1 OP A2` | **destruye** A1; típico de **CISC** (x86: `add eax, ebx`) |
| **1 dirección** | `OP A1` | `AC ← AC OP A1` | **acumulador implícito**; es el de **BLUE** |

## Cómo se lee cada uno con un ejemplo
Calcular `X = A + B` (con A, B y X en memoria):

**4 direcciones**
```
ADD  X, A, B, prox    ; M[X] ← M[A] + M[B] ; PC ← prox
```
1 instrucción, pero 4 direcciones en el código ⇒ 4 lecturas de memoria + 1 escritura.

**3 direcciones**
```
ADD  X, A, B          ; M[X] ← M[A] + M[B]
```

**2 direcciones**
```
MOV  X, A             ; M[X] ← M[A]
ADD  X, B             ; M[X] ← M[X] + M[B]
```
2 instrucciones; la primera deja el dato en X y la ADD lo destruye.

**1 dirección (acumulador)**
```
LDA  A                ; AC ← M[A]
ADD  B                ; AC ← AC + M[B]
STA  X                ; M[X] ← AC
```
3 instrucciones. **Más instrucciones, pero más cortas** ⇒ el programa completo ocupa similar y la CPU es
más simple (un solo registro).

## El compromiso (lo que se pregunta)
| | 4 dir. | 3 dir. | 2 dir. | 1 dir. |
|---|---|---|---|---|
| Largo de la instrucción | mayor | medio | menor | mínimo |
| Cantidad de instrucciones por programa | menor | menor | media | **mayor** |
| Bits totales del programa | alto | medio | bajo | bajo |
| Complejidad de la CPU | alta | media | media | **baja** (1 registro, el AC) |
| Ejemplo real | máquinas antiguas | ARM, MIPS, RISC-V | x86 | BLUE, 8085, primeros micros |

> [!tip] La regla de oro
> Leer y escribir memoria es caro (lento) y codificar direcciones ocupa bits. Los dos extremos son:
> **muchas direcciones** (instrucción larga, pocas instrucciones) o **pocas direcciones** (instrucción corta,
> muchas instrucciones + registro implícito). La solución moderna: **3 direcciones con registros** y sólo
> `LOAD`/`STORE` para tocar memoria (ver [[CISC y RISC]]).

## Formato de la instrucción en BLUE
BLUE es de **1 dirección (acumulador)** con 16 bits:
```
  ┌────────┬──────────────────────────┐
  │ opcode │  dirección (operando)    │
  │ 4 bits │      12 bits             │
  └────────┴──────────────────────────┘
```
- El **resultado siempre va al AC** (implícito).
- La **dirección** apunta al operando en memoria (o es el destino del salto).
- En la versión **indexada** el formato cambia a `opcode (5) | dirección (16) | modificador (2)`
  (ver [[BLUE indexada (RIF, RID, nuevo formato)]]).

## Cómo responderlo en el final (pregunta principal #2)
1. Definir formato de instrucción = reparto de bits entre opcode y direcciones.
2. Dibujar los cuatro formatos con sus campos.
3. Mostrar el mismo cálculo (`X = A + B`) en los cuatro, contando instrucciones.
4. Explicar el compromiso (largo de instrucción vs cantidad de instrucciones vs complejidad de la CPU).
5. Aterrizar en BLUE: `4 + 12` bits, formato de **una dirección con acumulador implícito**.

## Errores típicos
- Decir que el formato de 1 dirección "no tiene operandos": tiene **uno**, el otro es implícito (el AC).
- Confundir formato (cuántas direcciones) con modo de direccionamiento (cómo se calcula la dirección).
- Olvidar el formato de 4 direcciones (es el que justifica la existencia de las instrucciones de salto).
- Decir que 2 direcciones "no destruye operandos": sí los destruye (`A1 ← A1 OP A2`).

## Relacionado
[[Modos de direccionamiento]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[CISC y RISC]] · [[BLUE indexada (RIF, RID, nuevo formato)]]
