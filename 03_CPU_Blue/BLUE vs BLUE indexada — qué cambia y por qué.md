---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# BLUE vs BLUE indexada — qué cambia y por qué

> [!abstract] En una frase
> La **BLUE** es la máquina elemental del apunte de Foster: 16 instrucciones, 4096 celdas, instrucción de
> una palabra con **4 bits de opcode + 12 de dirección** y un solo modo de direccionamiento (directo).
> La **BLUE indexada** es la misma máquina con hardware agregado —**RIF, RID, registro base, sumador de
> direcciones, dos registros de entrada W y X y un decodificador del campo modificador**— para tener
> **32 instrucciones, 65536 celdas y 4 modos de direccionamiento**, con instrucciones de **2 palabras**.

## Partamos de cero: qué es "indexar" y por qué alguien querría hacerlo
Imaginate que en la memoria hay 100 números guardados uno al lado del otro, en las direcciones 1000, 1001,
1002… y querés sumarlos. Con la BLUE original tendrías que escribir **100 instrucciones distintas**
(`ADD 1000`, `ADD 1001`, …), cada una con su dirección "cableada" en la instrucción. Funciona, pero:
- el programa ocupa 100 palabras de memoria,
- si querés sumar 200 números, reescribís todo,
- y el programa **sólo sirve para esa posición de memoria**: si lo cargás en otra zona, todas las
  direcciones quedan mal.

La solución es **separar la dirección en dos partes**: una parte fija que dice la instrucción (el
*desplazamiento* o *offset*) y una parte variable que está en un **registro** de la CPU. La dirección
efectiva es la **suma** de las dos. Eso es indexar: `EA = desplazamiento + registro índice`. Con eso, el
mismo código recorre cualquier arreglo y cualquier posición (un lazo en lugar de 100 instrucciones).

> [!important] Las cuatro cosas que hay que poder decir de memoria
> 1. **Qué se agregó**: RIF, RID, RB, sumador de direcciones, W y X, decodificador del modificador.
> 2. **Qué cambió en el formato**: de 4+12 (16 bits, 1 palabra) a 5+2+9+16 (32 bits, 2 palabras).
> 3. **Qué ganó**: 32 instrucciones, 65 536 celdas, 4 modos de direccionamiento, programas reubicables.
> 4. **Qué costó**: instrucciones más largas (2 palabras), más ciclos de máquina (de 1 a 4), más hardware.

## La comparación, punto por punto

| | **BLUE** (máquina elemental) | **BLUE indexada** |
|---|---|---|
| Memoria | 4096 celdas (2¹²) de 16 bits | **65 536** celdas (2¹⁶) de 16 bits |
| Código de operación | **4 bits** ⇒ 16 instrucciones | **5 bits** ⇒ 32 instrucciones (se usan 00…37 octal) |
| Campo de dirección | 12 bits | **16 bits** |
| Otros campos | — | **modificador 2 bits** + 9 bits sin uso |
| Formato de instrucción | fijo, **1 palabra** | **variable: 1 o 2 palabras** |
| Modos de direccionamiento | **directo** (y por registro, implícito en el AC) | **4**: directo (0), indirecto (1), indexado por RIF (2), indexado por RID (3) |
| Registros | PC, MAR, MBR, IR, AC, SR (llaves), Y, Z | los mismos **+ RIF, RID, RB, W, X** |
| Sumador de direcciones | no | **sí**, dedicado (no gasta tiempo de ALU) |
| Instrucciones nuevas | — | RXT, SIX, LIX, ENI, INI, IJP (+ ION, IOF, SKF, EMR, RTI si se agregan interrupciones) |
| Instrucciones que salen | — | ninguna: las 16 originales siguen, con el modificador 0 |
| Ciclos por instrucción | 1 o 2 (+ los de E/S) | **de 1 a 4** según instrucción y modo |
| Dirección del programa | fija (se arma para una posición) | **reubicable** (registro base) |
| Interrupciones | **no tiene** | se le agregan (sistema elemental con SI, IRQ, estados F/E/I) |

## Qué significa cada agregado de hardware

**RIF y RID (Registros Índice Fuente y Destino)** — dos registros de 16 bits que el programador maneja con
`ENI` (cargar valor), `INI` (incrementar), `LIX`/`SIX` (cargar/guardar desde memoria) y `RXT` (copiar entre
registros). Son los "punteros" que permiten recorrer arreglos.

**Sumador de direcciones (Σ)** — un sumador dedicado a calcular `dirección + índice`. ¿Por qué uno aparte y
no la ALU? Porque **no gasta tiempo de ALU**: mientras el sumador de direcciones calcula la dirección del
operando, la ALU puede estar resolviendo otra cosa. Sus entradas son **W** y **X** (dos registros
temporarios): en uno se carga el campo de dirección de la instrucción y en el otro el índice (o el 0 del modo
directo).

**Registro Base (RB)** — se suma **siempre** que se hace una referencia a memoria, y el programador común no
lo toca. Sirve para **reubicar** programas: si el programa se cargó en 5000, se pone 5000 en RB y todas las
direcciones quedan automáticamente desplazadas, sin tocar las constantes. Es lo que hace innecesario el
*Relocating Loader* que tenía que distinguir direcciones de constantes al reubicar.

**Decodificador del campo modificador** — un decodificador de 2 bits que, además del decodificador de
instrucciones, elige el modo: 00 directo, 01 indirecto, 10 índice RIF, 11 índice RID.

> [!example] El mismo programa en las dos máquinas
> **BLUE:** `LDA 1000` — 1 palabra; carga el contenido de la celda 1000. Siempre la misma celda.
>
> **BLUE indexada:** `LDA 3, 1000` — 2 palabras; si RID contiene 5000, carga `M[1000 + 5000] = M[6000]`.
> Cambiando RID se recorre todo el arreglo **sin cambiar la instrucción**.
>
> Y `LDA 0, 1000` es exactamente la `LDA 1000` de la BLUE original: **las viejas instrucciones son un caso
> particular de las nuevas** (modificador 0). Eso es lo que hay que decir en el final: la indexada **no
> reemplaza** a la BLUE, la **extiende**.

## El formato, dibujado

```
BLUE (16 bits = 1 palabra)
┌────────┬────────────────────┐
│ Opcode │   Dirección        │
│ 4 bits │     12 bits        │
└────────┴────────────────────┘

BLUE INDEXADA (32 bits = 2 palabras)
┌────────┬──────┬──────────┬──────────────────────┐
│ Opcode │ Modif│ sin uso  │  Campo de dirección  │
│ 5 bits │2 bits│  9 bits  │       16 bits        │
└────────┴──────┴──────────┴──────────────────────┘
```

Como la instrucción **ya no entra en una palabra**, el ciclo de búsqueda trae sólo la primera palabra y el
campo de dirección se busca en un **ciclo de máquina extra** (por eso la `LDA` pasa de 16 a 24 pulsos).
Desarrollo completo en [[Ciclo de LDA indexada (los 24 pulsos)]].

## Cómo responderlo en el final (2–3 minutos)
1. **Definición**: "la BLUE es la máquina elemental de Foster; la indexada es la BLUE con registros índice,
   registro base y sumador de direcciones para agregar modos de direccionamiento".
2. **Dibujo**: los dos formatos, uno arriba del otro (4+12 vs 5+2+9+16). El dibujo ya explica la mitad.
3. **Tabla**: memoria, opcodes, tamaño de instrucción, modos, registros nuevos, ciclos.
4. **Por qué**: recorrer arreglos con un lazo, reubicar programas, direccionar más memoria.
5. **Cierre**: "las 16 instrucciones de la BLUE original siguen existiendo con modificador 0: la indexada es
   una **extensión compatible**, y el precio es instrucciones de 2 palabras y ciclos más largos".

## Errores típicos
- Decir que la BLUE indexada **reemplaza** a la BLUE: la extiende.
- Confundir los **4 modos** del modificador (0 directo, 1 indirecto, 2 RIF, 3 RID) con los 7 modos teóricos
  de los libros. En el final de esta cátedra, los 4 de la BLUE indexada son los que importan:
  ver [[Modos de direccionamiento]].
- Olvidar que el **registro base se suma siempre**; el índice se suma **sólo si el modificador lo pide**.
- Decir "24 pulsos" sin poder explicar que son **3 ciclos de máquina de 8**.

## Relacionado
[[Ciclo de LDA indexada (los 24 pulsos)]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] ·
[[Registros base e índice]] · [[Modos de direccionamiento]] · [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] ·
[[TP15 Arquitectura de Von Neumann (IAS)]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
