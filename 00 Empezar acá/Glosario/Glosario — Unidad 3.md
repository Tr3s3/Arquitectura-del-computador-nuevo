---
tipo: glosario
unidad: 3
---
# Glosario — Unidad 3: transferencia de registros y microoperaciones

> [!abstract] Qué hay acá
> Las **12 fichas** de la unidad: cómo se describe el movimiento de datos dentro de la CPU (notación, bus, buffers),
> qué es la ALU y qué son los registros. Índice alfabético en [[Glosario]].

### Transferencia entre registros (RTL)
**Qué es.** Notación que describe **qué registro copia a cuál** en un pulso: `R1 ← R2` (o `R2out, R1in`).
**Para qué sirve.** Es el idioma con el que la cátedra pide describir el ciclo de una instrucción: cada pulso = una
transferencia.
**Características.** · Se lee de derecha a izquierda: el origen primero · todas las transferencias de un pulso
ocurren **simultáneamente** · una operación de la ALU se escribe `R3 ← R1 + R2`.
**Se estudia en** [[3.1.1 Notación de transferencia entre registros]].

### Microoperación
**Qué es.** Operación **elemental** que se hace en **un** pulso de reloj: mover un dato, incrementar un registro,
sumar dos registros.
**Para qué sirve.** Descomponer una instrucción en los pasos mínimos que el hardware puede ejecutar.
**Características.** · Es **indivisible**: no se puede hacer media microoperación · se clasifican en de
transferencia, aritméticas, lógicas y de control · una instrucción = varias microoperaciones en secuencia.
**Se estudia en** [[3.1.1 Notación de transferencia entre registros]].

### Bus único
**Qué es.** Un solo conjunto de líneas que **todos** los registros comparten para mover datos.
**Para qué sirve.** Ahorrar cables: la BLUE lo usa y por eso necesita **8 pulsos** por ciclo.
**Características.** · **Una** transferencia por pulso · sólo un registro puede **escribir** a la vez, varios pueden
leer · cada registro necesita una señal `out` y una `in`.
**Se estudia en** [[3.1.2 Bus único y buffers de 3 estados]].

### Buffer de tres estados
**Qué es.** Amplificador cuya salida puede ser `0`, `1` o **alta impedancia** (`Z`): desconectado.
**Para qué sirve.** Permitir que **muchos** registros cuelguen del mismo bus sin cortocircuitarse.
**Características.** · Se habilita con una señal (`R1out = 1`) · si dos escriben a la vez hay **conflicto de bus** ·
`Z` no es 0 ni 1: es "no existo" para el circuito.
**Se estudia en** [[3.1.2 Bus único y buffers de 3 estados]].

### Buses de datos, de direcciones y de control
**Qué es.** Los tres grupos de líneas que conectan la CPU con memoria y periféricos.
**Para qué sirve.** Separar **qué** viaja (dato), **a dónde** (dirección) y **cuándo/cómo** (control).
**Características.** · **Direcciones**: unidireccional, define la capacidad (`n` líneas ⇒ `2ⁿ` posiciones) ·
**datos**: bidireccional, define el ancho de palabra · **control**: señales de lectura/escritura, reloj,
interrupciones · son **externos** al chip; el interno es el que une registros dentro de la CPU.
**Se estudia en** [[3.1.3 Buses de datos, de direcciones y de control]].

### ALU
**Qué es.** Unidad aritmético-lógica: recibe dos operandos y una **selección** de operación, y devuelve el resultado
más las banderas.
**Para qué sirve.** Es donde se hacen las cuentas y las operaciones lógicas: el corazón del camino de datos.
**Características.** · Entradas `A`, `B` y `Sel`; salidas `G` (resultado), `G`/`P` (genera/propaga) y las banderas ·
la selección es un código que elige entre suma, resta, AND, OR, XOR, NOT, desplazamientos · internamente es un
**MUX** de funciones sobre un sumador.
**Se estudia en** [[3.2.1 Estructura, G-P y señales de selección]].

### Banderas (Z, C, V, N)
**Qué es.** Bits de estado que la ALU actualiza en cada operación: **Z** cero, **C** acarreo, **V** desborde con
signo, **N** negativo.
**Para qué sirve.** Que el programa **decida**: un salto condicional mira las banderas (`JZ`, `JC`, `JN`).
**Características.** · `Z = 1` si el resultado es todo 0 · `C` = acarreo de salida · `V = Cin ⊕ Cout` del bit de
signo · `N` = el bit más significativo · **C y V no son lo mismo**: uno es aritmético sin signo, el otro con signo.
**Se estudia en** [[3.2.2 Operaciones aritméticas, lógicas y flags]].

### Registros de la CPU (AC, PC, IR, MAR, MBR)
**Qué es.** Las "cajas" donde la CPU guarda lo que está usando: acumulador, contador de programa, registro de
instrucción, registro de dirección y buffer de memoria.
**Para qué sirve.** Cada uno cumple un papel fijo en el ciclo de instrucción: el `PC` dice qué sigue, el `MAR` a
dónde ir, el `MBR` qué llegó, el `IR` qué se ejecuta y el `AC` el resultado.
**Características.** · `PC` y `MAR` tienen el ancho de la **dirección**; `MBR`, `IR` y `AC` el de la **palabra** ·
sin `MAR` ni `MBR` no hay forma de hablar con la memoria · son la memoria **más rápida** de la jerarquía.
**Se estudia en** [[3.3.1 AC, PC, IR, MAR y MBR]].

### Base, índice, puntero de pila y estado
**Qué es.** Registros auxiliares: **base** (dirección de un bloque), **índice** (desplazamiento dentro de él),
**SP** (tope de la pila) y **registro de estado** (banderas).
**Para qué sirve.** Que el programa recorra estructuras y llame subrutinas **sin recalcular** direcciones.
**Características.** · Base + índice = dirección efectiva en un solo cálculo · `SP` crece o decrece con `PUSH`/`POP`
· el registro de estado se guarda y restaura en las interrupciones.
**Se estudia en** [[3.3.2 Base, índice, puntero de pila y estado]].

### Camino de datos (datapath)
**Qué es.** El conjunto de registros, bus y ALU por donde **circulan** los datos, más el cableado que los une.
**Para qué sirve.** Separar en el diseño dos cosas: el **camino de datos** (qué se puede mover) y el **control**
(qué se mueve en cada pulso).
**Características.** · Es hardware **fijo**; lo que cambia es qué señales están activas · su ancho define el tamaño
de palabra · sobre el mismo camino se ejecutan todas las instrucciones.
**Se estudia en** [[3.2.1 Estructura, G-P y señales de selección]].

### Habilitación (enable) y reloj
**Qué es.** La señal `enable` (o `LOAD`) permite que un registro **tome** el dato del bus sólo en un pulso
determinado; el `CLK` marca **cuándo**.
**Para qué sirve.** Que un registro del bus no se cargue con cualquier cosa: sólo cuando corresponde.
**Características.** · `Q⁺ = E·D + E'·Q` · sin `enable` el registro **mantiene** · el reloj es común a todos los
registros de la máquina.
**Se estudia en** [[3.3.1 AC, PC, IR, MAR y MBR]].

### Ancho de palabra y de dirección
**Qué es.** Cuántos bits tiene **un dato** (palabra) y cuántos tiene **una dirección**.
**Para qué sirve.** Dimensionar la memoria, el `MAR`, el bus de datos y los registros.
**Características.** · Ancho de dirección ⇒ `2ⁿ` posiciones · ancho de palabra ⇒ precisión de los datos ·
pueden ser distintos (la BLUE: 12 de dirección y 16 de dato).
**Se estudia en** [[3.1.3 Buses de datos, de direcciones y de control]].
