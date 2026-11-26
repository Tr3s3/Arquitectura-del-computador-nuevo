---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S10 · Ciclo de ejecución para todas las operaciones

> [!question] Pregunta
> Describa el ciclo de ejecución para todas las operaciones de BLUE: ¿qué familias hay y cuántos ciclos y pulsos cuesta cada una?

## 1. Teoría previa

**Ciclo de ejecución.** Es la parte de la instrucción después de la búsqueda. Depende del opcode. Cada ciclo de ejecución son 8 pulsos.

**Familias de instrucciones de BLUE.** Según qué hacen en el ciclo de ejecución:

| Familia | Instrucciones | Ejecución |
|---|---|---|
| Transferencia | LDA, STA | cargan o guardan el AC desde o hacia memoria |
| Aritmético-lógica | ADD, XOR, AND, IOR, NOT, RAL | operan sobre el AC |
| Control | JMP, JMA, SRJ, HLT, NOP | cambian el PC o detienen la máquina |
| E/S | INP, OUT | transfieren datos de 8 bits con un periférico |
| Registros | CSA | copia las llaves al AC |

## 2. Contexto

Es la pregunta de la **tabla maestra**. El profesor quiere que sepas que no todas las instrucciones tardan lo mismo: la cantidad de ciclos depende de si necesitan un acceso a memoria o hablan con un periférico. Es el complemento de S12 (qué hace cada una) y de S11 (el LDA con sus pulsos).

## 3. Gráfico

![[S10-ciclos-por-familia.svg]]

*Lectura:* la tabla resume las familias, sus instrucciones, los ciclos y los pulsos.

## 4. Desarrollo detallado

### 4.1 Familia 1: se resuelven en la búsqueda (1 ciclo, 8 pulsos)
- **HLT**: CP8 pone `RUN ← 0`.
- **JMP**: CP8 envía IR(dir) a PC.
- **JMA**: CP8 envía IR(dir) a PC **sólo si A15 = 1** (AC negativo).
- **SRJ**: CP7 guarda el PC en A; CP8 carga PC con la dirección.
- **NOT**: CP7 A → Z; CP8 Z' → A.
- **RAL**: CP7 A → Z; CP8 2·Z → A (rotación a la izquierda).
- **CSA**: CP7 SR → A (copia las llaves).
- **NOP**: nada.

### 4.2 Familia 2: operando en memoria (2 ciclos, 16 pulsos)
- **LDA**: ejecución `IR → MAR`, lectura, `MBR → A`.
- **STA**: ejecución `A → MBR`, `IR → MAR`, escritura.
- **ADD / XOR / AND / IOR**: ejecución `IR → MAR`, lectura, `A → Z`, `MBR → Y`, CP8 `SUMA/XOR/AND/OR → A`.

### 4.3 Familia 3: E/S (2 + n ciclos, 16 pulsos o más)
- **INP**: en CP7 se activa TRA = 1 y se envía el número de dispositivo. Si R = 1 (listo), el dato entra al AC y TRA = 0.
- **OUT**: similar, el AC sale al dispositivo.
- Si el periférico no está listo, el ciclo se **repite**. Por eso el número de ciclos es variable.

### 4.4 Cómo se decide la cantidad de ciclos
- Si la instrucción no toca memoria ni periféricos → 1 ciclo.
- Si toca memoria por el operando → 2 ciclos.
- Si la dirección se calcula con índice (BLUE indexada) → 3 ciclos o más.
- Si espera a un periférico → más de 2.

## 5. Cómo se responde (3–4 minutos)

1. **Definición:** "La ejecución depende del opcode; cada familia tiene su cantidad de ciclos."
2. **Dibujo:** la tabla de familias con ciclos y pulsos.
3. **Ejemplos:** una de cada familia con sus pulsos clave.
4. **Cierre:** "Cuantos más accesos a memoria o a periféricos, más ciclos."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántos pulsos cuesta un JMP? | 8, porque se resuelve en la búsqueda. |
| ¿Por qué INP puede tardar mucho? | Porque espera a que el periférico esté listo (R = 1). |
| ¿Qué instrucción es la condicional? | JMA: salta sólo si A15 = 1. |
| Error común | Decir que todas las instrucciones duran 16 pulsos. |

## 7. Relacionado

- [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] · [[Ciclo de ejecución — todas las operaciones]]
- [[S11 Ciclo LDA (24 pulsos)]] · [[S12 Operaciones de máquina BLUE]]
