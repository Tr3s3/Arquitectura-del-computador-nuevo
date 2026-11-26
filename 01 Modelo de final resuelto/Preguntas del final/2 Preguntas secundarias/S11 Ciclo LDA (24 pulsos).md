---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S11 · Ciclo LDA (24 pulsos)

> [!question] Pregunta
> Describa el ciclo de la instrucción LDA. ¿Por qué cuesta 24 pulsos? Dibuje la secuencia.

## 1. Teoría previa

**LDA (Load Accumulator).** Carga en el AC el contenido de una dirección de memoria.

**Por qué 24 pulsos (aclaración importante).** Hay dos máquinas:
- En la **BLUE base**, LDA ocupa **2 ciclos** = 16 pulsos (búsqueda + ejecución).
- En la **BLUE indexada**, el formato del LDA ocupa **dos palabras** (opcode 5 + dirección 16 + modificador). Por eso aparece un **tercer ciclo** de ocho pulsos que lee la segunda palabra y calcula la dirección. Total: **3 ciclos = 24 pulsos** en el modo directo.

Las notas de estudio a veces dicen "LDA = 24 pulsos (8 + 16)" sin aclarar la máquina. En el final, aclaralo.

**Microoperaciones de la ejecución.** `IR → MAR`, `lectura`, `MBR → AC`, `flags`, `STATE → F`.

## 2. Contexto

El LDA es la instrucción **más preguntada** del ciclo de ejecución. Es el ejemplo perfecto para explicar la búsqueda, la ejecución y el cambio de estado (F/E). Por eso el profesor la pide por nombre.

## 3. Gráfico

![[S11-lda-24-pulsos.svg]]

*Lectura:* tres bloques de ocho pulsos: búsqueda, ejecución 1 (segunda palabra y sumador) y ejecución 2 (operando al AC).

## Figuras reales (libros y resumen de cátedra)

![[catedra-said-lda3-ejecucion.png]]

*Pulsos CP1 a CP8 de las dos fases de ejecución de LDA 3, X.* · Resumen de cátedra (Said)

![[libro-quiroga-f7-13.png]]

*Fig. 7.13 — Fase execute LDA.* · Quiroga, *Arquitectura de computadoras*, p. 182

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Ciclo 1: búsqueda (8 pulsos)
| Pulso | Acción |
|---|---|
| CP1 | PC → MAR, PC → Z, lectura |
| CP2 | +1 → Y |
| CP4 | SUMA → PC |
| CP6 | MBR → IR |
| CP8 | E → STATE |

### 4.2 Ciclo 2: ejecución 1 (8 pulsos, en la indexada)
| Pulso | Acción |
|---|---|
| CP1 | PC → MAR, lectura (se lee la segunda palabra) |
| CP4 | PC + 1 |
| CP5 | RID → X (o RIF, o 0 en el modo directo) |
| CP6 | MBR → W (el campo de dirección) |
| CP8 | sigue en E |

### 4.3 Ciclo 3: ejecución 2 (8 pulsos)
| Pulso | Acción |
|---|---|
| CP1 | Σ → MAR, lectura |
| CP6 | MBR → Acc |
| CP8 | F → STATE |

### 4.4 Cómo se cuenta
- **BLUE base:** búsqueda (8) + ejecución (8) = **16**.
- **Indexada directo:** búsqueda (8) + 2 de ejecución (16) = **24**.
- **Indexada indirecto:** un ciclo extra para leer el puntero = **32**.

## 5. Cómo se responde (4 minutos)

1. **Aclarar la máquina:** "En la BLUE indexada, el LDA directo son 3 ciclos de 8 pulsos."
2. **Dibujo:** tres bloques de ocho pulsos con su contenido.
3. **Desarrollo:** los tres ciclos con los pulsos clave.
4. **Cierre:** "El LDA dura lo que tarda acceder a la memoria dos o tres veces."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántos ciclos tiene un LDA directo indexado? | 3, de 8 pulsos cada uno. |
| ¿Qué cambia en el LDA indirecto? | Un ciclo extra: 32 pulsos. |
| ¿En qué pulso entra el dato al AC? | CP6 del último ciclo: MBR → Acc. |
| Error común | Decir "LDA = 24 pulsos" sin aclarar que es la indexada. |

## 7. Relacionado

- [[Ciclo de la instrucción LDA (24 pulsos)]] · [[Ciclo de LDA indexada (los 24 pulsos)]]
- [[P06 Ciclo de ejecución BLUE indexada y sin indexar]] · [[S10 Ciclo de ejecución para todas las operaciones]]
