---
unidad: 6
tipo: concepto
examen: secundario
prioridad: alta
---
# Unidad de control cableada y microprogramada

> [!abstract] En una frase
> Hay dos formas de construir la UC: **cableada** (lógica combinacional + secuencial que genera las señales
> directamente: rápida, rígida) y **microprogramada** (una **memoria de control** guarda "microinstrucciones"
> que dicen qué señales activar en cada pulso: flexible, más lenta). Un **microprograma** es el programa que
> ejecuta la UC para ejecutar una instrucción de máquina.

## Idea central del control microprogramado
Cada instrucción de máquina (LDA, ADD, JMP…) se **descompone** en microoperaciones. Si en lugar de cablear
esa secuencia se guarda en una **memoria de control** una palabra por microoperación, entonces:

- la **dirección** de la memoria de control indica *en qué paso* está la UC;
- el **contenido** de esa palabra (la **microinstrucción**) son las **señales de control** de ese paso.

Ventaja conceptual: **se programa el control como si fuera software** (de ahí "firmware").

## Diagrama de bloques
```
   ┌──────────────┐   opcode    ┌───────────────────┐
   │  IR (opcode) │────────────→│ lógica de mapeo   │
   └──────────────┘             │ (dirección inicial│
                                │  de la rutina)    │
                                └─────────┬─────────┘
                                          │ dirección de microinstrucción
                                          ▼
   ┌────────────────┐  señales   ┌───────────────────┐
   │ REGISTRO DE    │───────────→│ MEMORIA DE CONTROL│
   │ DIRECCIÓN (CP) │←───────────│  (ROM de µinst.)  │
   └────────────────┘  próxima   └───────────────────┘
          ▲            dirección           │
          │                                ▼ señales de control
   ┌──────┴───────┐                 (registros, ALU, buses,
   │ lógica de    │                  memoria, E/S)
   │ secuenciam.  │← flags, reloj
   └──────────────┘
```

## Secuenciamiento de la dirección (lo que se pregunta)
El **contador de microprograma** (o registro de dirección de control) avanza. Hay tres mecanismos:

1. **Incremento normal:** el siguiente paso es `dirección + 1` (secuencia lineal de microoperaciones).
2. **Transferencia condicional (salto condicional):** la próxima dirección depende de un **flag** o de una
   condición (p. ej. `si Z = 1` ir a la rutina del salto; si no, seguir). Se implementa con un
   [[Multiplexor]] en la entrada de la dirección, seleccionado por la condición.
3. **Mapeo de las instrucciones:** al comienzo del ciclo de ejecución, la **lógica de mapeo** convierte el
   **opcode** del IR en la **dirección inicial** de la rutina de microprograma de esa instrucción. Para no
   cablear mucho, se coloca el opcode en algunos bits de la dirección (por ejemplo `dirección = 1 opcode 00`).
4. **Subrutinas de microprograma:** secuencias comunes (por ejemplo la búsqueda, o el cálculo de la
   dirección efectiva) se implementan como **subrutina** y se llaman desde varias rutinas, con una **pila de
   microprograma** para el retorno. Ahorra memoria de control.

## El formato de la microinstrucción
Cada palabra de la memoria de control se divide en **campos**; cada campo controla un bloque:
```
 ┌──────────┬──────────┬──────────┬──────────┬──────────┬─────────┐
 │ campos de│ campos de│ campo de │ control  │ control  │ próxima │
 │ registros│ la ALU   │ memoria  │ de buses │ de cond. │ dirección│
 └──────────┴──────────┴──────────┴──────────┴──────────┴─────────┘
```
- **Microinstrucción horizontal:** todos los bits de control en la misma palabra (una microoperación por
  palabra) ⇒ microprograma largo pero **paralelo y rápido**.
- **Microinstrucción vertical:** pocos bits, codificados; hay que decodificar ⇒ microprograma corto pero más
  lento.

## La rutina de búsqueda microprogramada (ejemplo)
| Dirección µ | Microoperación | Señales |
|---|---|---|
| 0 | `MAR ← PC` | `PCout`, `MARin` |
| 1 | `MBR ← M[MAR]`, `PC ← PC+1` | `MEMR`, `MBRload`, `PCinc` |
| 2 | `IR ← MBR` | `MBRout`, `IRin` |
| 3 | (mapeo) salto a la rutina del opcode | usa el opcode del IR |

Ese microprograma es **idéntico** al ciclo de búsqueda de BLUE explicado en
[[Ciclo de búsqueda (7 y 8 pulsos)]]: la única diferencia es que acá cada fila es una palabra de memoria de
control.

## Cableada vs microprogramada (tabla de examen)
| | **Cableada** | **Microprogramada** |
|---|---|---|
| Implementación | compuertas + flip-flops (máquina de estados) | ROM de control + secuenciador |
| Velocidad | **más rápida** (sin acceso a memoria de control) | más lenta (un acceso por microinstrucción) |
| Flexibilidad | rígida: cambiar implica rediseñar | **flexible**: se cambia el microprograma |
| Costo | crece rápido con la complejidad del ISA | barata para ISA complejos |
| Uso típico | **RISC**, máquinas simples | **CISC** (x86), máquinas con muchas instrucciones |

## Origen y evolución (para el oral)
- **Wilkes (1951)** propone el control microprogramado como forma sistemática de diseñar la UC.
- Se populariza en los 60–70 con los CISC (IBM/360, VAX): muchísimas instrucciones ⇒ imposible cablearlas.
- Con los RISC (80s) vuelve la **cableada** (ISA simple, pipeline).
- Hoy: **híbrido** — un núcleo RISC cableado que ejecuta microoperaciones, con una etapa de traducción que
  convierte el ISA CISC en esas microoperaciones (así funcionan los x86 modernos).

## Cómo responderlo en el final
1. Definir microprograma, microinstrucción y memoria de control.
2. Dibujar el bloque (memoria de control + registro de dirección + lógica de secuenciamiento + mapeo).
3. Explicar los cuatro mecanismos de secuenciamiento (incremento, salto condicional, mapeo, subrutinas).
4. Mostrar el formato de la microinstrucción (horizontal vs vertical).
5. Comparar cableada vs microprogramada con la tabla y cerrar con la evolución (CISC↔RISC↔híbrido).

## Errores típicos
- Confundir **microprograma** (lo que hace la UC) con **programa** (lo que hace la máquina).
- Decir que la microprogramada es más rápida (es más **flexible**, no más rápida).
- Olvidar el **mapeo del opcode** (sin él, la UC no sabe dónde empieza la rutina de la instrucción).
- Confundir el registro de dirección de control con el PC (son contadores distintos).

## Relacionado
[[Unidad de Control]] · [[CISC y RISC]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Técnicas para aumentar la velocidad]]
