---
unidad: 2
tipo: concepto
examen: secundario
---
# Registros

> [!abstract] En una frase
> Un registro es un conjunto de **n flip-flops** que se leen y escriben **como una unidad**: guarda una
> palabra de n bits dentro de la CPU. Según cómo se cargan y se sacan los bits se clasifica en
> **PIPO, SISO, PISO, SIPO** y **bidireccional con carga en paralelo**.

## Por qué existe
Los flip-flops sueltos no sirven: la CPU manipula **palabras** (8, 16, 32 bits). El registro agrupa n
biestables con un **reloj común** y una señal de **habilitación (LOAD)**, de modo que la palabra se
carga y se lee completa en un solo pulso. Son los "bolsillos" internos de la CPU
(ver [[Registros de la CPU]]).

## Registro con carga en paralelo (PIPO: Parallel In – Parallel Out)
n flip-flops D, todos con el **mismo reloj**; cada D recibe un bit de la entrada y cada Q es un bit de
la salida. La señal **LOAD** (habilitación) decide si el registro se actualiza o mantiene su contenido:

```
        D0 ──[FF0]── Q0        LOAD = 1 → en el flanco se cargan los n bits
        D1 ──[FF1]── Q1        LOAD = 0 → el registro mantiene su valor
        ...                    CLK común a todos (sincronismo)
        Dn ──[FFn]── Qn
```
Con un [[Multiplexor]] en la entrada de cada FF se puede elegir entre "cargar dato nuevo" y "mantener"
o "desplazar" — así se arma un registro **versátil** (carga paralela + desplazamiento).

## Registro de desplazamiento (shift register, SISO)
Los flip-flops se conectan **en cadena**: la salida de uno entra al siguiente.
```
  entrada serie → [FF0] → [FF1] → [FF2] → [FF3] → salida serie
                   ↑       ↑       ↑       ↑
                  CLK (común): en cada pulso el dato corre una posición
```
- **SISO** (Serial In – Serial Out): entra y sale bit a bit. Se usa para **retardar** n pulsos y para
  conversión serie.
- **SIPO** (Serial In – Parallel Out): entra serie, se lee todo junto (recepción serie → bus paralelo).
- **PISO** (Parallel In – Serial Out): se carga todo junto y se transmite bit a bit (transmisión
  paralelo → serie, típico en la [[Interrupciones y entrada-salida|E/S serie]]).

## Registro de desplazamiento bidireccional con carga en paralelo
Es el más completo y el que pide el plan: puede **cargar en paralelo**, **desplazar a la izquierda**,
**desplazar a la derecha** y **mantener**. Se implementa con un **MUX de 4 canales** por cada flip-flop:

| Modo (2 bits) | Entrada que llega al FF i |
|---|---|
| Mantener | Qᵢ (retroalimentación) |
| Cargar | Dᵢ (dato paralelo) |
| Desplazar a la izquierda | Qᵢ₊₁ (viene del vecino de la derecha) |
| Desplazar a la derecha | Qᵢ₋₁ (viene del vecino de la izquierda) |

Todos los FF comparten CLK; el modo lo fija la [[Unidad de Control]] con dos señales.

> [!tip] Microoperaciones de desplazamiento
> Los desplazamientos son **microoperaciones** de la CPU: `shl` (×2), `shr` (÷2), desplazamiento
> aritmético (conserva el signo), rotación (el bit que sale entra por el otro extremo).
> En [[ALU]] se implementan con un desplazador conectado al bus.

## Los ejercicios de la cátedra (TP10 y TP11)
| Registro | Dato del TP | Qué hay que mostrar |
|---|---|---|
| **PIPO 8 bits** | `10101010` | carga **en un solo pulso**: los 8 FF copian a la vez |
| **SISO 8 bits** | `11001100` | tabla **pulso a pulso** del corrimiento (8 pulsos para entrar) |
| **SIPO 8 bits** | `10101010` | entra bit a bit y se lee completo al pulso 8 |
| **PISO 8 bits** | `11001100` | se carga junto y **sale** un bit por pulso |

Las tablas pulso a pulso están resueltas en [[TP10 Registros PIPO y SISO]] y [[TP11 Registros SIPO y PISO]].

## Cómo responderlo en el final## Cómo responderlo en el final
1. Definición: n FF + reloj común + LOAD; guarda una palabra.
2. Clasificar por entradas/salidas: PIPO, SISO, SIPO, PISO.
3. Describir el bidireccional: MUX de 4 canales por FF, con los cuatro modos.
4. Aplicaciones: registros de la CPU (PC, IR, MAR, MBR, AC), transmisión serie, retardos, acumulador de
   multiplicación (desplazamiento + suma).

## Errores típicos
- Decir que el registro "guarda en memoria": guarda dentro de la CPU; el acceso es en un pulso.
- Confundir PISO con SIPO (mirar el orden: entrada-salida).
- Olvidar que el desplazamiento **pierde** el bit que sale por el extremo (salvo en la rotación).

## Relacionado
[[Flip-Flops SR, D, JK y T]] · [[Contadores]] · [[Registros de la CPU]] · [[ALU]]
