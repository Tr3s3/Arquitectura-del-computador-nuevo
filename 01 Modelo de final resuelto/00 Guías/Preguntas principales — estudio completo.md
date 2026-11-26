---
tipo: examen
prioridad: maxima
---
# Preguntas principales — estudio completo

> [!abstract] Cómo usar este archivo
> Acá están las **8 preguntas principales** del final (las que valen la nota), cada una **desarrollada completa en este mismo archivo**: definición, qué dibujar, desarrollo, cierre y las preguntas típicas de repregunta. No hace falta abrir otras notas para estudiar cada tema; los enlaces al final de cada pregunta son solo para ampliar.
>
> El final es **oral** y se aprueba **dibujando**. Para cada pregunta: **1)** definición en una frase · **2)** dibujo en el pizarrón · **3)** desarrollo señalando el dibujo · **4)** cierre con una consecuencia.

| # | Pregunta | Ir a |
|---|---|---|
| 1 | Flujo de información (datos y direcciones) | [[#1. Flujo de información (datos y direcciones)]] |
| 2 | Formato de la instrucción (las 4 variantes) | [[#2. Formato de la instrucción (las cuatro)]] |
| 3 | Ciclo de máquina | [[#3. Ciclo de máquina]] |
| 4 | Estructura básica de un computador | [[#4. Estructura básica de un computador]] |
| 5 | Memoria RAM 8×3 | [[#5. Memoria RAM 8×3]] |
| 6 | Ciclo de ejecución: BLUE indexada y sin indexar | [[#6. Ciclo de ejecución: BLUE indexada y BLUE sin indexar]] |
| 7 | Unidad de Control | [[#7. Unidad de Control]] |
| 8 | Interrupciones | [[#8. Interrupciones]] |

> [!important] Antes de empezar: los datos que más se repiten
> - BLUE: palabra de **16 bits**, direcciones de **12 bits**, **4096** celdas. Instrucción sin indexar: `opcode 4 + dirección 12`.
> - BLUE indexada: `opcode 5 + dirección 16 + modificador 2`, **32** opcodes y **65 536** celdas.
> - Ciclo de búsqueda: **7 u 8 pulsos**. LDA sin indexar: **24 pulsos** (8 de búsqueda + 16 de ejecución).
> - Un solo bus: en cada pulso **una** fuente habilita su salida y **un** destino carga. Nunca dos fuentes a la vez.

---

## 1. Flujo de información (datos y direcciones)

**Definición.** En BLUE toda la información circula por **un bus único**. En cada pulso, **un** registro habilita su salida de tres estados y **otro** activa su `LOAD`: una transferencia por pulso. Si hubiera dos fuentes activas, se cortocircuitaría el bus.

**Qué dibujar.** Los 5 registros (PC, MAR, MBR, IR, AC) colgados del bus, la memoria arriba y la UC/ALU abajo. Dos flechas separadas: una para **direcciones** (12 bits) y otra para **datos** (16 bits).

**Desarrollo.** Hay dos flujos distintos:

- **Direcciones (12 bits, unidireccional):**
  - En la búsqueda: `PC → MAR → bus de direcciones → memoria`.
  - En la ejecución: `IR (campo dirección) → MAR → memoria`.
  - En la versión indexada se intercala el **sumador de direcciones**: `EA = D + RIF/RID`.
- **Datos (16 bits, bidireccional):**
  - Lectura de la instrucción: `memoria → MBR → IR`.
  - Lectura de un operando: `memoria → MBR → AC`.
  - Escritura: `AC → MBR → memoria`.
  - Las operaciones de la ALU no salen a memoria: `AC → ALU → AC`.

**Cierre.** El mismo bus transporta direcciones o datos; lo que define qué es cada cosa es **el uso** que se le da. Ejemplo: en `JMP`, la "dirección" que viene en la instrucción no va al MAR sino al **PC**, porque en un salto esa dirección es el dato que se carga.

**Repreguntas típicas.**
- *¿Por qué no pueden salir dos datos por el bus a la vez?* → Porque se cortocircuitan las salidas; por eso existe el buffer de tres estados.
- *¿Por qué el MBR está entre la memoria y el resto?* → Es el registro de intercambio de datos con la memoria; el MAR hace lo mismo con las direcciones.

Ampliación: [[Flujo de información en BLUE (datos y direcciones)]].

---

## 2. Formato de la instrucción (las cuatro)

**Definición.** El formato es el reparto de bits de una instrucción entre el **código de operación (opcode)** y las **direcciones** de los operandos y del resultado.

**Qué dibujar.** Las cuatro variantes como cajas de campos (OP + A1…A4), de la más larga a la más corta.

**Desarrollo.** Tomamos el mismo ejemplo en los cuatro formatos: `X = A + B`.

| Direcciones | Cómo queda | Características |
|---|---|---|
| **4** | `ADD X, A, B, prox` | Una sola instrucción. Es la más larga porque incluye la dirección de la próxima instrucción; no necesita salto. |
| **3** | `ADD X, A, B` | Formato equilibrado. Es la base de RISC. |
| **2** | `MOV X, A` + `ADD X, B` | Destruye el primer operando. Típico de CISC. |
| **1** | `LDA A` + `ADD B` + `STA X` | Usa un **acumulador implícito**. Es el formato de **BLUE**: `opcode 4 bits + dirección 12 bits`. |

**Cierre.** Es un compromiso:
- Más direcciones ⇒ instrucción más larga, pero menos instrucciones por programa.
- Menos direcciones ⇒ instrucción corta, pero más instrucciones y un registro implícito (el AC).
- Los procesadores modernos usan **3 direcciones con registros** y solo `LOAD/STORE` para acceder a memoria.

**Repreguntas típicas.**
- *¿Cuántos bits quedan para el opcode en BLUE?* → 16 − 12 = **4 bits**, es decir, 16 operaciones.
- *¿Qué es un acumulador implícito?* → Un registro que no aparece en la instrucción porque siempre es un operando y el destino (el AC).

Ampliación: [[Formato de la instrucción (4 formatos)]].

---

## 3. Ciclo de máquina

**Definición.** Es la unidad de trabajo de la CPU. Mientras `RUN = 1`, se repite para cada instrucción: **búsqueda (fetch) → decodificación → ejecución (execute)**. Se mide en pulsos, y cada pulso ejecuta una microoperación.

**Qué dibujar.** El lazo búsqueda ↔ ejecución con el estado `STATE = F / E`.

**Desarrollo.**
- **Búsqueda** (igual para toda instrucción): `MAR ← PC`, `MEMR`, `MBR ← M[MAR]`, `PC ← PC + 1`, `IR ← MBR`, decodificación del opcode, `STATE ← E`.
- **Ejecución** (depende del opcode):
  - LDA lee el operando y lo carga en el AC.
  - STA escribe el AC en memoria.
  - ADD opera en la ALU y actualiza los flags.
  - JMP carga el PC.
  - HLT pone `RUN = 0`.
- **Control:** los flip-flops **RUN** (marcha), **STATE** (F/E) y **CLOCK** (pulsos) dan la sincronía.

**Cierre.** La búsqueda es idéntica para todas las instrucciones porque, antes de decodificar, no se puede hacer nada específico. Eso permite cablearla en la UC y simplifica el diseño.

**Repreguntas típicas.**
- *¿Cuántos pulsos tiene la búsqueda?* → 7 u 8, según cómo se cuente la espera de memoria (ver [[Ciclo de búsqueda (7 y 8 pulsos)]]).
- *¿Qué pasa cuando se ejecuta HLT?* → `RUN` pasa a 0 y el ciclo se detiene.

Ampliación: [[Ciclo de máquina]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]].

---

## 4. Estructura básica de un computador

**Definición.** Cuatro unidades unidas por tres buses. Es la arquitectura **von Neumann**: una sola memoria para instrucciones y datos.

**Qué dibujar.** CPU (UC + ALU + registros) y memoria arriba, E/S abajo, y el bus en el medio, con sus tres grupos de líneas.

**Desarrollo.**
- **CPU:**
  - La **UC** decodifica y genera las señales de control.
  - La **ALU** opera y fija los flags Z y C.
  - Los **registros** guardan dirección, instrucción, dato y resultado.
- **Memoria:** guarda programa y datos; se direcciona por el bus de direcciones.
- **E/S:** interfaces y controladores. Se comunican por **polling**, **interrupciones** o **DMA**.
- **Buses:**
  - **Datos**: 16 bits, bidireccional. Su ancho define la palabra.
  - **Direcciones**: 12 bits, de la CPU hacia la memoria. Su ancho define el espacio: `2¹² = 4096` posiciones.
  - **Control**: señales como `MEMR`, `MEMW`, petición o cesión de bus, interrupción.
- Un dispositivo que comparte el bus tiene que poder ponerse en **alta impedancia**.

**Cierre.** Como hay un solo bus, no se puede traer una instrucción y un dato al mismo tiempo. Ese es el **cuello de botella de von Neumann**, y de ahí salen el pipeline, las cachés separadas y el DMA.

**Repreguntas típicas.**
- *¿Qué diferencia hay entre el bus de datos y el de direcciones?* → El de datos es bidireccional y su ancho es la palabra; el de direcciones es unidireccional y su ancho define la capacidad de memoria.
- *¿Qué es Harvard?* → Arquitectura con memorias separadas para instrucciones y datos; evita el cuello de botella.

Ampliación: [[Estructura básica de un computador]].

---

## 5. Memoria RAM 8×3

**Definición.** Memoria de **8 palabras de 3 bits**: 3 líneas de dirección (2³ = 8 posiciones), 3 líneas de datos y capacidad total de **24 bits**.

**Qué dibujar.** Decodificador 3→8, las 8 palabras de 3 flip-flops cada una, buffer de tres estados a la salida, y las líneas `CS` y `R/W'`.

**Desarrollo.**
- **Mapa de direcciones:** `000` a `111` señalan la palabra 0 a la 7. El decodificador activa **una sola** línea, que es un mintérmino de la dirección.
- **Lectura** (`CS = 1`, `R/W' = 1`): la dirección entra al decodificador → se selecciona la palabra → sus 3 bits salen por el buffer de tres estados → bus de datos.
- **Escritura** (`CS = 1`, `R/W' = 0`): dirección + dato. En el flanco, los 3 flip-flops de esa palabra cargan el dato.
- **Conexión con la CPU:** MAR (o PC) al bus de direcciones, MBR al bus de datos, y la UC genera `CS` y `R/W'`.
- **Expansión:**
  - En **horizontal** (misma dirección y CS, datos en paralelo) se agranda el ancho de palabra.
  - En **vertical** (datos y control compartidos, CS decodificado) se agregan palabras.

**Cierre.** El mismo esquema, escalado, es la memoria de BLUE: 12 bits de dirección ⇒ 4096 palabras de 16 bits.

**Repreguntas típicas.**
- *¿Cuántos bits de dirección necesita una RAM de 8 palabras?* → 3, porque log₂ 8 = 3.
- *¿Para qué sirve CS?* → Habilita el chip. Si `CS = 0`, el chip no responde aunque la dirección sea correcta.
- *¿Qué pasa si se escriben dos palabras a la vez?* → Solo se puede escribir una por ciclo: el decodificador activa una sola línea.

Ampliación: [[Memoria RAM 8x3]].

---

## 6. Ciclo de ejecución: BLUE indexada y BLUE sin indexar

**Definición.** La **búsqueda es igual** en las dos versiones. Lo que cambia es cómo se calcula la **dirección efectiva (EA)** durante la ejecución.

**Qué dibujar.** El formato nuevo (`opcode 5 | dirección 16 | modificador 2`) y el **sumador de direcciones** que recibe `D` y el índice.

**Desarrollo: sin indexar.**
`MAR ← IR(dir)` → `MEMR` → `MBR ← M[MAR]` → `AC ← MBR` → flags → `STATE ← F`.
Solo hay direccionamiento directo. Total para LDA: **24 pulsos** (8 de búsqueda + 16 de ejecución).

**Desarrollo: indexada.**
- El **modificador** de 2 bits decide el modo:
  - `00` directo: `EA = D`.
  - `01` indirecto: `EA = M[D]`, con dos accesos a memoria.
  - `10` indexado por RIF: `EA = D + RIF`.
  - `11` indexado por RID: `EA = D + RID`.
- El **decodificador del modificador** habilita el camino correcto. El **sumador de direcciones** calcula la EA y la pone en el MAR, sin usar la ALU.
- Las instrucciones nuevas `INI RIF` y `ENI RID` cargan y habilitan los índices.
- Cuenta de pulsos de LDA: **directo 24**, **indirecto 32**.

**Cierre.** La indexada no cambia la estructura del ciclo: cambia **quién calcula la dirección**. Con eso, un mismo código recorre arreglos y tablas de cualquier tamaño.

**Repreguntas típicas.**
- *¿Qué ventaja tiene la indexada?* → Recorrer arreglos con un solo código, ahorrar bits de dirección y ser reubicable.
- *¿Qué diferencia hay entre RIF y RB?* → RIF lo maneja el programador y se suma solo en los modos 2 y 3. RB lo maneja el sistema, se suma siempre y sirve para reubicar el programa.

Ampliación: [[BLUE indexada (RIF, RID, nuevo formato)]] · [[Ciclo de ejecución — todas las operaciones]] · [[BLUE vs BLUE indexada — qué cambia y por qué]].

---

## 7. Unidad de Control

**Definición.** La UC **gobierna**: decodifica el opcode del IR y genera las señales que producen las transferencias. No procesa datos.

**Qué dibujar.** La UC al centro. Entran opcode, flags y reloj; salen las señales hacia registros, ALU, memoria y buses.

**Desarrollo: las cuatro funciones.**
1. **Sincronizar** con el reloj y los pulsos.
2. **Decodificar** el opcode.
3. **Secuenciar** el orden de las microoperaciones.
4. **Generar las señales de control.**

**Desarrollo: señales, con ejemplos.**

| Señal | Efecto |
|---|---|
| `MARin` / `PCout` | `MAR ← PC` en el primer pulso de la búsqueda |
| `MEMR` / `MEMW` | lectura / escritura de memoria |
| `MBRload` / `MBRout` | el MBR toma de la memoria / entrega al bus |
| `IRin` | carga la instrucción al final de la búsqueda |
| `PCinc` / `PCin` | incremento normal / carga en un salto |
| `ALUop` + `load flags` | elige la operación y guarda Z y C |

**Por qué es importante.** Todos los demás bloques son "tontos": la ALU suma si le dicen que sume, el registro carga si su `LOAD = 1`, la memoria lee si `MEMR = 1`. **La inteligencia del computador está en la UC**: el programa se convierte en la secuencia de señales que la UC enciende pulso a pulso.

**Cierre.** En BLUE la sincronía la dan tres flip-flops: RUN, STATE (F/E) y CLOCK. Además, la UC puede ser **cableada** (rápida y rígida, típica de RISC) o **microprogramada** (flexible y más lenta, típica de CISC).

**Repreguntas típicas.**
- *¿Qué es una señal de control?* → Un bit que habilita o deshabilita una transferencia o una operación en un bloque.
- *¿Cableada o microprogramada?* → Cableada: compuertas fijas. Microprogramada: una memoria de control con microinstrucciones.

Ampliación: [[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]].

---

## 8. Interrupciones

**Definición.** Es un pedido de atención que **rompe la secuencia** del programa. La CPU termina la instrucción en curso, guarda el contexto, salta a una rutina de servicio y después retorna como si nada hubiera pasado. Existe porque la CPU es mucho más rápida que un periférico: esperarlo con **polling** es desperdiciarla.

**Qué dibujar.** Línea `INT` → CPU → "¿SI = 1?" → guardar PC → saltar a la ISR → `RETI`.

**Desarrollo: la secuencia.**
1. El periférico activa **INT**.
2. La CPU **termina** la instrucción en curso.
3. Verifica que las interrupciones estén **habilitadas** (`SI` o flag I).
4. **Guarda el contexto** (PC y flags) en la pila o en registros de respaldo.
5. **Identifica la fuente**:
   - por **polling** (consulta a cada periférico), o
   - **vectorizada**: el periférico entrega un número de vector que indexa una **tabla de vectores**.
6. Carga el PC con la dirección de la rutina y salta.
7. La rutina atiende al periférico (lee o escribe el registro de datos y baja el pedido).
8. **Restaura** el contexto y ejecuta `RETI`, que vuelve a habilitar las interrupciones.

**Clasificación y prioridades.**
- Por origen: de **hardware** (externas) o de **software** (`INT n`).
- Por máscara: **enmascarables** (se pueden deshabilitar) o **no enmascarables** (NMI, por ejemplo una falla de alimentación).
- Internas o **excepciones**: división por cero, fallo de página.
- Con varios pedidos simultáneos se resuelve por **prioridad**. En hardware, con un codificador con prioridad o un controlador de interrupciones; en software, con el orden de polling. Una interrupción de mayor prioridad puede **anidarse** sobre otra.

**En BLUE.** `SI` habilita o deshabilita; `INT` es el pedido; `INTACK` es el reconocimiento. La UC pasa por los estados **F / E / I** (búsqueda, ejecución, interrupción).

**Cierre.** Lo que hace útil a la interrupción es que sea **transparente** para el programa. Por eso es crítico guardar el PC (que ya apunta a la instrucción siguiente) y restaurarlo.

**Repreguntas típicas.**
- *¿Por qué se guarda el PC?* → Para volver a la instrucción siguiente al terminar la rutina.
- *¿Qué diferencia hay entre polling e interrupción?* → Con polling la CPU pregunta todo el tiempo; con interrupción, el periférico avisa cuando lo necesita.
- *¿Qué es la tabla de vectores?* → La tabla donde está la dirección de cada rutina de servicio, indexada por el número de vector.

Ampliación: [[Interrupciones y entrada-salida]].

---

> [!warning] Si la mesa pregunta por los códigos de operación
> La **tabla oficial de la cátedra** es la octal del apunte de Foster, la misma que usa la BLUE indexada:
>
> | Octal | Instrucción | Octal | Instrucción |
> |---|---|---|---|
> | `00` | HLT | `10` | SRJ |
> | `01` | ADD | `11` | JMA |
> | `02` | XOR | `12` | JMP |
> | `03` | AND | `13` | INP |
> | `04` | IOR | `14` | OUT |
> | `05` | NOT | `15` | RAL |
> | `06` | LDA | `16` | CSA |
> | `07` | STA | `17` | NOP |
>
> El **simulador del TP16 usa otra numeración**, decimal y simplificada (`1` cargar, `5` sumar, `2` o `3` almacenar, `C` parar). Es una ayuda didáctica, **no** la tabla de la máquina.
>
> *Cómo decirlo sin trabarse:* "Según el simulador del TP los códigos son 1, 5, 2 y C. Según la tabla octal de la máquina, `06` es LDA, `01` es ADD, `07` es STA y `00` es HLT. Para el ciclo de pulsos uso la tabla octal."

## Frases de cierre (sirven para cualquier pregunta)

1. "Todo pasa por **un bus único**, y en cada pulso **uno habla y los demás escuchan**."
2. "La **UC** no hace cuentas: **manda**. La que hace cuentas es la **ALU**."
3. "La instrucción dice **qué** hacer; el **modo de direccionamiento** dice **dónde** está el dato."
4. "La memoria es un **vector**: la dirección es el índice de la celda, y el decodificador elige la fila."
5. "Si el dato no está en el camino, se lo **busca**; si está, se lo **ejecuta**: búsqueda y ejecución."

## Checklist antes de sentarse

- [ ] Sé qué dibujar para cada una de las 8 preguntas.
- [ ] Sé explicar la RAM 8×3 de punta a punta: dirección → decodificador → celda → salida.
- [ ] Puedo contar el ciclo de búsqueda (7 u 8 pulsos) y el LDA (24 pulsos).
- [ ] Tengo una frase de cierre para cada tema.
- [ ] Si me preguntan algo que no está, lo conecto con lo que sí sé.

## Relacionado

[[Guion de respuestas — preguntas principales]] · [[Banco de preguntas del final]] · [[00 Matriz del final — las 3 tandas]] · [[Cómo dibujar los circuitos (checklist de pizarrón)]] · [[Tablas de verdad de memoria]]
