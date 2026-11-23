---
unidad: 6
tipo: concepto
examen: principal
prioridad: maxima
---
# Unidad de Control (UC): funciones, señales e importancia

> [!abstract] En una frase
> La UC **no hace cuentas: manda**. Sus cuatro funciones son **sincronizar** (reloj), **decodificar** (leer el opcode del IR), **secuenciar** (decidir qué pasa en cada pulso y cuándo se pasa de búsqueda a ejecución) y **generar las señales de control** (`MEMR`, `MEMW`, `PCin`, `PCout`, `MARin`, `MBRout`, `ACin`, `ACout`, `Load IR`, `ALUop`, `load flags`…). Sin esas señales **no se transfiere nada**: por eso es el bloque que "hace que la máquina funcione".

> [!note] Si es la primera vez que ves esto
> Una computadora es un montón de registros, una ALU y una memoria conectados a un bus. **Ninguno de ellos sabe nada**: si no se los habilita, quedan quietos. La UC es **la que aprieta los botones en el orden correcto y en el momento correcto**. Pensalo como una cocina: los registros son los utensilios, la ALU la licuadora, la memoria la heladera; nadie cocina solo. El chef es la UC: dice "ahora batí", "ahora al horno", "ahora esperá". Ese *orden* y ese *momento* convierten un montón de fierros en una máquina que ejecuta instrucciones.

> [!tip] Dos notas, dos preguntas distintas
> - **Esta nota**: *qué hace* la UC y *qué señales genera* (pregunta principal del modelo de final).
> - [[Cómo se implementa la Unidad de Control]]: *cómo se construye* (cableada vs microprogramada), que es el
>   ítem "¿cómo se implementa la UC?" de la 1.ª tanda de la matriz.

---

## 1. Las cuatro funciones (la respuesta mínima)

| Función | Qué significa | Ejemplo en la BLUE |
|---|---|---|
| **1. Sincronizar** | marcar el compás | habilita el reloj sólo si `RUN = 1`; genera `CP1…CP8` |
| **2. Decodificar** | averiguar **qué** instrucción es | los 4 bits del opcode entran al árbol 1→16 y activan una sola línea |
| **3. Secuenciar** | decidir **qué** pasa en **cada** pulso y cuándo se cambia de estado | en CP6 pone el MBR en el IR; en CP8 decide `E→STATE` o `F→STATE` |
| **4. Generar señales** | activar la microorden de cada pulso | `Send PC`, `Load MAR`, `MEMR`, `Send SUM`, `Load A`… |

**Y una quinta implícita**: **atender excepciones** (en la versión con interrupciones: aceptar IRQ al final de la instrucción, pasar al estado I).

---

## 2. Qué necesita saber la UC para decidir

| Entrada | De dónde viene | Para qué la usa |
|---|---|---|
| **Opcode** (`IR15…IR12`) | registro de instrucción | saber qué instrucción ejecutar |
| **Estado** (`RUN`, `STATE` F/E, `TRA`, `SI`) | sus propios biestables | saber si está corriendo, buscando, ejecutando o en E/S/interrupción |
| **Tiempo** (`CP1…CP8`) | reloj maestro | saber en qué pulso está |
| **Condiciones** (`A15`/signo, `Z`, `C`, `R` del periférico) | ALU y dispositivos | resolver saltos condicionales y el fin de la E/S |

> [!important] La fórmula que hay que decir
> **Cada señal de control = estado · pulso · instrucción.** Por ejemplo: `Send MBR / Load IR` se activa con `STATE = F · CP6` (no importa qué instrucción sea); en cambio `Send SUM / Load A` se activa con `STATE = E · CP8 · ADD`. Si te olvidás de alguno de los tres factores, la señal se dispara cuando no debe.

---

## 3. El catálogo de señales de control (con qué efecto)

### 3.1 Señales de registro (habilitan el bus o cargan)

| Señal | Efecto | Se usa en |
|---|---|---|
| `PCout` / `PCin` / `PCinc` | poner el PC en el bus / cargarlo / incrementarlo | búsqueda (CP1, CP4), saltos |
| `MARin` | cargar el registro de direcciones | CP1 de búsqueda y de ejecución |
| `MBRout` / `MBRload` (strobe) | sacar el MBR al bus / copiarle lo del bus | CP5 y CP6 |
| `IRin` / `IRout` | cargar el IR / sacar su campo de dirección | CP6 de búsqueda; CP1 de ejecución |
| `ACin` / `ACout` | cargar el acumulador / ponerlo en el bus | casi todas |
| `Zin` / `Yin` | cargar las entradas de la ALU | aritméticas (CP2 y CP6) |
| `SRout` | poner el registro de llaves en el bus | `CSA` |

### 3.2 Señales de memoria y E/S

| Señal | Efecto |
|---|---|
| `MEMR` (orden de lectura) | la memoria entrega el dato de la dirección del MAR |
| `MEMW` (orden de escritura) | la memoria guarda en la dirección del MAR lo que hay en el bus de datos |
| `TRA` | hay una operación de E/S en curso (se envían los 6 bits del IR como selección de dispositivo) |
| `INTACK` / `ACK` | reconocimiento de interrupción |

### 3.3 Señales de la ALU y de estado

| Señal | Efecto |
|---|---|
| `SUM`, `XOR`, `AND`, `IOR`, `Z'` (Zbar), `2·Z` | **qué salida de la ALU** se pone en el bus (esto es el "ALUop" de la BLUE) |
| `load flags` | actualizar Z/C (en máquinas con registro de flags) |
| `Set STATE = E / F` | cambiar de fase |
| `Reset RUN` | detener la máquina (`HLT` o overflow) |

> [!example] Por qué las señales "importan" — una microoperación concreta
> `MAR ← PC` requiere **dos** señales simultáneas: `PCout` (el PC pone su contenido en el bus) y `MARin` (el MAR lo copia). Si falta `PCout`, el MAR copia **lo que esté flotando** en el bus (basura). Si falta `MARin`, el PC queda en el bus y no pasa nada. **Dos señales bien puestas = una transferencia.** Toda la computadora es eso, repetido millones de veces por segundo.

---

## 4. Cómo se organizan las señales en el tiempo (el "programa" de la UC)

Cada instrucción es una **secuencia de microórdenes** que la UC dispara pulso a pulso. Para la BLUE base:

| Instrucción | CP1 | CP2 | CP4 | CP5 | CP6 | CP8 |
|---|---|---|---|---|---|---|
| *búsqueda (todas)* | `PCout, MARin, MEMR` | `+1→Y` | `SUM, PCin` | `MBR strobe` | `MBRout, IRin` | `E→STATE` |
| LDA | `IR→MAR, MEMR` | — | `MBR strobe` | `MBR→AC` | — | `F→STATE` |
| STA | `IR→MAR` | — | `AC→MBR, MEMW` | — | — | `F→STATE` |
| ADD | `IR→MAR, MEMR` | `AC→Z` | `MBR strobe` | `MBR→Y` | — | `SUM→AC, F→STATE` |
| JMP | — | — | — | — | — | `IR→PC` |
| HLT | — | — | — | — | — | `Reset RUN` |

**Esa tabla es la UC vista como tabla.** Y esa es justamente la diferencia entre las dos formas de construirla: en la **cableada** esa tabla está hecha de compuertas; en la **microprogramada** está guardada como datos en una **memoria de control**. Ver [[Cómo se implementa la Unidad de Control]].

---

## 5. La importancia (por qué es una pregunta de examen)

1. **Sin UC la máquina no funciona**: son las señales las que permiten que un registro hable y otro escuche. Un bus sin control es un cable muerto.

2. **Coordina el tiempo**: el mismo hardware sirve para todas las instrucciones porque la UC cambia *qué* señal se activa en *cada* pulso.

3. **Define el repertorio**: cada instrucción nueva es, en el fondo, una nueva secuencia de señales.

4. **Determina la velocidad**: cuántas microórdenes por instrucción ⇒ cuántos pulsos ⇒ cuánto tarda.

5. **Es el punto donde se elige CISC o RISC**: control **microprogramado** (flexible, instrucciones complejas) o **cableado** (rápido, instrucciones simples).

---

## 6. UC en la BLUE: los detalles que la cátedra espera

- **Biestables** de la UC: **RUN** (corrida), **STATE** (F/E), **TRA** (transferencia) — y en la indexada **SI** e **I** (interrupciones).

- **Decodificación**: los 4 bits del IR entran a un **demultiplexor 1→16** (el "árbol completo de decodificación") ⇒ **16 líneas**, una por instrucción. Ese mismo circuito es el decodificador de la 3.ª tanda del final ([[Decodificador]]).

- **Señales de familia** que simplifican el diseño: `REF = LDA+STA+ADD+XOR+AND+IOR` · `ARITH = ADD+XOR+AND+IOR` · `DTA = las que traen o llevan dato`.

- **El truco de las OR**: si `Load A` viene de LDA, ADD, NOT, RAL, CSA e INP, **se juntan con una OR**; la UC es una **suma de productos** enorme.

- **La UC y la memoria**: en las máquinas microprogramadas, la UC **lee sus propias microinstrucciones de una ROM** (memoria de control). En la BLUE, en cambio, es **cableada**.

---

## 7. Cómo responderlo en el final (3–4 minutos)

**Movimiento 1 — definición (20 s).** "La UC sincroniza, decodifica, secuencia y genera las señales de control: no calcula, **manda**."

**Movimiento 2 — dibujo (60 s).** La UC al centro; entran **opcode, estado y reloj**; salen las señales `MEMR/MEMW`, `PCin/PCout`, `MARin`, `MBRout`, `IRin`, `ACin/ACout`, `ALUop`.

**Movimiento 3 — desarrollo (90 s).**

1. Las **cuatro funciones** con un ejemplo de cada una.

2. La fórmula **`estado · pulso · instrucción`** y un caso concreto (`MBR→IR` en `F·CP6`).

3. El **árbol de decodificación** 1→16 y las señales de familia (`REF`, `ARITH`, `DTA`).

4. La **importancia**: sin señales no hay transferencias; y de ella dependen cuántos pulsos tarda cada instrucción.

**Movimiento 4 — cierre (20 s).** "La UC es la que convierte una tabla de microoperaciones en cables (o en microcódigo). Si te preguntan cómo se construye, hay dos caminos: **cableada** (rápida, rígida) o **microprogramada** (flexible, más lenta)."

### Repreguntas típicas

| Repregunta | Respuesta corta |
|---|---|
| ¿La UC hace las operaciones? | No: elige **qué salida de la ALU** se habilita. Las cuentas las hace la ALU |
| ¿Cómo sabe qué instrucción llegó? | Decodifica los 4 bits del **opcode** del IR (árbol 1→16) |
| ¿Quién decide pasar a ejecución? | La UC, en **CP8 de la búsqueda**, si la instrucción referencia memoria |
| ¿Qué pasa con una instrucción que la máquina no conoce? | En un árbol de 4 bits **siempre** hay una línea activa; en la BLUE, un opcode no usado cae en NOP o en una acción indefinida; en CPUs reales ⇒ **interrupción por opcode inválido** |
| ¿Cómo se relaciona con el reloj? | La UC **no genera el tiempo**: lo usa. Con `RUN = 0` deja de aplicar señales |
| ¿Qué es una microoperación? | Una transferencia elemental (`MAR ← PC`) que ocupa un pulso |

---

## 8. Errores típicos

- Decir que la UC "ejecuta" las instrucciones: las ejecuta la máquina **bajo el control** de la UC.

- Confundir **instrucción** con **microoperación** (o **microinstrucción** en las microprogramadas).

- Olvidar el factor **estado** en las señales (decir que `IR→MAR` ocurre "en CP1", sin decir "en estado E y si la instrucción referencia memoria").

- Creer que el decodificador de instrucciones "es un programa": en la BLUE es **hardware** (1→16).

- Decir que la UC guarda los datos: no guarda nada, sólo **dirige**.

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **`blue.pdf`** (Foster) | sección **"Unidad de control"** (clasificación sincrónica/asincrónica, los biestables RUN/STATE/TRA) y **"Circuitos de la unidad de control"** (figs. 19 a 29) | el árbol de decodificación, las compuertas de cada señal, la generación de `ARITH`, `DTA`, `REF` | **Es la fuente exacta**: las figs. 20-29 son la UC de la BLUE señal por señal |
| **Apuntes de cátedra**, *Unidad 4* y *Unidad 5* | sección de unidad de control; en la U5, el **decodificador del campo modificador** | cómo la cátedra enumera las funciones y qué señales nuevas agrega la indexada | Alineación con la terminología del profesor |
| **[[Cómo se implementa la Unidad de Control]]** | la nota de la bóveda | la construcción: cableada (compuertas) vs microprogramada (ROM de control, PLA, secuenciador) + el ejemplo del 8088 | Responde el ítem de la matriz "¿cómo se implementa la UC?" |
| **[[Unidad de control cableada y microprogramada]]** | la nota de la bóveda | el microprograma de ejemplo y las ventajas/desventajas | Profundizar la alternativa microprogramada |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **control cableado** y **microprogramado** | el diseño de la sección de control, el formato de microinstrucción, el secuenciador | La referencia formal del tema |
| **Tanenbaum, *Estructura de computadores*** | capítulo de **microprogramación** | microinstrucciones, microprogramas, nanomemoria | Clara, con ejemplos de microcódigo |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo del **procesador**: control cableado vs microprogramado | cómo se implementa el control de una CPU RISC (cableado) | Para contrastar con CISC y cerrar con [[CISC y RISC]] |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **control del procesador** | funciones del control, señales internas y externas | Otra enumeración de funciones, útil para ampliar |
| **Brey, *Los microprocesadores Intel 8086/8088*** | capítulo de la **unidad de control** del 8086 | cómo un chip real genera sus señales | Ejemplo industrial |

---

## Relacionado
[[Cómo se implementa la Unidad de Control]] · [[Unidad de control cableada y microprogramada]] · [[Registros de la CPU]] · [[ALU]] · [[Ciclo de máquina]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · [[Decodificador]] · [[CISC y RISC]]
