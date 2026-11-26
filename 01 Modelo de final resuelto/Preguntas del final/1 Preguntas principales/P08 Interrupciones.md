---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P08 · Interrupciones

> [!question] Pregunta
> ¿Qué es una interrupción? Describa la secuencia de atención, los tipos de interrupción y cómo se resuelve en BLUE (SI, IRQ, estados F/E/I).

## 1. Teoría previa

**Interrupción.** Es un pedido de atención que **rompe la secuencia normal** del programa. La CPU termina la instrucción en curso, atiende el pedido y retorna como si nada hubiera pasado.

**Por qué existe.** Un periférico lento (teclado, disco) tarda milisegundos; una instrucción de la CPU tarda ~1 µs. La diferencia es de 1000 a 1 000 000 veces. Si la CPU espera al periférico (**polling**), desperdicia casi todo el tiempo.

**Tipos.**

| Criterio | Tipos | Ejemplo |
|---|---|---|
| Origen | de hardware (externas) | teclado, disco, timer |
| | de software | la instrucción `INT n` |
| | internas (excepciones) | división por cero, código de operación inválido, fallo de página |
| Máscara | enmascarables | periféricos (se pueden deshabilitar) |
| | no enmascarables (NMI) | falla de alimentación |
| Identificación | polling | la CPU pregunta bandera por bandera (BLUE) |
| | vectorizadas | el periférico entrega un número de vector (8086) |

**Elementos de BLUE con interrupciones.**
- **SI**: habilita (1) o deshabilita (0) el sistema. Se maneja con ION e IOF.
- **IRQ**: pedido único, la OR de las banderas de los dispositivos.
- **I**: marca que se está atendiendo una interrupción.
- **Estados F / E / I**: búsqueda, ejecución e interrupción.
- **RTI**: retorno de interrupción, recupera el PC y vuelve a poner SI = 1.

## 2. Contexto

Las interrupciones son la respuesta del computador al problema de la **E/S**. Son además la pregunta más larga del bloque de arquitectura: el profesor quiere ver que sabés el **orden** de los pasos y **por qué** se guarda el PC. Conecta con P04 (E/S), S12 (operaciones de BLUE) y con los modos de E/S (programada, por interrupción, DMA).

## 3. Gráfico

![[P08-interrupciones.svg]]

*Lectura:* nueve pasos en orden, de arriba a abajo. Los tres pasos en verde son los que más se preguntan: guardar contexto, saltar a la rutina y retornar.

## Figuras reales (libros y resumen de cátedra)

![[libro-stallings-f3-9.png]]

*Fig. 3.9 — Ciclo de instrucción con interrupciones.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 91

![[libro-stallings-f7-6.png]]

*Fig. 7.6 — Procedimiento de interrupción simple.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 244

![[libro-stallings-f10-8.png]]

*Fig. 10.8 — Uso de una pila para implementar el anidamiento de subrutinas.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 397

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Secuencia general (la respuesta que se espera)

1. **El periférico pide**: activa su línea de pedido (INT o IRQ).
2. **La CPU termina la instrucción en curso.** La interrupción se acepta al final de la instrucción, nunca en el medio; si no, se perdería un estado intermedio.
3. **Verifica la habilitación**: SI debe estar en 1.
4. **Reconoce el pedido**: genera INTACK.
5. **Guarda el contexto**: al menos el **PC**, que ya apunta a la siguiente instrucción. En máquinas reales, también los flags y los registros que usa la rutina.
6. **Identifica la fuente**: por polling, o por vector (el número indexa una tabla de vectores).
7. **Salta a la rutina de servicio** (ISR).
8. **La rutina atiende**: lee o escribe el registro de datos del periférico y baja el pedido.
9. **Restaura el contexto** y ejecuta RTI.

### 4.2 Lo que pasa en los pulsos de BLUE

| Pulso | Acción | Para qué |
|---|---|---|
| CP1 | SI ← 0 | se deshabilita para que no interrumpa otra interrupción |
| CP2 | PC → MBR | se prepara la dirección de retorno |
| CP3 | 0 → MAR, orden de escritura | el PC queda guardado en la **posición 0** |
| CP4 | 1 → PC | la rutina empieza en la **posición 1** |
| CP5–CP7 | — | la rutina corre |
| CP8 | I ← 0 | termina el reconocimiento |

### 4.3 Prioridades y anidamiento

- Si llegan varios pedidos a la vez, la CPU atiende primero el de **mayor prioridad**. En hardware se resuelve con un codificador con prioridad.
- Una interrupción de mayor prioridad puede **anidarse** sobre otra: se guarda el contexto de la primera, se atiende la segunda y se vuelve.
- El **puntero de pila (SP)** permite el anidamiento porque el contexto se guarda en pila.

### 4.4 Polling vs vectorizada

- **Polling:** la rutina de atención recorre los dispositivos y pregunta bandera por bandera. Simple, pero lento si hay muchos.
- **Vectorizada:** el dispositivo entrega su número de vector; la CPU salta directamente a la rutina de la tabla.

### 4.5 Formas de E/S que se mencionan junto

- **Programada (por consulta):** la CPU inicia y espera.
- **Por interrupción:** la CPU sigue y el periférico avisa.
- **DMA:** un controlador mueve bloques entre memoria y periférico; avisa al terminar.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Es un pedido de atención que rompe la secuencia; la CPU termina la instrucción, guarda el PC, atiende y retorna."
2. **Dibujo:** línea INT → CPU → "¿SI = 1?" → guardar PC → ISR → RTI.
3. **Desarrollo:** los nueve pasos, con énfasis en guardar el PC y en la tabla de vectores.
4. **BLUE:** SI, IRQ, INTACK, estados F/E/I.
5. **Cierre:** "Lo útil de la interrupción es que es transparente: por eso se guarda el PC y se restaura."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Por qué se guarda el PC? | Para volver a la siguiente instrucción al terminar la rutina. |
| ¿Polling o interrupción? | Polling: la CPU pregunta todo el tiempo. Interrupción: el periférico avisa cuando lo necesita. |
| ¿Qué es la tabla de vectores? | La tabla con la dirección de cada rutina, indexada por el número de vector. |
| ¿Puede interrumpirse una interrupción? | Sí, si la de mayor prioridad está habilitada: se anida. |
| Error común | Decir que la interrupción "para el programa". La CPU sólo cambia de rutina y luego vuelve. |

## 7. Relacionado

- [[Interrupciones y entrada-salida]] · [[5.5.1 IRQ, SI y CP8]] · [[5.5.2 Máscara, pila y RTI]] · [[10.2.1 Mecanismo completo]]
- [[P04 Estructura básica de un computador]]
