---
tipo: examen
---
# Guion de respuestas — preguntas principales

> [!abstract] Cómo usar esta nota
> Son las 8 respuestas **completas y ordenadas**, pensadas para decirlas en 2–3 minutos mientras dibujás.
> La estructura es siempre la misma: **definición → dibujo → desarrollo → cierre con una consecuencia**.
> Si te trabás, volvé al esquema: la nota de cada pregunta está linkeada.

> [!warning] El final es **oral** y se aprueba **dibujando**
> No recite: **dibuje y explique lo que dibuja**. Cada respuesta de este guion tiene cuatro movimientos:
> **1) la definición en una frase** (10 s) · **2) el dibujo en el pizarrón** (40 s, trazo grande y de
> izquierda a derecha) · **3) el desarrollo hablado señalando el dibujo** (60–90 s) · **4) el cierre con una
> consecuencia** (10 s). Si se queda sin palabras, **vuelva al dibujo**: cada bloque que dibujó es una frase.
> Antes de entrar, repase [[Cómo dibujar los circuitos (checklist de pizarrón)]] y
> [[Tablas de verdad de memoria]].

| # | Pregunta | Minutos | Qué dibujar | Tabla que conviene tener a mano |
|---|---|---|---|---|
| 1 | Flujo de información | 3 | 5 registros colgados del bus + memoria + ALU | — |
| 2 | Formato de la instrucción | 3 | las 4 cajas de campos, de la más larga a la más corta | — |
| 3 | Ciclo de máquina | 2 | bucle búsqueda–ejecución con STATE F/E | — |
| 4 | Estructura básica | 3 | CPU + memoria + E/S con los 3 buses | — |
| 5 | RAM 8×3 | 4 | decodificador 3→8 + 8 celdas + CS/R-W' | tabla de la RAM |
| 6 | BLUE indexada / sin indexar | 4 | camino de datos y después el sumador de direcciones | — |
| 7 | Unidad de Control | 3 | UC al centro: IR/CLOCK/flags entran, señales salen | — |
| 8 | Interrupciones | 3 | línea INT → guardar PC → ISR → RETI | estados F/E/I |

---

## 1. Flujo de información (dato y direcciones)

**Definición.** En BLUE toda la información circula por **un bus único**. En cada pulso, **un** registro
habilita su salida de tres estados y **otro** activa su `LOAD`: una transferencia por pulso, nunca dos
fuentes a la vez (se cortocircuitaría el bus).

**Dibujo.** Los 5 registros (PC, MAR, MBR, IR, AC) colgando del bus, con la memoria arriba y la UC/ALU abajo.
→ ![blue_flujo](../assets/blue_flujo.svg)

**Desarrollo.** Hay dos flujos:
- **Direcciones (12 bits, unidireccional):** `PC → MAR → bus de direcciones → memoria` en la búsqueda;
  `IR(campo dirección) → MAR → memoria` en la ejecución. En la versión indexada se intercala el
  **sumador de direcciones** (`EA = D + RIF/RID`).
- **Datos (16 bits, bidireccional):** `memoria → MBR → IR` (la instrucción) o `memoria → MBR → AC`
  (el operando); y `AC → MBR → memoria` al escribir. Las operaciones de la ALU no salen a memoria:
  `AC → ALU → AC`.

**Cierre.** El mismo bus transporta direcciones o datos: lo que define qué es cada cosa es **el uso** que
se le da. El ejemplo perfecto es `JMP`: la "dirección" que viene en la instrucción no va al MAR sino al PC,
porque en un salto esa dirección **es** el dato que se carga.

→ Nota completa: [[Flujo de información en BLUE (datos y direcciones)]]

---

## 2. Formato de la instrucción (las cuatro)

**Definición.** El formato es el reparto de bits entre el **opcode** y las **direcciones** de los operandos
y del resultado.

**Dibujo.** Los cuatro formatos con sus campos (OP + A1…A4).

**Desarrollo.** Ejemplo `X = A + B`:
- **4 direcciones:** `ADD X, A, B, prox` — 1 instrucción, la más larga (incluye la próxima dirección: no
  necesita instrucción de salto).
- **3 direcciones:** `ADD X, A, B` — el más equilibrado; base de RISC.
- **2 direcciones:** `MOV X, A` + `ADD X, B` — destruye el primer operando; típico de CISC.
- **1 dirección:** `LDA A` + `ADD B` + `STA X` — acumulador implícito; es el de **BLUE**
  (`opcode 4 bits + dirección 12 bits`).

**Cierre.** Es un compromiso: más direcciones ⇒ instrucción más larga y menos instrucciones por programa;
menos direcciones ⇒ instrucción corta, pero más instrucciones y un registro implícito (el AC). Los
procesadores modernos eligen **3 direcciones con registros** y sólo `LOAD/STORE` para memoria.

→ Nota completa: [[Formato de la instrucción (4 formatos)]]

---

## 3. Ciclo de máquina

**Definición.** Es la unidad de trabajo de la CPU: mientras `RUN = 1`, se repite **búsqueda (fetch) →
decodificación → ejecución (execute)** para cada instrucción. Se mide en pulsos y cada pulso ejecuta una
microoperación.

**Dibujo.** El lazo búsqueda ↔ ejecución con STATE = F / E.

**Desarrollo.**
- **Búsqueda (fija para toda instrucción):** `MAR ← PC`, `MEMR`, `MBR ← M[MAR]`, `PC ← PC+1`, `IR ← MBR`,
  decodificación del opcode, `STATE ← E`.
- **Ejecución (depende del opcode):** LDA lee el operando y lo carga en el AC; STA escribe el AC; ADD opera
  en la ALU y actualiza flags; JMP carga el PC; HLT pone `RUN = 0`.
- **Control:** los flip-flops **RUN** (marcha), **STATE** (F/E) y **CLOCK** (pulsos) le dan la sincronía.

**Cierre.** La búsqueda es idéntica para todas las instrucciones porque antes de decodificar no se puede
hacer nada específico: eso permite "cablearla" en la UC y simplifica el diseño.

→ Nota completa: [[Ciclo de máquina]]

---

## 4. Estructura básica de un computador (unidades y buses)

**Definición.** Cuatro unidades unidas por tres buses. Es la arquitectura **von Neumann**: una sola memoria
para instrucciones y datos.

**Dibujo.** CPU (UC + ALU + registros) y memoria arriba, E/S abajo, bus en el medio.

**Desarrollo.**
- **CPU:** la **UC** decodifica y genera las señales de control; la **ALU** opera (y fija los flags Z, C);
  los **registros** guardan dirección, instrucción, dato y resultado.
- **Memoria:** guarda programa y datos; se direcciona por el bus de direcciones.
- **E/S:** interfaces y controladores; se comunica por polling, interrupciones o DMA.
- **Buses:** **datos** 16 bits (bidireccional), **direcciones** 12 bits (CPU → memoria), **control**
  (señales como MEMR, MEMW). La anchura de datos define la palabra; la de direcciones define el espacio
  (`2¹² = 4096`). Un dispositivo que comparte el bus debe poder ponerse en **alta impedancia**.

**Cierre.** La consecuencia es el **cuello de botella de von Neumann**: como hay un solo bus, no se puede
traer una instrucción y un dato al mismo tiempo; de ahí el pipeline, las cachés separadas y el DMA.

→ Nota completa: [[Estructura básica de un computador]]

---

## 5. Memoria RAM 8×3

**Definición.** 8 palabras de 3 bits: 3 líneas de dirección (2³ = 8 posiciones), 3 líneas de datos,
capacidad **24 bits**.

**Dibujo.** Decodificador 3→8, 8 palabras de 3 flip-flops, buffer de tres estados, CS y R/W'.

**Desarrollo.**
- **Mapa de direcciones:** 000 a 111 señalan la palabra 0 a 7. El decodificador activa **una** línea (un
  mintérmino de la dirección).
- **Lectura:** dirección → decodificador → palabra seleccionada vuelca sus 3 bits → buffer de tres estados →
  bus de datos. Con `CS = 1` y `R/W' = 1`.
- **Escritura:** dirección + dato, `CS = 1` y `R/W' = 0`; en el flanco, los 3 FF de esa palabra cargan el dato.
- **Conexión a la CPU:** MAR (o el PC) al bus de direcciones, MBR al bus de datos y la UC dando CS y R/W'.
- **Expansión:** en horizontal (misma dirección y CS, datos en paralelo) se agranda el ancho; en vertical
  (datos y control compartidos, CS decodificado) se agregan palabras.

**Cierre.** El mismo esquema, escalado, es la memoria de BLUE: 12 bits de dirección ⇒ 4096 palabras de 16 bits.

→ Nota completa: [[Memoria RAM 8x3]]

---

## 6. Ciclo de ejecución de BLUE indexada y sin indexar

**Definición.** La **búsqueda es igual** en las dos versiones; lo que cambia es cómo se calcula la
**dirección efectiva** en la ejecución.

**Dibujo.** El formato nuevo (`opcode 5 | dirección 16 | modificador 2`) y el sumador de direcciones.

**Desarrollo — sin indexar:**
`MAR ← IR(dir)` → `MEMR` → `MBR ← M[MAR]` → `AC ← MBR` → flags → `STATE ← F`. Sólo hay direccionamiento
directo. Total para LDA: 24 pulsos (8 + 16).

**Desarrollo — indexada:**
- El **modificador** de 2 bits decide: `00` directo (`EA = D`), `01` indirecto (`EA = M[D]`, dos accesos),
  `10` indexado por RIF (`EA = D + RIF`), `11` indexado por RID.
- El **decodificador del modificador** habilita el camino; el **sumador de direcciones** calcula la EA y la
  pone en el MAR (no gasta un pulso de ALU).
- Las instrucciones nuevas `INI RIF` / `ENI RID` cargan y habilitan los índices.
- En el ciclo, el pulso donde "se arma la dirección" pasa de copiar el campo del IR a **sumarlo con el
  índice**; en el indirecto se agrega un acceso completo a memoria.

**Cierre.** La indexada no cambia la estructura del ciclo: cambia **quién calcula la dirección**. Con eso
un mismo código recorre arreglos y tablas de cualquier tamaño.

→ Notas: [[BLUE indexada (RIF, RID, nuevo formato)]] · [[Ciclo de ejecución — todas las operaciones]]

---

## 7. Unidad de Control: funciones, señales de control e importancia

**Definición.** La UC **gobierna**: decodifica el opcode del IR y genera las señales que producen las
transferencias. No procesa datos.

**Dibujo.** UC en el centro, con opcode/flags/reloj como entradas y las señales saliendo hacia registros,
ALU, memoria y buses.

**Desarrollo — cuatro funciones:** sincronizar (reloj y pulsos), decodificar (opcode), secuenciar (orden de
microoperaciones) y generar las señales de control.

**Desarrollo — señales (con ejemplo):**

| Señal | Efecto |
|---|---|
| `MARin` / `PCout` | `MAR ← PC` en el primer pulso de la búsqueda |
| `MEMR` / `MEMW` | lectura / escritura de memoria |
| `MBRload` / `MBRout` | el MBR toma de la memoria / entrega al bus |
| `IRin` | carga la instrucción al final de la búsqueda |
| `PCinc` / `PCin` | incremento normal / carga en un salto |
| `ALUop` + `load flags` | elige la operación y guarda Z y C |

**Por qué son importantes.** Todos los bloques son "tontos": la ALU suma si le dicen que sume, el registro
carga si su `LOAD = 1`, la memoria lee si `MEMR = 1`. **La inteligencia del computador está en la UC**: el
programa se convierte en la secuencia de señales que la UC enciende pulso a pulso.

**Cierre.** En BLUE la sincronía son tres flip-flops: RUN, STATE (F/E) y CLOCK. Y la UC puede ser **cableada**
(rápida, rígida: RISC) o **microprogramada** (flexible, más lenta: CISC).

→ Nota completa: [[Unidad de Control]]

---

## 8. Interrupciones

**Definición.** Es un pedido de atención que **rompe la secuencia** del programa. La CPU termina la
instrucción en curso, guarda el contexto, salta a una rutina de servicio y luego retorna como si nada.
Existe porque la CPU es millones de veces más rápida que un periférico: esperarlo (**polling**) es
desperdiciarla.

**Dibujo.** Línea INT → CPU → "¿SI = 1?" → guardar PC → saltar a la ISR → RETI.

**Desarrollo — secuencia:**
1. El periférico activa **INT**.
2. La CPU **termina** la instrucción en curso.
3. Verifica que las interrupciones estén **habilitadas** (`SI` / flag I).
4. **Guarda el contexto** (PC y flags) en la pila o registros de respaldo.
5. **Identifica la fuente**: por *polling* (consulta a cada periférico) o **vectorizada** (el periférico
   entrega el número de vector, que indexa una **tabla de vectores**).
6. Carga el PC con la dirección de la rutina y salta.
7. La rutina atiende (lee/escribe el registro de datos, baja el pedido).
8. **Restaura** el contexto y ejecuta `RETI`, que rehabilita las interrupciones.

**Clasificación y prioridades.** De hardware (externas) o de software (`INT n`); **enmascarables** (se
pueden deshabilitar) o **no enmascarables** (NMI: falla de alimentación); internas o **excepciones**
(división por cero, fallo de página). Con varios pedidos simultáneos se resuelve por **prioridad**
(hardware: codificador con prioridad / controlador de interrupciones; software: orden de polling), y una de
mayor prioridad puede **anidar** sobre otra.

**En BLUE.** `SI` habilita/deshabilita, `INT` es el pedido, `INTACK` el reconocimiento, y el estado de la UC
pasa por **F / E / I** (búsqueda, ejecución, interrupción).

**Cierre.** Lo que hace que la interrupción sea útil es ser **transparente**: por eso es crítico guardar el
PC (que ya apunta a la instrucción siguiente) y restaurarlo.

→ Nota completa: [[Interrupciones y entrada-salida]]

---

## Si la mesa pregunta por los códigos de operación

> [!warning] Discrepancia real entre la cátedra y el mapa de la máquina BLUE
> Hay **tres** conjuntos de códigos circulando en el material, y conviene tenerlos claros para no trabarse:
>
> | Instrucción | Simulador del [[TP16 Ciclo de instrucción básico]] (decimal) | Mapa BLUE de la cátedra (hex) | Tabla de 16 opcodes (binario) |
> |---|---|---|---|
> | Cargar | `1` | `1` | `LDA 0000` |
> | Sumar | `5` | `5` | `ADD` (uno de los 16) |
> | Almacenar | `2` (y `3` en el TP16) | `2`/`3` | `STA` |
> | Fin | `C` (hex 12) | `C` = **parar** | `HLT 1110` |
>
> **Cómo manejarlo en el oral (esto es lo que se hace):** primero se dice **"en el material de la cátedra el
> código de parar es C"**, y recién después se muestra la tabla de 16 opcodes. No se corrige al profesor ni
> se inventa una tercera versión: se **aclara la fuente** ("según el simulador…", "según el mapa…") y se sigue
> con la secuencia de microoperaciones, que es lo que se evalúa.
> El desarrollo completo está en [[TP16 Ciclo de instrucción básico]] y [[TP20 Lenguaje máquina]].

## Las cinco frases que cierran cualquier respuesta

1. "Todo pasa por **un bus único**, y en cada pulso **uno habla y los demás escuchan**."
2. "La **UC** no hace cuentas: **manda**; la que hace cuentas es la **ALU**."
3. "La instrucción dice **qué** hacer; el **modo de direccionamiento** dice **dónde** está el dato."
4. "La memoria es un **vector**: dirección = índice de la celda, y el decodificador elige la fila."
5. "Si el dato no está en el camino, se lo **busca**; si está, se lo **ejecuta**: búsqueda y ejecución."

## Antes de sentarse (checklist de 60 segundos)
- [ ] Tengo claro **cuál es el dibujo** de cada una de las 8 principales.
- [ ] Sé decir la **tabla de verdad del sumador completo** sin mirar (8 filas).
- [ ] Sé explicar la **RAM 8×3** de punta a punta (dirección → decodificador → celda → salida).
- [ ] Puedo contar el **ciclo de búsqueda** en 7 pulsos y el **LDA** en 24.
- [ ] Tengo una **frase de cierre** para cada tema (las de arriba).
- [ ] Si me preguntan algo que no está: lo **conecto** con lo que sí sé (los TPs del
  [[00 Índice de TPs y qué aporta cada uno|índice]] cubren casi todo el plan).
