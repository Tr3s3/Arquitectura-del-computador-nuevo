---
unidad: 3
tipo: concepto
examen: secundario
prioridad: maxima
---
# Memoria ROM y sus tipos

> [!abstract] En una frase
> La **ROM** (*Read Only Memory*) es una memoria **no volátil**: conserva su contenido **sin alimentación**, y en
> operación normal **sólo se lee**. Guarda lo que tiene que estar desde el arranque: **firmware/BIOS**, tablas
> fijas y la **memoria de control** de las CPUs microprogramadas. Sus tipos, de menos a más flexibles:
> **ROM de máscara → PROM → EPROM (luz UV) → EEPROM → Flash**.

> [!note] Si es la primera vez que ves esto
> Cuando encendés la computadora, la RAM está **vacía**: es volátil, se borra al apagar. Entonces, ¿quién le dice
> a la máquina qué hacer en el primer instante? Ahí entra la **ROM**: una memoria que **no se olvida**. Es como
> el manual de instrucciones impreso que viene pegado dentro del electrodoméstico: no lo podés reescribir con el
> uso, pero está siempre. Su celda no es un biestable: es un **diodo o transistor que está o no está** (o una
> compuerta flotante cargada). Por eso **no se pierde**: no hay nada que se descargue ni que se realimente.

---

## 1. RAM vs ROM (el cuadro que se pregunta)

| | **RAM** | **ROM** |
|---|---|---|
| Operación | lectura **y escritura** | **sólo lectura** en operación normal |
| Volatilidad | **volátil** (pierde al apagar) | **no volátil** (conserva sin alimentación) |
| Velocidad | rápida (SRAM más que DRAM) | más lenta que la RAM (sobre todo al escribir) |
| Celda | biestable (SRAM) o capacitor (DRAM) | diodo/transistor presente o ausente; puerta flotante |
| Para qué | datos y programas **en ejecución** | **firmware**, tablas fijas, **memoria de control**, BIOS |
| ¿Se puede grabar? | sí, siempre | sólo con equipo/procedimiento especial, y **pocas veces** |
| Costo por bit | mayor | menor |

> [!important] La precisión que sube nota
> Hoy la mayoría de las ROM **se pueden programar** (PROM, EPROM, EEPROM, Flash). Entonces la diferencia con la
> RAM **no es "no se puede escribir"**, sino: (1) es **no volátil** y (2) **escribir es mucho más lento** y con
> **desgaste** (número limitado de ciclos). Decir esto demuestra que entendiste, no que memorizaste.

---

## 2. Los tipos, de menos a más flexibles

| Tipo | Cómo se graba | ¿Se puede borrar? | Comentario |
|---|---|---|---|
| **ROM de máscara** (MROM) | en **fábrica**, al fabricar el chip (el contenido está en el patrón de conexiones) | **no** | sólo para grandes series; si tenía un error, se tiraba el lote |
| **PROM** | una sola vez, por el **usuario**, "quemando" fusibles | **no** | programable una vez |
| **EPROM** | eléctricamente, con tensiones especiales | **sí**, con **luz ultravioleta** (hay una ventanita de cuarzo) | se borra **toda** la memoria de una vez |
| **EEPROM** | eléctricamente | **sí**, **eléctricamente** (byte a byte) | más cómoda, más lenta y más cara |
| **Flash** | eléctricamente | **sí**, por bloques | la evolución de la EEPROM: la de los pendrives, SSD y el firmware de hoy |

**Cómo se guarda el bit, físicamente**:
- **Diodo/transistor presente o ausente**: si en el cruce fila-columna hay un dispositivo, hay un 1; si no, un 0.
  Es el caso de la ROM de máscara y de la PROM (donde se "quema" el fusible).
- **Puerta flotante**: se introducen cargas en una compuerta aislada (**celda FAMOS** por avalancha, o
  **FLOTOX** por efecto túnel). La carga atrapada cambia el umbral del transistor y eso guarda el bit. Para
  **borrar**, se saca la carga: con **UV** (EPROM) o eléctricamente (EEPROM/Flash).

---

## 3. La ROM como circuito: es un bloque combinacional

Este es el detalle que más impresiona y además conecta con la 3.ª tanda del final:

> [!important] Una ROM de 2ⁿ × m es **un decodificador + m compuertas OR**
> - **n bits de dirección** ⇒ decodificador de **n → 2ⁿ** (una línea por palabra).
> - **m salidas** ⇒ **m compuertas OR**, cada una con las entradas que correspondan a los 1 de esa columna.
>
> Es decir: **una ROM es un circuito combinacional que implementa m funciones booleanas de n variables**. No
> tiene nada de "mágico": es la tabla de verdad hecha hardware.

```
   dirección (n) ──► [ decodificador n→2ⁿ ] ──┐
                                              │   (2ⁿ líneas)
                        ┌─────────────────────┴──────────────┐
                        │  matriz de OR (una por salida)     │──► m bits de dato
                        │  cada OR "ve" sólo las filas      │
                        │  que tienen un 1 en su columna     │
                        └────────────────────────────────────┘
```

**Ejemplo**: una ROM de 8 × 4 con contenidos `0,1,2,…` es exactamente un decodificador 3→8 con 4 ORs que
"eligen" qué bits de cada dirección salen. Por eso se dice que **una ROM puede reemplazar cualquier circuito
combinacional**: se pone la tabla de verdad adentro y listo.

---

## 4. Para qué se usa (con los ejemplos de la cátedra)

| Uso | Por qué en ROM |
|---|---|
| **BIOS / firmware** | tiene que estar al encender, cuando la RAM está vacía |
| **Memoria de control** de una CPU **microprogramada** | las microinstrucciones están fijas en el chip (ver [[Cómo se implementa la Unidad de Control]]) |
| **Tablas fijas** | generadores de caracteres, tablas de senos, conversores de código |
| **Sistemas embebidos** | el programa completo del microcontrolador (lavarropas, horno, juguete) |
| **Arranque (bootloader) de celulares y PC** | código mínimo que carga el resto desde el disco |

> [!example] El dato de la cátedra
> El **8088** tiene una UC **microprogramada** con una **ROM de control de 504 palabras de 21 bits**. Es decir:
> la propia secuencia de microórdenes de la CPU **está en una ROM**. Si esa ROM fuera RAM, al apagar la máquina
> olvidaría cómo funcionar.

---

## 5. Cómo responderlo en el final (2–3 minutos)

**Movimiento 1 — definición (20 s).** "ROM: memoria no volátil de sólo lectura en operación normal; conserva el
contenido sin alimentación."

**Movimiento 2 — el cuadro RAM/ROM (40 s).** Operación, volatilidad, celda, velocidad, uso.

**Movimiento 3 — los tipos (40 s).** Máscara → PROM → EPROM (UV) → EEPROM → Flash, diciendo **qué se puede
borrar** en cada uno.

**Movimiento 4 — el cierre técnico (30 s).** "Una ROM de 2ⁿ × m es **un decodificador de n entradas y m
compuertas OR**: es un circuito combinacional que implementa m funciones. Y su uso estrella es el **firmware** y
la **memoria de control** de una UC microprogramada."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Por qué no se pierde el dato? | Porque no hay carga que se descargue ni biestable que se realimente: el bit es una **conexión física** o una **carga atrapada** |
| ¿Se puede escribir una ROM? | Las programables sí, con procedimiento especial, **lento** y con **desgaste**; la de máscara no |
| ¿Diferencia entre EPROM y EEPROM? | EPROM se borra con **UV y toda junta**; EEPROM **eléctricamente** y byte a byte |
| ¿Y el Flash? | EEPROM **por bloques**, más densa y barata: pendrives, SSD, firmware |
| ¿Por qué una ROM es más lenta que una RAM? | Porque su lectura depende de la matriz y la tecnología está optimizada para **densidad**, no para velocidad |
| ¿Dónde está el programa cuando la máquina está apagada? | En ROM o en disco; la RAM se carga al arrancar ([[Estructura básica de un computador]]) |
| ¿Una ROM puede reemplazar un circuito combinacional? | **Sí**: se guarda la tabla de verdad y la ROM la implementa (decodificador + OR) |

---

## 6. Errores típicos
- Decir "ROM = no se puede escribir nunca": las PROM/EPROM/EEPROM/Flash **se graban**.
- Confundir **volátil** con "se puede escribir": son cosas distintas (la RAM es volátil, la ROM no; el Flash se
  puede escribir y es no volátil).
- Decir que la ROM es más rápida que la RAM: **no**.
- Olvidar el uso como **memoria de control** en CPUs microprogramadas (es el ejemplo que conecta con la UC).
- Confundir **EPROM** (UV) con **EEPROM** (eléctrica).

---

## 7. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 3 — Memorias electrónicas* | sección de **ROM** y el **cuadro RAM vs ROM** | la clasificación que usa la cátedra y los usos que enumera | **Es la fuente exacta** de esta pregunta |
| **`memorias.pdf`** — Tema 7 | **7.2 Memorias ROM**: 7.2.1 ROM con diodos/BJT, 7.2.2 ROM con MOS, 7.2.3 **programación**; transparencias de **puerta flotante** (FAMOS, FLOTOX) | cómo se guarda físicamente el bit, cómo se borra con UV y eléctricamente, y la idea de **ROM = decodificador + OR** | Es el material más profundo que tenés sobre ROM |
| **[[TP12 Memoria principal]]** | el TP | el cuadro comparativo y los usos pedidos | Lo que se entrega por escrito |
| **[[Cómo se implementa la Unidad de Control]]** | nota de la bóveda | la **memoria de control** como ROM y el ejemplo del 8088 (504 × 21 bits) | Conecta ROM con UC microprogramada |
| **[[Decodificador]]** y **[[Mintérminos y maxtérminos]]** | notas de la bóveda | decodificador + OR = tabla de verdad hecha hardware | Para explicar por qué una ROM es combinacional |
| **Floyd, *Fundamentos de sistemas digitales*** | tema de **memorias** (ed. 1996: tema 12, págs. 594-644) | ROM, PROM, EPROM, EEPROM con figuras | Dibujos claros de la matriz |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **memoria** | implementación de funciones con ROM, PLA | Para el paralelo ROM vs PLA vs PAL |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **memoria interna** | ROM, flash, EPROM y su papel en el arranque | Contexto de sistema |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo de **jerarquía** y de **control microprogramado** | la ROM de control | Cierra con CISC/RISC |

---

## Relacionado
[[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · [[Jerarquía de memorias]] · [[Memoria caché]] ·
[[Cómo se implementa la Unidad de Control]] · [[Estructura básica de un computador]] · [[Decodificador]]
