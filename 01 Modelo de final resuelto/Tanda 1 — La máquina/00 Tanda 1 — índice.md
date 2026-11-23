---
tipo: indice
prioridad: maxima
---
# Tanda 1 — La máquina (8 preguntas)

> [!abstract] Cómo está armada esta tanda
> Cada **pregunta** tiene su **carpeta** con los archivos que le corresponden: primero el **desarrollo principal** (la nota que responde la pregunta) y después los **subtemas** que hay que saber para poder contestarla. Todo está en la misma carpeta: no hay que buscar nada afuera.

| # | Pregunta | Carpeta | Archivos que corresponden |
|---|---|---|---|
| 1.1 | **Flujo de información (direcciones y datos)** | `1.1 Flujo de información (direcciones y datos)/` | [[Flujo de información en BLUE (datos y direcciones)]] |
| 1.2 | **BLUE vs BLUE indexada** | `1.2 BLUE vs BLUE indexada/` | [[BLUE vs BLUE indexada — qué cambia y por qué]] · *en `Apoyo a la pregunta/`:* [[BLUE indexada (RIF, RID, nuevo formato)]] |
| 1.3 | **Ciclo de LDA indexada (24 pulsos)** | `1.3 Ciclo de LDA indexada (24 pulsos)/` | [[Ciclo de LDA indexada (los 24 pulsos)]] · *en `Apoyo a la pregunta/`:* [[Ciclo de la instrucción LDA (24 pulsos)]] |
| 1.4 | **Memoria RAM 8×3** | `1.4 Memoria RAM 8x3/` | [[Memoria RAM 8x3]] |
| 1.5 | **Estructura básica del computador** | `1.5 Estructura básica del computador/` | [[Estructura básica de un computador]] |
| 1.6 | **Implementación de la Unidad de Control** | `1.6 Implementación de la Unidad de Control/` | [[Cómo se implementa la Unidad de Control]] · *en `Apoyo a la pregunta/`:* [[Unidad de Control]] |
| 1.7 | **Formato de la instrucción (4 → 1 campo)** | `1.7 Formato de la instrucción (4 formatos)/` | [[Formato de la instrucción (4 formatos)]] · *en `Apoyo a la pregunta/`:* [[Espacio de direccionamiento y cálculo de CodOp-Dirección]] |
| 1.8 | **Ciclo de máquina y ciclo de instrucción** | `1.8 Ciclo de máquina y ciclo de instrucción/` | [[Ciclo de máquina]] · *en `Apoyo a la pregunta/`:* [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] · [[Proceso de manejo de una instrucción]] |

> [!note] La carpeta `Apoyo a la pregunta/` (está dentro de cada pregunta)
> Cada pregunta tiene adentro **`Apoyo a la pregunta/`** con la nota **`00 Apoyos — N.M …`**: la lista de los archivos que hacen falta para responderla, **para qué sirve cada uno** y el enlace a los apoyos que viven en otras tandas. La nota principal de la pregunta lo resume en un bloque al principio, así que nunca hay que adivinar qué leer antes.

---

## El orden en que conviene estudiarla

1. **1.5 Estructura básica** — qué piezas tiene una computadora (si no sabés esto, el resto no cierra).

2. **1.1 Flujo de información** — cómo viaja un dato por el bus único.

3. **1.7 Formato de la instrucción** — cómo se parte la palabra de 16 bits.

4. **1.8 Ciclo de máquina** — los 8 pulsos y las 5 fases.

5. **1.4 Memoria RAM 8×3** — el circuito que se dibuja.

6. **1.6 Implementación de la UC** — quién genera las señales.

7. **1.2 BLUE vs indexada** — qué se agrega y qué cambia.

8. **1.3 LDA indexada (24 pulsos)** — el caso completo, pulso por pulso.

> [!tip] Lo que se dibuja de esta tanda
> La RAM 8×3 (con decodificador y biestables) · el diagrama de bloques con el bus único · el ciclo de búsqueda en 8 pulsos · la tabla pulso por pulso de la LDA indexada. Práctica: [[Cómo dibujar los circuitos (checklist de pizarrón)]].

---

## Ficha rápida (para repasar en 5 minutos)

| Pregunta | Lo que no se puede omitir |
|---|---|
| 1.1 | Una sola transferencia por pulso (bus único); el MAR va al bus de direcciones y el MBR al de datos |
| 1.2 | La indexada agrega RIF, RID, RB, sumador de direcciones y modificador de 2 bits; **paga** 24 pulsos |
| 1.3 | 3 ciclos de 8: el 2.º trae la 2.ª palabra y calcula la EA; el 3.º accede al dato |
| 1.4 | 8 palabras × 3 bits, decodificador 3→8, biestable + selección + L/E por celda |
| 1.5 | CPU (UC + ALU + registros) + memoria + E/S, unidos por buses |
| 1.6 | `señal = estado · pulso · instrucción`, juntadas por OR; decodificador 1→16 |
| 1.7 | 4 formatos de instrucción → 1 campo de dirección de 12 bits; `bits dir = log₂ celdas` |
| 1.8 | 8 pulsos de 125 ns; `PC→MAR` en CP1, `PC+1` en CP2-CP4, `MBR→IR` en CP6, `E→State` en CP8 |

---

## Relacionado
[[00 Índice — el final resuelto]] · [[00 Tanda 2 — índice]] · [[00 Tanda 3 — índice]] · [[00 Matriz del final — las 3 tandas]] · [[02 Chequeo de los 12 temas]]
