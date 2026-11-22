---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Ciclo de máquina

> [!abstract] En una frase
> El ciclo de máquina es la **unidad de trabajo** de la CPU: mientras `RUN = 1`, la máquina repite
> **búsqueda (fetch) → decodificación → ejecución (execute)** de una instrucción, y vuelve a empezar con la
> siguiente. Ese ciclo se mide en **pulsos de reloj**, y cada pulso habilita una microoperación.

## El ciclo, dibujado
![ciclo_maquina](assets/ciclo_maquina.svg)

```
        ┌──────────────────────────────────────────────┐
        │                                              │
   RUN=1 ▼                                              │
 ┌──────────────┐   decodifica    ┌──────────────────┐  │
 │  BÚSQUEDA    │ ──────────────→ │   EJECUCIÓN      │──┘
 │ (STATE = F)  │                 │  (STATE = E)     │
 └──────────────┘                 └──────────────────┘
   trae la instrucción             hace lo que dice
   de la dirección del PC          la instrucción
```

## Las dos fases
| Fase | Qué hace | Resultado |
|---|---|---|
| **Búsqueda (fetch)** | `PC → MAR → memoria → MBR → IR`; incrementa el PC | la instrucción está en el **IR** |
| **Ejecución (execute)** | decodifica el opcode y ejecuta las microoperaciones del caso | el resultado queda en un registro o en memoria |

## Quién manda en cada fase
| Elemento | En la búsqueda | En la ejecución |
|---|---|---|
| **STATE** | F | E |
| **PC** | se lee y se incrementa | se carga si hay salto |
| **MAR** | recibe la dirección de la instrucción | recibe la dirección del operando |
| **IR** | se carga | se decodifica (el opcode va a la UC) |
| **UC** | genera las señales de la búsqueda | genera las señales de **esa** instrucción |
| **ALU** | no participa (salvo el incremento del PC) | opera (ADD, SUB, AND…) |

## Por qué la búsqueda es igual para todas las instrucciones
Antes de saber qué instrucción es, la CPU **no puede** hacer nada específico: tiene que traerla. Por eso la
búsqueda es **fija** (misma secuencia de pulsos para toda instrucción) y la que varía es la ejecución.
Eso simplifica enormemente la UC: la secuencia de búsqueda está "cableada" y la de ejecución depende del
opcode.

## Cuántos pulsos
- La búsqueda en BLUE ocupa **7 u 8 pulsos** según cómo se cuente (ver
  [[Ciclo de búsqueda (7 y 8 pulsos)]]).
- La ejecución depende de la instrucción, pero en BLUE está acotada: por ejemplo `LDA` totaliza
  **24 pulsos** contando búsqueda + ejecución (ver [[Ciclo de la instrucción LDA (24 pulsos)]]).
- Una instrucción completa = búsqueda + ejecución ⇒ **ciclo de instrucción**. Dentro de él, cada pulso
  hace **una** microoperación.

> [!tip] Nomenclatura que conviene usar
> **Ciclo de máquina** = búsqueda + ejecución de una instrucción. **Ciclo de instrucción** = lo mismo.
> **Pulso (T)** = unidad mínima; en cada pulso se hace una microoperación de transferencia.
> Muchos textos llaman "ciclo de máquina" a lo que dura un acceso a memoria; en esta cátedra es el ciclo
> completo de la instrucción.

## El arranque y la parada
- **RESET / RUN = 1**: el PC se precarga (normalmente 0) y STATE = F ⇒ comienza la búsqueda.
- **HLT**: pone `RUN = 0`; el ciclo se detiene después de terminar la instrucción en curso.
- **Interrupción**: al final de una ejecución, si hay pedido habilitado, la UC fuerza un ciclo de
  interrupción en lugar de la próxima búsqueda (ver [[Interrupciones y entrada-salida]]).

## Cómo responderlo en el final (pregunta principal #3)
1. Definir: unidad de trabajo de la CPU, se repite mientras RUN = 1.
2. Nombrar las fases: búsqueda (fetch) → decodificación → ejecución.
3. Recorrer la búsqueda con sus microoperaciones (PC→MAR, MEMR, MBR, PC+1, IR).
4. Explicar la ejecución según el opcode, con un ejemplo (LDA y JMP son los mejores contrastes).
5. Cerrar con los FF RUN/STATE/CLOCK y la idea de pulso = microoperación.

## Errores típicos
- Decir que la decodificación es una "tercera fase" separada del ciclo: es el paso que cierra la búsqueda
  y dispara la ejecución.
- Olvidar el incremento del PC (sin él, se ejecuta la misma instrucción para siempre).
- Confundir ciclo de máquina con ciclo de reloj (uno contiene muchos del otro).
- Decir que el PC apunta a la instrucción que se ejecuta (apunta a la **siguiente**).

## Relacionado
[[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] · [[Unidad de Control]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
