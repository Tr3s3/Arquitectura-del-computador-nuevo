---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P01 · Flujo de información (datos y direcciones)

> [!question] Pregunta
> ¿Cómo circula la información (datos y direcciones) entre los registros, la memoria y la ALU en la máquina BLUE?

## 1. Teoría previa: qué tenés que saber antes

**Registro.** Es un conjunto de biestables que guarda una palabra. En BLUE, cada registro tiene dos señales de control:
- **LOAD** (carga): cuando vale 1, el registro toma el dato que hay en el bus en el próximo flanco de reloj.
- **OUT** (salida habilitada): cuando vale 1, el registro pone su contenido en el bus.

**Bus.** Es un conjunto de líneas compartidas. Si dos fuentes escriben a la vez, las señales se mezclan y el resultado es basura. Por eso se usan **buffers de tres estados**: cuando el dispositivo no habla, su salida queda desconectada (alta impedancia).

**Regla de oro del bus único.** En cada pulso de reloj:
- **una sola** fuente habilita su salida (OUT = 1);
- **uno o más** destinos cargan (LOAD = 1), y siempre leen lo que está en el bus.

**Registros de BLUE y su ancho.**

| Registro | Bits | Para qué |
|---|---|---|
| PC (contador de programa) | 12 | dirección de la próxima instrucción |
| MAR (registro de dirección de memoria) | 12 | dirección que va a la memoria |
| MBR (registro de intercambio con memoria) | 16 | dato que entra o sale de la memoria |
| IR (registro de instrucción) | 16 | instrucción en ejecución |
| AC (acumulador) | 16 | operando y resultado de la ALU |

**Dos tipos de información.** Direcciones (12 bits, de la CPU a la memoria) y datos (16 bits, en los dos sentidos). El mismo bus físico transporta ambos; lo que cambia es **qué significan** esos bits.

## 2. Contexto: por qué te preguntan esto

Esta pregunta es la base de todo lo que sigue: el ciclo de búsqueda, el LDA, la UC y las interrupciones son **secuencias de transferencias por el bus**. Si entendés el flujo, entendés cualquier ciclo. Además, el profesor usa la respuesta para ver si sabés que **un solo bus obliga a secuenciar** (una transferencia por pulso).

## 3. Gráfico

![[P01-flujo-de-informacion.svg]]

*Lectura del gráfico:* arriba está la memoria; en el medio, el bus único; abajo, los cinco registros, cada uno conectado al bus con una flecha. La UC (que manda) y la ALU (que calcula) están abajo.

## 4. Desarrollo detallado

### 4.1 Flujo de direcciones (12 bits, unidireccional)

**Búsqueda de la instrucción:**
1. `PC → MAR`: el PC pone su valor en el bus y el MAR lo carga.
2. `MAR → bus de direcciones → memoria`: la memoria recibe la dirección.
3. La memoria devuelve la instrucción por el bus de datos hacia el MBR.

**Ejecución de un LDA directo:**
1. `IR(campo dirección) → MAR`: los 12 bits de la dirección salen del IR y van al MAR.
2. La memoria devuelve el dato.

En BLUE indexada se agrega el **sumador de direcciones**: `EA = D + RIF/RID`. La dirección efectiva sale del sumador y se carga en el MAR.

### 4.2 Flujo de datos (16 bits, bidireccional)

- **Lectura de instrucción:** `memoria → MBR → IR`.
- **Lectura de operando:** `memoria → MBR → AC`.
- **Escritura (STA):** `AC → MBR → memoria`.
- **Operación aritmética:** `AC → ALU → AC`. La ALU no tiene salida directa a memoria.

### 4.3 Ejemplo completo: `LDA 500` leído en el bus

Supongamos que el PC vale 100 y en la dirección 500 hay el dato 7.

| Paso | Origen → destino | Qué viaja | Tipo |
|---|---|---|---|
| a | PC → MAR | 100 | dirección |
| b | memoria → MBR → IR | `LDA 500` | dato (instrucción) |
| c | IR(dir) → MAR | 500 | dirección |
| d | memoria → MBR → AC | 7 | dato |

El paso a y el c usan el mismo bus, pero en pulsos distintos.

### 4.4 Un caso que confunde: JMP

En `JMP 500`, la dirección 500 que viene en la instrucción **no** va al MAR. Va al **PC**, porque en un salto esa dirección es el dato que se carga en el contador. Esto muestra que lo que define el uso no es el bus, sino **el registro destino**.

## 5. Cómo se responde en el final (2–3 minutos)

1. **Definición en una frase:** "En BLUE todo pasa por un bus único; en cada pulso una fuente habilita su salida y un destino carga."
2. **Dibujo:** registros colgando del bus, memoria arriba, UC y ALU abajo; dos flechas separadas para direcciones (12) y datos (16).
3. **Desarrollo:** recorrer el LDA: PC→MAR, memoria→MBR→IR, IR(dir)→MAR, memoria→MBR→AC.
4. **Cierre:** "El bus transporta direcciones o datos; lo que lo define es el uso. Por eso el JMP carga el PC."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Por qué no pueden salir dos datos a la vez? | Se cortocircuitan las salidas. Por eso hay buffers de tres estados y una sola fuente por pulso. |
| ¿Cuántos bits tiene el bus de direcciones? | 12, porque 2¹² = 4096 celdas. |
| ¿Por qué el MBR está entre la memoria y los registros? | Es el registro de intercambio con la memoria. El MAR hace lo mismo con las direcciones. |
| ¿Cuál es el error más común? | Dibujar flechas directas de memoria a AC. Siempre pasa por el MBR. |

## 7. Relacionado

- Notas de estudio: [[Flujo de información en BLUE (datos y direcciones)]]
- Pregunta conexa: [[P03 Ciclo de máquina]] · [[P06 Ciclo de ejecución BLUE indexada y sin indexar]]
- Gráfico de la BLUE: [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
