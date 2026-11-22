---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Estructura básica de un computador

> [!abstract] En una frase
> Un computador tiene **cuatro unidades** —CPU (Unidad de Control + ALU + registros), Memoria, Entrada y
> Salida— unidas por **tres buses** (datos, direcciones y control). Todo el funcionamiento consiste en
> mover información entre esas unidades por los buses.

## El dibujo (hay que saber hacerlo de memoria)
![[estructura_basica.svg]]

## Las unidades y qué hace cada una
| Unidad | Función | Contiene |
|---|---|---|
| **CPU** | ejecuta las instrucciones | UC, ALU, registros |
| **Unidad de Control (UC)** | **decodifica** la instrucción y **genera las señales de control**: ordena qué se transfiere, cuándo y en qué orden | decodificador, secuenciador, reloj |
| **ALU** | hace las operaciones aritméticas y lógicas | sumador/restador, compuertas, registro de flags |
| **Registros** | guardan direcciones, datos, instrucciones y estado | PC, IR, MAR, MBR, AC (+ RIF, RID en BLUE indexada) |
| **Memoria** | guarda **programa y datos** en la misma espacio | RAM + ROM |
| **E/S** | comunica con el mundo exterior | interfaces, controladores, periféricos |

## Los tres buses (pregunta segura)
| Bus | Anchura en BLUE | Transporta | Dirección del flujo |
|---|---|---|---|
| **Datos** | 16 bits | el dato o la instrucción | bidireccional |
| **Direcciones** | 12 bits | la dirección de la palabra de memoria | CPU → memoria (unidireccional) |
| **Control** | líneas sueltas | señales: MEMR, MEMW, READ, WRITE, CS, R/W', INT, ACK | UC → todos |

**Por qué la anchura importa:**
- La anchura del bus de **datos** define el tamaño de palabra: 16 bits ⇒ la CPU opera con palabras de 16 bits.
- La anchura del bus de **direcciones** define el espacio direccionable: 12 bits ⇒ 2¹² = **4096 palabras**;
  32 bits ⇒ 4 GB. `espacio = 2^(nº de líneas de dirección) × tamaño de palabra`.

## Buses: características que se preguntan
- **Maestro / esclavo:** el maestro (CPU, o el DMA) inicia la transferencia; el esclavo responde.
- **Arbitraje:** si hay varios maestros (CPU y DMA), hace falta un árbitro (o un codificador con prioridad).
- **Síncrono vs asíncrono:** con reloj común (handshake no necesario) vs con señales de *handshake*
  (READY/ACK) para dispositivos de distinta velocidad.
- **Multiplexado:** datos y direcciones comparten líneas en momentos distintos (reduce pines, cuesta tiempo).
- **Jerarquía de buses:** bus local/CPU, bus del sistema, bus de E/S, buses de expansión (PCIe, USB).
- **Tres estados:** los dispositivos que comparten un bus deben poder ponerse en **alta impedancia**
  cuando no son seleccionados. Ver [[Celda elemental de memoria]].

## Von Neumann vs Harvard
- **Von Neumann** (la de la materia): **una sola memoria** para instrucciones y datos, un solo bus ⇒
  simple, pero el bus es cuello de botella (no se puede traer una instrucción y un dato a la vez:
  **cuello de botella de von Neumann**).
- **Harvard:** memorias y buses separados para instrucciones y datos ⇒ permite buscar la instrucción y el
  dato en paralelo; es lo que usan las cachés L1 (separadas en I y D) y muchos microcontroladores.
- **Híbrido** (lo real): von Neumann a nivel de memoria principal + Harvard en las cachés.

## Cómo se guarda el programa (Von Neumann)
Las **instrucciones se guardan en la misma memoria que los datos**, como si fueran números. El
**PC** contiene la dirección de la próxima instrucción; la UC la busca, la decodifica y la ejecuta
(ver [[Ciclo de máquina]]). Eso es lo que permite que un programa sea simplemente "datos cargados en
memoria" y que la CPU sea universal.

## Cómo responderlo en el final (pregunta principal #4)
1. Enumerar las unidades y la función de cada una, con el dibujo.
2. Describir los tres buses: qué transportan, en qué dirección, y qué define su anchura.
3. Explicar el ciclo: la UC toma la instrucción de memoria, la decodifica y genera señales para que
   ALU/registros/memoria ejecuten.
4. Mencionar von Neumann (una memoria para todo) y su cuello de botella; agregar maestro/esclavo y
   arbitraje como detalle que sube nota.

## Errores típicos
- Decir que el bus de direcciones es bidireccional (es CPU → memoria).
- Confundir anchura de datos con anchura de direcciones al calcular el espacio direccionable.
- Olvidar que la ALU **no** toma decisiones: decide la UC.
- Decir que la memoria guarda sólo datos (en von Neumann guarda también el programa).

## Relacionado
[[Registros de la CPU]] · [[Unidad de Control]] · [[ALU]] · [[Ciclo de máquina]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
