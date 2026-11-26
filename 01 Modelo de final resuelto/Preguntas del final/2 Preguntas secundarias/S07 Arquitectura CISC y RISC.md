---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S07 · Arquitectura CISC y RISC

> [!question] Pregunta
> Explique las arquitecturas CISC y RISC: diferencias, ventajas, ejemplos y por qué cada una usa un tipo de unidad de control.

## 1. Teoría previa

**CISC (Complex Instruction Set Computer).** Muchas instrucciones, complejas, de longitud variable. Puede operar directamente sobre memoria. Ejemplos: x86 (8086/8088), VAX, IBM 360.

**RISC (Reduced Instruction Set Computer).** Pocas instrucciones, simples y regulares, de longitud fija. Sólo `LOAD` y `STORE` acceden a memoria. Operan sobre registros. Ejemplos: ARM, MIPS, PowerPC, RISC-V.

**Tabla de comparación.**

| Característica | CISC | RISC |
|---|---|---|
| Cantidad de instrucciones | muchas y complejas | pocas y simples |
| Longitud | variable | fija |
| Modos de direccionamiento | muchos | pocos (registro + desplazamiento) |
| Acceso a memoria | cualquier instrucción | sólo LOAD / STORE |
| Operandos | 1 o 2, muchos implícitos | 3 registros explícitos |
| Registros | pocos | muchos (32 o más) |
| Unidad de control | microprogramada | cableada |
| Pipeline | difícil | natural |
| Ciclos por instrucción | 2 a 10 o más | casi 1 |
| Densidad de código | alta | menor |

## 2. Contexto

Es una de las preguntas de mayor peso según la matriz del profesor (peso 10). Es la pregunta que une **arquitectura, control y pipeline**. Si la explicás bien, sumás puntos en S06 y P07.

## 3. Gráfico

![[S07-cisc-risc.svg]]

*Lectura:* las dos columnas comparan las dos filosofías, fila por fila.

## Figuras reales (libros y resumen de cátedra)

![[libro-stallings-f13-8.png]]

*Formatos de instrucciones del MIPS.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed.

![[libro-stallings-f10-15.png]]

*Comparación de tres programas para el mismo cálculo.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed.

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Ejemplo: la misma operación en las dos
Queremos `M[X] = M[X] + 1`.
- **CISC:** `INC X` (una sola instrucción que opera sobre la memoria).
- **RISC:** `LOAD R1, X` · `ADD R1, R1, 1` · `STORE R1, X` (tres instrucciones simples).

Cuesta más instrucciones, pero cada una es simple y cabe en el pipeline.

### 4.2 Por qué CISC usa control microprogramado
Con instrucciones complejas, cablear cada caso sería un circuito enorme y difícil de corregir. El **microcódigo** (una ROM) ordena los pasos y permite cambiar el repertorio sin rehacer el hardware.

### 4.3 Por qué RISC usa control cableado
Con pocas instrucciones simples, el circuito es pequeño y rápido. La velocidad importa más que la flexibilidad.

### 4.4 Ventajas de cada una
- **CISC:** programas más cortos (densidad de código), compilador más directo en algunos casos.
- **RISC:** pipeline eficiente, CPU más simple y barata, ciclos casi de 1.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "CISC: muchas instrucciones complejas. RISC: pocas instrucciones simples y regulares."
2. **Dibujo:** las dos columnas comparativas con un ejemplo de instrucción de cada una.
3. **Desarrollo:** la tabla, enfocando en memoria, longitud, control y pipeline.
4. **Cierre:** "RISC busca que cada instrucción tarde casi un ciclo; CISC busca que cada instrucción haga mucho."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Por qué RISC tiene más registros? | Para evitar accesos a memoria; el compilador usa registros. |
| ¿Qué es el microcódigo? | El conjunto de microinstrucciones de la UC microprogramada, guardado en ROM. |
| ¿BLUE es RISC o CISC? | Es una máquina didáctica: un solo acumulador y pocas instrucciones, con acceso a memoria en varias. Se la analiza con los criterios de la tabla. |
| Error común | Decir que RISC "tiene menos código". Tiene más instrucciones, pero cada una es simple. |

## 7. Relacionado

- [[CISC y RISC]] · [[CISC y RISC]] · [[CISC y RISC]]
- [[S06 Pipeline (definir y ejemplificar)]] · [[P07 Unidad de Control (funciones, señales e importancia)]]
