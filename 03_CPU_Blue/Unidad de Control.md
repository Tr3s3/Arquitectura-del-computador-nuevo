---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Unidad de Control (UC)

> [!abstract] En una frase
> La UC es la que **manda**: lee el opcode de la instrucción (**IR**), decide **qué microoperaciones**
> hay que hacer y **en qué orden**, y las ejecuta emitiendo las **señales de control** que abren y cierran
> las compuertas de todos los demás bloques. No procesa datos: **gobierna**.

## Sus cuatro funciones (definición de examen)
1. **Sincronizar**: dar los pulsos de reloj y marcar los tiempos (los pulsos T0, T1, …).
2. **Decodificar**: interpretar el opcode del IR y saber qué instrucción es.
3. **Secuenciar**: determinar la secuencia de microoperaciones (búsqueda → ejecución → próxima).
4. **Generar señales de control**: activar en cada pulso las señales que producen las transferencias.

## Cómo genera las señales
Sus entradas y salidas:
```
 entradas:  opcode (del IR) · flags (Z, C) · reloj · señales externas (INT, READY, RESET)
 salidas:   señales de control → registros, ALU, memoria, buses, E/S
```
La UC es un **circuito secuencial**: sus salidas dependen del estado (en qué pulso y en qué fase está) y de
las entradas (opcode y flags). Internamente hay dos escuelas: **cableada** y **microprogramada**
(ver [[Unidad de control cableada y microprogramada]]).

## Por qué las señales de control son lo más importante
> [!important] La idea que hay que transmitir
> Todos los bloques del computador son **tontos**: la ALU suma si le dicen que sume; el registro carga si
> su señal `LOAD` está en 1; la memoria lee si `MEMR = 1`; el bus transporta el registro cuya salida de tres
> estados está habilitada. **La inteligencia del computador está en la UC**: el programa no es más que la
> secuencia de señales de control que la UC genera al decodificar cada instrucción.

## Señales de control típicas (con ejemplo de uso)
| Señal | Efecto | Cuándo la activa la UC |
|---|---|---|
| `PCout` | pone el PC en el bus | primer pulso de la búsqueda |
| `MARin` / `MARload` | carga el MAR desde el bus | al inicio de todo acceso a memoria |
| `MEMR` / `READ` | lectura de memoria | búsqueda y LDA/ADD/… |
| `MEMW` / `WRITE` | escritura en memoria | STA |
| `MBRout` / `MBRin` | saca/pone el MBR del bus | transferencia del dato leído |
| `IRin` | carga el IR | fin de la búsqueda |
| `PCin` | carga el PC desde el bus | saltos (JMP/JZ/JC) |
| `PCinc` | incrementa el PC | búsqueda |
| `ACout` / `ACin` | saca/pone el AC en el bus | operaciones y STA |
| `ALUop` (2–4 bits) | selecciona la operación | ADD, SUB, AND, … |
| `load flags` | guarda Z, C del resultado | fin de una operación aritmética |
| `STATE` = F/E | fase del ciclo | inicio y fin de la ejecución |
| `INTack`, `INTA` | reconoce una interrupción | ciclo de interrupción |

> [!example] Ejemplo concreto: `LDA` (cargar el AC)
> La UC, en el ciclo de ejecución, activa en orden: `IRout(dir)` → `MARin` → `MEMR` → `MBRout` → `ACin`
> (+ `load flags`). Ninguna de esas transferencias ocurre "sola": cada una es una señal que la UC enciende
> durante un pulso. Ver [[Ciclo de la instrucción LDA (24 pulsos)]].

## Sincronía en BLUE: los tres flip-flops
| Flip-flop | Función |
|---|---|
| **RUN** | 1 = máquina en marcha; 0 = detenida (HLT lo pone en 0) |
| **STATE** | **F** = ciclo de búsqueda (fetch), **E** = ciclo de ejecución (execute) |
| **CLOCK** | genera el tren de pulsos; cada pulso habilita **una** microoperación |

Con esos tres, la UC sabe "en qué está": si STATE = F hace la secuencia de búsqueda; si STATE = E, la
secuencia de la instrucción que indica el opcode. Eso es todo el control de BLUE.

## Cómo responderlo en el final (pregunta principal #7)
1. Definir la UC y sus **cuatro funciones** (sincronizar, decodificar, secuenciar, generar señales).
2. Explicar entradas/salidas: opcode, flags, reloj, interrupciones → señales de control.
3. Dar la **tabla de señales** con dos o tres ejemplos concretos (MEMR, MARin, PCinc, ALUop).
4. Mostrar el ejemplo de `LDA` señal por señal.
5. Cerrar con los FF RUN/STATE/CLOCK y la distinción cableada vs microprogramada.

## Errores típicos
- Decir que la UC ejecuta las operaciones (las ejecuta la ALU; la UC las ordena).
- Olvidar que la UC usa los **flags** (por eso un salto condicional depende de Z o C).
- Confundir el reloj (pulsos) con el estado (F/E): uno marca el tiempo, el otro la fase.
- No mencionar el IR: sin el opcode del IR la UC no tiene qué decodificar.

## Relacionado
[[Ciclo de máquina]] · [[Unidad de control cableada y microprogramada]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Interrupciones y entrada-salida]]
