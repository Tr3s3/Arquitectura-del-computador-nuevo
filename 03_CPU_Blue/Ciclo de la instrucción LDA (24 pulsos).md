---
unidad: 4
tipo: concepto
examen: secundario
prioridad: maxima
---
# Ciclo de la instrucción LDA (24 pulsos)

> [!abstract] En una frase
> La instrucción completa `LDA D` (`AC ← M[D]`) insume **24 pulsos**: **8 de búsqueda** (traer la
> instrucción) + **16 de ejecución** (traer el operando y cargarlo en el AC), contando **2 pulsos por
> microoperación** (fase 1: la fuente pone el dato en el bus; fase 2: el destino lo carga).

## La cuenta primero (para el pizarrón)
```
   búsqueda ..........  8 pulsos   (traer la instrucción al IR)
 + ejecución ......... 16 pulsos   (8 microoperaciones × 2 pulsos)
 ────────────────────────────────
   total LDA ......... 24 pulsos
```

## Búsqueda (T0 – T7) — igual para todas las instrucciones
| Pulso | Microoperación | Señales |
|---|---|---|
| T0 | `MAR ← PC` | `PCout`, `MARin` |
| T1 | `MEMR = 1` | `MEMR` |
| T2 | espera de memoria | — |
| T3 | `MBR ← M[MAR]` | `MBRload` |
| T4 | `PC ← PC + 1` | `PCinc` |
| T5 | `IR ← MBR` | `MBRout`, `IRin` |
| T6 | decodificar el opcode (`LDA`) | UC |
| T7 | `STATE ← E` | `STATE` |

## Ejecución (T8 – T23) — 8 microoperaciones × 2 pulsos
| Microoperación | Pulsos | Fase 1 (fuente → bus) | Fase 2 (bus → destino) |
|---|---|---|---|
| E1 · `MAR ← IR(dir)` | T8–T9 | `IRout` | `MARin` |
| E2 · activar lectura | T10–T11 | `MEMR = 1` | (espera) |
| E3 · `MBR ← M[MAR]` | T12–T13 | la memoria pone el dato | `MBRload` |
| E4 · `AC ← MBR` | T14–T15 | `MBRout` | `ACin` |
| E5 · desactivar lectura | T16–T17 | `MEMR = 0` | (libera el bus) |
| E6 · actualizar flags | T18–T19 | (la ALU/UC evalúa el AC) | `load flags` (Z, C) |
| E7 · preparar el próximo ciclo | T20–T21 | (el PC ya apunta a la siguiente) | (selección de la fuente de la próxima búsqueda) |
| E8 · `STATE ← F` | T22–T23 | — | `STATE` |

⇒ 8 microoperaciones × 2 pulsos = **16 pulsos** de ejecución ⇒ **8 + 16 = 24**.

## Diagrama de la instrucción completa
```
 T0 ─ T7 : BÚSQUEDA            T8 ─ T23 : EJECUCIÓN de LDA
 ┌─────────────────────┐       ┌───────────────────────────────────┐
 │ PC→MAR  MEMR  MBR    │  IR   │ MAR←IR  MEMR  MBR←M[MAR]  AC←MBR  │
 │ PC+1    IR←MBR  decod│──────→│ flags   STATE←F                   │
 └─────────────────────┘       └───────────────────────────────────┘
```

> [!warning] Sobre el número 24
> El número depende del criterio de conteo del apunte. Las dos formas de contarlo:
> - **2 pulsos por microoperación** (éste): `LDA` = 8 + 16 = **24**.
> - **1 pulso por microoperación** (con registros que se cargan en el mismo pulso en que se habilita el bus):
>   `LDA` ≈ 8 + 8 = **16**.
>
> En el oral, decí el criterio antes que el número: *"cuento dos pulsos por microoperación porque el bus
> único exige primero seleccionar la fuente y después cargar el destino; con ese criterio LDA da 24"*.
> Eso es exactamente lo que se quiere escuchar: **que la cuenta esté justificada**.

## Comparación con otras instrucciones (mismo criterio)
| Instrucción | Búsqueda | Ejecución | Total | Por qué |
|---|---|---|---|---|
| `LDA D` | 8 | 16 | **24** | un acceso a memoria + carga del AC |
| `STA D` | 8 | ~12 | ~20 | un acceso (escritura), menos pasos |
| `ADD D` | 8 | 16 | 24 | igual a LDA + el paso de ALU |
| `NOT` | 8 | 6 | ~14 | no accede a memoria |
| `JMP D` | 8 | 4 | ~12 | `PC ← IR(dir)`, sin memoria |

(En BLUE, si la máquina tiene ciclo fijo, las instrucciones cortas **gastan** los pulsos sobrantes: por eso
`NOP` existe. Si la UC tiene lógica de fin anticipado, terminan antes.)

## Cómo responderlo en el final
1. Enunciar la cuenta: 8 de búsqueda + 16 de ejecución = 24, con el criterio de 2 pulsos por microoperación.
2. Desarrollar la tabla de la búsqueda (T0–T7).
3. Desarrollar la tabla de la ejecución, microoperación por microoperación.
4. Explicar el rol de cada señal (`IRout`, `MARin`, `MEMR`, `MBRout`, `ACin`).
5. Cerrar: la búsqueda es común a todas las instrucciones; lo que cambia es la ejecución, y por eso
   `LDA`, `STA` y `ADD` difieren sólo en la última parte.

## Errores típicos
- Sumar mal: 8 + 16 = 24 √ (no 8 + 8).
- Poner `AC ← MBR` antes de `MBR ← M[MAR]`.
- Olvidar el pulso de `STATE ← F` (sin él la máquina no vuelve a buscar).
- Contar el pulso de espera de memoria dos veces (una en búsqueda y otra en ejecución) sin avisar.

## Relacionado
[[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] · [[Flujo de información en BLUE (datos y direcciones)]] · [[Unidad de Control]]
