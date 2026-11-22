---
unidad: 2
tipo: concepto
examen: secundario
prioridad: alta
---
# Memoria caché

> [!abstract] En una frase
> La caché es una memoria **pequeña, rápida y transparente** que guarda **copias de los bloques de la
> memoria principal** que la CPU está usando, para que el acceso promedio sea casi tan rápido como ella.
> Se organiza con un **mapeo** (directo, asociativo, por conjuntos), una **política de escritura** y una
> **política de reemplazo**.

## Idea: la caché es una "tabla de equivalencias" rápida
En cada acceso, la CPU pide una dirección; el hardware pregunta a la caché "¿tenés este bloque?".
- **Acierto (hit)**: el dato sale de la caché (rápido).
- **Fallo (miss)**: hay que ir a la RAM, traer el **bloque completo** (no sólo la palabra) y dejarlo en la
  caché (desalojando otro).

Se trae un bloque porque la **localidad espacial** dice que se van a usar las palabras vecinas
([[Jerarquía de memorias]]).

## La dirección vista por la caché
![cache_mapeos](../assets/cache_mapeos.svg)

Se parte la dirección en tres campos:
| Campo | Para qué sirve |
|---|---|
| **Etiqueta (tag)** | identificar **qué** bloque es (se compara con las etiquetas almacenadas) |
| **Índice (línea o conjunto)** | decir **dónde** puede estar dentro de la caché |
| **Desplazamiento (offset)** | elegir la palabra **dentro** del bloque |

Cada línea de caché guarda: `validez (1 bit) + etiqueta + bloque de datos (+ bit dirty si es write-back)`.

## Los tres mapeos
### 1) Mapeo directo
Cada bloque puede ir a **una sola** línea: `línea = nº de bloque mod nº de líneas`.
- Ventaja: comparación con **un solo** comparador (barato y rápido).
- Desventaja: **conflictos**: dos bloques que caen en la misma línea se desalojan mutuamente aunque la
  caché esté vacía en el resto (*thrashing*).

### 2) Mapeo asociativo total
Un bloque puede ir a **cualquier** línea. Hay que comparar la etiqueta con **todas** las líneas, en
paralelo: eso se hace con **memoria asociativa (CAM)**, ver [[Memoria auxiliar y memoria asociativa]].
- Ventaja: mínimos conflictos. Desventaja: hardware caro (un comparador por línea).

### 3) Mapeo asociativo por conjuntos (el real)
La caché se divide en **conjuntos** de k vías: el bloque va a **un conjunto fijo** (por índice) y dentro de
él, a **cualquiera de las k vías**.
- k = 1 ⇒ es directo. k = total de líneas ⇒ es asociativo total.
- Es el compromiso que se usa en L1/L2/L3 (típicamente 2, 4, 8 u 16 vías).

## Políticas de escritura
| Política | Qué hace | Cuándo conviene |
|---|---|---|
| **Write-through** (escritura directa) | escribe **siempre** en caché **y** en RAM | simple, memoria siempre coherente; mucho tráfico |
| **Write-back** (post-escritura) | escribe sólo en caché y marca el bit **dirty**; baja a RAM cuando el bloque se desaloja | menos tráfico; necesita coherencia |

En caso de fallo de escritura: *write-allocate* (trae el bloque y escribe) o *no-write-allocate*.

## Políticas de reemplazo (cuando el conjunto está lleno)
- **LRU** (least recently used): saca el que hace más tiempo no se usa — el mejor, pero caro de implementar.
- **FIFO**: saca el más antiguo (no mira uso).
- **Aleatorio**: sorprendentemente competitivo y baratísimo.
- **LFU**: el menos usado en el tiempo.

## Inicialización de la caché
Al encender (o al hacer RESET) la caché está **vacía**: todas las líneas con el **bit de validez en 0**.
No hay que borrar los datos: alcanza con invalidar. Cuando se carga un bloque, se escribe su etiqueta y se
pone **validez = 1**. Si se desea vaciarla (flush), se ponen todos los bits de validez en 0 (y si es
write-back, antes se bajan los bloques dirty a memoria).

## Niveles L1 / L2 / L3
- **L1**: dentro del núcleo, la más chica y rápida (decenas de KB), separada en datos e instrucciones
  (Harvard interno).
- **L2**: más grande, por núcleo o compartida.
- **L3**: compartida entre núcleos (MB), más lenta.
Bajan a RAM sólo los fallos de L3.

> [!example] Ejemplo numérico de mapeo directo
> Caché de 8 líneas, bloques de 4 palabras. Dirección de 12 bits: `etiqueta (5) | índice (3) | offset (2)`.
> Dirección 0x2A5 = `0010 1010 0101` ⇒ etiqueta `00101`, índice `010` (= línea 2), offset `01` (palabra 1 del bloque).
> Se mira la línea 2: si su validez = 1 y su etiqueta = 00101 ⇒ **hit**; si no ⇒ **miss** y se carga.

## Cómo responderlo en el final
1. Definición y objetivo (acercar el tiempo medio al de la SRAM, aprovechando localidad).
2. Partes de la dirección (etiqueta / índice / offset) y qué guarda cada línea.
3. Los tres mapeos con su compromiso (directo = barato con conflictos; asociativo = flexible y caro;
   por conjuntos = el real).
4. Escritura (write-through vs write-back) y reemplazo (LRU/FIFO/aleatorio).
5. Inicialización: bits de validez en 0 al arrancar.
6. Cerrar con niveles L1/L2/L3 y el cálculo de tiempo medio.

## Errores típicos
- Decir que la caché "guarda sólo el dato pedido" (guarda el **bloque** completo).
- Confundir escritura **directa** (write-through) con mapeo **directo**: son cosas distintas.
- Olvidar el bit de validez (sin él, al arrancar se leería basura).
- Decir que la caché es visible para el programa: es **transparente**.

## Relacionado
[[Jerarquía de memorias]] · [[Celda elemental de memoria]] · [[Memoria auxiliar y memoria asociativa]] · [[Técnicas para aumentar la velocidad]]
