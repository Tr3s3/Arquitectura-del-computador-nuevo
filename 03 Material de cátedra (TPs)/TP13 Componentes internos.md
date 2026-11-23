---
tp: 13
unidad: 2
tipo: tp
---
# TP13 — Componentes internos de la computadora

> [!abstract] Consigna (cátedra)
> **Ej. 1:** describir cada componente interno y cómo se relacionan: **procesador, memoria principal, placa
> madre, dispositivos de almacenamiento, buses y dispositivos de E/S**.
> **Ej. 2:** un gráfico que resuma todo.
> **Ej. 3:** investigar la configuración de tu propia computadora (por ejemplo con Speccy).

## Cómo se responde (componente por componente)
| Componente | Qué hace | Se conecta por |
|---|---|---|
| **Procesador (CPU)** | ejecuta las instrucciones: UC decodifica y genera señales, ALU opera, registros guardan | bus del sistema (con la memoria y la E/S) |
| **Memoria principal (RAM)** | guarda programa y datos en ejecución | bus de datos + bus de direcciones + control |
| **Placa madre** | es el **soporte físico y eléctrico**: zócalo del CPU, ranuras de memoria, chipset, buses, conectores de E/S | todos los buses y el chipset |
| **Chipset** | puente entre CPU, memoria y periféricos (north/south bridge, hoy integrado) | buses internos |
| **Almacenamiento** | guarda de forma **permanente**: HDD, SSD, óptico | interfaz SATA/NVMe/USB (bus de E/S) |
| **Buses** | transportan datos, direcciones y control entre los módulos | — |
| **E/S** | entrada/salida hacia el usuario y la red: teclado, mouse, monitor, impresora, NIC | puertos e interfaces |

**La relación en una frase:** el CPU pide (dirección) → la memoria responde (dato) → por los buses → y todo
lo coordina el chipset; los periféricos entran por interfaces que se comportan como "memoria" o "puertos".

> [!tip] El gráfico del Ej. 2
> Es el mismo de [[Estructura básica de un computador]] (CPU + memoria + E/S con los tres buses), pero
> **agregando** la placa madre como "caja" que contiene los buses y el chipset, y el almacenamiento colgando
> del bus de E/S. Sirve para mostrar que sabés ubicar la jerarquía real.

## Enlaces
Desarrollo: [[Estructura básica de un computador]] · Buses: [[TP14 Buses]]
Siguiente: [[TP14 Buses]]
