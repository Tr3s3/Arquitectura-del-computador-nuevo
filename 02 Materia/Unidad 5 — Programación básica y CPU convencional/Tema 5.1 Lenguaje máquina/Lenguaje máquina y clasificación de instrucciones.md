---
unidad: 5
tipo: concepto
examen: secundario
prioridad: alta
---
# Lenguaje máquina y clasificación de instrucciones

> [!abstract] En una frase
> El **lenguaje máquina** es el conjunto de instrucciones en binario que el procesador interpreta directamente; cada instrucción pertenece a uno de **cinco grupos**: transferencia de datos, aritméticas, lógicas, de control y de entrada/salida.

## Definición (la del TP20, que conviene decir así)
> "Es el sistema de códigos interpretable directamente por el circuito del procesador. Se compone de un conjunto de instrucciones que determinan las acciones de la máquina, y un programa es una **cadena de esas instrucciones** más los datos. Las instrucciones son **exclusivamente ceros y unos** y son **específicas de cada arquitectura**."

Se ejecutan **en secuencia**, con cambios de flujo por el propio programa (saltos) o por **eventos externos** (interrupciones).

## Niveles de lenguaje (para ubicar el tema)
```
lenguaje de alto nivel      C, Python
        ↓ (compilador)
lenguaje ensamblador        LDA 25h        ← mnemónicos, uno a uno
        ↓ (ensamblador)
lenguaje máquina            0000 0010 0101 ← lo único que ejecuta el hardware
```

## Clasificación de las instrucciones (con ejemplos)

| Grupo | Función | Ejemplos | En BLUE |
|---|---|---|---|
| **Transferencia de datos** | mover datos entre memoria, registros y E/S | `LOAD`, `STORE`, `MOV` | `LDA`, `STA` |
| **Aritméticas** | operar con la ALU | `ADD`, `SUB`, `INC`, `DEC` | `ADD`, `SUB` |
| **Lógicas** | operar bit a bit | `AND`, `OR`, `XOR`, `NOT`, `SHL`, `SHR` | `AND`, `OR`, `XOR`, `NOT` |
| **De control** | cambiar el flujo del programa | `JUMP`, `BRANCH`, `CALL`, `RET`, condicionales | `JMP`, `JZ`, `JC` |
| **De E/S** | comunicarse con periféricos | `IN`, `OUT` | `IN`, `OUT` |
| **(de sistema)** | control de la máquina | `HLT`, `NOP`, `PUSH`/`POP`, instrucciones de interrupción | `HLT`, `NOP` |

> [!tip] Por qué esta clasificación importa
> Porque cada grupo usa **hardware distinto**: transferencia → buses y memoria; aritméticas/lógicas → la **ALU** y los **flags**; control → el **PC**; E/S → los **puertos**. Si en el oral te piden "qué componente actúa", la respuesta sale de esta tabla.

## Formato de la instrucción (lo que se pide en el TP20)
Una instrucción es `opcode` (qué hacer) + operandos (con qué). En una máquina de 16 bits con registros:
```
 ┌────────┬───────────┬─────────────────┐
 │ opcode │  registro │    dirección    │
 └────────┴───────────┴─────────────────┘
```
En BLUE (sin registros de propósito general) es `opcode (4) + dirección (12)`. Ver [[Formato de la instrucción (4 formatos)]] y [[Espacio de direccionamiento y cálculo de CodOp-Dirección]].

## Ejemplo de programa y su explicación (lo que pide el TP20)
```
 156C   ; cargar el registro 5 con el contenido de la celda 6C
 166D   ; cargar el registro 6 con la celda 6D
 5056   ; sumar los registros 5 y 6 → registro 0
 306E   ; guardar el registro 0 en la celda 6E
 C000   ; parar
```
**Explicación:** el **PC** apunta a la primera instrucción; la UC la busca (`PC→MAR→memoria→MBR→IR`) y la decodifica; se ejecuta con los **registros** como operandos y la **ALU** en la suma; el PC se incrementa y se repite. Al final el resultado queda en la celda 6E.

## RISC vs CISC (resumen; el desarrollo está en su nota)

- **CISC**: instrucciones complejas, de longitud variable, operan sobre memoria; compilador simple, código corto; pero varios ciclos por instrucción y pipeline difícil.

- **RISC**: instrucciones simples de longitud fija, **load/store**, muchos registros; pipeline natural y rápida, pero más instrucciones por programa y necesita caché grande. Ver [[CISC y RISC]] para la tabla completa.

## Cómo responderlo en el final

1. Definir lenguaje máquina (binario, específico de la arquitectura, programa = cadena de instrucciones).

2. Ubicarlo en la jerarquía de lenguajes (alto nivel → ensamblador → máquina).

3. Clasificar las instrucciones en los cinco grupos con 2–3 ejemplos de cada uno.

4. Mostrar el formato de una instrucción de la máquina que te toque (opcode + operandos).

5. Ejemplificar con un programa corto y explicar el ciclo de cada instrucción.

## Errores típicos

- Decir que el lenguaje máquina es "el ensamblador" (el ensamblador es simbólico; el máquina es binario).

- Clasificar `JZ` como aritmética (es **de control**, aunque use un flag que dejó la ALU).

- Olvidar el grupo de **E/S**.

- Mezclar la clasificación de instrucciones con los **modos de direccionamiento** (son dos ejes distintos).

## Relacionado
[[TP20 Lenguaje máquina]] · [[CISC y RISC]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Modos de direccionamiento]]
