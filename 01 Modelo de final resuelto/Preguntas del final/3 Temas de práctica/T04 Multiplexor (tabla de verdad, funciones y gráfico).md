---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T04 · Multiplexor (tabla de verdad, funciones y gráfico)

> [!question] Pregunta
> Explique el multiplexor 4 → 1: tabla de verdad, función (SOP) y circuito. ¿Para qué se usa en la CPU?

## 1. Teoría previa

**Multiplexor (MUX).** Circuito con `2ⁿ` entradas de datos, `n` líneas de selección y **una** salida. La salida copia la entrada que indica la selección.

**Forma SOP (suma de productos).** La salida es la OR de los productos "selección · entrada". Para un 4 → 1:

`Y = S1'·S0'·I0 + S1'·S0·I1 + S1·S0'·I2 + S1·S0·I3`

## 2. Contexto

El multiplexor es la pieza que **elige** qué fuente llega al bus. En BLUE, el bus de la CPU recibe datos de varios registros: el selector de datos decide cuál escribe. Por eso aparece en el flujo de información (P01).

## 3. Gráfico

![[T04-multiplexor.svg]]

*Lectura:* cuatro entradas I0 a I3 a la izquierda; las selecciones S1 S0 abajo; la salida Y a la derecha. La tabla muestra qué entrada pasa para cada selección.

## Figuras reales (libros y resumen de cátedra)

![[libro-quiroga-f6-20.png]]

*Fig. 6.20 — Diagrama de bloque de un multiplexor para cuatro entradas.* · Quiroga, *Arquitectura de computadoras*, p. 149

![[catedra-said-mux-integrado.png]]

*El MUX 4:1 dibujado como integrado.* · Resumen de cátedra (Said)

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## Cómo se ve el circuito (combinacional)

El multiplexor 4 a 1 tiene 4 entradas de dato (I0 a I3), 2 de selección (S1, S0) y una salida Y. Las líneas de selección pasan por un decodificador 2 a 4; cada AND deja pasar solo una entrada de dato, y la OR junta las cuatro salidas.

![[C04-multiplexor-4a1-bloques.svg]]

> [!tip] Cómo leerlo
> - Con S1 S0 = 00 pasa I0; 01 pasa I1; 10 pasa I2; 11 pasa I3.
> - Las figuras reales del multiplexor de cátedra y de Quiroga (arriba) muestran el mismo esquema en forma de integrado.
> - Un multiplexor de n entradas necesita log₂(n) líneas de selección.

## 4. Desarrollo detallado

### 4.1 Tabla de verdad (selección → entrada)

| S1 | S0 | Y |
|---|---|---|
| 0 | 0 | I0 |
| 0 | 1 | I1 |
| 1 | 0 | I2 |
| 1 | 1 | I3 |

### 4.2 Función

`Y = S1'S0' I0 + S1'S0 I1 + S1S0' I2 + S1S0 I3`

Es una suma de cuatro productos: cada producto activa una entrada según su selección.

### 4.3 Circuito

1. **Inversores** para `S1'` y `S0'`.
2. **Cuatro AND de tres entradas**: cada una combina dos selecciones (o sus negados) con una entrada de dato.
3. **Una OR de cuatro entradas** que junta las cuatro salidas de las AND.

Es la forma **AND-OR**, la que se dibuja en el pizarrón.

### 4.4 Uso en la CPU
Si el bus de datos puede venir de AC, MBR, PC o IR, un multiplexor de 4 entradas elige cuál se pone en el bus. Las selecciones las da la UC.

## 5. Cómo se responde (4 minutos)

1. **Definición:** "Elige una de 2ⁿ entradas según la selección y la pone en la salida."
2. **Tabla:** las cuatro selecciones.
3. **Función:** la SOP de cuatro productos.
4. **Circuito:** inversores, cuatro AND, una OR.
5. **Uso:** elegir la fuente que va al bus.

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántas selecciones tiene un 8 → 1? | 3. |
| ¿Cuántas compuertas AND tiene un 4 → 1? | 4 (una por entrada). |
| ¿Qué pasa si S1S0 = 10? | La salida es I2. |
| Error común | Olvidar los negados en los productos (S1' y S0'). |

## 7. Relacionado

- [[Multiplexor]] · [[1.4.3 Multiplexor]] · [[TP7 Codificadores y multiplexores]]
- [[Flujo de información en BLUE (datos y direcciones)]] · [[T03 Demultiplexor (tabla de verdad, funciones y gráfico)]]
