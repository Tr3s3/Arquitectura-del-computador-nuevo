---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# BLUE indexada (RIF, RID, nuevo formato)

> [!abstract] En una frase
> Es la **evolución de BLUE** que agrega **dos registros índice (RIF y RID)** y un **modificador de 2 bits**
> en la instrucción, con un **sumador de direcciones** que calcula `EA = dirección ± RIF/RID` en el momento
> del acceso. Con eso, la misma instrucción sirve para recorrer arreglos y tablas: es el paso de una máquina
> de acumulador a una máquina con **modos de direccionamiento**.

## Lo que se agrega respecto de BLUE base
| Se agrega | Para qué |
|---|---|
| **RIF** (registro índice final) | guarda un desplazamiento/posición que se suma a la dirección |
| **RID** (registro índice de desplazamiento) | segundo índice (permite dos recorridos simultáneos: fila/columna de una matriz, dos arreglos) |
| **Nuevo formato de instrucción** | `opcode (5 bits) + dirección (16 bits) + modificador (2 bits)` |
| **Sumador de direcciones** | calcula `EA` sumando el índice al campo dirección |
| **Decodificador del modificador** | interpreta los 2 bits de modo y habilita el camino correcto |
| **Instrucciones nuevas** | `INI RIF` / `INI RID` (inicializar índice), `INC`/`DEC` de índice, etc. |
| **Sistema de interrupciones** | SI habilitado/inhabilitado, estados F/E/I ([[Interrupciones y entrada-salida]]) |

## El nuevo formato de instrucción
```
  ┌─────────┬───────────────────────────┬──────────────┐
  │ opcode  │        dirección          │ modificador  │
  │ 5 bits  │        16 bits            │   2 bits     │
  └─────────┴───────────────────────────┴──────────────┘
```
- **5 bits de opcode** ⇒ hasta 32 instrucciones (el doble que la BLUE base: entran las de índice y las de
  E/S nuevas).
- **16 bits de dirección** ⇒ espacio direccionable de 64 K palabras (mucho más que las 4096 de la base).
- **2 bits de modificador** ⇒ 4 modos:
  | Modificador | Modo | EA |
  |---|---|---|
  | `00` | **directo** | `EA = D` |
  | `01` | **indirecto** | `EA = M[D]` |
  | `10` | **indexado por RIF** | `EA = D + RIF` |
  | `11` | **indexado por RID** | `EA = D + RID` |

> [!warning] Total de bits
> `5 + 16 + 2 = 23 bits`. En los apuntes se lo suele completar a **24 bits (3 bytes)** por prolijidad, y
> algunos textos cuentan el modificador antes de la dirección. Copiá el orden exacto de campos de tu apunte:
> lo que importa es que puedas decir **qué hace cada campo** y **cuántos modos habilita**.

## El sumador de direcciones (la pieza nueva)
![modos_direccionamiento](assets/modos_direccionamiento.svg)

```
   dirección (16 bits, del IR) ──┐
                                 ├──→ SUMADOR ──→ EA ──→ MAR
   RIF o RID (según modificador)─┘
```
- Se activa **sólo** en los modos indexados; en directo e indirecto el campo dirección pasa sin sumar
  (el sumador está deshabilitado o suma 0).
- Es un [[Sumador completo|sumador]] de 16 bits; su resultado va al MAR en el pulso correspondiente.
- El **decodificador del modificador** es el que decide qué registro se suma (o ninguno): es un
  [[Multiplexor]] de 3 entradas (0, RIF, RID) controlado por los 2 bits.

## Ciclos de las instrucciones en la versión indexada
Los ciclos cambian según el modo, porque el número de accesos a memoria es distinto:

| Instrucción / modo | Accesos a memoria | Ciclo (esquema) |
|---|---|---|
| `LDA D` **directo** (`00`) | 1 | búsqueda + `MAR ← D` + lectura + `AC ← MBR` |
| `LDA D` **indirecto** (`01`) | **2** | búsqueda + lectura del puntero + **segunda** lectura + `AC ← MBR` |
| `LDA D` **indexado RIF** (`10`) | 1 | búsqueda + `MAR ← D + RIF` (sumador) + lectura + `AC ← MBR` |
| `LDA D` **indexado RID** (`11`) | 1 | igual, con RID |
| `INI RIF` | 0 (o 1 si el valor viene de memoria) | carga el registro índice: `RIF ← dato` |
| `ENI RID` | — | habilita/usa RID como índice activo |

Por eso en el apunte se habla de **"LDA 3/1/0"**: son las tres variantes de ciclo de `LDA` (los tres modos
con acceso a memoria) más los casos sin acceso. Ver [[Ciclo de la instrucción LDA (24 pulsos)]] para el
detalle pulso por pulso del modo directo.

> [!example] Cómo cambia la misma instrucción según el modificador
> Instrucción `LDA 100, mod` con `RIF = 4`:
> - `mod = 00` ⇒ carga `M[100]`
> - `mod = 01` ⇒ carga `M[M[100]]` (el contenido de 100 es una dirección)
> - `mod = 10` ⇒ carga `M[104]` (100 + RIF)
> - `mod = 11` ⇒ carga `M[100 + RID]`
> **Una sola instrucción, cuatro comportamientos**: eso es lo que gana la máquina indexada.

## Cómo responderlo en el final (pregunta principal #6)
1. Explicar qué problema resuelve: recorrer arreglos/tablas sin reescribir el código.
2. Enumerar los agregados: RIF, RID, nuevo formato, sumador de direcciones, decodificador del modificador,
   instrucciones nuevas.
3. Dibujar el formato `5 / 16 / 2` y la tabla de los 4 modos con su EA.
4. Comparar el **ciclo de ejecución sin indexar vs indexado**: misma secuencia, pero con el sumador en el
   camino de la dirección; y el indirecto con su segundo acceso.
5. Cerrar con la ventaja: **menos instrucciones, código reutilizable, direcciones cortas**.

## Errores típicos
- Decir que el indexado accede dos veces a memoria (eso es el indirecto).
- Olvidar el decodificador del modificador (sin él la UC no sabe qué modo ejecutar).
- Confundir RIF con RID (los dos son índices; el apunte usa RIF/RID como "final" y "desplazamiento").
- Pensar que el sumador de direcciones reemplaza a la ALU: es un sumador **dedicado** en el camino de la
  dirección, para no gastar un pulso de ALU.

## Relacionado
[[Modos de direccionamiento]] · [[Ciclo de ejecución — todas las operaciones]] · [[Formato de la instrucción (4 formatos)]] · [[Interrupciones y entrada-salida]]
