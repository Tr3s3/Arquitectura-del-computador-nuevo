---
unidad: 3
tipo: concepto
examen: secundario
prioridad: maxima
---
# Memoria caché

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[Jerarquía de memorias]] (Tanda 2 · 2.4 Jerarquía de memorias) · [[Celda elemental de memoria]] (Tanda 2 · 2.1 Celda elemental de memoria) · [[Memoria ROM y sus tipos]] (Tanda 2 · 2.2 Memoria ROM y sus tipos) · [[Pipeline]] (Tanda 2 · 2.7 Pipeline)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 2.3 Memoria caché]].


> [!abstract] En una frase
> La **caché** es una memoria **chica y rapidísima** (SRAM) puesta entre la CPU y la RAM para guardar **lo último
> que se usó**, apostando a que se va a volver a usar. Cuando la CPU pide un dato, primero mira la caché: si está
> (**acierto / hit**), sigue a toda velocidad; si no está (**fallo / miss**), va a la RAM y **deja copia**.

> [!note] Si es la primera vez que ves esto
> El problema: la CPU ejecuta una instrucción en ~1 ns y la RAM tarda ~50–100 ns en entregar un dato. Si la CPU
> pide todo a la RAM, pasa el **90 % del tiempo esperando**. La solución es la misma que usás en la cocina: tenés
> una **heladera chica** al lado de la mesada (caché) con lo que estás usando, y un **depósito grande** en el
> fondo (RAM). Ir al depósito es lento, pero vas pocas veces porque **lo que usás está cerca**. La caché no
> "adivina el futuro": apuesta a una regularidad de los programas que se llama **localidad**.

---

## 1. Por qué funciona: las dos localidades

| Localidad | Qué dice | Ejemplo |
|---|---|---|
| **Temporal** | si usaste un dato, es probable que lo vuelvas a usar pronto | el contador de un lazo, una variable de suma |
| **Espacial** | si usaste una posición, es probable que uses las **vecinas** | recorrer un arreglo; las instrucciones se ejecutan **en secuencia** |

Gracias a la localidad, **un caché chica puede capturar la mayoría de los accesos**: en la práctica, las cachés
tienen tasas de acierto del 90–99 %.

> [!important] El principio del promedio
> Aunque **cada fallo** cueste muchísimo (ir a la RAM), si los aciertos son el 95 %, el **tiempo promedio** se
> parece al de la caché. Eso es todo el truco de la jerarquía de memoria
> ([[Jerarquía de memorias]]).

---

## 2. Acierto, fallo y el tiempo promedio (AMAT)

```
   AMAT = t_acierto + tasa_de_fallo × penalidad_de_fallo
```
(tiempo medio de acceso a memoria)

**Ejemplo**: caché de 1 ns, RAM de 100 ns, y acierta el 95 % de las veces:
```
  AMAT = 1 ns + 0,05 × 100 ns = 1 + 5 = 6 ns
```
Sin caché serían **100 ns**. Es decir: **seis veces más rápido** con una memoria chiquita. Y si la tasa de
acierto sube al 99 %: `1 + 0,01 × 100 = 2 ns` ⇒ **cincuenta veces** más rápido.

> [!tip] Qué se pregunta de esto
> No hace falta memorizar la fórmula: hace falta saber decir **"el promedio mejora porque los aciertos son
> mayoría"** y saber hacer la cuenta con dos números dados.

---

## 3. Cómo se busca un dato: la dirección partida en tres

La CPU manda una **dirección** (por ejemplo de 16 bits) y la caché la interpreta así:

```
   dirección:  ┌──────────┬──────────┬───────────┐
               │   ETIQUETA (tag)    │  ÍNDICE   │  DESPLAZAMIENTO │
               └──────────┴──────────┴───────────┘
                  ¿es este?   ¿en qué  ¿qué palabra
                              línea?   dentro del bloque?
```

| Campo | Para qué sirve |
|---|---|
| **Índice** (o línea) | dice **en qué casillero** de la caché mirar |
| **Etiqueta** (tag) | dice **si el dato que está ahí es el que busco** (se guarda junto al dato) |
| **Desplazamiento** (offset) | dice **qué palabra** del bloque traído |

Con eso, la búsqueda es: **mirar el casillero del índice, comparar la etiqueta**; si coincide ⇒ **acierto**; si no
⇒ **fallo** (y hay que traer el bloque desde la RAM y escribir la etiqueta nueva).

**Conceptos que acompañan**:
- **Bloque (o línea)**: la unidad que se trae de la RAM de una vez (por ejemplo 16 o 64 bytes). Traer más que un
  dato aprovecha la **localidad espacial**.
- **Bit de validez**: indica si el casillero tiene un dato real (al encender, la caché está llena de basura).
- **Política de escritura**: qué hacer cuando la CPU escribe (abajo).

---

## 4. Los tres mapeos (lo que se pide dibujar)

| Mapeo | Cómo se elige el casillero | Ventaja | Desventaja |
|---|---|---|---|
| **Directo** | `casillero = dirección mod nº de líneas` (cada bloque de RAM tiene **un solo** lugar posible) | **simple y barato**; se compara una sola etiqueta | **conflictos**: dos bloques que caen en el mismo casillero se expulsan mutuamente |
| **Totalmente asociativo** | el bloque puede ir a **cualquier** casillero | **flexible**: menos expulsiones | hay que comparar **todas** las etiquetas a la vez (hardware caro) |
| **Asociativo por conjuntos** (*set associative*) | la caché se divide en **conjuntos** de k líneas; el bloque va a un conjunto fijo, a **cualquiera** de sus k vías | **el compromiso**: casi tan simple como el directo, casi tan flexible como el asociativo | un poco más de hardware |

![Formas de mapear la memoria principal en la caché](../../../assets/cache_mapeos.svg)

> [!example] Ejemplo resuelto de mapeo directo
> Caché de **8 líneas** de 1 palabra, direcciones de 0 a 63, `casillero = dirección mod 8`:
> - Dirección **13** ⇒ casillero `13 mod 8 = 5`.
> - Dirección **21** ⇒ casillero `21 mod 8 = 5` ⇒ **choca** con la 13: si traigo la 21, expulso la 13.
> - Dirección **14** ⇒ casillero 6: **no** choca.
> Moraleja: **el mapeo directo es barato pero genera conflictos previsibles**.

---

## 5. Políticas: qué hacer al escribir y a quién expulsar

**Al escribir** (la CPU modifica un dato):
| Política | Cómo funciona | Ventaja | Desventaja |
|---|---|---|---|
| **Write-through** (escritura directa) | se escribe **en la caché y en la RAM a la vez** | la RAM siempre está actualizada; simple | **más tráfico** a memoria, más lento |
| **Write-back** (post-escritura) | se escribe **sólo en la caché** y se marca la línea como **"sucia"**; se baja a la RAM cuando la expulsan | menos tráfico, más rápido | la RAM queda desactualizada; más complejo (bit *dirty*) |

**Al reemplazar** (cuando el conjunto está lleno, hay que sacar una línea):
| Política | Criterio |
|---|---|
| **LRU** (*least recently used*) | se expulsa la que **hace más tiempo** que no se usa (la mejor, y la más cara de implementar) |
| **FIFO** | se expulsa la **más antigua** |
| **Aleatoria** | cualquiera (sorprendentemente funciona bien y es baratísima) |

**Inicialización**: al encender, la caché tiene **basura**. Por eso cada línea tiene un **bit de validez**: si está
en 0, el contenido se ignora (se trata como fallo).

---

## 6. Los niveles (L1, L2, L3)

| Nivel | Tamaño típico | Velocidad | ¿Dónde está? |
|---|---|---|---|
| **L1** | 32–256 KB | la más rápida (1–2 ns) | **dentro** del núcleo; suele estar **partida** en I-cache (instrucciones) y D-cache (datos) |
| **L2** | 256 KB – 2 MB | intermedia | en el chip, por núcleo |
| **L3** | varios MB | más lenta que L2, más rápida que RAM | compartida entre núcleos |

> [!important] El detalle "Harvard por dentro"
> Que L1 esté **separada en instrucciones y datos** es lo que hace que las CPUs modernas sean **Harvard por
> dentro y von Neumann por fuera** ([[Estructura básica de un computador]]): se pueden buscar la instrucción y el
> dato **al mismo tiempo**, sin pelear por un bus.

Y una mención que suma: **coherencia de caché** — cuando hay varios núcleos, cada uno con su L1/L2, hay que
mantener las copias sincronizadas (protocolos tipo MESI). Y **memoria virtual**: la misma idea aplicada al disco
([[Memoria virtual y administración de memoria]]).

---

## 7. Cómo responderlo en el final (3 minutos)

**Movimiento 1 — el problema (20 s).** "La CPU es mucho más rápida que la RAM; la caché tapa esa diferencia
guardando lo último usado."

**Movimiento 2 — por qué funciona (30 s).** **Localidad temporal y espacial** + la cuenta del AMAT
(`1 + 0,05 × 100 = 6 ns`).

**Movimiento 3 — el dibujo (60 s).** La **dirección partida** en etiqueta / índice / desplazamiento y los **tres
mapeos** (directo, asociativo por conjuntos, totalmente asociativo).

**Movimiento 4 — políticas (40 s).** Escritura: **write-through vs write-back** (con el bit *dirty*). Reemplazo:
**LRU / FIFO / aleatoria**. **Bit de validez** al inicializar.

**Movimiento 5 — cierre (20 s).** "L1 dentro del núcleo y partida en I/D (Harvard por dentro), L2 por núcleo, L3
compartida. Y el remate: **la caché no reduce el tiempo de un acceso, reduce el tiempo promedio**."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Qué pasa en un fallo? | Se trae el **bloque** completo desde la RAM, se guarda con su etiqueta y se marca válido |
| ¿Por qué traer un bloque y no sólo el dato? | Por **localidad espacial**: lo que sigue casi seguro se va a usar |
| ¿Qué es una línea "sucia"? | La que se escribió con **write-back** y todavía no se copió a la RAM |
| ¿Qué mapeo es mejor? | El **asociativo por conjuntos** es el que usan todas las CPUs reales (compromiso) |
| ¿La caché es SRAM o DRAM? | **SRAM** (rapidez); la DRAM es la memoria principal |
| ¿Qué pasa al encender? | Todo es basura: los **bits de validez** en 0 hacen que cada acceso sea un fallo |
| ¿Caché y memoria virtual son lo mismo? | No: una tapa la **latencia de la RAM**; la otra **amplía la memoria** usando el disco. Misma idea, distinto nivel |

---

## 8. Errores típicos
- Decir que la caché "guarda todo": guarda **lo último usado**, es chica.
- Confundir **acierto** con "el dato está en la RAM" (es al revés: **no hace falta** ir a la RAM).
- Decir que write-back es "peor" porque la RAM queda desactualizada: es un **compromiso**, y en la práctica es
  más rápido.
- Olvidar el **bit de validez** y el problema de la inicialización.
- Confundir **bloque** (lo que se trae) con **palabra** (lo que pide la CPU).
- Decir que el mapeo directo "no tiene desventajas": tiene **conflictos**.

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 3 — Memorias electrónicas* | sección de **memoria caché** (está después de la RAM y la ROM) | los mapeos tal como los presenta la cátedra, políticas de escritura, inicialización y niveles | **Es la fuente exacta** de esta pregunta |
| **[[TP12 Memoria principal]]** | el TP | qué se pide de caché por escrito | Lo que hay que entregar |
| **`memorias.pdf`** | **Jerarquía de memoria** (transparencias iniciales) | el lugar de la caché en la pirámide, SRAM vs DRAM | Contexto y vocabulario |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo de **jerarquía de memoria** | mapeo directo / asociativo por conjuntos, LRU, write-back, AMAT | **La mejor ampliación**: es el tema central del capítulo |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **memoria caché** | principios, diseño (tamaño de línea, reemplazo, escritura), multinivel | Muy ordenado y con tablas |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **jerarquía de memoria** | caché, coherencia, memoria virtual | Formalización |
| **Tanenbaum, *Estructura de computadores*** | capítulo de **memoria** | caché y su relación con la memoria virtual | Explicaciones con analogías |
| **[[Jerarquía de memorias]]** | nota de la bóveda | el marco general (dónde encaja la caché) | Para arrancar la respuesta por el lugar y no por el detalle |
| **[[Memoria virtual y administración de memoria]]** | nota de la bóveda | la misma idea aplicada al disco | Para el cierre "un nivel más abajo" |

---

## Relacionado
[[Jerarquía de memorias]] · [[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] ·
[[Memoria virtual y administración de memoria]] · [[Técnicas para aumentar la velocidad]] ·
[[Pipeline]] · [[Estructura básica de un computador]]
