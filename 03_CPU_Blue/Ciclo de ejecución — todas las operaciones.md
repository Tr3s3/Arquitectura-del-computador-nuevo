---
unidad: 4
tipo: concepto
examen: secundario
prioridad: maxima
---
# Ciclo de ejecución — todas las operaciones

> [!abstract] En una frase
> Terminada la búsqueda, el **opcode del IR** decide qué microoperaciones se hacen. Las instrucciones se
> agrupan en cuatro familias —**transferencia con memoria, operaciones de ALU, control de flujo y E/S**— y
> cada familia tiene su secuencia característica.

## Esquema general
```
búsqueda (fija, 8 pulsos) → decodificación → ejecución (según opcode) → STATE ← F
```

## Familia 1 — Transferencia de datos: LDA y STA
**LDA D** (`AC ← M[D]`)
| Paso | Microoperación | Señales |
|---|---|---|
| 1 | `MAR ← IR(dirección)` | `IRout`, `MARin` |
| 2 | `MEMR = 1` | `MEMR` |
| 3 | `MBR ← M[MAR]` | `MBRload` |
| 4 | `AC ← MBR` | `MBRout`, `ACin` |
| 5 | actualizar flags (Z, C) | `load flags` |
| 6 | `STATE ← F` | `STATE` |

**STA D** (`M[D] ← AC`)
| Paso | Microoperación | Señales |
|---|---|---|
| 1 | `MAR ← IR(dirección)` | `IRout`, `MARin` |
| 2 | `MBR ← AC` | `ACout`, `MBRload` |
| 3 | `MEMW = 1` | `MEMW` |
| 4 | `M[MAR] ← MBR` | — (lo hace la memoria) |
| 5 | `STATE ← F` | `STATE` |

> [!tip] La diferencia clave
> En `LDA` el dato va **memoria → MBR → AC**; en `STA` va **AC → MBR → memoria**. El MBR siempre mira al
> bus de datos: es el "despachante" de la memoria.

## Familia 2 — Operaciones de la ALU: ADD, SUB, AND, OR, XOR
Todas siguen el mismo esqueleto de `LDA` pero con un paso extra: **operar**.

| Paso | Microoperación | Señales |
|---|---|---|
| 1 | `MAR ← IR(dirección)` | `IRout`, `MARin` |
| 2 | `MEMR = 1` | `MEMR` |
| 3 | `MBR ← M[MAR]` | `MBRload` |
| 4 | `AC ← AC op MBR` | `ACout`, `MBRout`, `ALUop`, `ACin` |
| 5 | actualizar flags (Z, C) | `load flags` |
| 6 | `STATE ← F` | `STATE` |

- **ADD**: `AC ← AC + MBR` (sumador, ver [[Sumador completo]]).
- **SUB**: `AC ← AC − MBR` (el mismo sumador con `SUB = 1` y `B` negado en complemento a 2, ver [[ALU]]).
- **AND / OR / XOR**: operaciones bit a bit, **sin acarreo** ⇒ `C` no cambia (o se pone en 0).
- **NOT**: `AC ← AC'`, **no accede a memoria** (no usa el campo dirección) ⇒ ciclo mucho más corto.

## Familia 3 — Control de flujo: JMP, JZ, JC, NOP, HLT
| Instrucción | Microoperaciones | Pulsos |
|---|---|---|
| **JMP D** | `PC ← IR(dirección)` (¡la dirección es el dato!) | muy corta: no hay acceso a memoria |
| **JZ D** | `si Z = 1 → PC ← IR(dir)`; si no, nada (PC ya está en la siguiente) | depende del flag |
| **JC D** | `si C = 1 → PC ← IR(dir)` | depende del flag |
| **NOP** | no hace nada (gasta el ciclo) | — |
| **HLT** | `RUN ← 0` | termina la ejecución |

> [!important] Detalle de examen
> En los saltos **no hay ciclo de memoria**: el campo dirección del IR se lleva **directo al PC**. La
> condición se evalúa con los **flags** del registro de estado, que la ALU dejó actualizados en la
> instrucción anterior (por eso un `JZ` "mira" el resultado del `SUB` anterior).

## Familia 4 — Entrada/Salida: IN y OUT
| Instrucción | Microoperación | Comentario |
|---|---|---|
| **IN P** | `AC ← puerto P` | el campo dirección es el número de puerto |
| **OUT P** | `puerto P ← AC` | el puerto toma el dato del bus |

En la práctica son como `LDA`/`STA` pero el "destino" no es la memoria sino un registro de puerto
(ver [[Interrupciones y entrada-salida]]).

## Cuadro resumen
| Familia | Instrucciones | ¿Accede a memoria? | ¿Usa la ALU? | Efecto |
|---|---|---|---|---|
| Transferencia | LDA, STA | sí (1 acceso) | no | mueve datos |
| ALU | ADD, SUB, AND, OR, XOR | sí (1 acceso) | **sí** | transforma el AC |
| ALU sin memoria | NOT | no | sí | complementa el AC |
| Control | JMP, JZ, JC | no | no | cambia el PC |
| Control | NOP, HLT | no | no | gasta ciclo / detiene |
| E/S | IN, OUT | no (usa puerto) | no | comunica |

> [!warning] Sobre la cantidad de pulsos
> El número exacto de pulsos por instrucción depende de cómo se cuente cada microoperación (1 o 2 pulsos por
> transferencia: fase de habilitar la fuente y fase de cargar el destino). En esta bóveda se usa el criterio
> de [[Ciclo de la instrucción LDA (24 pulsos)]]: **2 pulsos por microoperación**, con lo que `LDA` totaliza
> 24. Si tu apunte cuenta 1 pulso por microoperación, los totales se reducen a la mitad: **la secuencia es
> la misma**, cambia el conteo. Decilo así en el final y no hay forma de que te lo tomen mal.

> [!example] Ejercicio de la cátedra (TP16)
> El [[TP16 Ciclo de instrucción básico|TP16]] da un programa de 3 instrucciones (`1 650`, `5 651`, `2 652`)
> y pide describir **los 6 pasos** en cada una. Ese ejercicio es la mejor forma de practicar esta nota:
> búsqueda → decodificación → operando → ejecución → escritura → próxima instrucción.

## Cómo responderlo en el final
1. Explicar que la ejecución depende del opcode y agrupar las 16 instrucciones en las 4 familias.
2. Desarrollar `LDA` y `STA` completos (son las que se piden siempre).
3. Mostrar `ADD` como representante de la familia ALU (con `ALUop` y flags).
4. Mostrar `JMP` y `JZ` remarcando que la dirección va al PC y la condición sale de los flags.
5. Cerrar con el cuadro resumen y la aclaración del conteo de pulsos.

## Errores típicos
- Meter un acceso a memoria en un salto (no lo hay).
- Olvidar `load flags` después de una operación de ALU (entonces `JZ` no funciona).
- Confundir en `STA` el orden: **primero** el dato al MBR, **después** `MEMW`.
- Decir que `NOT` y `NOP` usan el campo dirección.

## Relacionado
[[Ciclo de la instrucción LDA (24 pulsos)]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[BLUE indexada (RIF, RID, nuevo formato)]]
