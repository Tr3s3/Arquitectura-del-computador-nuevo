---
tipo: glosario
unidad: 4
---
# Glosario — Unidad 4: organización y diseño básico

> [!abstract] Qué hay acá
> Las **13 fichas** de la unidad: unidades funcionales, la máquina IAS, la BLUE y su ciclo de instrucción, los pulsos y la generación de señales de control. Índice alfabético en [[Glosario]].

### Unidad funcional
**Qué es.** Cada gran bloque de una computadora: **entrada, salida, memoria, ALU y unidad de control**. **Para qué sirve.** Entender el nivel "de arriba": con cinco bloques y buses se describe cualquier computadora. **Características.** · Se conectan por buses · la **UC** manda, la **ALU** calcula, la **memoria** guarda, E/S comunica · es el esquema de von Neumann. **Se estudia en** [[4.1.1 Unidades funcionales de una computadora]].

### Programa almacenado
**Qué es.** Idea de von Neumann: las **instrucciones** se guardan en la misma memoria que los **datos**. **Para qué sirve.** Que la máquina sea **programable**: cambiar el programa es cambiar el contenido de memoria, no el cableado. **Características.** · Instrucción y dato comparten memoria y bus ⇒ **no** se pueden traer a la vez (cuello de botella) · permite compiladores y sistemas operativos · el `PC` recorre las instrucciones. **Se estudia en** [[4.1.2 IAS y el programa almacenado]].

### IAS
**Qué es.** La primera computadora con programa almacenado (von Neumann, 1945): 1000 palabras de 40 bits, `AC` y `MQ` de 40 bits, `PC`, `MAR`, `MBR`, `IR`. **Para qué sirve.** Es el **modelo histórico** de todo lo que vino después: en el final se pregunta su estructura. **Características.** · 40 bits por palabra: 20 de instrucción (8 de opcode + 12 de dirección) y 20 de dato · 1 000 palabras ⇒ 12 bits de dirección · ciclo búsqueda → decodificación → ejecución. **Se estudia en** [[4.1.2 IAS y el programa almacenado]].

### BLUE
**Qué es.** La máquina didáctica de la cátedra: **4096 palabras × 16 bits**, bus único, arquitectura de acumulador, **16 instrucciones** de una dirección. **Para qué sirve.** Sirve para **dibujar** un ciclo de instrucción completo: es lo suficientemente chica para entenderla y lo suficientemente real para tener pulsos y señales. **Características.** · Instrucción = **4 bits de opcode + 12 de dirección** · **8 pulsos de 125 ns** por ciclo de máquina (1 µs) · registros `PC`, `MAR`, `MBR`, `IR`, `AC` · `STATE` con los estados `F` (búsqueda), `E` (ejecución), `I` (interrupción). **Se estudia en** [[4.2.1 Especificación, registros y 4096x16]].

### Opcode octal
**Qué es.** El código de operación de cada instrucción de la BLUE, escrito en **octal** (`00` a `17`). **Para qué sirve.** Identificar la instrucción en el `IR` y saber cuántos pulsos tarda. **Características.** · **16 instrucciones** (4 bits) · `00 HLT`, `01 ADD`, `06 LDA`, `13 INP`, `17 NOP`… · las de **1 ciclo** no vuelven a memoria (8 pulsos) y las de **2 ciclos** sí (16 pulsos). **Se estudia en** [[4.2.2 Los 16 opcodes octales]].

### Ciclo de instrucción, de máquina y de reloj
**Qué es.** Las tres escalas de tiempo: **pulso de reloj** (125 ns) < **ciclo de máquina** (8 pulsos = 1 µs) < **ciclo de instrucción** (1 o 2 ciclos de máquina). **Para qué sirve.** Calcular tiempos: "¿cuánto tarda un programa de 10 instrucciones?" se responde con esta escala. **Características.** · 8 MHz ⇒ 8 millones de pulsos/s · cada ciclo de máquina tiene 8 **pulsos numerados** (`CP1`…`CP8`) · la instrucción con acceso a memoria agrega un ciclo de ejecución. **Se estudia en** [[4.3.1 Ciclo de reloj, de máquina y de instrucción]].

### Pulso de búsqueda (CP1 a CP8)
**Qué es.** Los ocho pulsos del ciclo de **búsqueda**: traer la instrucción de memoria al `IR`. **Para qué sirve.** Es el "ritmo" fijo que se repite con **cada** instrucción: `PC → MAR`, leer memoria, `MBR → IR`, `PC + 1`, decodificar. **Características.** · Siempre son **8** · al terminar, el `IR` tiene la instrucción y el `PC` apunta a la siguiente · en el 8.º pulso se decide si hace falta un ciclo de ejecución. **Se estudia en** [[4.3.2 Búsqueda, los 8 pulsos]].

### Señal de control
**Qué es.** Cada una de las líneas que la **unidad de control** activa para que se haga una microoperación (`PCout`, `MARin`, `MEMout`, `ALUadd`…). **Para qué sirve.** Es el "qué hacer ahora": sin la señal, el dato no se mueve. **Características.** · Cada transferencia necesita **dos**: origen y destino · se generan combinando **estado y pulso** · en la BLUE son del tipo `PCout`, `MBRout`, `ACin`, `IRin`, `Read`, `Write`. **Se estudia en** [[4.4.1 Funciones y señales de control]].

### estado · pulso · instrucción
**Qué es.** La forma canónica de una señal de control: se activa **sólo si** el estado es el correcto **y** el pulso es el correcto **y** (si hace falta) la instrucción es la que corresponde. **Para qué sirve.** Generar señales **sin ambigüedad**: que `PCout` no se active en un pulso donde no debe. **Características.** · Se escribe como producto lógico: `PCout = E1·CP1 + E2·CP1` · el **decodificador 1 de 16** convierte 4 bits de estado en 16 líneas · es la base del control cableado. **Se estudia en** [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]].

### Búsqueda (fetch) y ejecución (execute)
**Qué es.** Las dos fases de un ciclo de instrucción: **traer** la instrucción de memoria y **hacer** lo que dice. **Para qué sirve.** Entender por qué una instrucción tarda 1 o 2 ciclos de máquina: la búsqueda **siempre** existe y la ejecución se agrega si hay que ir a memoria o a un periférico. **Características.** · Búsqueda: 8 pulsos fijos · ejecución: 8 pulsos más (BLUE) · los estados de la UC son `F` y `E` (y `I` para interrumpir) · un salto con destino en el `PC` no necesita ejecución. **Se estudia en** [[4.3.1 Ciclo de reloj, de máquina y de instrucción]].

### Capacidad de memoria
**Qué es.** Cuántos bits guarda una memoria: `palabras × bits por palabra`. **Para qué sirve.** Expresar y comparar memorias: 4096 × 16 = 65 536 bits = **8 KB**. **Características.** · Se mide en bits o en bytes (1 B = 8 bits) · `K` en memorias suele ser 1024 · capacidad = `2^(bits de dirección) × ancho de palabra`. **Se estudia en** [[4.2.1 Especificación, registros y 4096x16]].

### Modificar el PC (PC + 1)
**Qué es.** La microoperación que **incrementa** el contador de programa después de buscar la instrucción. **Para qué sirve.** Que la próxima búsqueda traiga la instrucción siguiente; es lo que hace que un programa "avance solo". **Características.** · Ocurre **durante** la búsqueda, no en la ejecución · los saltos la **sobrescriben** con la dirección destino · si la instrucción es de 2 palabras, el `PC` avanza 2. **Se estudia en** [[4.3.2 Búsqueda, los 8 pulsos]].

### Decodificador de instrucción
**Qué es.** Circuito que toma los bits de **opcode** del `IR` y activa **una** línea por instrucción. **Para qué sirve.** Que la UC sepa qué instrucción está en el `IR` y genere las señales de su ejecución. **Características.** · Es un decodificador `n → 2ⁿ` · sus salidas se combinan con el estado y el pulso · en la BLUE decodifica **4 bits** en 16 líneas. **Se estudia en** [[4.4.2 estado·pulso·instrucción y el decodificador 1-16]].
