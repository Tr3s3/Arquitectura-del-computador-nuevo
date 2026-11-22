---
unidad: 5
tipo: concepto
examen: secundario
prioridad: alta
---
# Modos de direccionamiento

> [!abstract] En una frase
> El modo de direccionamiento es **cómo se calcula la dirección efectiva (EA)** —la que finalmente se pone
> en el MAR— a partir de lo que dice la instrucción: un valor inmediato, una dirección directa, un registro,
> un puntero en memoria o una dirección más un índice.

## La dirección efectiva (EA)
`EA` = dirección que se envía a la memoria para acceder al operando. Cada modo es una forma distinta de
calcularla; algunos modos **no acceden a memoria** (inmediato, registro) y otros acceden **una o dos veces**.

![modos_direccionamiento](assets/modos_direccionamiento.svg)

## Los cinco modos de la cátedra
| Modo | Forma simbólica | Cómo se calcula EA | Accesos a memoria | Uso típico |
|---|---|---|---|---|
| **Inmediato** | `OP dato` | no hay EA: el operando **es** el campo de la instrucción | 0 | cargar constantes: `LDI 5` |
| **Directo (absoluto)** | `OP D` | `EA = D` | 1 (el del operando) | variables globales: `LDA 25h` |
| **Por registro** | `OP R` | `EA = R` (el dato está en el registro) | 0 | operar entre registros |
| **Indirecto** | `OP @D` | `EA = M[D]` (en D hay una dirección) | **2** (uno para leer el puntero, otro para el dato) | punteros, listas, vectores |
| **Indexado** | `OP D + X` | `EA = D + X` (X = RIF o RID) | 1 | arreglos, tablas, recorridos |

> [!tip] Cómo se distinguen de un vistazo
> Preguntate: **¿cuántas veces hay que ir a memoria para tener el dato?**
> Inmediato = 0 (está en la instrucción) · Registro = 0 (está en un registro) · Directo = 1 · Indirecto = 2
> · Indexado = 1 (+ el registro que ya está en la CPU).

## Ejemplos con un vector
Supongamos el arreglo `V` que empieza en la dirección 100, con elementos de 1 palabra, y queremos sumar
`V[0] + V[1] + V[2]`.

**Sin indexado (directo puro):** hay que escribir una instrucción por elemento
```
LDA  100      ; V[0]
ADD  101      ; V[1]
ADD  102      ; V[2]
```
El código **depende de la posición**: para recorrer 50 elementos hay que escribir 50 instrucciones.

**Con indexado:** una sola instrucción dentro de un lazo
```
        LDA  cero
        STA  suma
        INI  RIF, 100     ; RIF ← 100 (puntero al arreglo)
        LDA  tres         ; contador de vueltas
        STA  cont
lazo:   LDA  0, RIF       ; EA = 0 + RIF ⇒ V[i]
        ADD  suma
        STA  suma
        INC  RIF          ; RIF ← RIF + 1  (siguiente elemento)
        LDA  cont
        SUB  uno
        STA  cont
        JZ   fin
        JMP  lazo
fin:    HLT
```
**Ventaja del indexado: el mismo código sirve para cualquier posición y cualquier tamaño del arreglo.**
Eso es lo que responde la pregunta "¿ventajas del direccionamiento indexado?".

## Ventajas del indexado (respuesta corta para el final)
1. **Recorrido de arreglos y tablas sin reescribir el código** (un lazo en lugar de n instrucciones).
2. **Ahorro de bits**: la dirección de la instrucción es un desplazamiento chico (`0`, `1`, `2`…) y el resto
   lo aporta el registro.
3. **Reubicación**: el mismo programa funciona en cualquier zona de memoria si se cambia el contenido del
   registro índice (base).
4. **Implementación barata**: un **sumador de direcciones** y dos registros índice.
5. Permite **estructuras de datos** (vectores, matrices, registros de una estructura) con desplazamiento fijo.

## Cómo se implementa el indexado en hardware
```
  campo dirección (IR) ──→ ┌──────────────┐
                          │  SUMADOR DE  │──→ MAR
      RIF / RID ─────────→│  DIRECCIONES │
                          └──────────────┘
```
- El **modificador** de la instrucción decide si se suma RIF, RID o nada.
- El resultado va al **MAR** en el momento del acceso. Esto se ve en
  [[BLUE indexada (RIF, RID, nuevo formato)]].

## Modos que conviene nombrar de más (suman)
- **Relativo al PC**: `EA = PC + desplazamiento` (saltos relativos, código reubicable).
- **Por registro indirecto**: `EA = M[R]` (el registro guarda la dirección, no el dato).
- **Base + índice**: `EA = base + índice + desplazamiento` (el clásico de x86 para matrices).
- **Autoincremento / autodecremento**: el registro se actualiza solo después/antes del acceso (pilas).

## Cómo responderlo en el final
1. Definir dirección efectiva y modo de direccionamiento.
2. Recorrer los cinco modos con el cálculo de EA y los accesos a memoria de cada uno.
3. Dar un ejemplo de código con vector: directo vs indexado.
4. Enumerar las **ventajas del indexado** (es la pregunta que sigue).
5. Mencionar la implementación (sumador de direcciones + RIF/RID).

## Errores típicos
- Confundir **indirecto** con **indexado**: el indirecto "va a buscar la dirección a memoria"; el indexado
  "suma un registro a la dirección".
- Decir que el inmediato tiene dirección efectiva.
- Olvidar que el indirecto hace **dos** accesos a memoria (lento).
- Confundir el registro índice (guarda un desplazamiento/posición) con el registro base (guarda el origen
  del bloque) — en la práctica se usan parecido.

## Relacionado
[[BLUE indexada (RIF, RID, nuevo formato)]] · [[Formato de la instrucción (4 formatos)]] · [[Registros de la CPU]] · [[CISC y RISC]]
