---
unidad: 5
tipo: concepto
examen: secundario
prioridad: maxima
---
# Registros base e índice

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[BLUE indexada (RIF, RID, nuevo formato)]] (Tanda 1 · 1.2 BLUE vs BLUE indexada) · [[BLUE vs BLUE indexada — qué cambia y por qué]] (Tanda 1 · 1.2 BLUE vs BLUE indexada) · [[Registros de la CPU]] (Materia · Unidad 5) · [[Modos de direccionamiento]] (Tanda 2 · 2.10 Modos de direccionamiento)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 2.9 Registros base e índice]].


> [!abstract] En una frase
> Los **registros índice** (RIF y RID en la BLUE indexada) son registros que el **programador** usa como
> punteros: su contenido **se suma al campo de dirección** sólo cuando la instrucción lo pide, y sirven para
> recorrer arreglos y tablas con un solo código. El **registro base** (RB) también se suma a la dirección,
> pero **siempre** —el programador común no lo controla— y sirve para **reubicar** el programa completo en
> memoria sin tocar una sola instrucción.

## Partamos de cero: el problema que resuelven
Supongamos que hay que sumar 100 números que están guardados a partir de la dirección 1000. Sin registros
índice, en la BLUE original, hay que escribir:

```
ADD 1000
ADD 1001
ADD 1002
...
ADD 1099      ← 100 instrucciones, 100 palabras de memoria
```

Tres problemas:
1. **Ocupa mucha memoria** (100 palabras para algo que es siempre lo mismo).
2. **No sirve para otro arreglo**: cambiás la posición inicial y hay que reescribir todo.
3. **No sirve para otro tamaño**: 200 números ⇒ otro programa.

La causa es que la dirección está **"incrustada" en la instrucción**. La solución: guardar la **parte que
cambia** (la posición) en un **registro**, y dejar en la instrucción sólo la **parte fija** (el
desplazamiento). La dirección real se calcula **sumando** las dos cosas justo antes de ir a memoria.

> [!important] La idea en una línea
> **Índice = "cuánto me muevo desde el principio" + "dónde está el principio".** El desplazamiento lo dice
> la instrucción; el principio lo dice el registro; la suma la hace un **sumador de direcciones** dedicado.

## Los registros índice de la BLUE indexada
| Registro | Bits | Para qué |
|---|---|---|
| **RIF** — Registro Índice Fuente | 16 | puntero al arreglo de **origen** (de donde leo) |
| **RID** — Registro Índice Destino | 16 | puntero al arreglo de **destino** (donde escribo) |
| **RB** — Registro Base | 16 | desplazamiento global del programa (lo carga el sistema) |
| **W** y **X** | 16 | registros temporales, **entradas del sumador de direcciones** (no los ve el programador) |

**Ojo con W y X**: no son registros índice. Son la "mesa de trabajo" del sumador de direcciones: en el ciclo
de ejecución, **W** recibe el campo de dirección leído de memoria y **X** recibe el índice (o el 0 del modo
directo). La suma `W + X` es la **dirección efectiva**.

## Los dos modos indexados (modificador 2 y 3)
```
  instrucción:  LDA 2, 1000      →  EA = 1000 + RIF
  instrucción:  LDA 3, 1000      →  EA = 1000 + RID
```
| Modificador | Modo | Dirección efectiva |
|---|---|---|
| `0` | directo | `EA = campo de dirección` |
| `1` | indirecto | `EA = M[campo de dirección]` |
| **`2`** | **indexado por RIF** | **`EA = campo + RIF`** |
| **`3`** | **indexado por RID** | **`EA = campo + RID`** |

Y en toda referencia a memoria, **además**: `dirección física = EA + RB`.

## Las instrucciones que los manejan
| Instrucción | Qué hace |
|---|---|
| `ENI Reg, valor16` | carga **un valor entero** en el registro (`ENI RID, 1000` ⇒ RID = 1000) |
| `INI Reg, valor11` | **incrementa** el registro en un valor (`INI RIF, 2` ⇒ RIF = RIF + 2) |
| `LIX Reg, dir` / `SIX Reg, dir` | carga / guarda el registro desde/hacia **memoria** |
| `RXT Reg, Reg` | copia un registro en otro (AC, RIF, RID) |
| `IJP Reg, dir` | **salta si el registro no es cero** (el "for" del repertorio: sirve para los lazos) |
| `ENI RB, valor16` | carga el registro base (**instrucción privada**: sólo el sistema) |

> [!warning] Detalle que vale puntos
> `LIX RIF, X` **no** tiene modo indexado. ¿Por qué? Porque sería "auto-indexado": estaría usando el registro
> que justamente va a cargar. En el final, si preguntan "¿todos los modos aplican a todas las instrucciones?",
> la respuesta es **no**.

## El arreglo con índice, dibujado
```
 memoria                         RIF = 1000
 ┌──────────────┐                    │
 │  1000  [ 7 ] │◄── EA = 0 + 1000   │  LDA 2, 0
 │  1001  [ 3 ] │◄── EA = 1 + 1000   │  INI RIF, 1
 │  1002  [ 9 ] │◄── EA = 2 + 1000   │  LDA 2, 1
 │   ...        │                    │
 └──────────────┘        campo de dirección = desplazamiento (constante)
                         RIF = posición actual (cambia en el lazo)
```

```
        INI RID, 0            ; i = 0
        ENI RIF, 1000         ; puntero al arreglo
        LDA  0, cero
        STA  0, suma
lazo:   LDA  2, 0              ; AC ← M[0 + RIF]  (el lazo siempre dice "0"!)
        ADD  0, suma
        STA  0, suma
        INI  RIF, 1           ; siguiente elemento
        INI  RID, 1           ; contador++
        LDA  2, 0 ...         ; (comparación con el tope, según el enunciado)
        IJP  RID, lazo        ; si no terminó, vuelve
```

Lo importante: **la instrucción del lazo no cambia nunca**; lo que cambia es el registro. Diez líneas sirven
para 100 o para 10 000 elementos.

## El registro base y la reubicación (para qué existe)
Un programa se escribe pensando que empieza en la dirección 0. Pero en un sistema real:
- puede haber **varios programas** en memoria a la vez (multiprogramación), y no todos pueden empezar en 0;
- las primeras direcciones suelen estar reservadas (vector de interrupciones, tablas del sistema);
- el **monitor** del sistema puede necesitar **mover** un programa ya cargado para juntar hueco libre.

Si hay que mover el programa, hay que **corregir todas las direcciones** de sus instrucciones… pero **no sus
constantes** (un 5 es un 5, no una dirección). Ese era el trabajo del *Relocating Loader*: distinguir una cosa
de la otra instrucción por instrucción. **El registro base elimina ese trabajo**: se carga en RB la dirección
donde empezó el programa y el hardware **suma RB a toda referencia a memoria**. Las constantes quedan intactas
porque no son referencias a memoria.

> [!example] El ejemplo de la cátedra
> Programa pensado desde 0:
> ```
> 0000  ENI RID, 1000     ; constante 1000
> 0001  LDA 3, 1234       ; M[1234 + 1000] = M[2234]
> ```
> Si el programa se carga a partir de **5000**, con RB = 5000 la segunda instrucción accede a
> `M[1234 + 1000 + 5000]` **sin que nadie modifique la instrucción 5001**. El programa quedó reubicado
> **sin tocar el código**.

## Índice vs base: la diferencia en un cuadro (pregunta típica)
| | **Registro índice (RIF/RID)** | **Registro base (RB)** |
|---|---|---|
| Quién lo controla | el **programador** (con ENI/INI/LIX) | el **sistema** (instrucción privada) |
| Cuándo se suma | **sólo si el modificador es 2 o 3** | **siempre**, en toda referencia a memoria |
| Para qué sirve | **recorrer** arreglos, tablas, cadenas | **reubicar** el programa completo |
| Qué representa | la **posición dentro** de la estructura | el **origen** de la estructura |
| Efecto en las constantes | ninguno (sólo afecta referencias indexadas) | ninguno (sólo afecta referencias a memoria) |
| Cuántos hay | 2 (fuente y destino) | 1 |

> [!tip] Frase para el oral
> "El índice dice **por dónde voy**; el base dice **dónde empieza todo**. El índice lo maneja el programador y
> se suma cuando la instrucción lo pide; el base lo maneja el sistema y se suma siempre."

## El hardware que los involucra
```
   campo de dirección (16) ──────┐
                                  ▼
   RIF / RID ──► MUX ──► X ──► ┌───────┐
                               │   Σ   │──► EA ──► [+] ──► MAR
   RB ────────────────────────►└───────┘           ▲
                                                   │
                                       (suma del base, permanente)
```
- **Sumador de direcciones**: dedicado, no gasta tiempo de ALU.
- **Multiplexor**: elige qué entra en X: `0` (directo), `RIF` o `RID` — lo manda el **decodificador del campo
  modificador**.
- El **RB** se suma a la dirección efectiva en toda referencia a memoria.

## Cómo responderlo en el final (2–3 minutos)
1. **Definición**: qué es un registro índice y para qué está (recorrer arreglos con un lazo).
2. **Dibujo**: memoria a la izquierda con el arreglo, el registro con una flecha al sumador, y la instrucción
   con su desplazamiento fijo.
3. **Modos**: `EA = campo + RIF/RID` (modificador 2/3) y las instrucciones `ENI`, `INI`, `LIX`, `SIX`, `RXT`,
   `IJP`.
4. **Base**: `EA + RB` siempre; reubicación; el ejemplo 1000 → 5000.
5. **Cierre**: la diferencia índice/base (tabla de arriba) y el beneficio: **el mismo código sirve para
   cualquier posición y tamaño**.

## Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 5* | sección de la **BLUE indexada**: registros nuevos, sumador de direcciones, campo modificador | la descripción de **RIF, RID y RB** con el formato de la instrucción | **Es la fuente exacta** de esta pregunta |
| **`blue.pdf`** (Foster) | el capítulo de la máquina elemental, donde explica por qué el bus común y el direccionamiento directo limitan el repertorio | el contraste: la BLUE **base no tiene** registros índice | Para justificar "qué se agregó y por qué" |
| **[[BLUE indexada (RIF, RID, nuevo formato)]]** · **[[BLUE vs BLUE indexada — qué cambia y por qué]]** | notas de la bóveda | el formato 5+2+9+16, las instrucciones `ENI`/`INI`/`LIX`/`SIX`/`RXT`/`IJP` y la tabla de "qué cambia" | El desarrollo completo del hardware |
| **[[Modos de direccionamiento]]** | nota de la bóveda | los siete modos y el ejemplo del vector con RIF | El marco conceptual: por qué el índice existe |
| **[[Ciclo de LDA indexada (los 24 pulsos)]]** | nota de la bóveda | `RID→X`, `MBR→W`, `Σ→MAR` en los pulsos exactos | Bajar el registro índice a señales concretas |
| **[[TP19 Modos de direccionamiento]]** | el TP | la tabla de modos y el ejercicio del arreglo | Lo que se entrega por escrito |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **modos de direccionamiento** | **indexado** y **base con desplazamiento**, y la diferencia conceptual entre ambos | La mejor ampliación teórica |
| **Brey, *Los microprocesadores Intel 8086/8088*** | capítulo de **direccionamiento** | `BX`/`SI`/`DI`/`BP` como base e índice, y la fórmula `seg × 10h + offset` | El caso real: los mismos conceptos con otros nombres |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **modos de direccionamiento** | indexado, autoincremento y registro base | Notación formal |

## Errores típicos
- Decir que el índice se suma siempre: se suma **sólo en los modos 2 y 3**.
- Confundir **W y X** con registros índice: son temporales del sumador de direcciones.
- Confundir **registro índice** con **registro de índice en un arreglo de C**: acá es hardware, un registro
  real de 16 bits dentro de la CPU.
- Decir que el RB cambia las constantes: no; sólo las **referencias a memoria**.

## Relacionado
[[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Ciclo de LDA indexada (los 24 pulsos)]] ·
[[Modos de direccionamiento]] · [[Registros de la CPU]] · [[TP19 Modos de direccionamiento]] ·
[[Espacio de direccionamiento y cálculo de CodOp-Dirección]]
