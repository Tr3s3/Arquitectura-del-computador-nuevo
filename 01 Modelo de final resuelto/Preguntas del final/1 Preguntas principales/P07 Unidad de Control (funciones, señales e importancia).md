---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P07 · Unidad de Control: funciones, señales de control e importancia

> [!question] Pregunta
> ¿Qué es la unidad de control (UC)? Explique sus funciones, las señales de control y por qué es importante, con ejemplos.

## 1. Teoría previa

**La UC.** Es el bloque de la CPU que **dirige** la operación: decodifica la instrucción y genera, en el momento justo, las señales que producen las transferencias y las operaciones. **No procesa datos**: no suma ni guarda resultados.

**Señal de control.** Es un bit (0 o 1) que habilita o deshabilita algo:
- habilitar la salida de un registro al bus (OUT);
- cargar un registro (LOAD);
- elegir una operación de la ALU;
- activar la lectura o escritura de la memoria (MEMR, MEMW).

**Entradas de la UC en BLUE:**

| Entrada | De dónde viene | Para qué |
|---|---|---|
| Opcode (IR15…IR12) | registro IR | saber qué instrucción es |
| Estado (RUN, STATE F/E, TRA) | biestables internos | saber si está corriendo, buscando o ejecutando |
| Tiempo (CP1…CP8) | reloj maestro | saber en qué pulso está |
| Flags (Z, signo, overflow) | ALU | decidir saltos condicionales |

**Dos formas de implementarla.**
- **Cableada:** la secuencia está en compuertas fijas. Rápida, pero no se puede cambiar. Típica de RISC y de BLUE.
- **Microprogramada:** la secuencia está en una memoria de control (ROM). Más lenta, pero flexible. Típica de CISC (x86).

## 2. Contexto

La UC es **el cerebro de la CPU** en el sentido de que decide. El profesor pregunta por ella porque conecta todo lo anterior: el flujo del bus (P01), el ciclo (P03), el LDA (P06). Si explicás la UC, explicás por qué cada registro carga en su pulso.

## 3. Gráfico

![[P07-unidad-control.svg]]

*Lectura:* a la izquierda, las cuatro entradas (opcode, estado, reloj, flags). En el centro, la UC. A la derecha, las salidas: control de registros (LOAD/OUT), operación de la ALU, memoria (MEMR/MEMW) y habilitación del bus.

## 4. Desarrollo detallado

### 4.1 Las cuatro funciones

1. **Sincronizar**: marca el ritmo con el reloj y los pulsos CP1…CP8.
2. **Decodificar**: identifica el opcode del IR y la familia de la instrucción.
3. **Secuenciar**: decide el orden de las microoperaciones dentro del ciclo.
4. **Generar las señales de control**: enciende las señales en cada pulso.

### 4.2 Ejemplos de señales

| Señal | Efecto | Cuándo |
|---|---|---|
| `PCout`, `MARin` | PC → MAR | CP1 de la búsqueda |
| `MEMR` / `MEMW` | lectura / escritura de memoria | cuando el MAR tiene la dirección |
| `MBRload` / `MBRout` | MBR toma / entrega el dato | CP5–CP6 |
| `IRin` | carga la instrucción | CP6 de la búsqueda |
| `PCinc` / `PCin` | incremento normal / carga de salto | CP4 / CP8 de JMP |
| `ALUop`, `load flags` | elige la operación y guarda Z y C | en la ejecución |

### 4.3 Ecuaciones conceptuales (cableada)

Por ejemplo, la señal que carga el MAR en la búsqueda:
- `Send PC, Load MAR` = `F · CP1` (estado F y pulso 1).

La que carga el IR:
- `Send MBR, Load IR` = `F · CP6`.

La que termina de ejecutar HLT:
- `Reset RUN` = `CP7 · HLT`.

Son funciones de **estado · pulso · instrucción**: una compuerta AND por cada condición, y una OR para juntar las que producen la misma señal.

### 4.4 Por qué es importante

Todos los bloques de la CPU son "tontos": la ALU suma si le dicen que sume; el registro carga si LOAD = 1; la memoria lee si MEMR = 1. **La inteligencia está en la UC**: el programa se convierte en una secuencia de señales que la UC enciende pulso a pulso.

### 4.5 Cableada vs microprogramada

| | Cableada | Microprogramada |
|---|---|---|
| Dónde está la secuencia | compuertas | ROM de control |
| Velocidad | más rápida | más lenta |
| Flexibilidad | nula | alta (se cambia la ROM) |
| Usada en | RISC, BLUE | CISC (x86) |

## 5. Cómo se responde (3 minutos)

1. **Definición:** "La UC gobierna: decodifica el opcode y genera las señales de control. No procesa datos."
2. **Dibujo:** UC al centro, entradas a la izquierda, salidas a la derecha.
3. **Funciones:** sincronizar, decodificar, secuenciar, generar.
4. **Ejemplos:** dos o tres señales con su efecto.
5. **Cierre:** "La inteligencia del computador está en la UC; cableada si es rápida, microprogramada si es flexible."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué es una señal de control? | Un bit que habilita una transferencia o una operación. |
| ¿Cableada o microprogramada? | Cableada: compuertas fijas. Microprogramada: memoria de control. |
| ¿Qué tres biestables sincronizan BLUE? | RUN, STATE y CLOCK. |
| Error común | Decir que la UC suma. La ALU suma; la UC sólo ordena. |

## 7. Relacionado

- [[Unidad de Control]] · [[Cómo se implementa la Unidad de Control]] · [[Unidad de control cableada y microprogramada]]
- [[P03 Ciclo de máquina]] · [[P06 Ciclo de ejecución BLUE indexada y sin indexar]]
