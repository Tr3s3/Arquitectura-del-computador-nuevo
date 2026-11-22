---
tp: 14
unidad: 2
tipo: tp
prioridad: alta
---
# TP14 — Buses

> [!abstract] Consigna (cátedra)
> Desarrollar **qué es un bus**, sus **tipos** (datos, direcciones, control) y el detalle de cada uno.

## Definición (la de la cátedra)
> "Un **bus** es una vía de comunicación que conecta **dos o más dispositivos**. Una señal transmitida por
> cualquier dispositivo conectado será recibida por **todos** los otros."

De ahí salen dos consecuencias que hay que decir:
1. **Todos escuchan**: hay que **seleccionar** quién responde (por eso existen las direcciones y el
   chip select).
2. **Uno habla por vez**: las salidas de los dispositivos deben poder ponerse en **alta impedancia**
   (tres estados) para no cortocircuitarse.

## Los tres buses
| Bus | Función | Dirección del flujo | Qué determina su ancho |
|---|---|---|---|
| **Datos** | transporta el **dato** entre los módulos | bidireccional | el **tamaño de palabra** con el que opera el sistema |
| **Direcciones** | **designa a quién** va el dato (memoria o puerto de E/S) | CPU → memoria/E/S (unidireccional) | la **capacidad máxima de memoria** direccionable (2ⁿ) |
| **Control** | controla el **acceso y uso** de las líneas de datos y direcciones; órdenes y **temporización** (indica cuándo el dato/dirección es válido) | UC → todos | cantidad de señales de control |

**Líneas típicas del bus de control** (las enumera el TP): lectura y escritura de memoria · lectura y
escritura de E/S · **petición de bus** · **cesión de bus** · **petición de interrupción**.

## Dos datos que valen oro en el oral
> [!important] Ancho de bus y doble acceso
> "El ancho del bus es un factor clave en las prestaciones. Por ejemplo, **si el bus de datos tiene 8 bits y
> las instrucciones son de 16 bits, el procesador debe acceder al módulo de memoria dos veces por cada ciclo
> de instrucción.**"
>
> Y del lado de direcciones: "el ancho del bus de direcciones determina la **máxima capacidad de memoria**
> posible; además las líneas de direcciones se usan para direccionar **puertos de E/S**, y habitualmente los
> bits más altos seleccionan el módulo (memoria o E/S)".

## Otros conceptos de bus para nombrar
- **Maestro / esclavo**: el maestro inicia la transferencia (CPU, DMA); el esclavo responde.
- **Arbitraje**: si hay varios maestros, alguien decide el orden (petición/cesión de bus, prioridades).
- **Síncrono vs asíncrono**: con reloj común o con *handshake* (READY/ACK).
- **Multiplexado**: datos y direcciones comparten líneas en distintos momentos (menos pines, más tiempo).
- **Jerarquía**: bus local del CPU, bus del sistema, bus de E/S, buses de expansión (PCIe, USB).

## Enlaces
Desarrollo: [[Estructura básica de un computador]] · Tres estados: [[Celda elemental de memoria]]
Siguiente: [[TP15 Arquitectura de Von Neumann (IAS)]]
