---
unidad: 5
tipo: concepto
examen: principal
prioridad: maxima
---
# Ciclo de LDA indexada (los 24 pulsos)

> [!important] Qué necesitás para responder esta pregunta
> **En `Apoyo a la pregunta/`:** [[Ciclo de la instrucción LDA (24 pulsos)]]
> **En otra tanda o unidad:** [[Ciclo de búsqueda (7 y 8 pulsos)]] (Tanda 1 · 1.8 Ciclo de máquina y ciclo de instrucción) · [[Ciclo de máquina]] (Tanda 1 · 1.8 Ciclo de máquina y ciclo de instrucción) · [[BLUE indexada (RIF, RID, nuevo formato)]] (Tanda 1 · 1.2 BLUE vs BLUE indexada) · [[Sumador completo]] (Tanda 3 · 3.8 Sumadores) · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] (Tanda 2 · 2.5 Las 16 instrucciones, pulso por pulso)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 1.3 LDA indexada (24 pulsos)]].


> [!abstract] En una frase
> La `LDA 3, X` (cargar por índice RID) tarda **3 ciclos de máquina de 8 pulsos = 24 pulsos**:
> **8 de búsqueda** (traer la primera palabra de la instrucción), **8 de cálculo de la dirección efectiva**
> (traer el campo de dirección y sumarle el registro índice con el sumador de direcciones) y
> **8 de ejecución** (ir a buscar el dato y cargarlo en el acumulador).

## Partamos de cero: qué es un pulso y qué es un ciclo de máquina

**Reloj.** La BLUE es una máquina **sincrónica**: todo lo que pasa, pasa "a destiempo de un reloj". El reloj
genera pulsos iguales, y en cada pulso ocurre **una sola cosa** (una transferencia entre dos registros, o
una orden a la memoria).

**Ciclo menor = 1 pulso.** En la BLUE cada pulso dura 125 ns.

**Ciclo de máquina = 8 pulsos** (CP1 … CP8). Es la unidad de trabajo: la máquina hace un ciclo de **búsqueda**
o un ciclo de **ejecución**. ¿Por qué 8 y no 7? Porque la memoria original de núcleos de ferrita necesitaba un
pulso extra para **reescribir** el dato leído; con memorias de semiconductores los 7 primeros alcanzan y el 8.º
queda libre para adelantar ejecución. (Esa es exactamente la pregunta "7 y 8 pulsos":
[[Ciclo de búsqueda (7 y 8 pulsos)]]).

**Por qué 24 y no 16.** En la BLUE original la instrucción mide **16 bits = 1 palabra**, así que la búsqueda la
trae completa y alcanza con búsqueda + ejecución = 2 ciclos = 16 pulsos. En la **BLUE indexada** la instrucción
mide **32 bits = 2 palabras** (5 de opcode + 2 de modificador + 9 sin uso + 16 de dirección), y la memoria
entrega **una palabra por ciclo**. Entonces hace falta **un ciclo más** para traer el campo de dirección y
calcular la dirección efectiva. Tres ciclos: **8 + 8 + 8 = 24**.

> [!important] Si te piden "el ciclo de LDA de la BLUE indexada con esquema y los 24 pulsos"
> Hay que entregar **tres tablas de 8 pulsos** (búsqueda, ejecución 1, ejecución 2), decir qué registro se
> carga en cada CP, y aclarar cuántos ciclos de memoria hay (3) y por qué (instrucción de 2 palabras).

## Antes de empezar: qué significa cada microorden
| Microorden | Qué hace |
|---|---|
| **Envíe PC / Cargue MAR / Cargue Z** | el PC pone la dirección en el bus; el MAR la guarda; el registro Z (entrada de la ALU) también la copia |
| **Orden de lectura / escritura** | señal de control a la memoria |
| **Envíe 1 / Cargue Y** | se pone un 1 en Y para que la ALU pueda sumar |
| **Envíe SUMA / Cargue PC** | la ALU entrega `Z + Y` y el PC se incrementa en 1 |
| **Envíe MBR / Cargue IR** | la instrucción pasa del buffer de memoria (MBR) al registro de instrucción (IR) |
| **Envíe RID / Cargue X** | el registro índice va a la entrada X del **sumador de direcciones** |
| **Envíe MBR / Cargue W** | el campo de dirección leído de memoria va a la entrada W del **sumador de direcciones** |
| **Envíe Σ / Cargue MAR** | el sumador de direcciones entrega `W + X` (la dirección efectiva) y se carga en el MAR |
| **Envíe MBR / Cargue Acc** | el dato leído de memoria entra al acumulador |
| **Pasar a Ejecución / Seguir en Ejecución / Estado Búsqueda** | se cambia el biestable STATE (F ↔ E) |

## Ciclo 1 — BÚSQUEDA (pulsos 1 a 8)
Trae la **primera palabra** de la instrucción y deja el PC apuntando a la palabra siguiente.

| Pulso | Acción |
|---|---|
| **CP1** | Envíe PC, Cargue MAR, Cargue Z, **Orden de lectura** |
| **CP2** | Envíe 1, Cargue Y |
| **CP3** | — (la memoria y la ALU trabajan) |
| **CP4** | Envíe SUMA, Cargue PC |
| **CP5** | — (se espera el dato de memoria) |
| **CP6** | Envíe MBR, Cargue IR |
| **CP7** | — (decodificación) |
| **CP8** | **Pasar a Ejecución** |

## Ciclo 2 — EJECUCIÓN 1 (pulsos 9 a 16): traer el campo de dirección y calcular la EA
| Pulso | Acción |
|---|---|
| **CP1** | Envíe PC, Cargue MAR, Cargue Z, **Orden de lectura** ← se lee la **segunda palabra** |
| **CP2** | Envíe 1, Cargue Y |
| **CP3** | — |
| **CP4** | Envíe SUMA, Cargue PC ← el PC ya apunta a la próxima instrucción |
| **CP5** | **Envíe RID, Cargue X** ← el índice entra al sumador de direcciones |
| **CP6** | **Envíe MBR, Cargue W** ← el campo de dirección (leído) entra al sumador |
| **CP7** | — (el sumador Σ estabiliza: `EA = W + X`) |
| **CP8** | **Seguir en Ejecución** |

## Ciclo 3 — EJECUCIÓN 2 (pulsos 17 a 24): ir al operando y cargarlo
| Pulso | Acción |
|---|---|
| **CP1** | **Envíe Σ, Cargue MAR, Orden de lectura** ← se direcciona la dirección efectiva |
| **CP2** | — |
| **CP3** | — |
| **CP4** | — |
| **CP5** | — (se espera la memoria) |
| **CP6** | **Envíe MBR, Cargue Acc** ← el dato entra al acumulador |
| **CP7** | — |
| **CP8** | **Estado Búsqueda** (termina la instrucción) |

![Ciclo de 24 pulsos de la LDA indexada](../../../assets/lda24_pulsos.svg)

## Los cuatro modos de la LDA y cuántos pulsos cuesta cada uno
| Instrucción | Modo | Qué hace | Ciclos | Pulsos | Diferencia en el ciclo |
|---|---|---|---|---|---|
| `LDA 0, X` | directo | `AC ← M[X]` | 3 | **24** | en CP5 se carga **0** en X (el índice no participa) |
| `LDA 1, X` | indirecto | `AC ← M[M[X]]` | **4** | **32** | un ciclo extra: se necesita leer el puntero y después el dato |
| `LDA 2, X` | indexado RIF | `AC ← M[X + RIF]` | 3 | **24** | en CP5 se carga **RIF** en X |
| `LDA 3, X` | indexado RID | `AC ← M[X + RID]` | 3 | **24** | en CP5 se carga **RID** en X |

> [!tip] Lo que hay que tener claro para el oral
> El **directo** y los **dos indexados** cuestan lo mismo (24) porque en los tres hay que traer el campo de
> dirección de la segunda palabra y calcular una suma: `X + 0`, `X + RIF` o `X + RID`. **Sólo el indirecto**
> cuesta un ciclo más (32), porque hay que ir a memoria **dos veces**: una para leer la dirección del operando
> y otra para leer el operando.

## Esquema de la máquina para acompañar el dibujo
```
                    ┌──────────────── Memoria (65 536 × 16) ────────────────┐
                    └───────────────────────┬──────────────────────────────┘
                                            │  (lectura / escritura)
        ┌──────────┐   ┌──────────┐   ┌─────┴─────┐
        │   MAR    │   │   MBR    │   │  BUS      │
        └────▲─────┘   └────┬─────┘   └───────────┘
             │              │
      ┌──────┴──────┐  ┌────▼─────┐        ┌───────────────┐
      │ Sumador de  │  │    IR    │───────►│ decodificador │
      │ direcciones │  └──────────┘        │ de instrucción│
      │    ( Σ )    │                      │ + modificador │
      └──▲───────▲──┘                      └───────┬───────┘
         │       │                                 │
      ┌──┴──┐ ┌──┴──┐                        ┌─────▼──────┐
      │  W  │ │  X  │                        │ Unidad de  │
      └─────┘ └─────┘                        │  Control   │
     (campo)  (RID)                          └────────────┘
```

## Cómo responderlo en el final (4 minutos)
1. **Encuadre**: "la LDA indexada es la instrucción de carga con `EA = campo de dirección + RID`; en la BLUE
   indexada la instrucción ocupa **dos palabras**, así que el ciclo tiene **3 ciclos de máquina**".
2. **Dibujo**: la máquina con el sumador de direcciones y, arriba, la línea de tiempo dividida en 3 bloques
   de 8 pulsos (24 casillas). Marcar los 4 pulsos "clave": CP1/CP6 de búsqueda, CP5-CP6 de ejecución 1
   (carga de X y W) y CP1/CP6 de ejecución 2.
3. **Las tres tablas**, leyéndolas como una historia: *"busco la instrucción… busco el campo de dirección y
   sumo el índice… voy al operando y lo cargo"*.
4. **Cierre con el contraste**: "el directo también son 24; el indirecto 32 porque va dos veces a memoria".

## Errores típicos
- Contar **24 pulsos** pero decir **2 ciclos de máquina** (son 3).
- Poner la suma del índice en el ciclo de búsqueda: la suma es **ejecución 1** (CP5-CP6), no búsqueda.
- Olvidar el **segundo incremento del PC** (ejecución 1, CP4): si no, la próxima instrucción se leería en la
  segunda palabra de ésta.
- Confundir **MBR → IR** (búsqueda, CP6) con **MBR → W** (ejecución 1, CP6). Mismo origen, distinto destino.
- Decir que el registro base aparece en el ciclo: el RB se suma **además**, siempre, en toda referencia a
  memoria; en el gráfico de la cátedra no se dibuja en el ciclo para no complicarlo (ver
  [[Registros base e índice]]).

## Para ampliar: qué leer y qué buscar
| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 5* | sección **"Ciclos de instrucción"** de la BLUE indexada — las tablas de **`LDA 3, X`**, `LDA 1, X`, `LDA 0, X`, `INI` y `ENI` | las tres tablas de 8 pulsos con la columna **Acción** (Envíe/Cargue) tal como se copian en el pizarrón | **Es la fuente exacta**: esta nota es la transcripción comentada de esas tablas |
| **`blue.pdf`** (Foster) | **Tabla 2** (ciclo de búsqueda) y **Tabla 5** (LDA/STA de dos ciclos) | la base de 1 ciclo de búsqueda + 1 de ejecución, con la misma notación | De ahí sale la mitad del ciclo; después la indexada agrega el ciclo de la EA |
| **Apuntes de cátedra**, *Unidad 5*, comentarios finales | las 3 notas al pie de los ciclos ("1 a 4 ciclos según instrucción y modo", "la indexada no tiene formato fijo") | la explicación de por qué hay instrucciones de 1 a 4 ciclos | Para cerrar la respuesta con la generalización |
| **[[TP18 Direccionamiento de memoria]]** | el TP | los cálculos de memoria y direcciones | Complemento del "por qué 16 bits de dirección y 65 536 celdas" |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **microoperaciones** | cómo se escriben las microoperaciones por paso de reloj (`T0, T1…`) | Para poder pasar de "CP1…CP8" a la notación formal sin trabarte |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo del **procesador multiciclo** | por qué una instrucción que necesita dos accesos a memoria cuesta más ciclos | Entender el paralelo: `lw` en MIPS también usa varios ciclos |
| **[[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]** | la nota de la bóveda | las tablas de las otras instrucciones | Para responder si te piden comparar con LDA/STA/ADD |

## Relacionado
[[BLUE vs BLUE indexada — qué cambia y por qué]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] ·
[[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de la instrucción LDA (24 pulsos)]] ·
[[Modos de direccionamiento]] · [[Registros base e índice]] · [[Cómo dibujar los circuitos (checklist de pizarrón)]]
