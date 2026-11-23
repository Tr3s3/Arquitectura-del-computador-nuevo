---
tipo: glosario
unidad: 5
---
# Glosario — Unidad 5: programación básica y CPU convencional

> [!abstract] Qué hay acá
> Las **20 fichas** de la unidad: cómo es una instrucción, los formatos, los modos de direccionamiento y su costo, la BLUE indexada y las interrupciones. Índice alfabético en [[Glosario]].

### Instrucción
**Qué es.** La orden mínima que entiende la CPU: **qué** operación, **con qué** datos y **dónde** están. **Para qué sirve.** Es la unidad del programa: el `PC` las recorre y el `IR` guarda la que se ejecuta. **Características.** · Ocupa una o más palabras · se arma con **codop + operandos** · el conjunto de todas las instrucciones es el **repertorio** de la máquina. **Se estudia en** [[5.1.1 Instrucción, opcode y operandos]].

### Opcode y operando
**Qué es.** **Opcode**: código de la operación (4 bits en la BLUE). **Operando**: el dato o la dirección sobre la que se opera. **Para qué sirve.** El opcode dice **qué** hace la UC; el operando dice **sobre qué**. **Características.** · `k` bits de opcode ⇒ `2ᵏ` instrucciones · el operando puede estar **en la instrucción**, en un **registro** o en **memoria** · los operandos implícitos (el `AC`) no se escriben. **Se estudia en** [[5.1.1 Instrucción, opcode y operandos]].

### Clasificación de las instrucciones
**Qué es.** Los grupos del repertorio: transferencia de datos, aritméticas, lógicas, de control de flujo, de entrada/salida y de manejo de pila. **Para qué sirve.** Ordenar el repertorio al estudiarlo y reconocer una instrucción nueva por su grupo. **Características.** · Control de flujo = **saltos** y llamadas (cambian el `PC`) · las de E/S usan puertos, no memoria · las de pila usan `SP` implícito. **Se estudia en** [[5.1.2 Clasificación de las instrucciones]].

### Formatos de instrucción (4, 3, 2, 1 y 0 direcciones)
**Qué es.** Cuántas direcciones de operando lleva la instrucción en su codificación. **Para qué sirve.** Elegir el compromiso entre **largo de programa** y **largo de instrucción**. **Características.** · Más direcciones ⇒ menos instrucciones pero cada una más larga · la de **1 dirección** usa el `AC` implícito (la BLUE) · la de **0 direcciones** usa la **pila** · RISC suele usar 3, CISC 2 o 1. **Se estudia en** [[5.2.1 Los 4 formatos y el campo único de dirección]].

### Campo único de dirección
**Qué es.** Formato en el que la instrucción tiene **un solo** campo de dirección, porque el otro operando es implícito (`AC`). **Para qué sirve.** Aprovechar al máximo los bits: la BLUE gasta 4 en opcode y **12** en dirección. **Características.** · La operación se hace **contra el acumulador** · el resultado queda en el `AC` · todo el espacio de direcciones es alcanzable. **Se estudia en** [[5.2.1 Los 4 formatos y el campo único de dirección]].

### Modo de direccionamiento
**Qué es.** La regla que dice **cómo se calcula** la dirección del operando a partir de lo que dice la instrucción. **Para qué sirve.** Un mismo repertorio puede acceder a datos en registros, en memoria, en arreglos o en la pila. **Características.** · Son **7** en la cátedra: inmediato, directo, indirecto, de registro, registro indirecto, con desplazamiento y de pila · define el **costo** en accesos · es parte del formato (bits de modo). **Se estudia en** [[5.3.1 Los 7 modos]].

### Inmediato y directo
**Qué es.** **Inmediato**: el operando **es** el campo de la instrucción. **Directo**: el campo **es la dirección** del operando. **Para qué sirve.** El inmediato para constantes (`ADD 5`); el directo para variables globales. **Características.** · Inmediato: **0 accesos** a memoria, pero el valor queda fijo en el programa · directo: **1 acceso**, y el campo limita a `2^d` direcciones. **Se estudia en** [[5.3.1 Los 7 modos]].

### Indirecto
**Qué es.** El campo de la instrucción apunta a una celda que **contiene la dirección** del operando. **Para qué sirve.** Cambiar el destino sin cambiar el programa: punteros, estructuras dinámicas. **Características.** · **2 accesos** a memoria (uno para la dirección, otro para el dato) ⇒ el más lento · permite direccionar más allá del campo con una palabra completa · se puede anidar (indirecto doble). **Se estudia en** [[5.3.1 Los 7 modos]].

### De registro y registro indirecto
**Qué es.** **De registro**: el operando está **en** un registro. **Registro indirecto**: el registro **contiene la dirección** del operando. **Para qué sirve.** El de registro es el más rápido (0 accesos); el indirecto sirve para punteros. **Características.** · De registro: **0 accesos**, no requiere campo de dirección largo · registro indirecto: **1 acceso** · son la base de las arquitecturas tipo load/store. **Se estudia en** [[5.3.1 Los 7 modos]].

### Indexado (con desplazamiento)
**Qué es.** La dirección efectiva es `base o índice + desplazamiento`. **Para qué sirve.** Recorrer **arreglos**: el índice avanza y el desplazamiento es fijo. **Características.** · **1 acceso** (más el cálculo, que es gratis si el índice está en registro) · permite reubicar estructuras cambiando sólo la base · es el modo que la BLUE indexada implementa con `RIF`/`RID`. **Se estudia en** [[5.3.1 Los 7 modos]].

### De pila
**Qué es.** El operando está en el **tope de la pila**, apuntado por `SP`; la instrucción no lleva dirección. **Para qué sirve.** Evaluar expresiones y guardar contexto sin escribir direcciones (instrucciones más cortas). **Características.** · `SP` se modifica solo (`decrementa` al apilar) · **1 acceso** · es la base de las máquinas de 0 direcciones y del `PUSH`/`POP`. **Se estudia en** [[5.3.1 Los 7 modos]].

### Dirección efectiva (EA)
**Qué es.** La dirección **final** que se pone en el `MAR` para acceder al operando. **Para qué sirve.** Es el resultado de aplicar el modo: saber calcularla es saber resolver cualquier ejercicio de direccionamiento. **Características.** · Cada modo tiene su fórmula (`EA = campo`, `EA = M[campo]`, `EA = RIF + campo`…) · el costo se cuenta en **accesos a memoria**: 0, 1 o 2 · se calcula en el ciclo de ejecución. **Se estudia en** [[5.3.2 Dirección efectiva y costo en accesos]].

### RIF, RID y RB
**Qué es.** Los registros que agrega la **BLUE indexada**: `RIF` (índice fuente), `RID` (índice destino) y `RB` (base). **Para qué sirve.** Calcular la dirección efectiva **sumando** un índice a un desplazamiento: recorrer vectores. **Características.** · `EA = RB + campo + RIF (+ RID)` · son de 16 bits · los elige el **modificador** de 2 bits. **Se estudia en** [[5.4.1 RIF, RID y RB]].

### Modificador de 2 bits
**Qué es.** Campo que dice **qué índices** se suman a la dirección: ninguno, `RIF`, `RID` o los dos. **Para qué sirve.** Convertir un direccionamiento directo en indexado **sin cambiar de instrucción**. **Características.** · `00` directo · `01` + `RIF` · `10` + `RID` · `11` + los dos · la instrucción indexada mide **32 bits** (2 palabras) y tarda **24 pulsos**. **Se estudia en** [[5.4.2 Modificador de 2 bits y los 24 pulsos]].

### IRQ, SI y CP8
**Qué es.** Las tres condiciones para **aceptar** una interrupción: `IRQ` (el pedido), `SI` (interrupciones habilitadas) y `CP8` (fin del ciclo de instrucción). **Para qué sirve.** Que la interrupción entre en un momento **seguro**, no en medio de una instrucción. **Características.** · La señal es `IRQ · SI · CP8` · al aceptarla el hardware pone `SI = 0` para no anidar · la atención empieza en el ciclo siguiente. **Se estudia en** [[5.5.1 IRQ, SI y CP8]].

### Máscara y prioridad
**Qué es.** **Máscara**: bits que **habilitan o inhiben** cada interrupción. **Prioridad**: cuál se atiende si llegan varias a la vez. **Para qué sirve.** Que un dispositivo importante no quede esperando y que uno molesto no interrumpa siempre. **Características.** · `SI = 0` inhibe **todas** · la máscara por dispositivo inhibe selectivamente · la prioridad puede ser **fija por hardware** (cadena) o **programable** (8259). **Se estudia en** [[5.5.2 Máscara, pila y RTI]].

### Pila (PUSH y POP)
**Qué es.** Estructura **LIFO** en memoria; `PUSH` apila y `POP` desapila, con `SP` como puntero al tope. **Para qué sirve.** Guardar el contexto de una interrupción o subrutina y evaluar expresiones. **Características.** · La pila **crece hacia abajo** en el 8086 (`SP` decrece) · el orden de restauración es el **inverso** · si se desborda, pisa datos. **Se estudia en** [[5.5.2 Máscara, pila y RTI]].

### RTI (retorno de interrupción)
**Qué es.** Instrucción que **restaura** el estado guardado y devuelve el control al programa interrumpido. **Para qué sirve.** Que el programa continúe **exactamente** donde estaba, sin que se note la interrupción. **Características.** · Recupera el `PC` y el registro de estado · reactiva `SI` · es distinto de un salto: **no** vuelve por dirección del programa sino por la guardada. **Se estudia en** [[5.5.2 Máscara, pila y RTI]].

### BIU y EU (8086)
**Qué es.** La CPU del 8086 partida en dos: **BIU** (bus interface unit: busca instrucciones y datos) y **EU** (execution unit: las ejecuta). **Para qué sirve.** Que buscar y ejecutar ocurran **a la vez**: es el primer pipeline comercial. **Características.** · Se comunican por una **cola de 6 bytes** · si la cola está llena, la BIU espera · un salto vacía la cola (**penalidad**) · la EU no toca memoria: pide a la BIU. **Se estudia en** [[5.6.1 BIU, EU y segmentación]].

### Segmento y offset
**Qué es.** El 8086 arma la dirección física como `segmento × 16 + offset`, con registros de 16 bits. **Para qué sirve.** Direccionar **1 MB** con registros de 16 bits. **Características.** · 4 segmentos activos: código (`CS`), datos (`DS`), pila (`SS`) y extra (`ES`) · dirección física = `20 bits` · los segmentos se pueden **solapar**. **Se estudia en** [[5.6.2 La pila y el registro SP]].
