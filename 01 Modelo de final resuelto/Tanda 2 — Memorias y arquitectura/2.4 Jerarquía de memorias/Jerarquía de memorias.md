---
unidad: 3
tipo: concepto
examen: secundario
prioridad: maxima
---
# Jerarquía de memorias

> [!important] Qué necesitás para responder esta pregunta
> **En otra tanda o unidad:** [[Memoria caché]] (Tanda 2 · 2.3 Memoria caché) · [[Memoria RAM 8x3]] (Tanda 1 · 1.4 Memoria RAM 8x3) · [[Memoria virtual y administración de memoria]] (Materia · Unidad 2) · [[Memoria auxiliar y memoria asociativa]] (Materia · Unidad 2) El detalle de **para qué sirve cada apoyo** está en [[00 Apoyos — 2.4 Jerarquía de memorias]].

> [!abstract] En una frase
> La **jerarquía de memoria** es la organización en **pisos** de las memorias de un computador: **registros → L1 → L2/L3 → RAM → disco/SSD → cinta**, donde **arriba** hay poca capacidad, altísima velocidad y altísimo costo por bit, y **abajo** mucha capacidad, baja velocidad y bajo costo. Funciona porque los programas tienen **localidad**, y el objetivo es que el **tiempo promedio** se parezca al de arriba y el **costo** al de abajo.

> [!note] Si es la primera vez que ves esto
> Hay un triángulo imposible: queremos memorias **grandes** (para guardar mucho), **rápidas** (para no esperar) y **baratas**. Ninguna tecnología es las tres. La solución es usar **varias a la vez, ordenadas**: la heladera chica de la cocina (rápida, chica) y el depósito del fondo (lento, enorme). El sistema funciona porque **casi siempre** lo que necesitás está en la heladera. Ese "casi siempre" tiene un nombre técnico: **localidad**, y es lo que hace que la informática sea posible.

---

## 1. La pirámide

![Jerarquía de memorias](../../../assets/jerarquia_memorias.svg)

| Nivel | Tecnología | Tiempo típico | Quién lo administra |
|---|---|---|---|
| **Registros** | biestables dentro de la CPU | < 1 ns | el **programa** (el compilador asigna registros) |
| **Caché L1** | SRAM | 1–2 ns | el **hardware** (invisible al programa) |
| **Caché L2/L3** | SRAM | 5–20 ns | el **hardware** |
| **RAM** | DRAM | 50–100 ns | el **sistema operativo** (paginación) |
| **Disco/SSD** | magnético / flash | µs–ms | el **SO** (memoria virtual y archivos) |
| **Cinta / respaldo** | magnético secuencial | segundos | el **operador** (backup) |

> [!important] Las dos reglas de la pirámide
> 1. **Cuanto más arriba, más rápido y más caro por bit** (y más chico).
> 2. **Cada nivel es la "caché" del nivel de abajo**: guarda una copia de lo que se usa más, para que el de abajo
>    se consulte poco.

---

## 2. Por qué funciona: la localidad (otra vez)

| Localidad | Qué dice | Consecuencia |
|---|---|---|
| **Temporal** | lo que se usó se vuelve a usar pronto | los lazos y las variables calientes se quedan arriba |
| **Espacial** | lo vecino se usa pronto | se traen **bloques** (líneas de caché, páginas) y no datos sueltos |

Sin localidad, la jerarquía **no serviría**: cada acceso iría al nivel de abajo y el promedio sería el del disco. Con localidad, el 90–99 % de los accesos se resuelven arriba.

---

## 3. La cuenta que hay que saber hacer (AMAT)

```
   tiempo promedio = t(nivel superior) + tasa de fallo × penalidad
```
**Ejemplo con las tres capas** (L1 = 1 ns, RAM = 100 ns, disco = 10 ms):
```
  Solo RAM:      100 ns
  Con L1 al 95 %:  1 + 0,05 × 100 = 6 ns
  Con L1 (95 %) y L2 (del 5 % que falla, el 80 % acierta en L2 a 20 ns):
                  1 + 0,05 × (20 + 0,20 × 100) = 1 + 0,05 × 40 = 3 ns
```
Cada piso que se agrega mejora el promedio, siempre que la **tasa de acierto sea alta**. Si la tasa de acierto fuera baja, agregar niveles **no sirve** (y además cuesta).

---

## 4. Los saltos entre niveles: quién decide qué

| Salto | Qué se mueve | Quién lo hace | Tamaño del bloque |
|---|---|---|---|
| Registros ↔ L1 | palabras | el **hardware** (el compilador ya decidió qué va a registros) | 1 palabra |
| L1 ↔ L2/L3 ↔ RAM | **líneas / bloques** | el **hardware** (control de caché) | 16–64 bytes |
| RAM ↔ disco | **páginas** | el **SO** (memoria virtual) | 4 KB típico |
| Disco ↔ cinta | archivos / imágenes | el **operador** | lo que se respalde |

> [!tip] La idea que une todo (y que impresiona en el oral)
> **Es el mismo mecanismo repetido tres veces**: guardar arriba lo que se usa, traer de a bloques y reemplazar lo que no se usa. Cambia el **tamaño del bloque** (palabra, línea, página), **quién lo administra** (compilador, hardware, SO) y **qué pasa si falta** (esperar unos ns, decenas de ns, o milisegundos).

---

## 5. Ejemplo resuelto: por qué se nota en la práctica

Programa que suma un arreglo de 1 000 000 de enteros (4 MB):

- **Sin caché**: cada acceso cuesta ~100 ns ⇒ 100 000 000 ns ≈ **0,1 s** sólo en esperas de memoria.

- **Con caché** (localidad espacial: los 4 MB se recorren en orden, 64 bytes por línea ⇒ 16 enteros por línea, y la línea se trae una vez): ~1 acceso a RAM cada 16 elementos ⇒ ~6 ns promedio ⇒ **0,006 s**.

- **Diferencia**: ~**16 veces** más rápido, sin cambiar una línea de código. Eso es la jerarquía.

---

## 6. Lo que se pregunta junto con esto

| Tema | Dónde está en la bóveda |
|---|---|
| cómo funciona la caché por dentro (mapeos, políticas) | [[Memoria caché]] |
| el nivel "disco" (memoria virtual, paginación, TLB) | [[Memoria virtual y administración de memoria]] |
| memorias asociativas (comparación en paralelo, usadas en caché y TLB) | [[Memoria auxiliar y memoria asociativa]] |
| SRAM vs DRAM y celdas | [[Celda elemental de memoria]] · [[Memoria RAM 8x3]] |
| por qué esto mejora el rendimiento junto con el pipeline | [[Técnicas para aumentar la velocidad]] · [[Pipeline]] |

---

## 7. Cómo responderlo en el final (3 minutos)

**Movimiento 1 — definición (20 s).** "Es la organización de las memorias en niveles: registros, caché, RAM, disco y respaldo, de más rápida y cara a más lenta y barata."

**Movimiento 2 — la pirámide dibujada (40 s).** Con los cinco niveles, poniendo al costado **tiempo** y **capacidad**.

**Movimiento 3 — el porqué (40 s).** **Localidad temporal y espacial**; y que cada nivel es la caché del de abajo.

**Movimiento 4 — la cuenta (40 s).** `1 + 0,05 × 100 = 6 ns`: el promedio se acerca al de arriba. Mencionar que cada salto lo administra alguien distinto (compilador, hardware, SO).

**Movimiento 5 — cierre (20 s).** "El objetivo de la jerarquía no es que todo sea rápido, sino que el **tiempo promedio** se parezca al nivel de arriba con el **costo** del de abajo."

### Repreguntas típicas

| Repregunta | Respuesta corta |
|---|---|
| ¿Por qué no todo es SRAM? | Porque es **carísima** y ocupa mucho lugar por bit: 1 GB de SRAM costaría una fortuna |
| ¿Por qué no todo es disco? | Porque es **lentísimo** (milisegundos contra nanosegundos) |
| ¿Quién administra cada nivel? | Registros: el **programa** · caché: el **hardware** · RAM-disco: el **SO** |
| ¿Qué pasa si un programa no tiene localidad? | La jerarquía **no ayuda**: el rendimiento cae al del nivel más bajo |
| ¿La memoria virtual es parte de la jerarquía? | **Sí**: es el nivel RAM-disco, y usa el mismo principio con **páginas** |
| ¿Qué es un fallo de caché y qué es un fallo de página? | Lo mismo a distinta escala: no está arriba ⇒ hay que traerlo de abajo |
| ¿Dónde entra el TLB? | En la traducción de direcciones de la memoria virtual: es una **caché de la tabla de páginas** |

---

## 8. Errores típicos

- Poner el **disco** arriba de la RAM (¡la pirámide está al revés en la cabeza de muchos!).

- Decir que la jerarquía "hace que la memoria sea más rápida": hace que el **promedio** sea mejor.

- Olvidar que los **registros** son el primer nivel (y el más rápido).

- Confundir **capacidad** con **velocidad**: crecen en sentidos opuestos.

- Decir que la memoria virtual "es otra memoria física": es un **mecanismo** que usa el disco como si fuera memoria.

---

## 9. Para ampliar: qué leer y qué buscar

| Fuente | Dónde | Qué buscar | Para qué te sirve |
|---|---|---|---|
| **Apuntes de cátedra**, *Unidad 3 — Memorias electrónicas* | comienzo de la unidad (parámetros de las memorias) y la sección de **jerarquía** | la pirámide y las propiedades que enuncia la cátedra | **Es la fuente exacta** de esta pregunta |
| **`memorias.pdf`** | transparencias iniciales: **tipología** y **jerarquía de memoria en un ordenador** | la figura de la pirámide con "capacidad creciente / coste creciente" | La imagen que conviene copiar en el pizarrón |
| **[[TP12 Memoria principal]]** | el TP | las características de cada tipo y el cuadro RAM/ROM | Lo que se entrega |
| **Patterson & Hennessy, *Estructura y diseño de computadores*** | capítulo de **jerarquía de memoria** (y el de **almacenamiento**) | AMAT, localidad, los cinco niveles, y por qué el rendimiento depende de la memoria | **La mejor ampliación**: el tema central del capítulo |
| **Stallings, *Organización y arquitectura de computadores*** | capítulos de **memoria interna** y **memoria externa** | jerarquía, caché, memoria virtual, disco | Cobertura completa y ordenada |
| **Hamacher, Vranesic, Zaky, *Organización de computadoras*** | capítulo de **jerarquía de memoria** | los mismos conceptos con notación formal | Para profundizar |
| **Tanenbaum, *Estructura de computadores*** | capítulo de **memoria** | la jerarquía y la memoria virtual explicadas con analogías | Muy claro para entender rápido |
| **[[Memoria caché]]** · **[[Memoria virtual y administración de memoria]]** | notas de la bóveda | los dos niveles que más se preguntan | Desarrollo de cada piso |
| **[[Técnicas para aumentar la velocidad]]** | nota de la bóveda | cómo la jerarquía se combina con pipeline y paralelismo | Para el cierre "las tres palancas del rendimiento" |

---

## Relacionado
[[Memoria caché]] · [[Memoria virtual y administración de memoria]] · [[Memoria auxiliar y memoria asociativa]] · [[Celda elemental de memoria]] · [[Memoria RAM 8x3]] · [[Memoria ROM y sus tipos]] · [[Técnicas para aumentar la velocidad]]
