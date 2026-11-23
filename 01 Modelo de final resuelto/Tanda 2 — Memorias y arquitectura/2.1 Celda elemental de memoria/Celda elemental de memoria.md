---
unidad: 3
tipo: concepto
examen: secundario
prioridad: maxima
---
# Celda elemental de memoria

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[Flip-Flops SR, D, JK y T]] (Tanda 3 · 3.6 Flip-flops D, T y RS) · [[Memoria RAM 8x3]] (Tanda 1 · 1.4 Memoria RAM 8x3) · [[Memoria ROM y sus tipos]] (Tanda 2 · 2.2 Memoria ROM y sus tipos) · [[Jerarquía de memorias]] (Tanda 2 · 2.4 Jerarquía de memorias)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 2.1 Celda de memoria]].


> [!abstract] En una frase
> La **celda elemental** es el circuito que guarda **un bit** dentro de una memoria: un **biestable** (o un
> capacitor, según la tecnología) **más compuertas** para tres cosas: **ser seleccionada** entre miles (línea de
> selección), **decidir si lee o escribe** (línea L/E) y **colgarse o no del bus de datos** (buffer de tres
> estados).

> [!note] Si es la primera vez que ves esto
> Si un biestable guarda 1 bit, una memoria de 8 GB guarda 64 mil millones de bits: no puede ser "un biestable
> por cable". La celda elemental resuelve el problema: es **un bit + el kit para convivir con miles de vecinos**.
> Pensalo como un casillero de un vestuario gigante: el casillero (biestable) guarda tu campera, pero además
> necesita **un número** para encontrarlo (selección), **una puerta con cerradura** que se abra sólo cuando
> corresponde (L/E) y **no estorbar el pasillo** cuando no lo usás (tres estados). Ese casillero, repetido en
> forma de matriz y con un decodificador que elige la fila, **es** una memoria.

---

## 1. Qué tiene adentro (los cuatro bloques)

```
                 línea de SELECCIÓN (viene del decodificador)
                            │
        L/E ──────►┌────────▼─────────┐
   (0 = escribe)   │   BIESTABLE       │◄── dato de entrada (D)
   (1 = lee)       │   (1 bit)         │
                   └────────┬──────────┘
                            │ Q
                     ┌──────▼───────┐
                     │ buffer de 3  │────► salida al bus de datos
                     │   estados    │      (se desconecta si no está seleccionada)
                     └──────────────┘
```

| Bloque | Para qué sirve | Qué pasa si falta |
|---|---|---|
| **Biestable** (o capacitor) | **guardar** el bit | no hay memoria, hay cable |
| **Línea de selección** | que la celda sepa que **la eligieron** | todas las celdas responderían a la vez |
| **Línea L/E** (o `R/W'`) | decidir **lectura o escritura** | escribirías cuando querés leer |
| **Buffer de tres estados** | **conectarse o desconectarse** del bus | todas las celdas pelearían por el mismo cable |

> [!important] La lógica, en una frase
> Con **selección = 1** la celda está habilitada. Si **L/E = 1** (lectura) **se bloquean las entradas** del
> biestable y se **habilita la compuerta de salida**: la celda "habla". Si **L/E = 0** (escritura) se bloquea la
> salida y **se habilita la entrada**: la celda "escucha". **Con selección = 0 no hace nada**: queda
> desconectada del bus.

---

## 2. Los dos tipos de celda (esto es lo que distingue SRAM de DRAM)

| | **Celda estática (SRAM)** | **Celda dinámica (DRAM)** |
|---|---|---|
| Qué guarda el bit | un **biestable** (dos inversores realimentados) | un **capacitor** (carga = 1, sin carga = 0) |
| Transistores por celda | ~6 | **1 transistor + 1 capacitor** |
| ¿Se degrada? | **no**, se mantiene mientras haya alimentación | **sí**: el capacitor se descarga por fugas |
| ¿Necesita refresco? | **no** | **sí**, hay que regenerar cada cierto tiempo recorriendo las filas |
| Velocidad | **más rápida** | más lenta |
| Densidad y costo | menor densidad, más cara por bit | **mucha más densidad**, más barata por bit |
| Dónde se usa | **caché** (L1, L2, L3) y registros | **memoria principal** (los módulos RAM) |
| Volatilidad | volátil (pierde al apagar) | volátil (pierde al apagar) |

**Cómo funciona la celda estática**: dos inversores conectados en anillo (la salida de uno a la entrada del
otro). Si en la entrada hay un 1, la salida se refuerza a sí misma: el estado **se sostiene solo** indefinidamente.
Alcanza para guardar el bit mientras haya alimentación.

**Cómo funciona la celda dinámica**: cargás el capacitor para un 1 y lo descargás para un 0. El problema es que
**se descarga solo** por pequeñas fugas de carga: aunque esté alimentado, el dato se pierde. Por eso:
- cada lectura usa un **amplificador sensor** que regenera el valor, y
- periódicamente se **refresca** la memoria: se recorren las filas en forma secuencial y los amplificadores
  reescriben lo que había. Ese refresco consume un pequeño porcentaje del tiempo de la memoria.

> [!tip] Detalle que conecta con la BLUE
> Las primeras memorias de la BLUE eran de **núcleos de ferrita**, que también eran **destructivas al leer**
> (había que reescribir el dato). Ese es el origen del **8.º pulso** del ciclo de máquina
> ([[Ciclo de búsqueda (7 y 8 pulsos)]]). La DRAM tiene el mismo problema "de fondo": leer puede destruir, por eso
> **toda lectura la regenera**.

---

## 3. De la celda a la memoria: la matriz

Una celda sola no sirve: se las ordena en **matriz** y se agrega un **decodificador** que elige la fila.

| Organización | Cómo se selecciona una celda | Ventaja |
|---|---|---|
| **2D** | **una** línea de selección por palabra (una por fila) | simple |
| **3D** | **dos** líneas: fila **y** columna, que deben coincidir | decodificadores **más chicos** (clave en memorias grandes) |

```
   dirección ──► [ decodificador ] ──► una sola línea de selección
                                          │
        ┌─────────────────────────────────┼──────────────┐
        │  fila 0:  [celda][celda][celda] │  ← una palabra
        │  fila 1:  [celda][celda][celda] │
        │  ...                            │
        └─────────────────────────────────┴──────────────┘
                                          │
                    bus de datos ◄────────┘
```

En la **RAM 8×3**, por ejemplo, hay **24 celdas elementales** (8 filas × 3 columnas) y un decodificador 3→8
([[Memoria RAM 8x3]]).

---

## 4. Ejemplo resuelto: leer y escribir en una celda

**Escribir un 1** en la celda (4, 2):
1. El decodificador activa la línea de selección de la fila 4.
2. La CPU pone `L/E = 0` (escritura) y el dato `1` en la línea de entrada.
3. La entrada del biestable queda habilitada ⇒ el biestable pasa a 1.
4. La salida queda bloqueada: la celda **no habla** en el bus.
5. Se quita la selección: el biestable **mantiene** el 1 (realimentación).

**Leer** la misma celda:
1. El decodificador activa la fila 4.
2. La CPU pone `L/E = 1` (lectura).
3. Las entradas del biestable se bloquean (no se puede escribir sin querer).
4. Se habilita el buffer de tres estados ⇒ el valor aparece en el bus de datos.

---

## 5. Cómo responderlo en el final (2–3 minutos)

**Movimiento 1 — definición (20 s).** "La celda elemental guarda un bit: es un biestable más compuertas de
selección y control."

**Movimiento 2 — dibujo (40 s).** El biestable, la línea de selección arriba, L/E a un costado y el buffer de
tres estados a la salida.

**Movimiento 3 — funcionamiento (40 s).** Selección = 1 habilita. `L/E = 1` ⇒ lee (bloquea entradas, habilita
salida). `L/E = 0` ⇒ escribe (bloquea salida, habilita entrada).

**Movimiento 4 — cierre con los dos tipos (40 s).** Estática = biestable, no necesita refresco, se usa en
**caché**. Dinámica = capacitor, **necesita refresco**, se usa en la **memoria principal**. Y una frase de
cierre: "repetida en matriz y con un decodificador, esta celda **es** la memoria".

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Por qué el buffer es de tres estados? | Porque muchas celdas comparten el **mismo bus de datos**: la que no está seleccionada debe **desconectarse** |
| ¿Qué pasa si dos celdas se seleccionan juntas? | Si las dos hablan, el dato del bus es indefinido (conflicto) |
| ¿Por qué la estática no necesita refresco? | Porque la **realimentación** del biestable sostiene el estado solo |
| ¿Por qué se usa DRAM en la memoria principal? | **Densidad y costo**: 1 transistor contra ~6 ⇒ más bits por mm² y más barata |
| ¿Y por qué no DRAM en la caché? | Porque es **más lenta** (y el refresco quita tiempo): la caché necesita SRAM |
| ¿La celda ROM es igual? | No: guarda el bit **sin biestable** (diodo/transistor presente o ausente, o puerta flotante cargada) ⇒ no volátil ([[Memoria ROM y sus tipos]]) |

---

## 6. Errores típicos
- Decir que la celda "tiene un registro": tiene un **biestable** (un registro es un conjunto de ellos, con carga
  paralela).
- Olvidar la **línea de selección**: sin ella no hay forma de elegir una celda entre millones.
- Confundir **L/E** con la **selección**: la primera dice **qué hacer**; la segunda, **a quién**.
- Decir que la SRAM pierde el dato por fugas: **eso es la DRAM**.
- Decir que la DRAM no es volátil: **sí lo es** (pierde al apagar); lo que necesita es **refresco** mientras está
  alimentada.

---

## 7. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 3 — Memorias electrónicas* | sección de **celda elemental** (es la primera después de los parámetros de las memorias) | el esquema de la celda con selección, L/E y compuertas, tal como lo pide la cátedra | **Es la fuente exacta** de esta pregunta |
| **`memorias.pdf`** — *Dispositivos Electrónicos*, Tema 7 | **7.3.2 RAM estática**: celda básica y accesos; **7.3.3 RAM dinámica**: celda, **refresco**, accesos; **7.2 ROM** | el biestable de dos inversores, la celda de 1 transistor + capacitor, el **amplificador sensor**, el refresco secuencial por filas | Es el material más técnico: ahí está el "por dentro" que impresiona en el oral |
| **[[Memoria RAM 8x3]]** | la nota de la bóveda | cómo 24 celdas se convierten en una memoria con decodificador | El paso siguiente, que casi siempre se pregunta junto |
| **[[TP12 Memoria principal]]** | el TP | el cuadro RAM vs ROM y las características que pide la cátedra | Lo que se entrega por escrito |
| **Floyd, *Fundamentos de sistemas digitales*** | el tema de **memorias semiconductoras** (ed. 1996: tema 12, págs. 594-644 — referencia que cita la cátedra) | celdas SRAM/DRAM, arquitectura de la matriz | Figuras claras para dibujar |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **memoria** | celda de RAM, decodificación, organización 2D/3D | Rigor de diseño |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo de **jerarquía de memoria** | por qué SRAM arriba y DRAM abajo | Conecta con [[Jerarquía de memorias]] y [[Memoria caché]] |
| **[[Tablas de verdad de memoria]]** | nota de práctica | la tabla de la celda elemental lista para el pizarrón | Repaso rápido |

---

## Relacionado
[[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] · [[Flip-Flops SR, D, JK y T]] · [[Decodificador]] ·
[[Jerarquía de memorias]] · [[Memoria caché]]
