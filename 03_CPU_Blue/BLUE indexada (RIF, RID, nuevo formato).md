---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# BLUE indexada (RIF, RID, nuevo formato)

> [!abstract] En una frase
> La BLUE indexada es la BLUE con **dos registros índice (RIF y RID)**, un **registro base (RB)**, un
> **sumador de direcciones** y un **campo modificador de 2 bits** en la instrucción. Con eso pasa a tener
> **4 modos de direccionamiento**, 32 instrucciones y 65 536 celdas, y calcula
> **`EA = campo de dirección + RIF/RID`** en el momento del acceso.

> [!note] Esta nota es el mapa; el detalle está en tres notas
> - **Qué cambia y por qué**: [[BLUE vs BLUE indexada — qué cambia y por qué]]
> - **El ciclo de 24 pulsos**: [[Ciclo de LDA indexada (los 24 pulsos)]]
> - **Los registros índice, el base y la reubicación**: [[Registros base e índice]]

## Los registros que se agregan
| Registro | Nombre correcto | Para qué |
|---|---|---|
| **RIF** | Registro Índice **Fuente** | puntero al arreglo de origen |
| **RID** | Registro Índice **Destino** | puntero al arreglo de destino |
| **RB** | Registro **Base** | desplazamiento global del programa (lo maneja el sistema) |
| **W** y **X** | entradas del sumador de direcciones | temporales: el campo de dirección y el índice |

> [!warning] Corrección de nombres
> RIF = índice **Fuente**, RID = índice **Destino** (no "final" ni "de desplazamiento"). En los apuntes
> aparece como "RFI" en un par de tablas por error de tipeo: es el mismo registro.

## El nuevo formato (32 bits = 2 palabras)
```
┌─────────┬────────────┬───────────┬──────────────────────┐
│ Opcode  │ Modificador│  sin uso  │  Campo de dirección  │
│ 5 bits  │  2 bits    │  9 bits   │       16 bits        │
└─────────┴────────────┴───────────┴──────────────────────┘
```
- **5 bits de opcode** ⇒ hasta 32 instrucciones (la cátedra usa 00…37 octal).
- **2 bits de modificador** ⇒ 4 modos.
- **16 bits de dirección** ⇒ 65 536 posiciones.
- **No hay formato fijo**: hay instrucciones de 1 palabra (sin campo de dirección útil) y de 2 palabras.

## Los 4 modos del campo modificador
| Modificador | Modo | Dirección efectiva | Ejemplo |
|---|---|---|---|
| `0` | **directo** | `EA = campo` | `LDA 0, 1000` ⇒ `M[1000]` |
| `1` | **indirecto** | `EA = M[campo]` | `LDA 1, 1000` ⇒ `M[M[1000]]` |
| `2` | **indexado por RIF** | `EA = campo + RIF` | `LDA 2, 1000` ⇒ `M[1000 + RIF]` |
| `3` | **indexado por RID** | `EA = campo + RID` | `LDA 3, 1000` ⇒ `M[1000 + RID]` |

Y en **toda** referencia a memoria se suma además el **registro base**. Teoría general:
[[Modos de direccionamiento]].

## Las instrucciones nuevas
| Instrucción | Qué hace |
|---|---|
| `ENI Reg, valor` | carga un valor en un registro (`ENI RID, 1000`) |
| `INI Reg, valor` | incrementa el registro (`INI RIF, 1`) |
| `LIX Reg, dir` / `SIX Reg, dir` | carga / guarda el registro desde/hacia memoria |
| `RXT Reg, Reg` | copia entre AC, RIF y RID |
| `IJP Reg, dir` | salta si el registro no es cero (lazos) |
| `ENI RB, valor` | carga el registro base (instrucción **privada**) |
| `ION` / `IOF` / `SKF` / `EMR` / `RTI` | sistema de interrupciones ([[Interrupciones y entrada-salida]]) |

## Cuántos pulsos cuesta (resumen)
| Instrucción | Ciclos de máquina | Pulsos |
|---|---|---|
| sin referencia a memoria (HLT, NOP, NOT, RAL, CSA, JMP, JMA, SRJ) | 1 | 8 |
| con referencia a memoria, modo directo o indexado (LDA, STA, ADD, …) | 3 | **24** |
| con referencia a memoria, modo **indirecto** | 4 | **32** |
| INP / OUT | 2 + espera | 16+ |

Desarrollo pulso por pulso: [[Ciclo de LDA indexada (los 24 pulsos)]].

## Ventajas (y costos) de la BLUE indexada — la pregunta "¿ventajas?"

> [!important] La respuesta en una línea
> La indexada **no hace más rápida una instrucción**: la hace **más lenta** (24 pulsos contra 16). Lo que gana
> es **capacidad de expresar programas**: con un registro índice, **un lazo recorre un arreglo entero** sin
> reescribir el código. Se cambia **velocidad por potencia de programación**.

**Ventajas:**

| # | Ventaja | Por qué |
|---|---|---|
| 1 | **Recorrer arreglos con un lazo** | `EA = campo + RIF` permite `LDA 2, 100` dentro de un lazo: **una** instrucción para **n** elementos |
| 2 | **Más memoria** | el campo pasa de **12 a 16 bits** ⇒ de 4 096 a **65 536** celdas |
| 3 | **Más instrucciones** | el opcode pasa de **4 a 5 bits** ⇒ de 16 a **32** (aparecen `ENI`, `INI`, `LIX`, `SIX`, `RXT`, `IJP`, y las de interrupciones) |
| 4 | **4 modos de direccionamiento** | el campo **modificador de 2 bits** agrega **indirecto** y **dos indexados** (antes sólo había directo) |
| 5 | **Reubicación del programa** | el **registro base** desplaza todas las referencias ⇒ el mismo programa corre en cualquier zona de memoria |
| 6 | **Copiar bloques (vector a vector)** | con **RIF** (origen) y **RID** (destino) a la vez, un lazo copia elemento a elemento |
| 7 | **Lazos más baratos de codificar** | `IJP Reg, dir` (salta si el registro no es cero) evita tener que comparar contra cero con el AC |
| 8 | **Base para interrupciones** | el hardware nuevo habilita `ION/IOF/SKF/EMR/RTI` y la pila con `SP` |

**Costos (decirlos sube nota):**

| Costo | Detalle |
|---|---|
| **Más pulsos por instrucción** | 24 en vez de 16 (3 ciclos: uno más para leer la 2.ª palabra y calcular la EA); el indirecto, **32** |
| **Instrucción de 2 palabras** | ocupa el doble de memoria y hay que buscar la segunda palabra |
| **Hardware extra** | sumador de direcciones, RIF, RID, RB, W, X y el decodificador del modificador |
| **Programas más difíciles de leer** | hay que administrar los índices (`ENI`, `INI`) a mano |

> [!tip] La frase que cierra la respuesta
> "La BLUE base es un **juguete didáctico**: 16 instrucciones y direccionamiento directo, 8 o 16 pulsos. La
> indexada es **una máquina de verdad**: 32 instrucciones, 64 K, cuatro modos y arreglos con lazos. **Paga** con
> pulsos (24 en lugar de 16) y con hardware; **gana** en programas posibles."

## Cómo responderlo en el final (3–4 minutos)

1. **Definir qué se agregó (30 s).** RIF, RID, RB, sumador de direcciones (Σ), W/X y el **decodificador del
   modificador**. Es la BLUE base + un bloque de cálculo de dirección.
2. **Dibujar el formato (40 s).** 5 + 2 + 9 + 16 = 32 bits (2 palabras) y decir qué gana cada campo:
   **más opcodes**, **más modos**, **más memoria**.
3. **Los 4 modos con su EA (40 s).** directo, indirecto, `+RIF`, `+RID` (y recordar que **siempre** se suma el
   **RB**).
4. **Las ventajas (50 s).** La lista: **lazos sobre arreglos**, 64 K, 32 instrucciones, reubicación con RB,
   copia vector-vector con RIF y RID. Y el **costo**: **24 pulsos** (32 el indirecto) contra 16.
5. **Cierre con un ejemplo (30 s).** `INI RIF, 100` y un lazo con `LDA 2, 0` recorre **todo** el arreglo; el
   mismo código, con otra base, recorre otro. "**Eso es lo que la BLUE base no podía hacer.**"

## Errores típicos
- Decir que la indexada es "más rápida": es **más lenta** por instrucción (24 vs 16); lo que gana es
  **expresividad**.
- Decir que el índice se suma siempre (sólo en modos 2 y 3).
- Confundir **indirecto** (`EA = M[campo]`) con **indexado** (`EA = campo + RIF/RID`).
- Contar 16 pulsos para la LDA indexada (son **24**: la instrucción ocupa 2 palabras).

## Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 5* | *"Nuevo hardware, nuevas instrucciones"*, *"BLUE Indexada"*, *"Registro base"* | el formato 5+2+9+16, los modos y la lista de instrucciones nuevas | **Es la fuente exacta** |
| **`blue.pdf`** (Foster) | las conclusiones del capítulo de la máquina elemental | qué limitaciones tiene la BLUE base (bus único, una dirección) | Para justificar **por qué** se la indexa |
| **[[BLUE vs BLUE indexada — qué cambia y por qué]]** | nota de la bóveda | la tabla "qué cambia" (hardware, formato, modos, pulsos) | La comparación completa |
| **[[Ciclo de LDA indexada (los 24 pulsos)]]** | nota de la bóveda | el ciclo de 24 pulsos de punta a punta | El costo, medido |
| **[[Registros base e índice]]** · **[[Modos de direccionamiento]]** | notas de la bóveda | RIF/RID/RB y los siete modos de la teoría general | El detalle de cada pieza |
| **[[Interrupciones y entrada-salida]]** | nota de la bóveda | `ION/IOF/SKF/EMR/RTI` y la pila con `SP` | La otra ventaja del hardware nuevo |
| **[[TP19 Modos de direccionamiento]]** | el TP | el ejercicio del arreglo con índice | Lo que se entrega |
| **Stallings, *Organización y arquitectura de computadores*** | capítulo de **modos de direccionamiento** | indexado y base + desplazamiento | Contexto teórico |

## Relacionado
[[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Ciclo de LDA indexada (los 24 pulsos)]] ·
[[Registros base e índice]] · [[Modos de direccionamiento]] ·
[[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · [[Interrupciones y entrada-salida]]
