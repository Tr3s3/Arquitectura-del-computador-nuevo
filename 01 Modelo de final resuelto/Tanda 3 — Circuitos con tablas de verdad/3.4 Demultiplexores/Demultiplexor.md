---
unidad: 2
tipo: concepto
examen: practica
prioridad: maxima
---
# Demultiplexor (DEMUX)

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[Decodificador]] (Tanda 3 · 3.1 Decodificadores) · [[Compuertas lógicas]] (Tanda 3 · 3.0 Herramientas (Karnaugh y compuertas)) · [[Memoria RAM 8x3]] (Tanda 1 · 1.4 Memoria RAM 8x3)
> El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 3.4 Demultiplexores]].


> [!abstract] En una frase
> Un **demultiplexor de 1 a 2ⁿ** recibe **un dato** y **n líneas de selección**, y **envía el dato a una sola**
> de sus **2ⁿ salidas** (las demás quedan en 0): `Yi = D · mi`. Es, literalmente, **un decodificador con el dato
> como habilitación**.

> [!note] Si es la primera vez que ves esto
> Es la **cañería con una llave de derivación**: entra agua por un caño (el dato) y, según cómo gires la palanca
> (la selección), el agua sale por **una** de las cuatro bocas; las otras tres quedan secas.
>
> Es el **repartidor** del sistema: el dato llega a la entrada y el DEMUX decide **a qué destino va**. En un bus,
> el MUX elige **quién habla** y el DEMUX (o el decodificador de escritura) decide **quién escucha**. Juntos son
> el modelo del **bus común** de la BLUE. Y tiene un uso muy concreto en memoria: escribir en **una** celda o en
> **un chip** de los varios que comparten el bus de datos.

---

## 1. Demultiplexor 1 → 2 (el mínimo)

| D | S | Y0 | Y1 |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | **1** | 0 |
| 1 | 1 | 0 | **1** |

**Funciones:** `Y0 = D · S'`  ·  `Y1 = D · S`
**Circuito:** 1 NOT (para `S'`) + 2 AND de 2 entradas.

---

## 2. Demultiplexor 1 → 4 (el que se dibuja)

| D | S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|---|
| **0** | X | X | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | **1** | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | **1** | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | **1** | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | **1** |

**Funciones:**
```
   Y0 = D · S1'·S0'      Y1 = D · S1'·S0      Y2 = D · S1·S0'      Y3 = D · S1·S0
       └── dato ──┘└─ mintérmino de la selección ─┘
```
O sea: **`Yi = D · mi`** — el dato multiplicado por el mintérmino de la selección.

**Circuito: 2 inversores + 4 AND de 3 entradas** (las 2 selecciones + el dato). ¡Idéntico al decodificador 2→4,
con el dato agregado a cada AND!

![Demultiplexor 1 a 4](../../../assets/demux_1x4.svg)

> [!important] La relación que hay que decir
> **DEMUX = decodificador con EN = dato.** Si al 74LS138 (decodificador 3→8) le conectás el dato en la entrada
> de *enable*, obtenés un demultiplexor 1→8. Por eso en los apuntes y en los TPs los dos bloques aparecen juntos:
> **es el mismo circuito visto de dos maneras**.

---

## 3. La tabla en palabras (para no confundirse nunca)

| Si… | …entonces |
|---|---|
| `D = 0` | **todas** las salidas en 0 (no hay nada que repartir) |
| `D = 1` | la salida elegida se pone en **1** y las demás en 0 ⇒ **se comporta como un decodificador** |
| Cambia la selección | se **mueve** el dato de salida (eso es lo que lo hace útil para "rutear") |

---

## 4. Expansión y variantes

| Caso | Cómo se arma |
|---|---|
| **1 → 8** | tres líneas de selección + 8 AND de 4 entradas (3 selecciones + D) |
| **1 → 16 con dos 1 → 8** | el bit de mayor peso habilita uno de los dos DEMUX (con su EN) |
| **DEMUX con EN** | si `EN = 0`, todas las salidas en 0: es lo que permite usarlo como "escritura habilitada" |
| **Salidas activas bajas** | en chips reales lo seleccionado va a **0**; en el pizarrón conviene aclarar la convención |

---

## 5. Aplicaciones (las que se nombran)

| Uso | Cómo |
|---|---|
| **Repartir datos en un bus** | el MUX elige la fuente y el DEMUX el destino ⇒ bus **unidireccional** completo |
| **Escritura selectiva en memoria** | el dato va al chip/banco que habilita el decodificador-demux: **`Write` + selección** |
| **Selección de registro destino** | la UC manda el dato al registro cuyo `LOAD` activa el decodificador |
| **Reparto de pulsos de reloj** | enviar el pulso a una etapa por vez (en la BLUE, cada pulso habilita etapas distintas) |
| **Serial → paralelo** | el mismo dato entra y se va depositando en distintas salidas (el inverso de multiplexar) |

> [!example] En la BLUE, con nombres propios
> En CP1 se activa `PC → MAR` y `Read`; en CP5, `strobe MBR`; en CP8, `E → State`. Ese "dirigir el dato a un
> destino distinto en cada pulso" es exactamente lo que hace un **demultiplexor**, aunque en el circuito se
> implemente con **buffers de 3 estados + decodificador**. Ver
> [[Flujo de información en BLUE (datos y direcciones)]] y [[Cómo se implementa la Unidad de Control]].

---

## 6. Decodificador vs demultiplexor (la pregunta trampa)

| | **Decodificador** | **Demultiplexor** |
|---|---|---|
| Entradas | **n** (sólo selección) | **n + 1** (selección **y** dato) |
| Salidas | 2ⁿ | 2ⁿ |
| Salida activa | **una**, siempre en 1 (si EN = 1) | **una**, y **copia el dato** |
| Función | `Yi = mi` | `Yi = D · mi` |
| Relación | — | **es un decodificador con el dato en EN** |
| Uso | **seleccionar** (leer) | **repartir / escribir** |

**Frase para el oral:** "el decodificador dice **dónde**; el demultiplexor dice dónde **y le manda el dato**".

---

## 7. Cómo responderlo en el final (3 minutos)

**Movimiento 1 — definición (20 s).** "Un dato, n selecciones, 2ⁿ salidas; el dato va a una sola salida."

**Movimiento 2 — tabla y funciones (60 s).** Tabla del **1→4** (filtrando por `D`) y las cuatro funciones
`Yi = D·S1'·S0'`, etc.

**Movimiento 3 — el circuito y la clave (60 s).** 2 inversores + 4 AND de 3 entradas, y la frase que lo cierra:
**"es un decodificador con EN = dato"**.

**Movimiento 4 — comparación (40 s).** Cuadro decodificador / MUX / DEMUX: señala, elige, reparte.

**Movimiento 5 — cierre (20 s).** "Se usa para **rutear**: elegir el chip de memoria a escribir, el registro
destino, o repartir el dato por el bus."

### Repreguntas típicas
| Repregunta | Respuesta corta |
|---|---|
| ¿Cuántas entradas de selección para 8 salidas? | **3** |
| ¿Qué pasa si D = 0? | Todas las salidas en **0** |
| ¿En qué se diferencia del decodificador? | En que **además del dato**: `Yi = D·mi` en lugar de `Yi = mi` |
| ¿Se puede hacer un DEMUX con un decodificador? | **Sí**: el dato entra por el `EN` |
| ¿Y un decodificador con un DEMUX? | Sí, con `D = 1` fijo |
| ¿Diferencia con el MUX? | El MUX **concentra** (muchos→uno); el DEMUX **reparte** (uno→muchos) |
| ¿Dónde aparece en la materia? | En el **bus** y en la **escritura selectiva** de memoria/registros |

---

## 8. Errores típicos
- Confundir **demultiplexor** con **decodificador** (el DEMUX tiene el dato; el decodificador no).
- Decir que reparte el dato a **varias** salidas a la vez (a **una** sola; las demás en 0).
- Poner el dato como **entrada de selección**: el dato va **en serie con todos los AND**.
- Confundir el sentido: **MUX = muchos a uno**, **DEMUX = uno a muchos**.
- Olvidar el `EN` cuando se compara con el chip comercial.

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 2* | sección de **demultiplexores** (junto a decodificadores) | la tabla del 1→4 y las funciones `Yi = D·mi` | **Es la fuente exacta** |
| **[[TP6 Decodificadores y demultiplexores]]** | el TP | los circuitos y la comparación pedida | Lo que se entrega |
| **Floyd, *Fundamentos de sistemas digitales*** | capítulo de **funciones combinacionales** | demultiplexor, uso del 74LS138 como DEMUX | **La mejor ampliación** |
| **Mano, *Lógica digital y diseño de computadoras*** | capítulo de **circuitos combinacionales** | decodificador/demultiplexor y aplicaciones en memoria | Formalización |
| **[[Decodificador]]** · **[[Multiplexor]]** · **[[Codificador]]** | notas de la bóveda | los otros tres bloques | Estudiarlos juntos |
| **[[Flujo de información en BLUE (datos y direcciones)]]** · **[[Memoria RAM 8x3]]** | notas de la bóveda | el bus como MUX + DEMUX y el `Write` selectivo | La aplicación real |

---

## Relacionado
[[Decodificador]] · [[Multiplexor]] · [[Codificador]] · [[Compuertas lógicas]] · [[Memoria RAM 8x3]] ·
[[Flujo de información en BLUE (datos y direcciones)]]
