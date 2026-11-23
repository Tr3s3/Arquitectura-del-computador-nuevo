---
tp: 19
unidad: 5
tipo: tp
prioridad: maxima
---
# TP19 — Modos de direccionamiento de memoria

> [!abstract] Consigna (cátedra)
> Desarrollar, para cada modo de direccionamiento, sus **características, ventajas y desventajas**
> (y su gráfico). Los siete modos del TP son: **inmediato, directo, indirecto, de registro,
> registro indirecto, de desplazamiento y de pila (stack)**.

> [!important] Esta es la lista oficial de la cátedra
> Son **siete** modos, no cinco. En el final conviene nombrar los siete con su característica principal y
> una ventaja/desventaja de cada uno; el desarrollo completo está en [[Modos de direccionamiento]].

## Los siete modos, en una tabla (respuesta rápida)
| # | Modo | Característica | Accesos a memoria | Ventaja | Desventaja |
|---|---|---|---|---|---|
| 1 | **Inmediato** | el dato está **en la instrucción** | 0 | rápido, sin acceso a memoria | el dato queda limitado a los bits de la instrucción |
| 2 | **Directo** | la instrucción contiene la **dirección efectiva** | 1 | simple y fácil de usar | limitado a la memoria direccionable |
| 3 | **Indirecto** | la instrucción apunta a una celda **que contiene la dirección** | **2** | direcciona mucha más memoria | más lento (dos accesos) |
| 4 | **De registro** | el operando está en un **registro** de la CPU | 0 | muy rápido, menos tráfico de bus | pocos registros disponibles |
| 5 | **Registro indirecto** | el registro contiene **una dirección** de memoria | 1 | usa el registro como **puntero** (listas/arrays) | un acceso a memoria igual |
| 6 | **De desplazamiento** | `EA = base + desplazamiento (offset)` | 1 | ideal para **arrays y estructuras** | sobrecarga de cálculo; offset limitado |
| 7 | **De pila (stack)** | el operando se saca/pone de la **pila** (LIFO) con PUSH/POP | 1 | automatiza llamadas a subrutina y contexto | riesgo de desbordamiento de pila |

## Cómo se dice cada uno en 20 segundos
1. **Inmediato:** "el dato viaja dentro de la instrucción; no se va a memoria. Ejemplo: cargar la constante 5."
2. **Directo:** "la instrucción dice la dirección del dato: es el `LDA 25h` clásico. Un solo acceso."
3. **Indirecto:** "la instrucción dice dónde está la dirección del dato: punteros. **Dos accesos**, por eso
   es más lento pero direcciona mucho más."
4. **De registro:** "el dato ya está en un registro del CPU; no hay acceso a memoria. Es el más rápido."
5. **Registro indirecto:** "el registro guarda una **dirección**, no el dato: sirve de puntero para recorrer
   listas o arreglos."
6. **De desplazamiento:** "se suma un **offset** a una base: `EA = base + desplazamiento`. Es el modo de los
   vectores, matrices y campos de una estructura; en la práctica es el **indexado** (BLUE indexada con
   RIF/RID)."
7. **De pila:** "el operando se toma del tope de la pila (LIFO) con `PUSH`/`POP`; es clave para subrutinas e
   interrupciones, porque guarda y recupera la dirección de retorno."

> [!tip] Puente con el final
> La pregunta "modos de direccionamiento en BLUE indexada ¿ventajas?" se responde con el **modo 6**: el
> indexado permite recorrer arreglos con un mismo código, ahorra bits de dirección y es reubicable. Ver
> [[BLUE indexada (RIF, RID, nuevo formato)]].

## Enlaces
Desarrollo: [[Modos de direccionamiento]] · Aplicación: [[BLUE indexada (RIF, RID, nuevo formato)]]
Siguiente: [[TP20 Lenguaje máquina]]
