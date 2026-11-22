---
unidad: 7
tipo: concepto
examen: secundario
prioridad: alta
---
# CISC y RISC

> [!note] Si es la primera vez que ves esto
> Hay dos filosofías para diseñar el repertorio de instrucciones de una CPU. **CISC**: "que la instrucción
> haga mucho" (pocas instrucciones, complejas, largas, con control microprogramado). **RISC**: "que la
> instrucción haga poquito pero rapidísimo" (muchas instrucciones simples, todas del mismo tamaño, control
> cableado, pipeline). Es la diferencia entre un **cuchillo multiuso** y un juego de **cuchillos
> especializados**: el multiuso hace de todo con un solo objeto, el juego es más rápido si sabés cuál usar.
> Las CPUs actuales son híbridas: por fuera hablan CISC (x86), por dentro trabajan RISC.

> [!abstract] En una frase
> **CISC** (*Complex Instruction Set Computer*) apuesta a **pocas instrucciones complejas** que hagan mucho
> trabajo (x86); **RISC** (*Reduced Instruction Set Computer*) apuesta a **muchas instrucciones simples y
> rápidas**, de formato fijo, que se ejecutan en un ciclo y se pipelines sin problemas (ARM, MIPS, RISC-V).

## Por qué existen dos filosofías
En los 70 la memoria era carísima: convenía que **cada instrucción hiciera mucho** (CISC) para ocupar
pocos bytes. Cuando la memoria se abarató y las compiladoras mejoraron, se vio que las instrucciones
complejas casi no se usaban y que era mejor **hardware simple y rápido** (RISC).

## Tabla comparativa (la respuesta de examen)
| Característica | **CISC** | **RISC** |
|---|---|---|
| Conjunto de instrucciones | grande (100–500), complejas, de longitud variable | chico (30–100), simples, de **longitud fija** |
| Formato | variable y muchos modos de direccionamiento | **pocos formatos fijos** y pocos modos |
| Acceso a memoria | las operaciones pueden operar **directo sobre memoria** | sólo `LOAD`/`STORE` (**arquitectura load/store**) |
| Registros | pocos, especializados | **muchos registros de propósito general** |
| Ciclos por instrucción | variable (muchos) | ≈ 1 (ideal), muy pipelineables |
| Unidad de control | **microprogramada** (el microcódigo traduce la instrucción compleja) | **cableada** (hardware dedicado, más rápido) |
| Pipeline | difícil (instrucciones desparejas) | natural (etapas balanceadas) |
| Programa en memoria | **más chico** (menos instrucciones) | más grande (más instrucciones, pero cada una más corta) |
| Consumo / complejidad | mayor complejidad de decodificación | menor consumo, diseño más simple |
| Ejemplos | x86 (Intel/AMD), 8088/8086, VAX | ARM, MIPS, SPARC, RISC-V, PowerPC |

## Arquitectura de carga/almacenamiento (load/store)
Es la regla de oro de RISC: **las operaciones aritméticas sólo trabajan entre registros**. Para operar con
un dato de memoria hay que traerlo con `LOAD`, operar y devolverlo con `STORE`.
```
RISC:  LOAD  R1, [x]      ; R1 ← M[x]
       LOAD  R2, [y]      ; R2 ← M[y]
       ADD   R3, R1, R2   ; R3 ← R1 + R2   (registros, formato de 3 direcciones)
       STORE R3, [z]      ; M[z] ← R3
```
Ventaja: el pipeline no se complica y el compilador puede optimizar el uso de registros.
En **BLUE**, en cambio, `ADD` opera directamente sobre memoria: eso es CISC puro.

## Unidad de control asociada
- **CISC → microprogramada**: la instrucción compleja se descompone en microinstrucciones guardadas en una
  ROM de control. Flexible (se puede corregir un microprograma) pero más lento.
- **RISC → cableada**: lógica combinacional que genera las señales directamente. Más rápida, pero rígida.
Ver [[Unidad de control cableada y microprogramada]].

## Máquinas híbridas (lo que existe hoy)
Los procesadores actuales **son híbridos**:
- Mantienen el **ISA CISC** (x86) por compatibilidad, pero **por dentro traducen** cada instrucción compleja
  a varias microoperaciones simples tipo RISC y las ejecutan en un núcleo **superescalar con pipeline**.
- Los ARM (RISC) agregan instrucciones complejas (SIMD, DSP) cuando conviene.
⇒ La frontera se corrió: **ISA CISC, microarquitectura RISC**.

## Ejemplos para nombrar
- **8088/8086**: CISC de 16 bits, el microprocesador "convencional" de la Unidad 5 (registros AX/BX/CX/DX,
  segmentos, modos de direccionamiento complejos).
- **ARM / RISC-V**: RISC modernos, load/store, 16–32 registros de propósito general.
- **x86 actual (Core / Ryzen)**: híbrido.

> [!example] Del TP20
> El [[TP20 Lenguaje máquina|TP20]] pide RISC y CISC con **ventajas y desventajas** (y son las que están en la
> tabla de esa nota). Si te las piden en el oral, arrancá por la tabla y cerrá con "los procesadores actuales
> son **híbridos**: ISA CISC, microarquitectura RISC".

## Cómo responderlo en el final
1. Definir las dos filosofías y el contexto histórico (memoria cara vs compiladores buenos).
2. Dar la tabla comparativa (al menos 6 filas: ISA, formato, memoria, registros, ciclos, UC).
3. Explicar load/store y el pipeline como consecuencia.
4. Nombrar ejemplos concretos de cada familia y aclarar que los actuales son **híbridos**.
5. Cerrar: la discusión no es "cuál es mejor", sino qué compromiso se elige para un objetivo.

## Errores típicos
- Decir que RISC tiene "menos instrucciones porque hace menos cosas": hace lo mismo, con más instrucciones
  simples.
- Confundir CISC/RISC (diseño del **ISA**) con pipeline/multicore (microarquitectura).
- Decir que x86 "es CISC y por eso no tiene pipeline": tiene pipeline y superescalaridad.
- Olvidar que la consecuencia principal de RISC es que **cabe en un pipeline** y la UC es cableada.

## Relacionado
[[Pipeline]] · [[Unidad de control cableada y microprogramada]] · [[Formato de la instrucción (4 formatos)]] · [[Técnicas para aumentar la velocidad]]
