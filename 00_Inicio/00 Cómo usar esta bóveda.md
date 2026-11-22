---
tipo: guia
---
# Cómo usar esta bóveda

> [!abstract] Idea general
> La bóveda no es un resumen del libro: está construida **desde las preguntas del final**.
> Cada pregunta del modelo tiene (1) una nota de concepto que la explica desde cero, con
> gráficos, y (2) un guion para responderla oralmente. Estudiás por concepto, pero rendís por pregunta.

## Los cuatro recorridos

| Si estás… | Empezá por | Después |
|---|---|---|
| **Sin base**, primera lectura | [[01 Mapa de la materia (MOC)]] → notas de las Unidades 1 y 2 | [[03 Ruta de estudio para el final]] |
| **Con poco tiempo** (1 semana) | [[03 Ruta de estudio para el final]] | [[Banco de preguntas del final]] |
| **Repasando** (2 días antes) | [[04 Resumen integrador de la materia]] | [[Guion de respuestas — preguntas principales]] |
| **El día antes, oral** | [[Guion de respuestas — preguntas principales]] + [[Cómo dibujar los circuitos (checklist de pizarrón)]] | [[Tablas de verdad de memoria]] · [[Autoevaluación]] |

> [!important] El final es oral, y en la práctica se aprueba **dibujando**
> La mesa pide **circuitos en el pizarrón y la explicación de sus tablas de verdad**. Por eso cada nota
> termina con un *cómo responderlo en el final* que es un **guion hablado**, y los diagramas están
> pensados para **reproducirse a mano** en 2 o 3 minutos. No estudies leyendo: estudiá hablando y dibujando.

## Los dos bloques (así está organizada la bóveda)

> [!important] La bóveda tiene **dos bloques de desarrollo** y dos carpetas de apoyo
> Cada nota vive en **un solo** bloque, en el lugar donde más se usa, pero **se llega a ella desde los dos**.

| Bloque | Qué contiene | Puerta de entrada |
|---|---|---|
| **`10_Examen_Final/`** — *desarrollo del modelo de final* | las **27 preguntas de las 3 tandas** de la matriz, cada una como respuesta oral (tabla + dibujo + guion + repreguntas + "qué leer"), y las **guías** (matriz, chequeo de los 12 temas, fuentes, banco, guion) | [[00 Índice — bloque examen (las 3 tandas)]] |
| **`20_Programa_Materia/`** — *desarrollo del programa* | la materia **completa, unidad por unidad** (las 10 unidades), con las notas que el final **no** pregunta (memoria virtual, contadores, registros, ALU, paralelismo, 8086, microprogramación) y el **mapa que conecta todo**, incluidas las notas del otro bloque | [[00 Índice — bloque programa (las 10 unidades)]] |

| Carpeta de apoyo | Qué contiene |
|---|---|
| **`00_Inicio/`** | portada, mapa (MOC), plan de las 10 unidades, ruta para el final, resumen integrador, fuentes y glosario |
| **`01_Material_Catedra/`** | los **21 TPs** con la consigna textual, qué hay que saber y la respuesta sintetizada: **es la voz del profesor** (si hay diferencias de notación, manda el TP, y la bóveda lo advierte con un `[!warning]`) |
| **`30_Practica/`** | prácticas resueltas, checklist de dibujo, tablas de verdad de memoria y autoevaluación |

**Cómo elegir el bloque:** si te falta poco para el final ⇒ entrá por el bloque **examen** y estudiá por tandas.
Si estás cursando o querés entender la materia entera ⇒ entrá por el bloque **programa** y seguí las unidades.

Empezá por el [[00 Índice de TPs y qué aporta cada uno|índice de TPs]] si querés ver de un saque qué pide
la cátedra, y por [[04 Resumen integrador de la materia]] si querés el recorrido completo en 20 minutos.

## Cada nota maestra tiene material de consulta
Las notas de las **preguntas principales** terminan con una sección **"Para ampliar: qué leer y qué buscar"**:
una tabla con la fuente (cátedra y libros), **en qué parte** y **qué mirar**. Todo junto está en
[[01 Qué leer para cada pregunta principal]], con la bibliografía comentada (qué es bueno para qué) y un plan de
lectura según el tiempo que tengas.

Y para saber **si te falta algún tema**, está [[02 Chequeo de los 12 temas]]: la lista de la cátedra con su nota
maestra, su peso y **lo que hay que poder decir** de cada uno.

## Cómo leer cada nota

> [!tip] Las notas están escritas para alguien que **no sabe nada** del tema
> Las notas troncales arrancan con un bloque **"Si es la primera vez que ves esto"**: una analogía y el
> problema que resuelve ese concepto, antes de cualquier definición. Si ya sabés el tema, saltealo. Si no,
> leelo dos veces: está pensado para que el resto de la nota se entienda sin ayuda.

Todas las notas de concepto respetan el mismo esqueleto:

1. **En una frase** → la respuesta mínima que tenés que poder decir.
2. **Contexto** → por qué existe ese circuito / mecanismo y qué problema resuelve.
3. **Desarrollo** → definiciones, tablas, diagramas, ecuaciones.
4. **Cómo responderlo en el final** → guion oral de 1 a 3 minutos.
5. **Errores típicos** → lo que hace perder puntos.
6. **Relacionado / Para practicar** → enlaces.

## Convenciones

- `![nombre](../assets/nombre.svg)` = diagrama. En Obsidian podés hacer clic para agrandarlo (y `![nombre](../assets/nombre.svg)` para fijar el ancho).
- Los bloques de color (callouts) tienen significado fijo:
  - `[!abstract]` → la respuesta corta.
  - `[!warning]` → **verificar con el apunte de cátedra** (números de pulsos, nombres exactos de señales).
  - `[!example]` → ejercicio resuelto paso a paso.
  - `[!tip]` → truco de examen / regla mnemotécnica.
  - `[!danger]` → error conceptual frecuente.
- Los enlaces `[[...]]` funcionan entre notas: seguí el hilo del tema con el panel de enlaces.

## Qué está cubierto
- Las **8 preguntas principales**, las **12 secundarias** y las **7 prácticas** del modelo de final.
- Los **20 TPs** de la cátedra (consigna + resolución + qué agregar si el TP está incompleto).
- Los temas del plan que el modelo no nombra pero que se usan de apoyo (memoria virtual, control
  microprogramado, paralelismo, hardware aritmético).

## Qué falta / cómo crece

Si la cátedra entrega nuevos apuntes (o un final viejo), agregá una nota nueva y enlazala desde
[[Banco de preguntas del final]]. La bóveda está pensada para crecer por preguntas, no por capítulos.
