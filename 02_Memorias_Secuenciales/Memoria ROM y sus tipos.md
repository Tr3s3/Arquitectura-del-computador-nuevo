---
unidad: 2
tipo: concepto
examen: secundario
---
# Memoria ROM y sus tipos

> [!abstract] En una frase
> La ROM (Read Only Memory) es una memoria **no volátil** cuyo contenido se fija al fabricarla o se graba
> con un equipo especial: en operación normal **sólo se lee**. Se usa para el firmware/BIOS, para tablas
> fijas y para la **memoria de control** de la UC microprogramada.

## RAM vs ROM (la tabla que se pregunta)
| | RAM | ROM |
|---|---|---|
| Escritura en operación | sí (rápida, muchas veces) | no (sólo lectura) |
| Volatilidad | volátil (pierde sin energía) | no volátil |
| Uso | programa en ejecución y datos | firmware, tablas, microcódigo |
| Tipo de celda | latch (SRAM) / capacitor (DRAM) | conexión fija o transistor flotante |

## Tipos de ROM
| Tipo | Cómo se graba | ¿Se puede borrar? | Comentario |
|---|---|---|---|
| **Máscara (mask ROM)** | en fábrica, con la máscara del circuito | no | la más barata en volumen; sólo para grandes series |
| **PROM** | el usuario, una sola vez (fusibles) | no | programable por el usuario |
| **EPROM** | eléctricamente, con programador | sí, con **luz ultravioleta** (ventana de cuarzo) | lenta de borrar, ~20 min |
| **EEPROM** | eléctricamente, byte a byte | sí, eléctricamente | borrado/regrabado en el circuito |
| **Flash** | eléctricamente, por bloques | sí, eléctricamente | la EEPROM moderna: USB, SSD, firmware |

> [!tip] Mnemotecnia
> **P**ROM = programable una vez · **EP**ROM = *erasable* con UV · **EEP**ROM = *electrically erasable* ·
> **Flash** = EEPROM rápida por bloques.

## Estructura interna
Es igual a la de la RAM, pero **la matriz es fija**: el decodificador de filas selecciona la palabra y los
buffers de salida la ponen en el bus. No hay entrada de datos ni R/W': sólo `CS/OE` (output enable).
- Cada celda es un punto de la matriz que **existe o no existe** (transistor presente = 1, ausente = 0, o
  fusible intacto/volado).
- Como no se escribe, el acceso suele ser más rápido que en la RAM y no necesita refresco.

## Para qué se usa
1. **Firmware / BIOS**: el programa de arranque que no debe perderse al apagar.
2. **Tablas de constantes**: tablas de senos, tablas de conversión de código, caracteres de la fuente
   del display.
3. **Memoria de control** de la [[Unidad de control cableada y microprogramada|UC microprogramada]]: el
   microprograma se guarda en una ROM y se lee en cada pulso. (¡Es la aplicación que pide la Unidad 6!)
4. **Microcontroladores**: el programa completo del sistema embebido.

## Cómo responderlo en el final
1. Definir: memoria no volátil de sólo lectura.
2. Tabla de tipos (máscara, PROM, EPROM, EEPROM, Flash) con cómo se graba y si se puede borrar.
3. Estructura: decodificador + matriz fija + buffers; sin R/W'.
4. Aplicaciones: firmware, tablas y **memoria de control del microprograma**.

## Errores típicos
- Decir que la ROM es "memoria de sólo lectura" y que la Flash "es RAM" (es una ROM regrabable).
- Olvidar que la ROM también es de **acceso aleatorio** (se direcciona igual que la RAM); lo que cambia es
  que no se escribe.
- Confundir volátil (pierde el dato sin energía) con "de sólo lectura".

## Relacionado
[[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · [[Jerarquía de memorias]] · [[Unidad de control cableada y microprogramada]]
