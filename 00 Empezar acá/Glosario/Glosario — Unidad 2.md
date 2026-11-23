---
tipo: glosario
unidad: 2
---
# Glosario — Unidad 2: memorias y circuitos secuenciales

> [!abstract] Qué hay acá
> Las **34 fichas** de la unidad: biestables y flip-flops, registros y contadores, la celda de memoria, los tipos de RAM y ROM, la jerarquía con la caché y la memoria virtual, y la detección de errores. Índice alfabético en [[Glosario]].

## Biestables y flip-flops

### Biestable (latch) RS
**Qué es.** Circuito secuencial de **dos compuertas cruzadas** (NOR o NAND) que memoriza **1 bit** mientras tenga alimentación. **Para qué sirve.** Es la **unidad de memoria** más simple: de acá salen los registros, los contadores y las celdas de SRAM. **Características.** · Dos estados estables (`Q = 0` y `Q = 1`) · entradas `S` (set) y `R` (reset) · en la versión con NOR, `S = R = 1` es **estado prohibido** · es **asincrónico**: responde mientras la entrada está activa. **Se estudia en** [[2.1.1 Biestable RS (NOR y NAND)]].

### Nivel y flanco
**Qué es.** Un circuito es **sensible al nivel** si actúa mientras el reloj está en 1 (o en 0), y **sensible al flanco** si actúa sólo en la **transición** (subida o bajada). **Para qué sirve.** El flanco permite que **todos** los flip-flops de un registro cambien en el **mismo instante**, sin carreras. **Características.** · **Latch** = nivel · **flip-flop** = flanco · el símbolo lleva un **triángulo** en la entrada de reloj cuando es por flanco · `CLK` con círculo = flanco de bajada. **Se estudia en** [[2.1.1 Biestable RS (NOR y NAND)]].

### Flip-flop D
**Qué es.** Flip-flop que **copia** la entrada en el flanco: `Q⁺ = D`. **Para qué sirve.** Es el que se usa en **registros y memorias**: guardar un dato es ponerlo en `D` y dar un pulso. **Características.** · No tiene estado prohibido · con una entrada **enable** se convierte en celda de registro (`Q⁺ = E·D + E'·Q`) · dos latches en serie (maestro-esclavo) lo hacen sensible al flanco. **Se estudia en** [[2.1.2 Flip-flops D y T]].

### Flip-flop T
**Qué es.** Flip-flop que **alterna** cuando `T = 1` y mantiene cuando `T = 0`: `Q⁺ = T ⊕ Q`. **Para qué sirve.** **Contar**: con `T = 1` fijo divide la frecuencia por 2, y encadenando varios se arma un contador binario. **Características.** · Es un JK con `J = K = T` · la salida cambia a **la mitad** de la frecuencia de entrada · `n` flip-flops T en cascada cuentan hasta `2ⁿ`. **Se estudia en** [[2.1.2 Flip-flops D y T]].

### Flip-flop JK
**Qué es.** Flip-flop con dos entradas que **setea** (`J = 1, K = 0`), **resetea** (`J = 0, K = 1`), **mantiene** (`0,0`) y **alterna** (`1,1`). **Para qué sirve.** Es el más versátil: **elimina el estado prohibido** del RS y sirve para memoria y para conteo. **Características.** · `Q⁺ = J·Q' + K'·Q` · `J = K = 1` **no** es un problema: alterna · es la base de los flip-flops de las familias TTL (7476, 74112). **Se estudia en** [[2.1.3 Flip-flop JK y ecuaciones características]].

### Ecuación característica
**Qué es.** Fórmula que dice cómo queda el estado siguiente (`Q⁺`) en función de las entradas y del estado actual. **Para qué sirve.** Analizar y **diseñar** circuitos secuenciales sin dibujar la tabla completa cada vez. **Características.** · `D: Q⁺ = D` · `T: Q⁺ = T ⊕ Q` · `JK: Q⁺ = JQ' + K'Q` · `RS: Q⁺ = S + R'Q` (con `S·R = 0`). **Se estudia en** [[2.1.3 Flip-flop JK y ecuaciones características]].

### Tabla de estados y de excitación
**Qué es.** La **de estados** dice qué pasa con `Q` para cada entrada; la de **excitación** dice **qué entrada hay que poner** para pasar de un estado a otro. **Para qué sirve.** La de excitación es la que se usa para **diseñar** (por ejemplo, convertir un JK en D o armar un contador con flip-flops dados). **Características.** · Estados: `Q(t) → Q(t+1)` · excitación: al revés (`0→0` en D pide `D = 0`) · se resuelve con mapas de Karnaugh para cada entrada. **Se estudia en** [[2.1.4 Conversión entre biestables]].

### Conversión entre biestables
**Qué es.** Armar un tipo de flip-flop con otro: por ejemplo, un D usando un JK. **Para qué sirve.** Aprovechar el flip-flop que hay en el laboratorio (o el más barato) para la función que se necesita. **Características.** · Se iguala la ecuación del que **tengo** con la del que **quiero** y se despejan las entradas · `JK → D`: `J = D, K = D'` · `D → T`: `T = D ⊕ Q` · siempre se usan compuertas combinacionales alrededor. **Se estudia en** [[2.1.4 Conversión entre biestables]].

## Registros y contadores

### Registro
**Qué es.** Conjunto de `n` flip-flops con el **mismo reloj** que guarda una palabra de `n` bits. **Para qué sirve.** Guardar datos y moverlos: son el `AC`, el `IR`, el `MAR` de la CPU. **Características.** · Comparten `CLK`, y a veces `CLR` y `LOAD` · según cómo entren y salgan los bits se llaman PIPO, SISO, SIPO o PISO · un registro con desplazamiento puede **multiplicar o dividir por 2**. **Se estudia en** [[2.2.1 Registros PIPO y SISO]].

### PIPO y SISO
**Qué es.** **PIPO**: entrada y salida en **paralelo** (todo a la vez). **SISO**: entrada y salida **en serie** (bit por bit). **Para qué sirve.** PIPO para mover palabras dentro de la máquina; SISO para **retardar** o transmitir por un solo cable. **Características.** · PIPO: `n` bits en **1 pulso** · SISO: `n` bits en **n pulsos** · el PIPO es la carga del `IR` (`CP6: MBR → IR` en la BLUE). **Se estudia en** [[2.2.1 Registros PIPO y SISO]].

### SIPO y PISO
**Qué es.** **SIPO**: entra en serie, sale en paralelo. **PISO**: entra en paralelo, sale en serie. **Para qué sirve.** **Convertir** entre serie y paralelo: es la base de un `UART` (RS-232, USB). **Características.** · SIPO: 4 pulsos para tener la palabra completa · PISO: 1 pulso para cargar y `n` para sacar · los dos juntos hacen un **transmisor-receptor** completo. **Se estudia en** [[2.2.2 Registros SIPO y PISO]].

### Contador
**Qué es.** Registro que recorre una **secuencia** de estados con cada pulso de reloj. **Para qué sirve.** Contar eventos, dividir frecuencia, generar direcciones y tiempo. **Características.** · **Asincrónico** (*ripple*): cada flip-flop dispara al anterior (más lento, retardo acumulado) · **sincrónico**: todos con el mismo reloj (más rápido) · puede contar **ascendente, descendente** o **cargable**. **Se estudia en** [[2.2.3 Contadores binarios y módulo N]].

### Contador módulo N
**Qué es.** Contador que cuenta `N` estados y vuelve a empezar (no tiene por qué ser `2ⁿ`). **Para qué sirve.** Contar segundos (`N = 60`), dígitos (`N = 10`) o cualquier ciclo arbitrario. **Características.** · Necesita `n` flip-flops con `2ⁿ ≥ N` · se detecta el estado `N` y se resetea · ejemplo: módulo 6 con 3 flip-flops, detectando `110` con una NAND. **Se estudia en** [[2.2.3 Contadores binarios y módulo N]].

## La celda y el chip de memoria

### Celda de memoria
**Qué es.** Circuito que guarda **1 bit** y tiene cuatro partes: biestable, selección, lectura/escritura y buffer de 3 estados. **Para qué sirve.** Es el átomo de toda memoria: `n` celdas por palabra × cantidad de palabras = capacidad. **Características.** · El **buffer de 3 estados** la desconecta del bus cuando no se la lee (si no, todas hablarían a la vez) · la selección viene del decodificador de direcciones · `WE = 1` escribe, `WE = 0` lee. **Se estudia en** [[2.3.1 Celda elemental de memoria]].

### SRAM y DRAM
**Qué es.** Las dos tecnologías de RAM: **SRAM** = 6 transistores (latch), **DRAM** = 1 transistor + 1 capacitor. **Para qué sirve.** SRAM para lo **rápido y chico** (caché, registros); DRAM para lo **grande y barato** (memoria principal). **Características.** · SRAM: rápida, **no** necesita refresco, cara, 6× más área por bit · DRAM: lenta, **necesita refresco** (cada celda cada 64 ms), densa y barata · las dos son **volátiles**. **Se estudia en** [[2.3.2 SRAM y DRAM]].

### Refresco
**Qué es.** Reescritura periódica de cada fila de una DRAM, porque el capacitor se descarga solo. **Para qué sirve.** Que el dato no se pierda sin alimentación constante. **Características.** · Una fila cada `64 ms / cantidad de filas` (ej.: 4096 filas ⇒ cada 15,6 µs) · lo hace un **contador de refresco** del propio chip · **roba ciclos** al bus (baja el rendimiento). **Se estudia en** [[2.3.2 SRAM y DRAM]].

### Organización 2D y 3D
**Qué es.** Formas de ubicar las celdas: **2D** = una sola línea de selección (matriz simple, memorias chicas); **3D** = dos líneas de selección (fila y columna) con decodificadores separados. **Para qué sirve.** Direccionar mucha capacidad con pocos pines: con `m` bits de dirección en 3D se accede a `2^m` celdas usando dos decodificadores más chicos. **Características.** · 3D usa **dos** líneas de selección simultáneas (fila **y** columna) · es lo que permite los chips actuales · 2½D agrega un decodificador intermedio. **Se estudia en** [[2.3.3 Matriz, expansión y RAM 8x3]].

### Expansión de memoria y chip select
**Qué es.** Unir varios chips para lograr **más palabras** (expansión de palabra) o **palabras más anchas** (expansión de bit), y elegir cuál responde con la señal **`CS`**. **Para qué sirve.** Construir un módulo de memoria del tamaño que pida el diseño. **Características.** · Para duplicar palabras: un bit más de dirección que va al **decodificador de `CS`** · para duplicar el ancho: los chips comparten dirección y cada uno aporta sus bits de dato · con `CS = 1` el chip queda desconectado. **Se estudia en** [[2.3.3 Matriz, expansión y RAM 8x3]].

## ROM y memorias no volátiles

### ROM
**Qué es.** Memoria de **sólo lectura**: el contenido se fija al fabricar el chip. **Para qué sirve.** Guardar lo que no cambia: firmware, tablas de verdad, el microprograma de la unidad de control. **Características.** · Internamente es un **decodificador + matriz OR** · no volátil · no se puede reescribir · las versiones programables son PROM, EPROM, EEPROM y flash. **Se estudia en** [[2.4.1 ROM = decodificador + OR]].

### PROM, EPROM, EEPROM y Flash
**Qué es.** Las ROM **programables**: PROM (una vez), EPROM (se borra con luz UV), EEPROM (se borra **eléctricamente** por byte) y **flash** (se borra por **bloques**). **Para qué sirve.** Tener memoria no volátil **actualizable**: el firmware, la BIOS/UEFI, un pen drive, un SSD. **Características.** · EPROM se programa con `VPP` ≈ 12,5 V y se borra entera · EEPROM es lenta y cara pero byte a byte · **flash** combina densidad y borrado eléctrico por sectores · la celda es un transistor con **compuerta flotante**. **Se estudia en** [[2.4.2 PROM, EPROM, EEPROM y Flash]].

## Jerarquía y caché

### Jerarquía de memoria
**Qué es.** Escalonamiento **registros → caché → memoria principal → disco** donde arriba hay poca capacidad y mucha velocidad, y abajo al revés. **Para qué sirve.** Lograr casi la velocidad de la SRAM con el costo de la DRAM: el programa "ve" una memoria grande y rápida. **Características.** · Cada nivel es **caché** del siguiente · funciona gracias a la **localidad** · `AMAT` mide la mezcla. **Se estudia en** [[2.5.1 Jerarquía y localidad]].

### Localidad (temporal y espacial)
**Qué es.** Propiedad de los programas: **temporal** = lo que se usó se vuelve a usar pronto; **espacial** = lo que está al lado se usa después. **Para qué sirve.** Es la **justificación** de toda la jerarquía: sin localidad, la caché no serviría de nada. **Características.** · Temporal: contadores de un bucle, variables activas · espacial: arreglos recorridos, instrucciones consecutivas · el tamaño de bloque/línea explota la espacial. **Se estudia en** [[2.5.1 Jerarquía y localidad]].

### Caché, línea y bloque
**Qué es.** **Caché**: memoria SRAM chica y rápida que copia partes de la principal. **Línea (o bloque)**: la unidad que se copia y se trae/expulsa de una vez. **Para qué sirve.** Evitar ir a la memoria principal: si el dato está en la caché, se entrega en 1-3 ciclos. **Características.** · Se direcciona por **etiqueta + conjunto + desplazamiento** · se trae la **línea completa** (32-64 B) aunque se pida 1 byte · acierto (*hit*)/fallo (*miss*). **Se estudia en** [[2.5.2 Caché, mapeos y políticas]].

### Mapeos: directo, asociativo y por conjuntos
**Qué es.** Dónde puede ir a parar un bloque de la memoria principal dentro de la caché. **Para qué sirve.** Decidir el compromiso entre **velocidad de búsqueda** y **flexibilidad** de colocación. **Características.** · **Directo**: un solo lugar posible (1 comparación, pero conflictos) · **asociativo total**: cualquier lugar (comparación con todas las etiquetas, en paralelo) · **por conjuntos de `k` vías**: `k` lugares (el que usan todas las PC). **Se estudia en** [[2.5.2 Caché, mapeos y políticas]].

### Políticas de escritura y de reemplazo
**Qué es.** **Escritura**: `write-through` (escribe en caché **y** en memoria) o `write-back` (sólo en caché, marca la línea "sucia" y la baja después). **Reemplazo**: qué línea se sacrifica (LRU, FIFO, aleatorio). **Para qué sirve.** Mantener la coherencia y decidir qué se pierde cuando la caché está llena. **Características.** · `write-through` es simple pero genera más tráfico · `write-back` es el estándar · **LRU** (la menos usada recientemente) es la más efectiva y la más cara de implementar. **Se estudia en** [[2.5.2 Caché, mapeos y políticas]].

### AMAT
**Qué es.** *Average Memory Access Time*: el tiempo promedio de un acceso, `AMAT = h + m × P` (acierto + tasa de fallos × penalidad). **Para qué sirve.** Medir si la caché **sirve** y cuánto mejora el sistema. **Características.** · Se expresa en ciclos · ejemplo: `h = 1`, `m = 0,05`, `P = 100` ⇒ **6 ciclos**, contra 100 sin caché · agregar un segundo nivel baja el `AMAT`, no el `h`. **Se estudia en** [[2.5.3 AMAT y cálculo de mejora]].

## Memoria virtual y memorias complementarias

### Memoria virtual y paginación
**Qué es.** Técnica que da a cada programa un espacio de direcciones **falso** (virtual), traducido a direcciones **físicas** por páginas de tamaño fijo. **Para sirve.** Permitir programas más grandes que la RAM, aislar procesos y compartir memoria. **Características.** · La dirección se parte en **VPN + desplazamiento** (12 bits para páginas de 4 KB) · la traducción la hace la **MMU** con la **tabla de páginas** · si la página no está en RAM se produce un **fallo de página** (va al disco). **Se estudia en** [[2.6.1 Memoria virtual y paginación]].

### MMU y TLB
**Qué es.** **MMU**: unidad que traduce direcciones. **TLB**: caché **asociativa** de esas traducciones. **Para qué sirve.** Que traducir no cueste un acceso a memoria en **cada** instrucción. **Características.** · TLB de 64-1024 entradas, búsqueda en **1 ciclo** · si falla, hay que ir a la tabla de páginas (1 acceso extra o más) · acierto típico > 90 %. **Se estudia en** [[2.6.1 Memoria virtual y paginación]].

### Memoria asociativa (CAM)
**Qué es.** Memoria que se busca **por contenido** y no por dirección: se compara la clave contra **todas** las entradas a la vez. **Para qué sirve.** Búsquedas en un ciclo: TLB, tablas de ruteo, cachés asociativas. **Características.** · Comparación **en paralelo** con hardware por celda · es **cara** (muchos transistores por bit) ⇒ se usa chica · la memoria auxiliar (disco/SSD) es lo contrario: grande, lenta, no volátil. **Se estudia en** [[2.6.2 Memoria auxiliar y memoria asociativa]].

## Detección y corrección de errores

### Paridad
**Qué es.** Un bit extra que hace que la cantidad de unos del grupo sea **par** (o impar). **Para qué sirve.** Detectar que un dato se corrompió en memoria o en el cable. **Características.** · Detecta **1** bit, no 2 · **no corrige** (no sabe dónde está el error) · ocupa 1 bit por byte (9 bits por byte en los módulos con paridad). **Se estudia en** [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]].

### LRC y CRC
**Qué es.** **LRC**: paridad **longitudinal** por bloque (un byte de paridad por columna). **CRC**: código **polinómico**: el bloque se divide por un polinomio generador y se manda el resto. **Para qué sirve.** Detectar **ráfagas** de errores: LRC en E/S industrial, CRC en discos, redes, ZIP. **Características.** · LRC: suma hexadecimal + complemento a 2 (`01+08+…+62 = CC` ⇒ `LRC = 34`) · CRC-8/12/16 con `G(X)` normalizado; en el receptor el resto debe dar **0** · ninguno corrige. **Se estudia en** [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]].

### Hamming y síndrome
**Qué es.** Código corrector: los bits de control van en las **potencias de 2** y el **síndrome** (patrón de fallas de los controles) indica la **posición** del bit con error. **Para qué sirve.** **Corregir** un bit mal sin parar el sistema: es lo que usan las memorias con ECC. **Características.** · `k` controles para `2ᵏ ≥ n + k + 1` datos · `P1` cubre 1,3,5,7,9,11 y así · el síndrome vale 0 sin error y `k` si falló el bit `k` · **SEC-DED** corrige 1 y detecta 2 (72 bits = 64 + 8 en ECC). **Se estudia en** [[2.3.4 Detección y corrección de errores (paridad, LRC, CRC y Hamming)]].

## Dimensionar memorias

### Bits de dirección
**Qué es.** Cantidad de líneas de dirección necesarias para acceder a todas las palabras de una memoria: `bits = log₂(cantidad de palabras)`. **Para qué sirve.** Dimensionar el decodificador, el `MAR` y el campo de dirección de la instrucción. **Características.** · Depende de la **cantidad de palabras**, no del ancho · 4096 palabras ⇒ **12 bits**, sea de 8 o de 16 bits cada una · el ancho define las líneas de **dato**. **Se estudia en** [[2.7.1 Bits de dirección igual a log2 de celdas]].

### CodOp contra campo de dirección
**Qué es.** El reparto de los bits de una instrucción entre **código de operación** y **dirección**. **Para qué sirve.** Saber cuántas instrucciones entran y cuánta memoria se puede direccionar con una palabra de `N` bits. **Características.** · `k bits de opcode ⇒ 2ᵏ instrucciones` · `d bits de dirección ⇒ 2^d palabras` · si crece la memoria, crece `d` y **se achica** `k` (o se alarga la instrucción) · en la BLUE: 4 + 12 = 16. **Se estudia en** [[2.7.2 CodOp vs campo de dirección]].
