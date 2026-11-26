---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S09 · Los 7 y 8 pulsos del ciclo de búsqueda

> [!question] Pregunta
> Describa los pulsos del ciclo de búsqueda: ¿qué hace cada uno? ¿Por qué se habla de 7 y de 8 pulsos?

## 1. Teoría previa

**Pulso de reloj (CP).** Cada tic del reloj. En cada pulso se ejecuta **una** microoperación.

**Ciclo de búsqueda.** Es la secuencia de pulsos que trae la instrucción de memoria al IR. En BLUE son **8 pulsos** (CP1…CP8) de 125 ns cada uno, es decir, 1 µs.

**Microoperaciones básicas que se usan:**
- `Envíe X`: poner el contenido de X en el bus.
- `Cargue Y`: copiar el bus en Y (LOAD = 1).
- `Orden de lectura`: pedir a la memoria que devuelva la celda direccionada.
- `Strobe MBR`: marcar que el dato ya está estable en el bus.

## 2. Contexto

Esta pregunta es **casi la misma que P03**, pero pide el detalle pulso por pulso. El profesor la pregunta por separado porque es el punto donde se ve si entendés el **tiempo**: por qué un paso va en un pulso y no en otro.

## 3. Gráfico

![[S09-pulsos-busqueda.svg]]

*Lectura:* cada fila es un pulso, con la microoperación y la razón. La fila de CP8 está resaltada: es el pulso que decide si la máquina pasa a ejecutar.

## Figuras reales (libros y resumen de cátedra)

![[libro-quiroga-f7-10.png]]

*Fig. 7.10 — Fase fetch.* · Quiroga, *Arquitectura de computadoras*, p. 178

![[catedra-said-lda3-ejecucion.png]]

*Tabla de pulsos de la fase de ejecución (referencia de la misma notación CP1 a CP8).* · Resumen de cátedra (Said)

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Los ocho pulsos

| Pulso | Microoperación | Por qué ahí |
|---|---|---|
| CP1 | PC → MAR, PC → Z, orden de lectura | la memoria tarda, conviene pedir pronto |
| CP2 | +1 → Y | la ALU se prepara para incrementar mientras la memoria trabaja |
| CP3 | (espera) | la memoria y la ALU trabajan |
| CP4 | SUMA → PC | `PC ← PC + 1` aprovechando que la ALU ya está lista |
| CP5 | strobe MBR | el dato ya está en el bus y es estable |
| CP6 | MBR → IR | la instrucción entra al IR |
| CP7 | decodificación | la UC identifica el opcode |
| CP8 | E → STATE (si la instrucción necesita ejecución) | pasa a E o queda en F |

### 4.2 ¿Por qué 7 y por qué 8?
- **7 pasos de trabajo** (CP1, CP2, CP4, CP5, CP6, CP7, CP8) y **1 de espera** (CP3).
- Las notas hablan de "7 pulsos" cuando no se cuenta la espera de memoria, y de "8 pulsos" cuando se cuenta.
- En el final, lo correcto es decir: "**8 pulsos**, de los cuales uno es de espera de memoria."

### 4.3 Qué pasa en CP8
- Si la instrucción no necesita ejecución (HLT, NOP, JMP, NOT…), CP8 hace su trabajo y **STATE no cambia**: la siguiente búsqueda empieza enseguida.
- Si la instrucción sí referencia memoria (LDA, ADD…), CP8 pone `E → STATE` y empieza la ejecución.

## 5. Cómo se responde (2–3 minutos)

1. **Definición:** "Es la secuencia de 8 pulsos que trae la instrucción al IR."
2. **Dibujo:** tabla CP1–CP8 con la microoperación.
3. **Razón:** se aprovecha la espera de memoria para preparar el incremento del PC.
4. **Cierre:** "Son 8 pulsos: 7 de trabajo y 1 de espera. CP8 decide si hay ejecución."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué pasa en el CP4? | El PC se incrementa con la ALU: `PC ← PC + 1`. |
| ¿Cuánto dura la búsqueda? | 8 pulsos × 125 ns = 1 µs. |
| ¿Qué es el strobe? | Una señal que avisa que el dato es estable en el bus. |
| Error común | Decir que la decodificación ocurre en un pulso aparte. Ocurre en CP6–CP7. |

## 7. Relacionado

- [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de máquina]] · [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]]
- [[P03 Ciclo de máquina]]
