---
tipo: glosario
unidad: 1
---
# Glosario — Unidad 1: circuitos de lógica digital

> [!abstract] Qué hay acá
> Las **31 fichas** de los conceptos de la unidad: qué es cada uno, **para qué sirve** y **cuáles son sus
> características**. Están ordenadas como se estudian (compuertas → álgebra → simplificación → bloques → aritmética
> → códigos). El índice alfabético está en [[Glosario]].

## Compuertas y álgebra

### Compuerta lógica
**Qué es.** Circuito electrónico mínimo que realiza una **operación lógica** sobre una o más señales binarias y
devuelve una salida binaria.
**Para qué sirve.** Es el ladrillo con el que se construye **todo** lo demás: una ALU, una memoria, un
microprocesador.
**Características.** · Se define por su **tabla de verdad**, no por su electrónica.
· Tiene `n` entradas y **una** salida · la salida cambia con un pequeño retardo de propagación.
**Se estudia en** [[1.1.1 Compuerta AND, OR y NOT]].

### Tabla de verdad
**Qué es.** Tabla que lista **todas** las combinaciones posibles de las entradas de una función y la salida en cada
una: `2ⁿ` filas para `n` variables.
**Para qué sirve.** Es la **definición** de la función (y del circuito): si dos circuitos tienen la misma tabla,
son el mismo circuito.
**Características.** · `n` variables ⇒ `2ⁿ` filas · se escribe en orden binario o en orden **Gray** (para Karnaugh)
· de ella se leen los mintérminos y los maxtérminos.
**Se estudia en** [[1.3.1 Mintérminos y maxtérminos]].

### AND (Y lógica)
**Qué es.** Compuerta que da **1 sólo si todas** sus entradas son 1 (`Y = A·B`).
**Para qué sirve.** Detectar que **se cumplen todas** las condiciones: es el "y" del idioma (activar si `A` y `B`).
**Características.** · `A·0 = 0` (es **dominante** el 0) · es la operación **producto** del álgebra de Boole ·
con 3 entradas hay una sola fila con salida 1.
**Se estudia en** [[1.1.1 Compuerta AND, OR y NOT]].

### OR (O lógica)
**Qué es.** Compuerta que da **1 si al menos una** entrada es 1 (`Y = A + B`).
**Para qué sirve.** Detectar que **basta con una** condición: es el "o" inclusivo.
**Características.** · `A + 1 = 1` (es dominante el 1) · es la **suma** booleana (no aritmética: `1+1=1`) ·
su dual es la AND.
**Se estudia en** [[1.1.1 Compuerta AND, OR y NOT]].

### NOT (inversor)
**Qué es.** Compuerta de **una** entrada que niega: `Y = A'`.
**Para qué sirve.** Invertir una señal; con AND/OR permite construir cualquier función en forma canónica.
**Características.** · Es la **única** compuerta de 1 entrada · se usa como **indicador de negación** en los
símbolos (el círculo en la salida de NAND/NOR es un NOT).
**Se estudia en** [[1.1.1 Compuerta AND, OR y NOT]].

### NAND y NOR
**Qué es.** AND negada y OR negada: `Y = (A·B)'` y `Y = (A + B)'`.
**Para qué sirve.** Son las compuertas **reales** de las familias TTL/CMOS y, por ser **universales**, permiten
fabricar cualquier circuito con un solo tipo de chip.
**Características.** · **NAND** = OR de las negaciones (DeMorgan) · **NOR** = AND de las negaciones ·
la NAND es más rápida y más barata en CMOS que la NOR.
**Se estudia en** [[1.1.2 NAND, NOR, XOR y XNOR]].

### XOR y XNOR
**Qué es.** **XOR** (o exclusivo): `Y = A ⊕ B`, vale 1 cuando las entradas son **distintas**. **XNOR**: la negación.
**Para qué sirve.** Detectar **diferencia** (XOR) o **igualdad** (XNOR); es la base del **sumador** y del
**comparador**.
**Características.** · `A ⊕ A = 0`, `A ⊕ 1 = A'`, `A ⊕ 0 = A` · no es asociativa con la negación pero sí
conmuta · con 3 entradas da **paridad impar**.
**Se estudia en** [[1.1.2 NAND, NOR, XOR y XNOR]].

### Compuerta universal
**Qué es.** Compuerta con la que se puede armar **cualquier** función lógica sin usar otra: lo son la **NAND** y la
**NOR**.
**Para qué sirve.** Fabricar un circuito completo con **un solo tipo** de compuerta (menos costo, más simple el
stock y el diseño).
**Características.** · NOT con NAND: unir las entradas · AND = NAND + NOT · OR = NAND con entradas negadas ·
**la XOR necesita 4 NAND**.
**Se estudia en** [[1.1.3 Compuertas universales]].

### Escalas de integración (SSI, MSI, LSI, VLSI)
**Qué es.** Clasificación de los circuitos integrados según **cuántas compuertas** entran en un chip.
**Para qué sirve.** Saber qué se espera cuando el enunciado dice "implemente con MSI": usar un **bloque ya hecho**
(decodificador, MUX) en vez de dibujar compuerta por compuerta.
**Características.** · **SSI** hasta 10 · **MSI** 10-100 · **LSI** 100-1000 · **VLSI** más de 1000 ·
la frontera creció con la integración (hoy un microprocesador es VLSI por millones).
**Se estudia en** [[1.1.3 Compuertas universales]].

### Postulado
**Qué es.** Verdad básica del álgebra de Boole que **no se demuestra** (se acepta) y de la que salen los teoremas.
**Para qué sirve.** Justificar cada paso de una simplificación: cuando se "saca" un término, se está aplicando un
postulado.
**Características.** · Identidad: `A+0=A`, `A·1=A` · dominante: `A+1=1`, `A·0=0` · conmutativa, asociativa,
distributiva · complemento: `A+A'=1`, `A·A'=0`.
**Se estudia en** [[1.2.1 Postulados, dualidad y teoremas]].

### Dualidad
**Qué es.** Regla que permite obtener una identidad **gemela** de otra: se cambia **AND por OR**, **OR por AND**,
**0 por 1** y **1 por 0**.
**Para qué sirve.** Demostrar una sola vez y usar la otra forma gratis; y pasar de **SOP a POS** sin rehacer cuentas.
**Características.** · El dual de `A+0=A` es `A·1=A` · el dual de la distributiva es su forma "rara"
`A+(B·C)=(A+B)(A+C)` · **no** se cambian las variables ni las negaciones.
**Se estudia en** [[1.2.1 Postulados, dualidad y teoremas]].

### Teoremas de DeMorgan
**Qué es.** Dos identidades que convierten una negación de una operación en la operación contraria de las negaciones:
`(A·B)' = A' + B'` y `(A+B)' = A'·B'`.
**Para qué sirve.** Pasar cualquier función a **NAND** o a **NOR**, que son las compuertas que existen en el chip.
**Características.** · "Se rompe la barra y **se cambia el signo**" · vale para cualquier cantidad de variables ·
es el puente entre SOP y POS.
**Se estudia en** [[1.2.2 Leyes de DeMorgan]].

### Simplificación analítica
**Qué es.** Reducir una expresión booleana aplicando postulados y teoremas hasta que no se pueda achicar más.
**Para qué sirve.** Menos términos ⇒ **menos compuertas**, menos costo, menos retardo y menos consumo.
**Características.** · Herramientas: absorción (`A+AB=A`), `A+A'B=A+B`, idempotencia, DeMorgan ·
no hay algoritmo fijo: es "ver el patrón" · se verifica igualando tablas de verdad.
**Se estudia en** [[1.2.3 Simplificación analítica]].

## Formas canónicas y Karnaugh

### Forma canónica (SOP y POS)
**Qué es.** Expresión en la que **todos** los términos contienen **todas** las variables: **SOP** = suma de
productos (mintérminos), **POS** = producto de sumas (maxtérminos).
**Para qué sirve.** Es la forma **única** de una función: sirve para pasar de la tabla al circuito sin pensar.
**Características.** · SOP se implementa con **AND-OR** (o sólo NAND) · POS con **OR-AND** (o sólo NOR) ·
las dos son equivalentes pero una puede ser mucho más corta.
**Se estudia en** [[1.3.1 Mintérminos y maxtérminos]].

### Mintérmino
**Qué es.** Producto que vale **1 en una sola fila** de la tabla de verdad (todas las variables, negadas o no).
**Para qué sirve.** Armar la SOP: se suman los mintérminos de las filas donde la función vale 1.
**Características.** · Se numera por el valor binario de la fila (`m₅` = `101`) · una función de `n` variables tiene
`2ⁿ` mintérminos · `Y = Σm(1,2,5)` es su notación compacta.
**Se estudia en** [[1.3.1 Mintérminos y maxtérminos]].

### Maxtérmino
**Qué es.** Suma que vale **0 en una sola fila** de la tabla de verdad.
**Para qué sirve.** Armar la POS: se multiplican los maxtérminos de las filas donde la función vale **0**.
**Características.** · Es el **dual** del mintérmino · se numera igual (por la fila) ·
`Y = ΠM(0,3)` es la POS compacta.
**Se estudia en** [[1.3.1 Mintérminos y maxtérminos]].

### Mapa de Karnaugh
**Qué es.** Grilla de `2ⁿ` celdas donde cada celda es un mintérmino, ordenadas en **código Gray**, para simplificar
**a ojo**.
**Para qué sirve.** Obtener la expresión mínima sin álgebra: agrupando 1 (SOP) o 0 (POS) se lee la función
directamente.
**Características.** · Grupos de **1, 2, 4, 8** celdas (potencias de 2) · cuanto más grande el grupo, menos
variables quedan · los grupos **pueden cruzar bordes** y **solaparse** · hay que cubrir **todos** los 1 con la
menor cantidad de grupos.
**Se estudia en** [[1.3.2 Mapa de Karnaugh de 2, 3 y 4 variables]].

### Don't care (condición "no importa")
**Qué es.** Combinación de entrada que **nunca va a ocurrir** (o cuya salida da igual): se marca `X` en la tabla.
**Para qué sirve.** Usarla como 1 **o** como 0, lo que convenga, para agrandar grupos y simplificar más.
**Características.** · **Nunca es obligatorio** cubrir una `X` · si se usa como 1, hay que cubrirla; si no, se
ignora · aparece en displays BCD (los códigos `1010` a `1111` no son dígitos).
**Se estudia en** [[1.3.3 Don't care y criterios de agrupación]].

## Bloques combinacionales

### Decodificador
**Qué es.** Circuito que convierte un código de `n` bits en **una** de `2ⁿ` líneas activas (`Yi = mi`).
**Para qué sirve.** **Seleccionar** una palabra de memoria, habilitar un chip, activar un display de 7 segmentos.
**Características.** · `n` entradas → `2ⁿ` salidas · salidas activas en alto o en bajo (74138) ·
tiene **habilitación** (`E`) para encadenar y armar decodificadores más grandes.
**Se estudia en** [[1.4.1 Decodificador]].

### Codificador
**Qué es.** El inverso del decodificador: de `2ⁿ` (o menos) líneas activas a un código de `n` bits.
**Para qué sirve.** Traducir **qué** entrada se activó a un número: teclado → BCD, posición → binario.
**Características.** · `2ⁿ` entradas → `n` salidas · la versión **simple** supone **una sola** entrada activa ·
la **prioritaria** resuelve cuando hay varias (la de mayor número gana).
**Se estudia en** [[1.4.2 Codificador]].

### Multiplexor (MUX)
**Qué es.** Selector: de `2ⁿ` entradas de dato elige **una** y la manda a la salida, según `n` bits de selección.
**Para qué sirve.** Elegir entre varias fuentes de datos (registros, buses) y **implementar funciones** con un solo
chip.
**Características.** · *many into one* · `F = Σ Si·Di` · un MUX de `2ⁿ` entradas implementa **cualquier** función de
`n` variables sin compuertas extra.
**Se estudia en** [[1.4.3 Multiplexor]].

### Demultiplexor (DEMUX)
**Qué es.** Reparte **una** entrada de dato hacia **una** de `2ⁿ` salidas.
**Para qué sirve.** Dirigir un dato a un destino (un registro entre varios).
**Características.** · *one into many* · con `D = 1` **es** un decodificador · es el dual del MUX.
**Se estudia en** [[1.4.4 Demultiplexor]].

## Aritmética combinacional

### Semisumador
**Qué es.** Circuito que suma **dos** bits y da suma y acarreo: `S = A ⊕ B`, `Cout = A·B`.
**Para qué sirve.** Es la celda del bit menos significativo (no tiene acarreo de entrada).
**Características.** · Una XOR + una AND · no sirve para los bits del medio (no recibe `Cin`).
**Se estudia en** [[1.5.1 Semisumador y sumador completo]].

### Sumador completo (FA)
**Qué es.** Suma **tres** bits (`A`, `B`, `Cin`) y da `S` y `Cout`.
**Para qué sirve.** Es la celda que se repite: encadenando `n` se suma `n` bits (sumador con acarreo en cascada).
**Características.** · `S = A ⊕ B ⊕ Cin` · `G = A·B` (genera acarreo), `P = A ⊕ B` (lo propaga) ·
`V = Cin ⊕ Cout` (desborde con signo) · el retardo crece con `n`.
**Se estudia en** [[1.5.1 Semisumador y sumador completo]].

### Acarreo (carry) y resta en complemento a 2
**Qué es.** El acarreo es el 1 que "se lleva" a la columna siguiente. La **resta** `A − B` se hace como
`A + B' + 1`.
**Para qué sirve.** Restar sin un circuito distinto: **el mismo sumador** sirve para sumar y restar.
**Características.** · El **Cout** de la última etapa es la bandera **C** · con signo, el desborde es
**V = Cin ⊕ Cout** · `A + A' + 1 = 0` (todo número más su complemento a 2 da cero).
**Se estudia en** [[1.5.2 Sumador de n bits y resta en complemento a 2]].

## Códigos binarios

### Código binario
**Qué es.** Regla que asigna a cada símbolo (un dígito, una letra) una combinación de `n` bits.
**Para qué sirve.** Representar información con dos niveles de tensión; con `n` bits hay `2ⁿ` combinaciones.
**Características.** · Puede ser **ponderado** (cada bit vale un peso) o **no ponderado** (una regla sin pesos) ·
**continuo** si los códigos de números seguidos son adyacentes · **cíclico** si además cierra el círculo.
**Se estudia en** [[1.6.1 Códigos ponderados y no ponderados]].

### BCD (decimal codificado en binario)
**Qué es.** Representación en la que **cada dígito decimal** ocupa 4 bits con los pesos `8-4-2-1`.
**Para qué sirve.** Mostrar y operar números decimales (calculadoras, displays, relojes): es lo que lee un display
de 7 segmentos.
**Características.** · **Empaquetado**: 2 dígitos por byte · **desempaquetado**: 1 dígito por byte ·
sólo se usan 10 de las 16 combinaciones · sumar en BCD necesita la **corrección +0110**.
**Se estudia en** [[1.6.1 Códigos ponderados y no ponderados]].

### AIKEN (2-4-2-1)
**Qué es.** Código **ponderado** de 4 bits con pesos `2-4-2-1`; el 9 se escribe `1111`.
**Para qué sirve.** Codificar dígitos decimales con un código que también es **autocomplementario**.
**Características.** · Del 0 al 4 es idéntico al binario natural · del 5 al 9 se diferencia ·
es **ponderado**, a diferencia del exceso 3.
**Se estudia en** [[1.6.1 Códigos ponderados y no ponderados]].

### Exceso 3
**Qué es.** Código **no ponderado** que se obtiene **sumando 3** al binario puro del dígito.
**Para qué sirve.** Transmitir y operar decimal con un código que **no usa** `0000` y que se complementa a 9
invirtiendo bits.
**Características.** · **Autocomplementario** · el `0000` no representa nada ⇒ un cable cortado se detecta ·
muy usado en transmisión y en sumadores decimales.
**Se estudia en** [[1.6.1 Códigos ponderados y no ponderados]].

### Código de Gray
**Qué es.** Código **continuo y cíclico**: entre un número y el siguiente cambia **un solo bit**.
**Para qué sirve.** Evitar **estados intermedios falsos** en codificadores de posición y convertidores rápidos; y
ordenar las filas del mapa de Karnaugh.
**Características.** · Es **reflejado**: el segundo grupo es el primero al revés con un 1 adelante ·
con `n` bits usa **todas** las `2ⁿ` combinaciones · conversión: `G = B ⊕ (B >> 1)`.
**Se estudia en** [[1.6.2 Códigos continuos y cíclicos]].

### Código Johnson
**Qué es.** Código **continuo y cíclico** que se genera con un registro de desplazamiento realimentado con la salida
negada.
**Para qué sirve.** Contar con pocas compuertas y con la garantía de que cambia un bit por paso.
**Características.** · Con `n` biestables da **`2n` estados** (no `2ⁿ`): 5 bits → 10 estados ·
primero entran unos, después ceros · también cierra el ciclo.
**Se estudia en** [[1.6.2 Códigos continuos y cíclicos]].
