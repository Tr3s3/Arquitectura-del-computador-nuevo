---
tp: 13
unidad: 2
tipo: tp
---
# TP13 — Componentes internos de la computadora

> [!abstract] Consigna (cátedra)
> **Ej. 1:** describir cada componente interno y cómo se relacionan: **procesador, memoria principal, placa madre, dispositivos de almacenamiento, buses y dispositivos de E/S**. **Ej. 2:** un gráfico que resuma todo. **Ej. 3:** investigar la configuración de tu propia computadora (por ejemplo con Speccy).

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

**La relación en una frase:** el CPU pide (dirección) → la memoria responde (dato) → por los buses → y todo lo coordina el chipset; los periféricos entran por interfaces que se comportan como "memoria" o "puertos".

> [!tip] El gráfico del Ej. 2
> Es el mismo de [[Estructura básica de un computador]] (CPU + memoria + E/S con los tres buses), pero **agregando** la placa madre como "caja" que contiene los buses y el chipset, y el almacenamiento colgando del bus de E/S. Sirve para mostrar que sabés ubicar la jerarquía real.

## Enlaces
Desarrollo: [[Estructura básica de un computador]] · Buses: [[TP14 Buses]] Siguiente: [[TP14 Buses]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Cómo funciona una computadora](https://www.youtube.com/watch?v=bwrG6Sdow14) | HelderC |
| ▶️ | [Componentes de una computadora](https://www.youtube.com/watch?v=6fz1Mjv_VHc) | HelderC |
| ▶️ | [CPU: el procesador](https://www.youtube.com/watch?v=aCUHp1KLX7E) | HelderC |
| ▶️ | [Memoria principal](https://www.youtube.com/watch?v=VPvVvy5ahAU) | HelderC |
| ▶️ | [Tarjeta madre](https://www.youtube.com/watch?v=PCMpxIzqEO4) | Leonardo Duarte |
| ▶️ | [Periféricos de entrada y salida](https://www.youtube.com/watch?v=unyZ8yNpBV8) | HelderC |
| ▶️ | [Almacenamiento secundario](https://www.youtube.com/watch?v=e27trfKcuBA) | HelderC |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
