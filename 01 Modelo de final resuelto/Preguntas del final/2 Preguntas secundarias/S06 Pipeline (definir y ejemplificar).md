---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S06 · Pipeline: definir y ejemplificar

> [!question] Pregunta
> Defina y ejemplifique el proceso de pipeline. ¿Qué conflictos aparecen y cómo se resuelven?

## 1. Teoría previa

**Pipeline (cauce de instrucciones).** Es una técnica de **paralelismo temporal**: la ejecución de una instrucción se divide en **etapas**, y cada etapa trabaja sobre una instrucción distinta al mismo tiempo.

**Etapas de la cátedra (cinco):**

| Etapa | Qué hace | Equivalente en BLUE |
|---|---|---|
| 1. Búsqueda (IF) | trae la instrucción | CP1–CP6 de la búsqueda |
| 2. Decodificación (ID) | identifica la instrucción y los operandos | CP6–CP7 |
| 3. Cálculo de dirección (EX/AGU) | calcula la EA | el sumador de la BLUE indexada |
| 4. Búsqueda de operandos (MEM) | lee la memoria o los registros | MBR → Y / Z → AC |
| 5. Ejecución y escritura (WB) | hace la operación y escribe | CP8 |

**Fórmula clave.** Con `k` etapas y `n` instrucciones:
- Sin pipeline: `k × n` ciclos.
- Con pipeline: `k + (n − 1)` ciclos.

## 2. Contexto

El pipeline es la idea que convierte una CPU de "una instrucción a la vez" en una que procesa varias a la vez. Es el puente entre la arquitectura clásica y la moderna. Se pregunta junto con RISC: el pipeline **pide** RISC.

## 3. Gráfico

![[S06-pipeline.svg]]

*Lectura:* cada fila es una instrucción; cada columna es un instante de tiempo. Las instrucciones se "escalonan": cuando la I1 pasa a ID, la I2 entra a IF.

## Figuras reales (libros y resumen de cátedra)

![[catedra-said-etapas-pipeline.png]]

*Las cinco etapas IF, ID, EX, MEM y WB con su función.* · Resumen de cátedra (Said)

![[libro-stallings-f12-10.png]]

*Fig. 12.10 — Diagrama de tiempos de un cauce de instrucciones.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 474

![[libro-stallings-f12-11.png]]

*Fig. 12.11 — Efecto de un salto condicional en un cauce.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 474

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Ejemplo numérico
4 instrucciones, 5 etapas:
- **Sin pipeline:** 4 × 5 = **20 ciclos**.
- **Con pipeline:** 5 + (4 − 1) = **8 ciclos**.
- Speedup ideal: 20 / 8 = 2,5. Con más instrucciones, el speedup se acerca a 5.

### 4.2 Los tres conflictos (hazards)

| Conflicto | Cuándo | Ejemplo | Solución |
|---|---|---|---|
| **Estructural** | dos etapas usan el mismo recurso | búsqueda de instrucción y acceso a datos a la misma memoria | cachés separadas (I y D) |
| **De datos (RAW)** | una instrucción necesita el resultado de otra que aún no terminó | `ADD R1,R2,R3` y luego `SUB R4,R1,R5` | forwarding (bypass) o burbuja |
| **De control** | no se sabe cuál es la próxima instrucción hasta resolver un salto | un `JMP` o un `JZ` | predicción de saltos, retardo del salto |

### 4.3 Por qué el pipeline pide RISC

| Requisito | Cómo lo cumple RISC | Problema en CISC |
|---|---|---|
| Instrucciones de longitud fija | todas de 4 bytes | no se sabe dónde empieza la siguiente |
| Etapas parejas | cada instrucción hace lo mismo | una instrucción puede tardar mucho más que otra |
| Pocos modos | registro + desplazamiento | cálculo de dirección impredecible |
| Acceso a memoria sólo load/store | etapa de memoria simple | operar sobre memoria alarga la etapa |

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Dividir la ejecución en etapas que trabajan en paralelo sobre instrucciones distintas."
2. **Dibujo:** la escalera de instrucciones solapadas.
3. **Ejemplo:** 4 instrucciones, 5 etapas, 8 ciclos contra 20.
4. **Conflictos:** estructural, de datos y de control, con su solución.
5. **Cierre:** "El pipeline da throughput, no reduce el tiempo de una instrucción sola."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿El pipeline reduce el tiempo de una instrucción? | No. Aumenta la cantidad de instrucciones terminadas por unidad de tiempo. |
| ¿Qué es el forwarding? | Pasar el resultado directo de una etapa a otra sin esperar la escritura. |
| ¿Por qué el salto es un problema? | Porque las instrucciones siguientes ya entraron al pipeline antes de saber a dónde ir. |
| Error común | Decir que el pipeline acelera cada instrucción. Acelera el conjunto. |

## 7. Relacionado

- [[Pipeline]] · [[7.1.1 Etapas y diagrama en escalera]] · [[Técnicas para aumentar la velocidad]]
- [[S07 Arquitectura CISC y RISC]]
