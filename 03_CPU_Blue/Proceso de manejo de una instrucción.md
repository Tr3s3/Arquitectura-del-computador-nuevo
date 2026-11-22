---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Proceso de manejo de una instrucción (y en qué unidad se usa)

> [!abstract] En una frase
> **Manejar una instrucción** es ejecutar el **ciclo de instrucción**: **búsqueda (fetch) → decodificación →
> búsqueda de operandos → ejecución → escritura del resultado**. La instrucción se trae de memoria, se guarda en
> el **RI**, y **la Unidad de Control** es la que la decodifica y emite las **señales de control** que ordenan
> cada transferencia; la **ALU** hace los cálculos y la **memoria** guarda datos e instrucciones.

> [!note] Si es la primera vez que ves esto
> Pensá en un **restaurante**. Hay un **cliente** (el programa) que pide platos, una **comanda escrita** (la
> instrucción: "mesa 4, milanesa"), un **mozo** que lleva la comanda a la cocina (el bus), un **jefe de cocina**
> que la lee y reparte el trabajo (la **Unidad de Control**) y **cocineros** que ejecutan (la **ALU** y la
> memoria).
>
> "Manejar la instrucción" es todo ese recorrido: **traerla → leerla → conseguir los ingredientes → cocinar →
> servir**. Y hay algo clave: **nadie improvisa**. El jefe de cocina siempre hace lo mismo, en el mismo orden:
> por eso se dice que el ciclo es **fijo** y que una computadora es una máquina **secuencial**.
>
> Y hay tres cosas distintas que se confunden todo el tiempo:
> | Concepto | Qué es | Ejemplo |
> |---|---|---|
> | **Instrucción** | la **orden** que está en memoria (lo que el programa dice) | `LDA 500` (opcode `06` + dirección) |
> | **Microoperación** | una **transferencia elemental** entre registros | `PC → MAR`, `MBR → AC` |
> | **Señal de control** | la **orden eléctrica** que habilita esa transferencia | `CP1·F·Read`, `CP8·E·LDA` |
>
> Una instrucción = **varias** microoperaciones = **muchas** señales de control en el momento justo.

---

## 1. Las cinco fases, y quién actúa en cada una

```
   ┌──────────────┐   ┌───────────────┐   ┌────────────────┐   ┌───────────┐   ┌────────────┐
   │ 1 BÚSQUEDA   │──►│ 2 DECODIFICAR │──►│ 3 OPERANDOS    │──►│ 4 EJECUTAR│──►│ 5 ESCRIBIR │
   │ (fetch)      │   │ (decode)      │   │ (dirección +   │   │ (ALU)     │   │ resultado  │
   │ MEM → RI     │   │ UC: ¿qué es?  │   │  leer los datos│   │           │   │ en registro│
   └──────────────┘   └───────────────┘   └────────────────┘   └───────────┘   └────────────┘
        memoria            Unidad de            memoria +          ALU            registro
        + PC/MAR/MBR       Control              MAR/MBR           (+ regs)       destino
```

| Fase | Qué pasa | **Unidad / bloque que actúa** | Registros que se tocan |
|---|---|---|---|
| **1. Búsqueda** | se trae la instrucción que apunta el PC | **Memoria** (lectura) + el camino de datos | `PC → MAR → MEM → MBR → RI` |
| **2. Decodificación** | se interpreta el **opcode**: "esto es un LDA" | **Unidad de Control** (decodificador) | `RI` (bits 15-12) |
| **3. Operandos** | se calcula la dirección efectiva y se lee el dato | **UC** (señal de lectura) + **memoria** / registros | `RI(11-0) → MAR → MEM → MBR` |
| **4. Ejecución** | se hace la operación | **ALU** | `AC → Z`, `MBR → Y`, `ALU → resultado` |
| **5. Escritura** | el resultado va al destino | **UC** (señal de `LOAD`/`Write`) | `resultado → AC` o `MBR → MEM` |

> [!important] La respuesta corta a "¿en qué unidad se usa?"
> **El proceso lo dirige la Unidad de Control** (es su razón de existir): ella **decodifica** la instrucción del
> RI, **secuencia** las fases y **genera** las señales. Los cálculos los hace la **ALU**; el almacenamiento,
> la **memoria**; y la **E/S** se ocupa de los periféricos.
> En la BLUE: la UC está formada por los flip-flops **RUN**, **STATE** y **TRA**, un **decodificador 1 → 16** (por
> el opcode) y compuertas que combinan `estado · pulso · instrucción`.

---

## 2. Las cuatro funciones de la UC en este proceso

| Función | Qué significa | En qué fase se nota |
|---|---|---|
| **1. Decodificar** | interpretar el opcode del RI (¿es LDA o ADD?) | fase 2 |
| **2. Secuenciar** | decidir **qué viene ahora** (pulso siguiente, siguiente ciclo, o volver a buscar) | todas |
| **3. Generar señales** | activar `PC→MAR`, `Read`, `strobe MBR`, `SUM→AC`… en el momento exacto | fases 1-5 |
| **4. Controlar el estado** | manejar el *RUN* (encendido), avanzar el *STATE* y atender interrupciones | transición entre ciclos |

**El "programa" de la UC** no está escrito en memoria: está **cableado** en compuertas (en la BLUE). Cada señal
se arma con la misma fórmula:

```
   señal =  (estado: F o E)  ·  (pulso: CP1…CP8)  ·  (instrucción: LDA, ADD, …)
```

Ejemplo: `MBR → AC` en un `LDA` se activa con **`E · CP8 · LDA`**. Es decir: **estamos en ejecución** (E), es
**el octavo pulso** y **la instrucción es LDA**. Ver [[Cómo se implementa la Unidad de Control]].

---

## 3. El proceso en la BLUE, con los pulsos

La BLUE hace todo con **8 pulsos por ciclo** (cada pulso = 125 ns). El manejo de una instrucción usa **uno o dos
ciclos**:

| Instrucción | Ciclos | Pulsos | Por qué |
|---|---|---|---|
| sin referencia a memoria (`HLT`, `NOP`, `JMP`, `JMA`, `SRJ`, `CSA`, `NOT`, `RAL`) | **1** | **8** | se resuelven en la fase 2: no hay que ir a buscar ningún dato |
| con referencia a memoria (`LDA`, `STA`, `ADD`, `XOR`, `AND`, `IOR`) | **2** | **16** | hace falta un ciclo extra para leer o escribir el operando |
| E/S (`INP`, `OUT`) | 2 o más | 16 o más | además esperan al periférico |

**El ciclo de búsqueda (fase 1 + 2), pulso por pulso:**

| Pulso | Microoperación | Para qué |
|---|---|---|
| **CP1** | `PC → MAR` + `Read` | arranca la lectura de la instrucción |
| **CP2** | `PC + 1 → Y` | prepara el incremento (¡solapado con la memoria!) |
| **CP3** | ALU: `Z + Y` | suma lista |
| **CP4** | `resultado → PC` | el PC ya apunta a la próxima instrucción |
| **CP5** | `strobe MBR` | el dato de memoria se guarda en el MBR |
| **CP6** | `MBR → IR` | **la instrucción queda en el RI** |
| **CP7** | decodificación | la UC ya sabe qué instrucción es |
| **CP8** | `E → State` | pasa a ejecución (o ejecuta directo si es de 1 ciclo) |

> [!tip] El detalle que hace la diferencia
> **Mientras la memoria busca la instrucción (CP2-CP5), la ALU incrementa el PC.** Eso es **solapamiento**: la
> máquina hace dos cosas a la vez, y es el primer ejemplo de pipeline de la materia ([[Pipeline]]).

---

## 4. Ejemplo completo: el manejo de un `LDA 500`

**Instrucción**: `LDA 500` ⇒ opcode `06` + dirección `500`.

| # | Fase | Microoperaciones | Quién actúa |
|---|---|---|---|
| 1 | **Búsqueda** | CP1 `PC→MAR`+`Read` · CP2-CP4 `PC+1→PC` · CP5 `MEM→MBR` · CP6 `MBR→RI` | UC + memoria |
| 2 | **Decodificación** | CP7: `RI15-12 = 06` ⇒ el decodificador 4→16 activa la línea **LDA** | **UC** |
| 3 | **Operandos** | 2.º ciclo CP1: `RI11-0 → MAR` + `Read`; CP5: `MEM→MBR` | UC + memoria |
| 4 | **Ejecución** | (no hay cálculo: LDA no opera, sólo copia) | — |
| 5 | **Escritura** | CP8: `MBR → AC` | UC (señal `E·CP8·LDA`) |

**Y al terminar** ⇒ `STATE ← F` y se vuelve a buscar. El PC ya apuntaba a la instrucción siguiente desde CP4: por
eso el programa **avanza solo**.

### Variante con cálculo: `ADD 500`
Igual, pero en la fase 4: CP2 `AC → Z`, CP6 `MBR → Y`, CP8 `SUM → AC`. Es decir, **la misma estructura** cambia
sólo en las microoperaciones de la fase de ejecución. Eso es lo que hay que decir: **el esqueleto es común; lo
que varía es la fase de ejecución**. Detalle completo en [[Ciclo de ejecución — todas las operaciones]].

---

## 5. ¿Qué pasa con las instrucciones de un solo ciclo?

`JMP 700` no necesita ir a memoria a buscar nada: la dirección **ya está** en el RI. Entonces el proceso se corta
en la **fase 2**:

```
   CP1-CP6:  búsqueda normal (trae el JMP al RI)
   CP7:      decodifica
   CP8:      IR11-0 → PC      ← ¡el salto ya ocurrió, dentro de la búsqueda!
```
Por eso `JMP`, `JMA`, `SRJ`, `NOP`, `HLT`, `NOT`, `RAL` y `CSA` **no tienen ciclo de ejecución**: se "ejecutan"
en el octavo pulso de la búsqueda. Es la respuesta a "¿por qué algunas tardan 8 y otras 16?".

---

## 6. Cómo responderlo en el final (4 minutos)

**Movimiento 1 — definición (20 s).** "Manejar una instrucción es el ciclo de instrucción: buscarla,
decodificarla, obtener los operandos, ejecutarla y guardar el resultado. Es fijo y lo repite la máquina con cada
instrucción del programa."

**Movimiento 2 — las fases con las unidades (60 s).** La tabla de las cinco fases diciendo, en cada una, **qué
unidad actúa**: memoria (búsqueda y operandos), **UC** (decodificación y señales), **ALU** (ejecución).

**Movimiento 3 — qué son las cosas (40 s).** Distinguir **instrucción** (la orden), **microoperación** (la
transferencia) y **señal de control** (`estado·pulso·instrucción`).

**Movimiento 4 — en la BLUE (60 s).** Los 8 pulsos de la búsqueda con sus microoperaciones (`PC→MAR`, `PC+1`,
`MBR→IR` en CP6, `E→State` en CP8) y la regla **8 pulsos = 1 ciclo** (sin memoria) / **16 pulsos = 2 ciclos**
(con memoria).

**Movimiento 5 — ejemplo y cierre (40 s).** `LDA 500` de punta a punta (16 pulsos) y decir: "**la UC es la que
maneja el proceso**; el RI guarda la instrucción, el PC apunta a la próxima y la ALU ejecuta".

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Cuál es el orden de las fases? | **Búsqueda → decodificación → operandos → ejecución → escritura** |
| ¿En qué unidad se usa? | En la **Unidad de Control**: decodifica, secuencia y genera las señales |
| ¿Qué diferencia hay entre instrucción y microoperación? | La instrucción es la **orden**; la microoperación es **una transferencia** entre registros |
| ¿De qué está hecha una señal de control? | `estado · pulso · instrucción` (y a veces condiciones, como `A15` en `JMA`) |
| ¿Dónde queda la instrucción mientras se ejecuta? | En el **RI** (Registro de Instrucción) |
| ¿Quién incrementa el PC? | La ALU, en CP2-CP4 del ciclo de búsqueda (solapado con la lectura) |
| ¿Por qué `JMP` termina en la búsqueda? | Porque no necesita operando: la dirección ya está en el RI (CP8) |
| ¿Qué pasa al terminar la instrucción? | `STATE ← F` y se busca la siguiente; si `RUN = 0` (por un `HLT`), la máquina se detiene |
| ¿Y las interrupciones? | Al final del ciclo se consulta `IRQ·SI`; si corresponde, se atiende antes de la próxima búsqueda ([[Interrupciones y entrada-salida]]) |

---

## 7. Errores típicos
- Decir que la UC "ejecuta" la instrucción: **la UC ordena**, la que opera es la **ALU**.
- Confundir **instrucción** con **microoperación** y con **señal de control**.
- Olvidar la fase de **búsqueda de operandos** (en las instrucciones con memoria hay **dos** accesos: uno para la
  instrucción y otro para el dato).
- Decir que el PC apunta a la instrucción **actual**: apunta a la **próxima** (se incrementa en CP4).
- Creer que todas las instrucciones tardan lo mismo: **8 o 16 pulsos** según haya referencia a memoria.
- Decir que el decodificador "es la UC": es **una parte** de la UC.

---

## 8. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **`blue.pdf`** (Foster, *Una máquina elemental*) | *"El ciclo de búsqueda"* (**Tabla 2**), *"Unidad de control"* (figs. 10-11) y *"Circuitos de la unidad de control"* (figs. 19-29) | la secuencia pulso por pulso y cómo se arma cada señal | **Es la fuente literal** de esta pregunta |
| **Apuntes de cátedra**, *Unidad 5* | sección de **ciclos de instrucción** y de la **UC** | el vocabulario de la cátedra (fases, estados, pulsos) | Alineación con lo que se espera escuchar |
| **Apuntes de cátedra**, *Unidad 4* | **estructura básica** y unidades funcionales | qué hace cada unidad (CPU, memoria, E/S) | Para responder "en qué unidad se usa" |
| **[[Ciclo de máquina]]** · **[[Ciclo de búsqueda (7 y 8 pulsos)]]** | notas de la bóveda | el ciclo completo y por qué son 8 pulsos (ferrita) | Prerrequisito y detalle |
| **[[Ciclo de ejecución — todas las operaciones]]** | nota de la bóveda | qué pasa en la fase de ejecución **en cada familia** de instrucciones | El paso siguiente |
| **[[Unidad de Control]]** · **[[Cómo se implementa la Unidad de Control]]** | notas de la bóveda | las 4 funciones y el circuito que genera las señales | El corazón de la respuesta |
| **[[TP16 Ciclo de instrucción básico]]** | el TP | los 6 pasos que pide la cátedra y el simulador | Lo que se entrega |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **unidad de control** y de **ciclo de instrucción** | fetch-decode-execute con microoperaciones y señales | **La mejor ampliación** |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo del **ciclo de instrucción** (figura clásica) | el esquema búsqueda-interrupción-ejecución | Orden y figura para el pizarrón |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo del **procesador** (datapath y control) | cómo el control gobierna el camino de datos | Formalización moderna |

---

## Relacionado
[[Ciclo de máquina]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] ·
[[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]] ·
[[Registros de la CPU]] · [[Flujo de información en BLUE (datos y direcciones)]]
