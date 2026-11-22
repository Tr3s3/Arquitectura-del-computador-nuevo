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

## Cómo responderlo en el final
1. Definir qué se agregó (RIF, RID, RB, Σ, W/X, decodificador del modificador).
2. Dibujar el formato nuevo y la máquina con el sumador de direcciones.
3. Los 4 modos con su EA.
4. Un ejemplo que cierre: `LDA 3, 1000` con RID = 5000 ⇒ `M[6000]`, y el mismo código recorre todo el arreglo.

## Errores típicos
- Decir que el índice se suma siempre (sólo en modos 2 y 3).
- Confundir **indirecto** (`EA = M[campo]`) con **indexado** (`EA = campo + RIF/RID`).
- Contar 16 pulsos para la LDA indexada (son **24**: la instrucción ocupa 2 palabras).

## Relacionado
[[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Ciclo de LDA indexada (los 24 pulsos)]] ·
[[Registros base e índice]] · [[Modos de direccionamiento]] ·
[[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · [[Interrupciones y entrada-salida]]
