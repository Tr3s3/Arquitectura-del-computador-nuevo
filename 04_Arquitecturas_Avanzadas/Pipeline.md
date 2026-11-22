---
unidad: 7
tipo: concepto
examen: secundario
prioridad: alta
---
# Pipeline (tubería / segmentación)

> [!abstract] En una frase
> El pipeline es una técnica de **paralelismo temporal**: se divide la ejecución de una instrucción en
> **etapas** que se hacen en hardware separado y se solapan, de modo que mientras una instrucción se está
> ejecutando, la siguiente se está decodificando y la anterior se está terminando. **No acelera una
> instrucción: aumenta la cantidad de instrucciones por unidad de tiempo.**

## La idea, con la analogía de la lavandería
Lavar, secar y planchar sin pipeline: una carga por vez, 3 horas por carga.
Con pipeline (tres máquinas y tres personas): mientras se seca una carga se lava la siguiente.
La primera carga sigue tardando 3 horas, pero después **sale una carga por hora**.
Eso es exactamente lo que hace la CPU.

![[pipeline.svg]]

## Ejemplo numérico (el que se pide "definir y ejemplificar")
4 etapas: **BI** (búsqueda) → **DE** (decodificación) → **OP** (lectura de operandos) → **EJ** (ejecución).
Supongamos 1 ciclo de reloj por etapa.

| | Sin pipeline | Con pipeline |
|---|---|---|
| Instrucciones | n | n |
| Ciclos por instrucción | 4 | 4 para la primera, después **1** |
| Ciclos totales para n = 5 | 20 | 4 + (5 − 1) = **8** |
| Ciclos totales para n grande | 4n | ≈ n + 3 |

**Speedup** = `n·k / (k + n − 1)` → tiende a **k** (el número de etapas) cuando n es grande.
Con 4 etapas, el límite teórico es **4×**; en la práctica se llega a 2–3× por los conflictos.

## Los tres tipos de conflicto (hazards)
| Conflicto | Qué pasa | Solución |
|---|---|---|
| **Estructurales (de recurso)** | dos etapas quieren el mismo hardware (una sola memoria) | memorias separadas, caché Harvard, más puertos |
| **De datos** | una instrucción necesita un resultado que la anterior todavía no escribió | **adelantamiento** (*forwarding*), **burbujas** (*stall*), o **carga retardada** |
| **De control** | un salto condicional: no se sabe qué instrucción sigue | **predicción de saltos**, retardo de salto (**transferencia retardada**), o *flush* del pipeline |

> [!example] Conflicto de datos clásico
> ```
> I1: ADD  R1, R2, R3     ; R1 ← R2 + R3
> I2: SUB  R4, R1, R5     ; necesita R1  ← ¡todavía no está!
> ```
> Soluciones: **(1)** *stall*: I2 espera un ciclo (burbuja); **(2)** *forwarding*: el resultado de la ALU se
> reenvía a la entrada de la ALU sin esperar a que se escriba el registro; **(3)** el compilador reordena e
> inserta una instrucción independiente en el hueco (**carga retardada**).

## Pipeline en las arquitecturas RISC
- **3 segmentos** (búsqueda, decodificación/operandos, ejecución) es el mínimo típico.
- **Carga retardada (delayed load):** el dato que se carga desde memoria **no está disponible** en la
  instrucción siguiente; la arquitectura obliga a que la instrucción que sigue sea independiente (el
  compilador rellena el hueco).
- **Transferencia retardada (delayed branch):** la instrucción siguiente al salto **siempre se ejecuta**
  (está en el "delay slot") mientras se resuelve el salto. Así el pipeline no se detiene.

## Pipeline aritmético (distinto del de instrucciones)
Dentro de la ALU también se puede segmentar una operación larga (por ejemplo una multiplicación o una suma
en punto flotante) en etapas: **pipeline aritmético**. Permite comenzar una operación nueva en cada ciclo
aunque cada una tarde varios ciclos. Es la base del **procesamiento vectorial**
(ver [[Paralelismo y procesamiento vectorial]]).

## Ventajas y límites
**Ventajas:** más rendimiento con el **mismo reloj** (no hay que subir la frecuencia); mejor uso del
hardware; es "gratis" desde el punto de vista del programa (transparente).
**Límites:** el rendimiento máximo es k×; los conflictos lo bajan; hay **latencia** adicional por los
registros de segmento; el **costo fijo** de llenado (k ciclos) hace que no convenga para programas muy
cortos; y si las etapas no están balanceadas, manda la más lenta.

## Cómo responderlo en el final
1. Definir: paralelismo temporal por etapas solapadas.
2. Dar el ejemplo de las 4 etapas con la tabla de ciclos y el cálculo de speedup (n·k / (k+n−1)).
3. Nombrar los tres conflictos con su solución (datos → forwarding/stall; control → predicción/retardo).
4. Mencionar carga retardada y transferencia retardada (RISC).
5. Cerrar con la distinción pipeline de instrucciones vs pipeline aritmético.

## Errores típicos
- Decir que el pipeline **reduce el tiempo de una instrucción** (reduce el tiempo *promedio por
  instrucción*, no la latencia individual).
- Olvidar los conflictos y decir que el speedup es exactamente k.
- Confundir pipeline (etapas de una instrucción) con **multiprocesamiento** (varias instrucciones en
  paralelo real, varios núcleos).
- Confundir *stall* con *flush* (uno espera, el otro descarta lo que estaba en el cauce).

## Relacionado
[[CISC y RISC]] · [[Paralelismo y procesamiento vectorial]] · [[Técnicas para aumentar la velocidad]] · [[Ciclo de máquina]]
