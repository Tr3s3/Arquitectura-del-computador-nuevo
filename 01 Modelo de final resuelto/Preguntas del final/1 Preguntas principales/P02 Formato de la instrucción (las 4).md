---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P02 · Formato de la instrucción (las 4 variantes)

> [!question] Pregunta
> Explique los formatos de instrucción según la cantidad de direcciones (4, 3, 2 y 1). Ejemplifique con una suma, `X = A + B`, y diga qué formato usa BLUE.

## 1. Teoría previa

**Instrucción.** Es una palabra de bits con dos partes:
- **Código de operación (opcode):** qué hacer (sumar, cargar, saltar).
- **Campos de direcciones:** dónde están los operandos y el resultado.

**Cuántos bits tiene cada campo.** Depende del ancho de la palabra. En BLUE la palabra es de 16 bits: 4 para el opcode y 12 para la dirección. Como 4 bits dan 2⁴ = 16 combinaciones, BLUE tiene **16 instrucciones**.

**Relación clave.** Cuanto más campos de dirección, más larga es la instrucción y menos instrucciones hacen falta para un programa. Cuanto menos campos, más corta es la instrucción, pero más instrucciones hacen falta.

## 2. Contexto

Este tema decide la **arquitectura**: cuántos operandos explícitos tiene cada instrucción, y dónde queda el resultado. Conecta con RISC (3 direcciones, registros) y CISC (2 direcciones, operaciones sobre memoria). Y explica por qué BLUE usa un **acumulador implícito**: no escribe la dirección del AC porque siempre está.

## 3. Gráfico

![[P02-formatos-instruccion.svg]]

*Lectura:* cada fila es un formato. El primer campo (rosa) es el opcode; los demás (celeste) son direcciones. La última fila es BLUE.

## Figuras reales (libros y resumen de cátedra)

![[catedra-said-formatos-comparacion.png]]

*Qué elimina cada formato al bajar de 4 a 1 dirección.* · Resumen de cátedra (Said)

![[catedra-said-formato-ri.png]]

*Corte del registro de instrucción: opcode 15..12 y dirección 11..0.* · Resumen de cátedra (Said)

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

Tomemos la misma operación en los cuatro formatos: `X = A + B`.

### 4.1 Cuatro direcciones

`ADD X, A, B, prox`

- Operandos: A y B. Resultado: X. Cuarta dirección: la próxima instrucción.
- **Ventaja:** una sola instrucción; no hace falta un salto para seguir.
- **Desventaja:** la instrucción es muy larga.

### 4.2 Tres direcciones

`ADD X, A, B`

- Es el formato equilibrado. Cada operando y el resultado van explícitos.
- Es la base de **RISC** (los procesadores modernos usan registros para estos campos).

### 4.3 Dos direcciones

`MOV X, A` seguido de `ADD X, B`

- El primer operando se **destruye** (X queda con el resultado, y el valor de A se pierde).
- Es típico de **CISC** (x86).

### 4.4 Una dirección (BLUE)

`LDA A` · `ADD B` · `STA X`

- El operando implícito es el **acumulador (AC)**. No se escribe porque siempre está.
- En BLUE: `opcode 4 bits + dirección 12 bits`.
- Cada instrucción carga un solo dato, por eso una suma necesita tres instrucciones.

### 4.5 Comparación

| Direcciones | Instrucciones para X = A + B | Tamaño | Ejemplo |
|---|---|---|---|
| 4 | 1 | el mayor | — |
| 3 | 1 | grande | RISC |
| 2 | 2 | medio | CISC (x86) |
| 1 | 3 | chico | BLUE |

### 4.6 Lo que hay que decir sobre el compromiso

Más direcciones = instrucción larga, pocas instrucciones y mayor complejidad en la decodificación. Menos direcciones = instrucción corta, más instrucciones y más accesos a memoria (cada `LDA` o `STA` es un acceso). Los procesadores modernos eligen 3 direcciones con registros y sólo `LOAD` y `STORE` para memoria.

## 5. Cómo se responde (2–3 minutos)

1. **Definición:** "El formato es el reparto de bits de la instrucción entre el opcode y las direcciones de los operandos."
2. **Dibujo:** las cuatro cajas, de la más larga a la más corta.
3. **Desarrollo:** el ejemplo `X = A + B` en las cuatro variantes.
4. **BLUE:** 4 + 12 bits, 16 instrucciones, acumulador implícito.
5. **Cierre:** "Es un compromiso entre longitud de la instrucción y cantidad de instrucciones."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántos bits quedan para el opcode en BLUE? | 16 − 12 = 4, o sea 16 instrucciones. |
| ¿Qué es un acumulador implícito? | Un registro que es operando y destino sin aparecer en la instrucción. |
| ¿Por qué RISC usa 3 direcciones? | Porque con registros los campos son cortos y la instrucción queda regular (longitud fija). |
| Error común | Decir que BLUE tiene 3 direcciones. Tiene 1, y el resto es implícito. |

## 7. Relacionado

- [[Formato de la instrucción (4 formatos)]] · [[CISC y RISC]] · [[TP17 Formato básico de instrucciones]]
- [[P07 Unidad de Control (funciones, señales e importancia)]] · [[P06 Ciclo de ejecución BLUE indexada y sin indexar]]
