---
unidad: 6
tipo: concepto
examen: principal
prioridad: maxima
---
# Cómo se implementa la Unidad de Control

> [!important] Qué necesitás para responder esta pregunta
> **En `Apoyo a la pregunta/`:** [[Unidad de Control]]
> **En otra tanda o unidad:** [[Decodificador]] (Tanda 3 · 3.1 Decodificadores) · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] (Tanda 2 · 2.5 Las 16 instrucciones, pulso por pulso) · [[Ciclo de máquina]] (Tanda 1 · 1.8 Ciclo de máquina y ciclo de instrucción) · [[CISC y RISC]] (Tanda 2 · 2.6 CISC y RISC) · [[Unidad de control cableada y microprogramada]] (Materia · Unidad 6)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 1.6 Implementación de la UC]].


> [!abstract] En una frase
> La UC se implementa como un **circuito secuencial** que combina tres cosas: **el estado** (los biestables
> RUN, STATE, TRA y los flags), **el tiempo** (el reloj maestro que genera CP1…CP8) y **la instrucción**
> (los 4 bits del opcode, decodificados en 16 líneas). Con esas tres entradas, **compuertas** generan las
> señales de control (`Send…`, `Load…`, `Orden de lectura`). Hay dos formas de hacerlo: **cableada** (las
> compuertas) y **microprogramada** (una memoria de control que guarda las microórdenes).

## Partamos de cero: qué es "controlar"
Una computadora es un montón de registros, una ALU y una memoria conectados a un bus. Ninguno de ellos "sabe"
qué hacer: si no se los habilita, quedan quietos. La **Unidad de Control es la que aprieta los botones en el
orden correcto y en el momento correcto**.

Pensalo como una cocina: los registros son los utensilios, la ALU es la licuadora, la memoria es la heladera.
Nadie cocina solo. La UC es el **chef** que dice "ahora batí", "ahora poné esto en el horno", "ahora esperá".
Ese "orden y momento" es lo que hace que un montón de fierros **ejecute instrucciones**.

Concretamente, la UC tiene **cuatro funciones**:
1. **Sincronizar** — marcar el ritmo con el reloj (CP1…CP8).
2. **Decodificar** — leer el opcode del IR y saber qué instrucción es.
3. **Secuenciar** — decidir qué pasa en cada pulso y cuándo se pasa de búsqueda a ejecución.
4. **Generar señales** — activar `Send X` / `Load Y` / `orden de lectura` de cada registro.

## Las tres entradas de la UC

| Entrada | De dónde viene | Para qué la usa |
|---|---|---|
| **Opcode** (IR15…IR12 en la BLUE) | registro de instrucción | decodificar qué instrucción hay que ejecutar |
| **Estado** (FF **RUN**, FF **STATE** F/E, FF **TRA**) | propios biestables internos | saber si está corriendo, si está buscando o ejecutando, si hay una E/S en curso |
| **Tiempo** (CP1…CP8) | reloj maestro | saber en qué pulso del ciclo está |
| (además) **flags** (A15/signo, overflow) y **R** del periférico | ALU y dispositivos | decidir saltos condicionales y el fin de la E/S |

## Implementación **cableada** (la de la BLUE): paso a paso

### 1) El estado: tres flip-flops
```
        START ──┐
       STOP ──┐ │      ┌─────────┐
       HLT  ──┤ ├────► │ RUN     │  1 = máquina corriendo
   Overflow ──┘ │      └────┬────┘
                │           │ habilita el reloj
                │      ┌────▼────┐
   CP8 (fin de ejecución) ──►│ STATE │  F = búsqueda · E = ejecución · (I = interrupción)
                │      └────┬────┘
                │      ┌────▼────┐
   INP/OUT (CP7 búsqueda) ──►│ TRA   │  1 = hay una operación de E/S en curso
                │      └─────────┘
                └──► todo esto son compuertas, no programa
```
- **RUN**: se pone en 1 con **START**, en 0 con **STOP**, con **HLT** o con **overflow**. Mientras RUN = 1 el
  reloj avanza; si RUN = 0, la máquina se congela.
- **STATE**: 1 bit que distingue **búsqueda (F)** de **ejecución (E)**. Se pone en E en **CP8 de la búsqueda**
  (sólo si la instrucción lo necesita) y vuelve a F en **CP8 de la ejecución**.
- **TRA**: biestable auxiliar de las instrucciones de E/S.

### 2) El tiempo: el reloj maestro de 8 pulsos
Un pulso pasa por una **cadena de 8 retardos** (de 125 ns cada uno). Cada derivación de la cadena da una
línea **CP1…CP8**: pulsos iguales, uno atrás del otro. Al final de la cadena el pulso **realimenta** el
circuito y vuelve a empezar **si RUN = 1** (o si STATE = E). Eso es lo que produce la sucesión de ciclos de
máquina.

### 3) La decodificación: el árbol de 4 bits a 16 líneas
Los 4 bits del opcode entran a un **demultiplexor 1→16** (el "árbol completo de decodificación") y se enciende
**una** de las 16 líneas: `HLT, ADD, XOR, AND, IOR, NOT, LDA, STA, SRJ, JMA, JMP, INP, OUT, RAL, CSA, NOP`.
Es decir: **decodificar la instrucción es un decodificador de 4 a 16**, exactamente el mismo circuito de la
3.ª tanda del final ([[Decodificador]]).

### 4) La generación de señales: compuertas que combinan estado × tiempo × instrucción
Cada señal de control es una **AND** de tres cosas: *"estoy en este estado"* **y** *"estoy en este pulso"*
**y** *"la instrucción es ésta"*. Ejemplos reales de la BLUE (las ecuaciones de las compuertas del apunte):

| Señal de control | Se activa cuando… | Ecuación conceptual |
|---|---|---|
| `Send PC, Load MAR` (búsqueda) | STATE=F **y** CP1 | `F · CP1` |
| `Send MBR, Load IR` | STATE=F **y** CP6 | `F · CP6` |
| `E → STATE` | fin de búsqueda de una instrucción con referencia a memoria | `F · CP8 · REF` |
| `Send IR, Load MAR` | STATE=E **y** CP1 **y** la instrucción referencia memoria | `E · CP1 · REF` |
| `Send A, Load Z` | STATE=E **y** CP2 **y** es aritmética | `E · CP2 · ARITH` |
| `Send SUM, Load A` | STATE=E **y** CP8 **y** es ADD | `E · CP8 · ADD` |
| `Send IR, Load PC` | CP8 **y** (JMP, o JMA con A15 = 1, o SRJ en CP8) | `CP8 · (JMP + JMA·A15 + SRJ)` |
| `Reset FF RUN` | HLT **y** CP8 (o overflow) | `CP7 · HLT` |

Y las **señales que agrupan familias** (esto es lo que más se pregunta):

```
REF   = LDA + STA + ADD + XOR + AND + IOR     (instrucciones que referencian memoria)
ARITH = ADD + XOR + AND + IOR                 (las que usan la ALU con dos operandos)
DTA   = LDA + STA + ADD + XOR + AND + IOR     (las que traen o llevan un dato)
```
> [!important] El detalle que impresiona en el oral
> Cuando **la misma señal se activa desde varios lugares distintos** (por ejemplo `Load A` viene de LDA, de
> ADD, de NOT, de RAL, de CSA, de INP…), **no se duplican cables: se juntan con una OR**. La UC es, en el
> fondo, un montón de **OR de AND** (suma de productos): cada AND dice "en este pulso, con esta instrucción,
> con este estado", y la OR junta todas las situaciones que producen la misma microorden.
> Dicho de otro modo: **la UC cableada es un circuito combinacional gigante alimentado por el estado y el
> reloj**. Y si eso te suena a la 3.ª tanda del final, es porque **es el mismo tema**: tabla de verdad →
> funciones → compuertas.

### 5) Resumen del camino completo
```
IR(4 bits) ──► decodificador 1→16 ──┐
                                    ├──► compuertas AND (estado · pulso · instrucción) ──► señales
FF STATE, FF RUN, FF TRA ───────────┤                                                        │
reloj CP1…CP8 ──────────────────────┘                                                        ▼
                                                                     Send/Load de cada registro,
                                                                     orden de lectura/escritura
```

## Implementación **microprogramada** (la alternativa)
En vez de "cablear" las compuertas, se guarda **la lista de microórdenes** en una memoria especial: la
**memoria de control** (una ROM). Cada palabra de esa ROM es una **microinstrucción** que dice, en bits, qué
señales activar en ese pulso.

| Concepto | Qué es |
|---|---|
| **Microinstrucción** | palabra de la memoria de control; describe una microoperación (o varias simultáneas) |
| **Microprograma** | secuencia de microinstrucciones que ejecuta **una** instrucción de máquina |
| **MicroMAR / secuenciador** | registro que apunta a la microinstrucción actual; el opcode lo carga al inicio |
| **PLA / ROM de traducción** | traduce el opcode a la **dirección inicial** del microprograma |
| **Registro SR / micro-pila** | guarda la dirección de retorno de una microsubrutina |

Cómo funciona, en una frase: *el opcode no "enciende compuertas", **elige una dirección** de la memoria de
control; de ahí en adelante el secuenciador va leyendo microinstrucciones, una por pulso de reloj*.

- **Ventajas**: se cambia el repertorio **cambiando la ROM** (no el cableado); permite instrucciones
  complejas (CISC); más barato y ordenado de diseñar.
- **Desventajas**: **más lento** (cada microorden cuesta un acceso a la memoria de control), y el
  microprograma es difícil de leer para el usuario.

**Ejemplo real (8088)**: la UC del 8088 es **microprogramada**, con una **ROM de 504 palabras de 21 bits** que
guarda unos **90 microprocedimientos**; cada instrucción usa al menos uno. El opcode, por medio de una **PLA**,
produce la dirección inicial del microprograma; cada microinstrucción tiene campos *fuente* (5 bits), *destino*
(5), *tipo* (3), *ALU* (4), *registro* (3) y *condición* (1). El 8088, además, parte el trabajo en **BIU**
(busca instrucciones y las encola en una FIFO de 4 bytes) y **EU** (las ejecuta): eso es ya hardware con
**pipeline** ([[Pipeline]]).

## Cableada vs microprogramada (cuadro que se pide)
| | **Cableada** | **Microprogramada** |
|---|---|---|
| Cómo se guarda la secuencia | en compuertas (fija) | en una ROM de control (cambiable) |
| Velocidad | **más rápida** | más lenta (acceso a la memoria de control) |
| Flexibilidad | nula una vez construida | alta: se actualiza cambiando la ROM |
| Costo / complejidad de diseño | alto para repertorios grandes | bajo, muy ordenado |
| Se usa en | **RISC**, máquinas chicas (BLUE) | **CISC** (8088, x86) |
| Instrucciones complejas | difíciles | naturales |

## Cómo responderlo en el final (3–4 minutos)
1. **Definición**: "la UC sincroniza, decodifica, secuencia y genera las señales de control".
2. **Dibujo**: el bloque UC con las tres entradas (opcode, estado, reloj) y a la salida las señales
   `Send/Load`; arriba el decodificador 1→16.
3. **Cableada**: contar cómo se arma cada señal con `estado · pulso · instrucción`, y el detalle de la **OR**
   que junta las señales repetidas. Mencionar `REF`, `ARITH`, `DTA`.
4. **Microprogramada**: memoria de control, microinstrucción, microprograma, PLA y secuenciador; ejemplo 8088.
5. **Cierre**: "cableada = rápida y rígida (RISC); microprogramada = lenta y flexible (CISC)". Y: "la UC no
   hace cuentas, **manda**; las cuentas las hace la ALU".

## Errores típicos
- Decir que la UC hace las operaciones aritméticas (las hace la ALU; la UC elige **qué** salida de la ALU se
  habilita).
- Confundir **instrucción** (de máquina, la del programa) con **microinstrucción** (la de la memoria de
  control).
- Olvidar el factor **estado** en las señales: `Send IR, Load MAR` **no** ocurre en todo CP1, sólo en
  `E · CP1 · REF`.
- Creer que la decodificación es "un programa": en la BLUE es un **demultiplexor 1→16**.

## Para ampliar: qué leer y qué buscar
| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **`blue.pdf`** (Foster) | sección **"Circuitos de la unidad de control"**: **fig. 19** (árbol de decodificación), **figs. 20-29** (compuertas de cada señal) y **tablas 2, 3, 4, 5 y 7** | cómo se arma cada señal con compuertas y de dónde salen `ARITH`, `DTA` y `REF` (fig. 25) | **Es la fuente exacta** del diseño cableado, compuerta por compuerta |
| **`blue.pdf`**, **"Unidad de control"** | clasificación **sincrónica vs asincrónica** y el circuito del reloj (fig. 10) | ventajas y desventajas de cada esquema | Para justificar por qué la BLUE es sincrónica |
| **Apuntes de cátedra**, *Unidad 5* | sección del **decodificador del campo modificador** y del **secuenciador** en la figura de la BLUE indexada | cómo crece la UC al agregar modos: un decodificador más | Mostrar que el diseño escala |
| **Apuntes de cátedra**, *Unidad 5* (sección del **8088**) | **BIU/EU**, la **ROM de control de 504 × 21 bits**, la PLA, el `microMAR`, el registro `SR` y el formato de microinstrucción | el ejemplo real de UC microprogramada con todos sus números | Es el caso concreto que se cita en el final |
| **[[Unidad de control cableada y microprogramada]]** | la nota de la bóveda | el microprograma de ejemplo | Complemento conceptual |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulos de **control cableado** y **microprogramado** | diseño de la sección de control y del secuenciador | La referencia formal del tema |
| **Tanenbaum, *Estructura de computadores*** | capítulo de **microprogramación** | microinstrucciones, microprograma, nanomemoria | Clara y con ejemplos |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo del **procesador: control** | control combinacional (cableado) vs microprogramado, y por qué RISC elige cableado | Cierra con [[CISC y RISC]] |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **control del procesador** | funciones y señales de control, implementación | Otra enumeración para ampliar |

## Relacionado
[[Unidad de Control]] · [[Unidad de control cableada y microprogramada]] · [[Registros de la CPU]] ·
[[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · [[Decodificador]] ·
[[CISC y RISC]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
