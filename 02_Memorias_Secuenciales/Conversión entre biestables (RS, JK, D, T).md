---
unidad: 2
tipo: concepto
examen: practica
prioridad: maxima
---
# Conversión entre biestables (RS, JK, D, T)

> [!abstract] En una frase
> Convertir un biestable en otro es **construir el biestable que tengo para que se comporte como el que
> quiero**: se escribe la tabla de transición del biestable pedido, se ve **qué entradas necesita el que
> tengo** para cada transición (tabla de excitación) y se obtienen esas entradas como **función booleana
> simplificada por Karnaugh**. Los cuatro resultados que hay que saber de memoria:
> **`S = J·Q̄`, `R = K·Q`** (RS a partir de JK) · **`D = J·Q̄ + K̄·Q`** (D a partir de JK) · **`J = K = T`** ·
> **`J = D`, `K = D̄`**.

## Partamos de cero: por qué se convierte un biestable
Un **biestable** guarda **1 bit**. Lo que cambia entre tipos es **cómo se le pide que cambie**:
- **RS**: le digo *seteá* (S) o *reseteá* (R).
- **D**: le digo *quedate con este dato* (D).
- **JK**: le digo *seteá* (J), *reseteá* (K), *no hagas nada* (00) o *cambiá de estado* (11).
- **T**: le digo *cambiá* (T = 1) o *no cambies* (T = 0).

En la práctica uno consigue un chip (por ejemplo, un 74LS76 de **JK**) y necesita **otro** comportamiento
(un **D**, o un **T**). No se tira el chip: se le pone **lógica combinacional en las entradas** para que "hable"
como el biestable que falta. Eso es convertir.

> [!important] Por qué en el final se pide con Karnaugh
> Porque el procedimiento es **siempre el mismo** y demuestra que sabés relacionar lo combinacional con lo
> secuencial: **tabla del biestable pedido → tabla de excitación → mapa de Karnaugh → función → compuertas**.
> Con ese método resolvés cualquier par (RS↔JK↔D↔T), no hace falta memorizar los 12 casos.

## Paso 0: las ecuaciones características (lo que cada biestable hace)
| Biestable | Ecuación característica | Tabla de transición | Observación |
|---|---|---|---|
| **RS** | `Q(t+1) = S + R̄·Q` | S=1 ⇒ Q=1 · R=1 ⇒ Q=0 · S=R=0 ⇒ mantiene | `S·R = 0` **prohibido** |
| **D** | `Q(t+1) = D` | copia la entrada | el más simple |
| **JK** | `Q(t+1) = J·Q̄ + K̄·Q` | J=1 ⇒ 1 · K=1 ⇒ 0 · 00 ⇒ mantiene · **11 ⇒ invierte** | resuelve el estado prohibido del RS |
| **T** | `Q(t+1) = T ⊕ Q` | T=1 ⇒ invierte · T=0 ⇒ mantiene | es un JK con `J = K = T` |

## Paso 1: la tabla de excitación (qué entrada necesito para cada transición)
Es la tabla "al revés": dado lo que quiero que pase (`Q → Q+`), qué tengo que poner en las entradas.

| Transición | **RS** | **JK** | **D** | **T** |
|---|---|---|---|---|
| **0 → 0** | S=0, R=X | J=0, K=X | D=0 | T=0 |
| **0 → 1** | S=1, R=0 | J=1, K=X | D=1 | T=1 |
| **1 → 0** | S=0, R=1 | J=X, K=1 | D=0 | T=1 |
| **1 → 1** | S=X, R=0 | J=X, K=0 | D=1 | T=0 |

`X` = no importa (don't care): se usa en el Karnaugh como casilla libre para agrandar los grupos.

## Caso A — de **RS a JK** (implementar un JK con un RS)
La pregunta del final: *"cómo pasar de un flip-flop RS a JK, con mapa de Karnaugh y función booleana"*.
Se quiere que el conjunto **RS + compuertas** se comporte como un JK.

### A.1 Tabla del comportamiento pedido (JK)
| J | K | Q | Q(t+1) | qué debe hacer el RS |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | mantener 0 |
| 0 | 0 | 1 | 1 | mantener 1 |
| 0 | 1 | 0 | 0 | mantener 0 |
| 0 | 1 | 1 | **0** | **resetear** ⇒ R = 1 |
| 1 | 0 | 0 | **1** | **setear** ⇒ S = 1 |
| 1 | 0 | 1 | 1 | mantener 1 |
| 1 | 1 | 0 | **1** | **setear** ⇒ S = 1 |
| 1 | 1 | 1 | **0** | **resetear** ⇒ R = 1 |

### A.2 Tabla de excitación: qué necesita el RS
Usando la tabla de excitación del RS sobre cada fila:

| J | K | Q | Q+ | **S** | **R** |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | X |
| 0 | 0 | 1 | 1 | X | 0 |
| 0 | 1 | 0 | 0 | 0 | X |
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | X | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |

### A.3 Mapa de Karnaugh de **S** (variables J, K en filas; Q en columnas)
| J K \ Q | **Q = 0** | **Q = 1** |
|---|---|---|
| **0 0** | 0 | X |
| **0 1** | 0 | 0 |
| **1 1** | **1** | 0 |
| **1 0** | **1** | X |

Agrupando las dos casillas de la columna `Q = 0` en las filas donde `J = 1` (y K es indiferente):
> **`S = J · Q̄`**

### A.4 Mapa de Karnaugh de **R**
| J K \ Q | **Q = 0** | **Q = 1** |
|---|---|---|
| **0 0** | X | 0 |
| **0 1** | X | **1** |
| **1 1** | 0 | **1** |
| **1 0** | 0 | 0 |

Agrupando las dos casillas de la columna `Q = 1` en las filas donde `K = 1`:
> **`R = K · Q`**

### A.5 El circuito y la verificación
```
        J ──┐
            AND ──► S ──┐
       Q̄ ──┘            │
                        ├──► biestable RS ──► Q
        K ──┐            │
            AND ──► R ──┘
        Q ──┘
```
Verificación rápida: `S` y `R` **nunca pueden ser 1 a la vez**, porque `S` necesita `Q = 0` y `R` necesita
`Q = 1`. Es decir: **la conversión elimina sola el estado prohibido del RS**. Y con `J = K = 1`:
- si `Q = 0` ⇒ `S = 1` ⇒ se setea (`0 → 1`)
- si `Q = 1` ⇒ `R = 1` ⇒ se resetea (`1 → 0`)
⇒ **invierte**, que es justo lo que hace el JK con 11.

## Caso B — de **JK a RS** (implementar un RS con un JK)
Al revés, y mucho más fácil: se mira la tabla de excitación del JK para las transiciones que pide el RS.

| S | R | Q → Q+ | **J** | **K** |
|---|---|---|---|---|
| 0 | 0 | mantiene | 0 | 0 |
| 1 | 0 | `Q+ = 1` | 1 | X |
| 0 | 1 | `Q+ = 0` | X | 1 |
| 1 | 1 | prohibido | X | X |

> **`J = S`** y **`K = R`** (y la combinación `1 1` queda como "no importa": el JK invierte, es lo que
> antes era el estado prohibido).

## Caso C — de **JK a D** (implementar un D con un JK)
El D tiene una sola entrada: se busca `D` en función de `J`, `K` y `Q` para que el JK produzca `Q+ = D`.
Como `D = Q(t+1)` y el JK cumple `Q(t+1) = J·Q̄ + K̄·Q`:

> **`D = J · Q̄ + K̄ · Q`**

Mapa de Karnaugh de `Q(t+1)` (es el mismo mapa, leído como si fuera D):

| J K \ Q | **Q = 0** | **Q = 1** |
|---|---|---|
| **0 0** | 0 | **1** |
| **0 1** | 0 | 0 |
| **1 1** | **1** | 0 |
| **1 0** | **1** | **1** |

Dos grupos: `J·Q̄` (columna Q=0, filas 11 y 10) y `K̄·Q` (columna Q=1, filas 00 y 10). Circuito: dos AND y una
OR a las entradas J y K.

## Caso D — de **D a JK** y de **T a JK** (los más fáciles)
| Conversión | Resultado | Por qué |
|---|---|---|
| **D → JK** | `J = D`, `K = D̄` | con J=1,K=0 se setea (D=1) y con J=0,K=1 se resetea (D=0): nunca se invierte |
| **T → JK** | `J = K = T` | `T·Q̄ + T̄·Q = T ⊕ Q` — la ecuación del T es la del JK con J=K |
| **JK → T** | `J = K = T` | lo mismo visto al revés |
| **RS → D** | `S = D`, `R = D̄` | D=1 ⇒ set, D=0 ⇒ reset (nunca 1-1) |
| **D → T** | `T = D ⊕ Q` | hay que invertir sólo si el dato es distinto del que ya tengo |
| **T → D** | `D = T ⊕ Q` | idem, la misma ecuación |

## Tabla resumen (la que conviene tener en la cabeza)
| Quiero… | …y tengo | Conexión |
|---|---|---|
| **JK** | RS | `S = J·Q̄` · `R = K·Q` |
| **RS** | JK | `J = S` · `K = R` |
| **D** | JK | `J = D` · `K = D̄` |
| **JK** | D | `J = D` · `K = D̄` + la ecuación `D = J·Q̄ + K̄·Q` si se pide el desarrollo |
| **T** | JK | `J = K = T` |
| **JK** | T | `J = K = T` |
| **D** | RS | `S = D` · `R = D̄` |
| **T** | D | `T = D ⊕ Q` |
| **RS** | D | `S = D` · `R = D̄` |

> [!tip] Regla mnemotécnica
> **"Para pedir un cambio uso Q, para no pedirlo uso Q̄."** `S = J·Q̄`: seteo cuando J lo pide **y todavía
> estoy en 0**. `R = K·Q`: reseteo cuando K lo pide **y ya estoy en 1**. Con eso se reconstruyen las dos
> fórmulas del caso A sin mirar el Karnaugh (y en el oral conviene igual dibujar el mapa, porque lo piden).

## Cómo se resuelve en el pizarrón (método en 5 pasos, sirve para cualquier par)
1. **Ecuación característica** del biestable que **quiero** (a la derecha de la tabla del Paso 0).
2. **Tabla de 8 filas** (entradas del que quiero + Q → Q+).
3. **Tabla de excitación** del biestable que **tengo**: para cada `Q → Q+`, qué entradas hay que poner.
4. **Karnaugh** de cada entrada del que tengo, con las `X` a favor.
5. **Función + circuito** (AND/OR/NOT o las compuertas que convengan) y **verificación** con una transición
   concreta, por ejemplo `J = K = 1`.

> [!example] Ejercicio del TP (resuelto en la bóveda)
> El [[TP8 Biestables RS|TP8]] pide el RS asincrónico y el sincrónico con su **circuito reducido**, y el
> [[TP9 Biestables D, JK y T|TP9]] el D, JK y T también reducidos. Reducir el circuito **es exactamente**
> aplicar estas conversiones: si un JK hecho con RS queda con `S = JQ̄` y `R = KQ`, se están usando 2
> compuertas en lugar de las 4 del circuito "de libro".

## Errores típicos
- Confundir **tabla del biestable** (qué hace) con **tabla de excitación** (qué entradas le doy para que
  haga eso): son inversas.
- Poner `S = J` y `R = K` para pasar de RS a JK: **está mal**, esa es la conversión al revés (de JK a RS).
  Con `S = J, R = K` aparecería el estado prohibido con `J = K = 1`.
- Olvidar las `X` en el Karnaugh y perder la simplificación (queda una función larga que igual funciona,
  pero no es la mínima y no es lo que se pide).
- Decir que el JK "no tiene estado prohibido": no lo tiene **de comportamiento** (con 11 invierte), pero sí
  hay que evitar `S = R = 1` si por dentro es un RS.

## Relacionado
[[Flip-Flops SR, D, JK y T]] · [[Mintérminos y maxtérminos]] · [[Álgebra de Boole — postulados y teoremas]] ·
[[Registros]] · [[Contadores]] · [[Cómo dibujar los circuitos (checklist de pizarrón)]]
