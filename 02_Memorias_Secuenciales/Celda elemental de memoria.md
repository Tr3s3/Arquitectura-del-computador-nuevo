---
unidad: 2
tipo: concepto
examen: secundario
prioridad: alta
---
# Celda elemental de memoria

> [!abstract] En una frase
> La celda elemental es el circuito que **guarda 1 bit** dentro de una memoria: un biestable (o latch)
> con una **línea de selección** para leerlo/escribirlo. Miles de celdas + decodificador + buffers de
> E/S = un chip de memoria.

## Del biestable a la celda
Un [[Flip-Flops SR, D, JK y T|flip-flop D]] guarda 1 bit, pero está siempre disponible: hay que poder
decidir **cuándo** se escribe y **cuándo** se lee. La celda elemental agrega eso:

```
        línea de selección (W / word line)
                 │
        ┌────────┴────────┐
  dato ─┤  FF D (bit)     ├─ dato (línea de bit / bit line)
        └─────────────────┘
                 │
           R/W' (leer/escribir)
```
- **Selección (W):** habilita la celda. Sin selección, la celda está "desconectada" del bus de datos.
- **R/W':** define la operación. `R/W' = 0` ⇒ escritura (el dato entra al FF). `R/W' = 1` ⇒ lectura
  (el FF pone su valor en la línea de bit).
- La salida del FF va al bus de datos a través de un **buffer de tres estados**: sólo la celda
  seleccionada habilita su salida, el resto queda en **alta impedancia (Z)** y no carga el bus.

> [!tip] "Tres estados" = 0, 1 y alta impedancia
> Es la clave para que muchas celdas compartan un mismo bus de datos sin cortocircuitarse.
> Aparece también en el [[Flujo de información en BLUE (datos y direcciones)|bus de la CPU]].

## Tipos de celda
| | SRAM (estática) | DRAM (dinámica) |
|---|---|---|
| Qué guarda | latch de 4-6 transistores (FF) | 1 transistor + 1 capacitor |
| Retención | mantiene mientras haya alimentación | el capacitor **se descarga** ⇒ **refresco** periódico (ms) |
| Velocidad | muy rápida | más lenta (necesita amplificador de lectura) |
| Densidad / costo | menor densidad, más cara | máxima densidad, más barata |
| Uso | caché, registros | memoria principal |

- **SRAM**: 6 transistores por bit (dos inversores cruzados + 2 de acceso). No necesita refresco.
- **DRAM**: el bit es **carga eléctrica**; se lee "destructivamente" (hay que reescribir el valor leído) y
  se refresca cada pocos milisegundos.
- **ROM**: la celda es un punto de conexión fijo (fusible, transistor ausente/presente): no se puede
  escribir en operación. Ver [[Memoria ROM y sus tipos]].

## Organización de la matriz (2D y 3D)
Las celdas se ordenan en una **matriz**; para n bits de dirección:
- **2D**: n bits → decodificador de fila → se habilita una de 2ⁿ filas; cada fila es una palabra completa
  (todos sus bits). Es el esquema de la [[Memoria RAM 8x3]].
- **3D (coincidencia de dos dimensiones)**: la dirección se parte en fila (X) y columna (Y); la celda
  **en la intersección** es la seleccionada. Ahorra decodificadores gigantes y es el esquema real de las
  memorias grandes: dos decodificadores de 2^(n/2) en lugar de uno de 2ⁿ.
- **Entrelazado de bancos**: la memoria se divide en bancos que pueden atender pedidos en paralelo
  (se ve en [[Paralelismo y procesamiento vectorial]]).

## Cómo responderlo en el final
1. Definición: celda = 1 bit + selección + R/W'.
2. Dibujo: FF D con línea de selección y buffer de tres estados hacia la línea de bit.
3. Explicar lectura (el FF vuelca su valor) y escritura (el dato entra al FF en el flanco de W).
4. Distinguir SRAM (latch, sin refresco) de DRAM (capacitor, refresco) y mencionar la ROM.
5. Cerrar: celdas + decodificador + buffers = chip de memoria; el decodificador elige la **palabra**.

## Errores típicos
- Decir que la celda DRAM "no pierde el dato": lo pierde en milisegundos sin refresco.
- Olvidar el buffer de tres estados (sin él, dos celdas en el mismo bus se destruyen).
- Confundir **línea de palabra** (selección de fila) con **línea de bit** (dato).

## Relacionado
[[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] · [[Memoria caché]] · [[Flip-Flops SR, D, JK y T]]
