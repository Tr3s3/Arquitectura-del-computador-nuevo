---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S04 · Memoria ROM

> [!question] Pregunta
> ¿Qué es una memoria ROM? Explique cómo está construida, sus tipos (máscara, PROM, EPROM, EEPROM, Flash) y para qué se usa.

## 1. Teoría previa

**ROM (Read Only Memory).** Memoria de **sólo lectura** en operación normal y **no volátil**: conserva el contenido sin alimentación.

**RAM vs ROM.**

| | RAM | ROM |
|---|---|---|
| Operación | lectura y escritura | sólo lectura |
| Volatilidad | volátil | no volátil |
| Velocidad | rápida | más lenta, sobre todo al escribir |
| Para qué | datos y programas en ejecución | firmware, tablas fijas, memoria de control, BIOS |
| Costo por bit | mayor | menor |

**Tipos.**

| Tipo | Cómo se graba | ¿Se borra? |
|---|---|---|
| ROM de máscara | en fábrica | no |
| PROM | una vez, por el usuario (fusibles) | no |
| EPROM | eléctricamente | sí, con luz ultravioleta (toda a la vez) |
| EEPROM | eléctricamente | sí, byte a byte |
| Flash | eléctricamente | sí, por bloques (pendrives, SSD) |

## 2. Contexto

La ROM es el ejemplo perfecto de **lógica combinacional usada como memoria**: un decodificador más una matriz de conexiones. Se pregunta para ver que entendés que una memoria no siempre es escribible y que la ROM tiene un uso fijo.

## 3. Gráfico

![[S04-rom.svg]]

*Lectura:* el decodificador 2→4 activa una línea de palabra (W0…W3). Cada punto (1) donde la línea cruza una columna de datos indica que ese bit vale 1. La tabla de abajo es el contenido.

## 4. Desarrollo detallado

### 4.1 La ROM es un bloque combinacional
Una ROM de `2ⁿ` palabras es un **decodificador `n → 2ⁿ`** seguido de una **matriz de OR**. Para cada salida de datos, se hace la OR de las palabras (líneas) que tienen un 1 en esa columna.

Ejemplo (según el gráfico): `D0 = W0 + W2` (las palabras 0 y 2 tienen un 1 en el bit 0) y `D1 = W1 + W2`. Para cada bit se suman las palabras que tienen un 1 en esa columna.

### 4.2 Cómo se graba
- En la **ROM de máscara**, el patrón de conexiones se define en la fabricación.
- En la **PROM**, el usuario "quema" fusibles para dejar o cortar cada conexión.
- En la **EPROM**, se borra con UV y se regraba con equipo.
- En la **EEPROM/Flash**, se borra y regraba eléctricamente.

### 4.3 Usos
- **Firmware** y BIOS: el programa que arranca la PC.
- **Tablas fijas**: senos, caracteres (generadores de caracteres).
- **Memoria de control**: la UC microprogramada guarda sus microinstrucciones en una ROM.

## 5. Cómo se responde (2–3 minutos)

1. **Definición:** "Memoria no volátil de sólo lectura, con contenido fijo o grabado una vez."
2. **Dibujo:** decodificador, matriz de palabras y salidas.
3. **Tipos:** máscara, PROM, EPROM, EEPROM, Flash, con cómo se borran.
4. **Uso:** firmware, tablas, memoria de control.

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Por qué la ROM es no volátil? | Su contenido está en la estructura o en la carga de la celda, no en la alimentación. |
| ¿Diferencia EPROM / EEPROM? | La EPROM se borra con UV toda a la vez; la EEPROM se borra eléctricamente. |
| ¿Qué es la memoria de control? | Una ROM con las microinstrucciones de la UC microprogramada. |
| Error común | Decir que la ROM no se puede leer en operación. Sí se lee; lo que no se escribe. |

## 7. Relacionado

- [[Memoria ROM y sus tipos]] · [[2.4.1 ROM = decodificador + OR]] · [[2.4.2 PROM, EPROM, EEPROM y Flash]]
- [[P07 Unidad de Control (funciones, señales e importancia)]]
