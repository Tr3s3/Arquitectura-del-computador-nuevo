---
tipo: glosario
---
# Glosario

> [!abstract] Uso
> Término → definición de una línea → nota donde se desarrolla. Sirve para el repaso rápido y para no quedar en blanco con una sigla en el oral.

## A – C

| Término | Definición | Nota |
|---|---|---|
| **AC** (acumulador) | registro que guarda un operando y el resultado de la ALU | [[Registros de la CPU]] |
| **ALU** | unidad que hace las operaciones aritméticas y lógicas | [[ALU]] |
| **Biestable / flip-flop** | circuito secuencial que memoriza 1 bit | [[Flip-Flops SR, D, JK y T]] |
| **Bus** | conjunto de líneas que transportan datos, direcciones o control | [[Estructura básica de un computador]] |
| **CAM** | memoria asociativa: se busca por contenido | [[Memoria auxiliar y memoria asociativa]] |
| **Chip select (CS)** | señal que habilita un chip en el bus | [[Memoria RAM 8x3]] |
| **CISC** | arquitectura de instrucciones complejas (x86) | [[CISC y RISC]] |
| **Codificador** | 2ⁿ entradas → n salidas (inverso del decodificador) | [[Codificador]] |
| **Combinacional** | circuito cuya salida depende sólo de las entradas actuales | [[Compuertas lógicas]] |
| **Contador** | registro que recorre una secuencia con cada pulso | [[Contadores]] |

## D – L

| Término | Definición | Nota |
|---|---|---|
| **Decodificador** | n entradas → 2ⁿ salidas; activa una sola | [[Decodificador]] |
| **DEMUX** | 1 → 2ⁿ: dirige un dato a una salida | [[Demultiplexor]] |
| **Dirección efectiva (EA)** | dirección final que se pone en el MAR | [[Modos de direccionamiento]] |
| **DMA** | transferencia periférico↔memoria sin la CPU | [[Técnicas para aumentar la velocidad]] |
| **DRAM** | RAM dinámica (capacitor), necesita refresco | [[Celda elemental de memoria]] |
| **Flag** | bit de estado (Z, C, N, V) que fija la ALU | [[ALU]] |
| **Flip-flop (tipo) — D, J-K, T, S-R** | variantes del biestable según su tabla de estados | [[Flip-Flops SR, D, JK y T]] |
| **IR** | registro de instrucción: la instrucción en ejecución | [[Registros de la CPU]] |
| **Interrupción** | pedido de atención que rompe la secuencia del programa | [[Interrupciones y entrada-salida]] |
| **Localidad** | propiedad por la que se reutilizan datos/instrucciones cercanos | [[Jerarquía de memorias]] |

## M – R

| Término | Definición | Nota |
|---|---|---|
| **MAR** | registro de dirección de memoria | [[Registros de la CPU]] |
| **MBR** | registro buffer de memoria (dato) | [[Registros de la CPU]] |
| **Microoperación** | transferencia u operación elemental que se hace en un pulso | [[Ciclo de máquina]] |
| **Microprograma** | programa que ejecuta la UC (en la memoria de control) | [[Unidad de control cableada y microprogramada]] |
| **Mintérmino** | producto que vale 1 para una sola combinación | [[Mintérminos y maxtérminos]] |
| **MUX** | 2ⁿ → 1: selector de datos | [[Multiplexor]] |
| **Opcode** | código de operación de la instrucción | [[Máquina BLUE — arquitectura y conjunto de instrucciones]] |
| **PC** | contador de programa: dirección de la próxima instrucción | [[Registros de la CPU]] |
| **Pipeline** | etapas solapadas para aumentar el ritmo de ejecución | [[Pipeline]] |
| **Polling** | consulta periódica de la CPU a los periféricos | [[Interrupciones y entrada-salida]] |
| **RAM / ROM** | memoria de lectura-escritura / de sólo lectura | [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] |
| **RIF / RID** | registros índice de BLUE indexada | [[BLUE indexada (RIF, RID, nuevo formato)]] |
| **RISC** | arquitectura de instrucciones reducidas (ARM) | [[CISC y RISC]] |

## S – Z

| Término | Definición | Nota |
|---|---|---|
| **SRAM** | RAM estática (latch), no necesita refresco | [[Celda elemental de memoria]] |
| **STATE (F/E/I)** | estado de la UC: búsqueda / ejecución / interrupción | [[Ciclo de máquina]] |
| **Tres estados** | salida 0, 1 o alta impedancia (Z) para compartir un bus | [[Celda elemental de memoria]] |
| **TLB** | caché asociativa de traducciones de página | [[Memoria virtual y administración de memoria]] |
| **UC** | unidad de control: decodifica y genera las señales | [[Unidad de Control]] |
| **Von Neumann** | arquitectura con una memoria y un bus para todo | [[Estructura básica de un computador]] |
| **Write-back / write-through** | políticas de escritura de la caché | [[Memoria caché]] |
| **Z (flag)** | indica resultado cero; lo consulta `JZ` | [[ALU]] |
