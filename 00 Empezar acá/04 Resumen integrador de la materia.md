---
tipo: resumen
examen: principal
prioridad: maxima
---
# Resumen integrador de la materia

> [!abstract] Cómo está armado este resumen
> Es la materia **en una sola pasada**, ordenada como un computador: **de la compuerta al programa**. Cada sección termina con lo que hay que poder decir en el oral y el enlace a la nota que lo desarrolla. Si tenés poco tiempo: leé esto, después [[Guion de respuestas — preguntas principales]] y después [[Tablas de verdad de memoria]].

---

## 1. La idea general: todo es jerarquía
Un computador es una **máquina de niveles**:

```
compuerta  →  circuito combinacional  →  bloque funcional  →  unidad  →  computador  →  sistema
(AND, OR)     (sumador, MUX, decod.)     (ALU, registro, RAM)  (CPU, memoria)   (von Neumann)
```

Cada nivel se construye con el anterior y **cada nivel se puede explicar sin conocer el de abajo**… salvo que el examen te pida bajar. El final recorre esa escalera: empieza dibujando compuertas y termina explicando por qué un pipeline es más rápido.

---

## 2. Nivel compuerta: lógica digital
**Lo que hay que saber:** las 7 compuertas (NOT, AND, NAND, OR, NOR, XOR, NXOR) con su tabla de verdad y su símbolo; el **álgebra de Boole** (postulados y teoremas) y **DeMorgan**; pasar de **tabla de verdad → función → circuito** (mintérminos, Karnaugh).

- `(A+B)' = A'·B'` y `(A·B)' = A'+B'` ⇒ **NAND y NOR son universales**.

- Simplificar = **menos compuertas, menos costo, menos retardo**. El método analítico exige **citar la ley** en cada paso.

- De la tabla a la función: `F = Σm(...)` (los unos) o `ΠM(...)` (los ceros), y el **mapa de Karnaugh** para minimizar agrupando unos adyacentes.

**Para el oral:** "toda función lógica tiene una expresión booleana y toda expresión un circuito; diseñar es ir de la especificación (tabla) al circuito mínimo". → [[Compuertas lógicas]] · [[Álgebra de Boole — postulados y teoremas]] · [[Leyes de DeMorgan]] · [[Mintérminos y maxtérminos]] · TPs: [[TP1 Compuertas lógicas]], [[TP2 Álgebra de Boole]], [[TP3 Simplificación analítica]], [[TP4 Mintérminos, maxtérminos y Karnaugh]]

---

## 3. Nivel bloque: combinacionales y secuenciales
**Combinacionales** (salida = f(entradas actuales), no tienen memoria):

- **Sumadores**: el [[Semisumador]] (`S = A⊕B`, `C = A·B`) y el [[Sumador completo]] (`S = A⊕B⊕Cin`, `Cout = A·B + Cin(A⊕B)`). Encadenando n sumadores completos (Cout → Cin) se suma en n bits. Es **el** circuito aritmético del computador: está en la ALU y en el incrementador del PC.

- **Decodificador** (n → 2ⁿ, una salida activa, es un **mintérmino**), **codificador** (2ⁿ → n, el inverso), **multiplexor** (2ⁿ → 1, **selector de datos**: el que decide quién escribe en el bus) y **demultiplexor** (1 → 2ⁿ, **reparte** un dato).

**Secuenciales** (tienen **memoria**, dependen del estado anterior):

- **Biestables**: RS (`Q = S + R'Q`, 1‑1 prohibido), **D** (`Q = D`, el de memoria), **JK** (`Q = JQ' + K'Q`, sin estado prohibido, conmuta) y **T** (`Q = T⊕Q`, divide por 2).

- **Registros**: n flip-flops con reloj y LOAD common ⇒ **PIPO** (todo junto), **SISO** (de a uno), **SIPO** (recepción serie), **PISO** (transmisión serie) y el **bidireccional con carga paralela**.

- **Contadores**: asíncronos (en cascada, retardo acumulado) y síncronos (reloj común); el **PC** es un contador con carga en paralelo.

**Para el oral:** la diferencia clave es **memoria o no**, y la frase que ordena todo: "*codificador = OR · decodificador = AND · MUX = AND+OR · DEMUX = AND con D*". → [[Sumador completo]] · [[Decodificador]] · [[Multiplexor]] · [[Flip-Flops SR, D, JK y T]] · [[Registros]] · [[Contadores]] · TPs: [[TP5 Sumadores]], [[TP6 Decodificadores y demultiplexores]], [[TP7 Codificadores y multiplexores]], [[TP8 Biestables RS]], [[TP9 Biestables D, JK y T]], [[TP10 Registros PIPO y SISO]], [[TP11 Registros SIPO y PISO]]

---

## 4. Nivel memoria: dónde vive el programa

- **Celda elemental**: 1 bit + selección + `R/W'` + **buffer de tres estados** (para compartir el bus).

- **RAM 8×3**: 8 palabras de 3 bits = 24 bits; 3 bits de dirección (decodificador 3→8), 3 de datos, `CS` y `R/W'`. Es el modelo de toda memoria: **dirección → decodificador → palabra**.

- **ROM**: no volátil, sólo lectura (máscara, PROM, EPROM, EEPROM, Flash). Guarda firmware, tablas y el **microcódigo** de la UC.

- **Jerarquía**: registros → L1 → L2/L3 → RAM → disco → cinta. Funciona por **localidad**; su objetivo es que el tiempo **medio** de acceso se acerque al nivel rápido.

- **Caché**: guarda **bloques**; dirección = `etiqueta | índice | offset`; mapeos **directo / asociativo / por conjuntos**; escritura *write-through* / *write-back*; reemplazo LRU/FIFO.

- **Cálculo de examen** (`CodOp` y dirección): `nº celdas = memoria / tamaño de celda`, `bits dirección = log₂(nº celdas)`, `bits CodOp = bits palabra − bits dirección`. Si da negativo ⇒ **la celda no alcanza** para contener la dirección.

**Para el oral:** "la memoria es una matriz de celdas direccionables; el decodificador elige la palabra; y la jerarquía existe porque ninguna tecnología es rápida, grande y barata a la vez". → [[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] · [[Jerarquía de memorias]] · [[Memoria caché]] · [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] · TPs: [[TP12 Memoria principal]], [[TP18 Direccionamiento de memoria]]

---

## 5. Nivel CPU: la máquina que ejecuta
**Unidades y buses (pregunta principal).** CPU (UC + ALU + registros), memoria y E/S unidas por **bus de datos** (16 bits en BLUE, bidireccional), **de direcciones** (12 bits, unidireccional) y **de control**. Von Neumann: **una sola memoria** para instrucciones y datos ⇒ simple, con **cuello de botella**. El ancho de datos fija la palabra; el de direcciones fija el espacio (`2ⁿ × celda`); si el bus es más angosto que la instrucción, hacen falta **varios accesos**.

**Registros.** `PC` (dirección de la próxima instrucción) · `IR` (la instrucción en curso) · `MAR` (dirección para memoria) · `MBR` (dato que entra/sale) · `AC` (acumulador). La indexada agrega **RIF/RID**.

**Unidad de Control (pregunta principal).** Sus **cuatro funciones**: sincronizar, decodificar, secuenciar y **generar las señales de control**. Todo el hardware es "tonto": la ALU suma si le dicen, el registro carga si `LOAD = 1`, la memoria lee si `MEMR = 1`. **La inteligencia está en la UC.** En BLUE la sincronía son tres flip-flops: **RUN** (marcha), **STATE** (F/E) y **CLOCK**.

**Ciclo de máquina (pregunta principal).** `búsqueda (fetch) → decodificación → ejecución`, repetido mientras RUN = 1. La búsqueda es **fija**: `MAR ← PC`, `MEMR`, `MBR ← M[MAR]`, `PC ← PC+1`, `IR ← MBR`, decodificar, `STATE ← E`. La ejecución depende del opcode. Conteo de pulsos: **8 pulsos** de búsqueda (7 + el de espera de memoria) y **LDA = 24** (8 + 16) si se cuentan **2 pulsos por microoperación**.

**Flujo de información (pregunta principal).** Un **bus único**: por pulso, una fuente habilita su salida de tres estados y un destino carga. **Direcciones** (12 bits): `PC`/`IR → MAR → memoria`. **Datos** (16 bits): `memoria → MBR → IR/AC` o `AC → MBR → memoria`. En un `JMP` la dirección del IR va **al PC**: la dirección es el *dato*.

**Formato de instrucción (pregunta principal).** 4, 3, 2 y 1 dirección; menos direcciones = instrucción más corta, más instrucciones y un operando implícito. BLUE: **1 dirección**, `opcode 4 + dirección 12`.

**Modos de direccionamiento.** Los **siete** de la cátedra: inmediato (0 accesos), directo (1), indirecto (2), de registro (0), registro indirecto (1), de desplazamiento/indexado (1) y de pila. El **indexado** permite recorrer arreglos con el mismo código y ahorra bits de dirección.

→ [[Estructura básica de un computador]] · [[Registros de la CPU]] · [[Unidad de Control]] · [[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de la instrucción LDA (24 pulsos)]] · [[Flujo de información en BLUE (datos y direcciones)]] · [[Formato de la instrucción (4 formatos)]] · [[Modos de direccionamiento]] · [[BLUE indexada (RIF, RID, nuevo formato)]] · TPs: [[TP15 Arquitectura de Von Neumann (IAS)]], [[TP16 Ciclo de instrucción básico]], [[TP17 Formato básico de instrucciones]], [[TP19 Modos de direccionamiento]], [[TP20 Lenguaje máquina]]

---

## 6. Nivel sistema: interrupciones, E/S y velocidad

- **Interrupciones**: pedido que rompe la secuencia. Termina la instrucción, **guarda contexto (PC/flags)**, salta a la **rutina de servicio** (por *polling* o **vectorizada** con tabla de vectores), atiende y **restaura**. Se clasifican en de hardware/software, **enmascarables/NMI** y excepciones; se resuelven por **prioridad** y pueden **anidarse**. Sin interrupciones, el *polling* desperdicia la CPU.

- **E/S**: transmisión **serie** (un bit por vez, largo alcance) vs **paralela** (todos los bits, corto alcance); puertas con registros de datos/estado/control; interfaces y **DMA** (transferencia sin la CPU).

- **Cómo se hace más rápido**: **pipeline** (etapas solapadas: `k + n − 1` ciclos en vez de `k·n`, con conflictos de datos/control/estructurales), **caché** (evita esperar a la RAM), **bancos de memoria** (ancho de banda), **DMA** (libera a la CPU) y **paralelismo** (superescalar, SIMD/vectorial, multicore).

- **CISC vs RISC**: instrucciones complejas y variables con UC **microprogramada** (x86) vs instrucciones simples de longitud fija, **load/store**, muchos registros y UC **cableada** (ARM). Los actuales son **híbridos**.

- **UC cableada vs microprogramada**: la microprogramada guarda en una **memoria de control** las microinstrucciones (flexible, más lenta); la cableada genera las señales con compuertas (rápida, rígida).

→ [[Interrupciones y entrada-salida]] · [[Pipeline]] · [[CISC y RISC]] · [[Unidad de control cableada y microprogramada]] · [[Técnicas para aumentar la velocidad]]

---

## 7. El final, en dos tablas

### Oral — las 8 preguntas principales y su respuesta en una línea

| # | Pregunta | Respuesta en una línea |
|---|---|---|
| 1 | Flujo de información | bus único: una fuente y un destino por pulso; direcciones al MAR, datos por el MBR |
| 2 | Formato de la instrucción | 4/3/2/1 dirección; BLUE = 1 dirección (4+12) con acumulador implícito |
| 3 | Ciclo de máquina | búsqueda (fija) + ejecución (según opcode), con STATE F/E y RUN |
| 4 | Estructura y buses | CPU (UC+ALU+registros) + memoria + E/S; datos/direcciones/control |
| 5 | RAM 8×3 | 8×3 = 24 bits; decodificador 3→8, CS y R/W' |
| 6 | Ciclo de ejecución (indexada y sin indexar) | sin indexar: `MAR ← IR(dir)`; indexada: `EA = D ± RIF/RID` con el sumador de direcciones y el modificador de 2 bits |
| 7 | UC | 4 funciones + señales (MEMR, MARin, PCinc, ALUop, load flags) |
| 8 | Interrupciones | guardar contexto → ISR → restaurar; polling vs vectorizada; prioridades |

### Práctica — lo que se dibuja

| Dibujo | Tabla asociada | Tiempo objetivo |
|---|---|---|
| Semisumador | 4 filas (S, C) | 2 min |
| Sumador completo | 8 filas (S, Cout) | 4 min |
| Sumador de 4 bits | suma binaria verificada | 5 min |
| Decodificador 2→4 | 4 filas, una salida en 1 | 4 min |
| Demultiplexor 1→4 | 4 filas, la salida copia D | 4 min |
| Multiplexor 4→1 | 4 filas, Y = Ii | 4 min |
| Biestable RS / D / JK / T | tabla de estados | 5 min |

→ [[Cómo dibujar los circuitos (checklist de pizarrón)]] · [[Tablas de verdad de memoria]]

---

## 8. Las cinco frases que resumen la materia

1. **"Todo se construye con compuertas, y toda función tiene una tabla de verdad."**

2. **"Combinacional = no recuerda; secuencial = recuerda (biestables)."**

3. **"La memoria es una matriz; el decodificador elige la palabra y el buffer de tres estados la pone en el bus."**

4. **"La CPU no piensa: la UC genera señales; la ALU opera; los registros guardan."**

5. **"Un computador es más rápido con pipeline, caché, DMA y paralelismo — y todas esas técnicas atacan el mismo problema: la diferencia de velocidad entre la CPU y la memoria."**

## Enlaces de arranque
[[00 Matriz del final — las 3 tandas]] · [[03 Ruta de estudio para el final]] · [[Banco de preguntas del final]] · [[Guion de respuestas — preguntas principales]] · [[Autoevaluación]]
