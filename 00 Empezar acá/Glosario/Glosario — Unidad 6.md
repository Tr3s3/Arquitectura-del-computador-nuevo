---
tipo: glosario
unidad: 6
---
# Glosario — Unidad 6: control microprogramado

> [!abstract] Qué hay acá
> Las **10 fichas** de la unidad: las dos formas de generar señales de control (cableada y microprogramada) y las
> piezas de la segunda. Índice alfabético en [[Glosario]].

### Control cableado
**Qué es.** Unidad de control hecha con **compuertas y flip-flops**: cada señal es una función lógica del estado y
del pulso.
**Para qué sirve.** Es la forma **más rápida** de generar señales: no hay que leer nada, la señal sale de una
compuerta.
**Características.** · Rápida y **rígida**: cambiar una instrucción es **rediseñar el circuito** ·
el diseño se hace con tablas y Karnaugh · se usa en máquinas RISC y en el camino crítico.
**Se estudia en** [[6.3.1 Cableada vs microprogramada]].

### Control microprogramado
**Qué es.** Unidad de control que guarda las señales como **datos** en una memoria de control: cada microinstrucción
dice qué señales activar en un pulso.
**Para qué sirve.** Cambiar el repertorio **sin cambiar el hardware**: se reescribe el microprograma.
**Características.** · Flexible y **más lenta** (hay que leer la memoria) · permite instrucciones complejas
(CISC) · se diseña como un programa, no como un circuito.
**Se estudia en** [[6.3.1 Cableada vs microprogramada]].

### Microinstrucción
**Qué es.** La palabra de la memoria de control: contiene **todas** las señales que se activan en un pulso, más
información de secuenciamiento.
**Para qué sirve.** Es el equivalente a "una instrucción" pero del nivel de control: una instrucción de máquina se
ejecuta con **varias** microinstrucciones.
**Características.** · Su ancho es la cantidad de señales + los bits de secuencia (21 bits en el 8088) ·
**horizontal**: 1 bit por señal (rápida, ancha) · **vertical**: código compacto que hay que decodificar (lenta,
angosta).
**Se estudia en** [[6.2.1 Memoria de control y microinstrucción]].

### Memoria de control
**Qué es.** La ROM (o RAM de control) que guarda el microprograma; se direcciona con el **microPC**.
**Para qué sirve.** Entregar la microinstrucción del pulso actual.
**Características.** · Es una ROM: no volátil y de acceso rápido · su tamaño = `microinstrucciones × ancho` ·
en el 8088: **504 × 21 = 10 584 bits**, con 9 bits de dirección.
**Se estudia en** [[6.2.1 Memoria de control y microinstrucción]].

### MicroPC y microprograma
**Qué es.** **MicroPC**: registro que apunta a la microinstrucción actual. **Microprograma**: la secuencia de
microinstrucciones que ejecuta una instrucción de máquina.
**Para qué sirve.** Recorrer el microcódigo igual que el `PC` recorre el programa.
**Características.** · El microPC se incrementa solo o se **carga** desde el campo de dirección de la
microinstrucción · hay un microprograma **por cada** instrucción · el arranque se hace en una dirección fija
(`0`) por instrucción.
**Se estudia en** [[6.2.2 Secuenciamiento y microPC]].

### Secuenciamiento y salto condicional
**Qué es.** La lógica que decide **cuál es la próxima** microinstrucción: la siguiente en secuencia o un salto.
**Para qué sirve.** Que el microprograma tenga bucles y decisiones (por ejemplo, "si no hubo acarreo, saltar").
**Características.** · Campos de la microinstrucción: **condición**, **dirección de salto** y **selección** ·
formatos de 1, 2 o 3 campos de dirección · la condición mira banderas o el estado de la UC.
**Se estudia en** [[6.2.2 Secuenciamiento y microPC]].

### Campo de dirección de control
**Qué es.** Los bits de la microinstrucción que indican **a dónde ir** si se cumple la condición de salto.
**Para qué sirve.** Implementar el control de flujo del microprograma.
**Características.** · Con **un** campo de dirección hay que multiplexar (dirección siguiente o salto) ·
con **dos** campos se puede elegir entre dos destinos sin multiplexor · ocupa bits que se le quitan a las señales.
**Se estudia en** [[6.2.2 Secuenciamiento y microPC]].

### ROM de control del 8088 (504 × 21)
**Qué es.** La memoria de control concreta del 8088: 504 microinstrucciones de 21 bits.
**Para qué sirve.** Es el ejemplo que la cátedra usa para **dimensionar**: cuántas palabras, cuántos bits, cuántos
bits de dirección.
**Características.** · `504 × 21 = 10 584 bits` ≈ 1,3 KB · `2⁹ = 512` ⇒ **9 bits** de dirección (504 usadas) ·
21 bits = 16 de señales + 5 de secuencia (aproximadamente).
**Se estudia en** [[6.3.2 El 8088, ROM de control 504x21]].

### Circuito de control (bloque)
**Qué es.** El bloque que, dado el **opcode** del `IR`, el **estado** y el **pulso**, genera todas las señales.
**Para qué sirve.** Ser el "director de orquesta" del camino de datos.
**Características.** · Entradas: opcode, banderas, reloj, estado · salidas: señales de control ·
se documenta con un **diagrama de estados** o con la tabla de microinstrucciones.
**Se estudia en** [[6.1.1 Circuito, compuertas y señales]].

### Microcódigo vertical y horizontal
**Qué es.** Dos estilos de codificar la microinstrucción: **horizontal** = un bit por señal; **vertical** = un
código compacto por grupo de señales.
**Para qué sirve.** Elegir entre **velocidad** (horizontal) y **tamaño de la ROM** (vertical).
**Características.** · Horizontal: ROM ancha, sin decodificar, rápida · vertical: ROM angosta, con decodificador,
más lenta pero permite microprogramas más largos · el compromiso se llama **diagonal**.
**Se estudia en** [[6.2.1 Memoria de control y microinstrucción]].
