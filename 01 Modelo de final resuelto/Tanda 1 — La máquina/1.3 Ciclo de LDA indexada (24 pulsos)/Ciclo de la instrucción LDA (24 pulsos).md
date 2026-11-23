---
unidad: 4
tipo: concepto
examen: secundario
prioridad: maxima
---
# Ciclo de la instrucción LDA (16 o 24 pulsos, según la máquina)

> [!abstract] En una frase
> La `LDA` **carga el acumulador con lo que hay en memoria**. En la **BLUE base** (instrucción de 1 palabra)
> tarda **2 ciclos de máquina = 16 pulsos**. En la **BLUE indexada** (instrucción de 2 palabras) tarda
> **3 ciclos de máquina = 24 pulsos**, porque hay un ciclo extra para traer el campo de dirección y calcular
> la dirección efectiva. **La pregunta del final ("los 24 pulsos") es la de la BLUE indexada.**

> [!warning] Leé esto antes que nada
> Si en algún resumen ves una cuenta de "8 de búsqueda + 16 de ejecución, a 2 pulsos por microoperación",
> **no es la cuenta de la cátedra**. El apunte de Foster (el que usa la materia) cuenta **ciclos de máquina de
> 8 pulsos**: 2 ciclos para la LDA de la BLUE base y 3 para la indexada. En el oral usá **siempre** la cuenta
> por ciclos de máquina, que es la que está en la tabla de abajo. La versión completa y dibujada está en
> [[Ciclo de LDA indexada (los 24 pulsos)]].

## Las dos cuentas, lado a lado
| | **BLUE base** | **BLUE indexada** |
|---|---|---|
| Formato de la instrucción | 16 bits = **1 palabra** | 32 bits = **2 palabras** |
| Ciclos de máquina | 2 | **3** |
| Pulsos | **16** | **24** |
| Por qué | búsqueda + ejecución | búsqueda + traer el campo de dirección y sumar el índice + ir al operando |

## BLUE base: 16 pulsos (2 ciclos)
**Ciclo 1 — búsqueda** (igual para todas las instrucciones): CP1 `PC→MAR` y orden de lectura · CP2 `+1→Y` ·
CP3 espera · CP4 `SUMA→PC` · CP5 strobe MBR · CP6 `MBR→IR` · CP7 — · CP8 `E→STATE`.

**Ciclo 2 — ejecución de LDA**: CP1 `IR→MAR` y orden de lectura · CP2-CP3 espera · CP4 strobe MBR ·
**CP5 `MBR→A`** (el dato entra al acumulador) · CP6-CP7 — · CP8 `F→STATE`.

## BLUE indexada: 24 pulsos (3 ciclos)
| Ciclo | Pulsos | Qué pasa |
|---|---|---|
| 1 · Búsqueda | 1–8 | se trae la **primera palabra** (opcode + modificador) y el PC apunta a la segunda |
| 2 · Ejecución 1 | 9–16 | se trae la **segunda palabra** (campo de dirección) y se calcula `EA = W + X` con el **sumador de direcciones** (X = 0, RIF o RID según el modificador) |
| 3 · Ejecución 2 | 17–24 | se direcciona `EA`, se lee y **CP22: `MBR→A`**; CP24: `F→STATE` |

![Los 24 pulsos de la LDA indexada](../../../assets/lda24_pulsos.svg)

## Los cuatro modos de LDA
| Instrucción | Modo | EA | Ciclos | Pulsos |
|---|---|---|---|---|
| `LDA 0, X` | directo | `X` | 3 | 24 |
| `LDA 1, X` | indirecto | `M[X]` | 4 | 32 |
| `LDA 2, X` | indexado RIF | `X + RIF` | 3 | 24 |
| `LDA 3, X` | indexado RID | `X + RID` | 3 | 24 |

## Cómo responderlo en el final
1. Aclarar **de qué máquina** hablás (BLUE base = 16; indexada = 24) — la pregunta es la indexada.
2. Decir la regla: **1 ciclo de máquina = 8 pulsos**; la LDA indexada usa **3**.
3. Dibujar la barra de 24 pulsos en tres bloques y marcar los cuatro pulsos clave (CP1, CP6, CP13-CP14, CP22).
4. Cerrar con el contraste: directo 24 · indexado 24 · **indirecto 32**.

## Errores típicos
- Mezclar las dos cuentas (decir 24 en la BLUE base o 16 en la indexada).
- Contar 24 pulsos pero **2 ciclos** de máquina.
- Olvidar el segundo incremento del PC (ciclo 2, CP4).

## Relacionado
[[Ciclo de LDA indexada (los 24 pulsos)]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] ·
[[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Registros base e índice]]
