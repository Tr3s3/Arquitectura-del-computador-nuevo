---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S03 · Modos de direccionamiento (ventajas de la BLUE indexada)

> [!question] Pregunta
> Explique los modos de direccionamiento. ¿Cuáles son las ventajas del modo indexado en la BLUE indexada?

## 1. Teoría previa

**Modo de direccionamiento.** Es la regla que dice **dónde está el operando**. La instrucción indica el modo; la CPU calcula la **dirección efectiva (EA)** y accede a esa celda.

**Dirección efectiva (EA).** Es la dirección real del dato, después de aplicar el modo.

**Los siete modos de la cátedra (TP19):**

| # | Modo | Cómo se calcula la EA | Accesos a memoria | Uso típico |
|---|---|---|---|---|
| 1 | Inmediato | el dato está en el campo | 0 | constantes |
| 2 | Directo | EA = campo | 1 | variables globales |
| 3 | Indirecto | EA = M[campo] | 2 | punteros dobles |
| 4 | De registro | el dato está en un registro | 0 | variables rápidas |
| 5 | Registro indirecto | EA = R | 1 | listas, vectores |
| 6 | Desplazamiento / indexado | EA = registro + campo | 1 | arreglos, tablas |
| 7 | De pila | EA = SP (tope de pila) | 1 | subrutinas |

**Los cuatro modos de la BLUE indexada** (los que importan en el final de esta cátedra):

| Modificador | Modo | EA |
|---|---|---|
| 0 | directo | `EA = D` |
| 1 | indirecto | `EA = M[D]` |
| 2 | indexado por RIF | `EA = D + RIF` |
| 3 | indexado por RID | `EA = D + RID` |

## 2. Contexto

Este tema es el **por qué** de la BLUE indexada (P06 explica el **cómo**). El profesor quiere que sepas las ventajas del indexado, y que lo justifiques con un ejemplo de arreglo.

## 3. Gráfico

![[S03-modos-direccionamiento.svg]]

*Lectura:* la tabla compara los siete modos. Abajo, los cuatro modos de la BLUE indexada, con el modificador.

## 4. Desarrollo detallado

### 4.1 Ejemplo numérico
Con la memoria: `dirección 30 = 0050`, `dirección 50 = 0012`, y `RIF = 2`:
- **Directo** `LDA 30`: AC = M[30] = 0050.
- **Indirecto** `LDA (30)`: EA = M[30] = 50 → AC = M[50] = 0012 (dos accesos).
- **Indexado RIF** `LDA 30, RIF`: EA = 30 + 2 = 32 → AC = M[32].

### 4.2 Ventajas del indexado
1. **Recorrer arreglos sin reescribir el código.** Un lazo que incrementa el índice reemplaza `n` instrucciones.
2. **Ahorro de bits.** El campo de la instrucción es la base; el resto lo aporta el registro.
3. **Reubicación.** El programa funciona en otra zona de memoria cambiando el registro base (RB) o el índice.
4. **Estructuras de datos.** Vectores, matrices (base + índice), campos de un registro.
5. **Implementación barata.** Un sumador de direcciones y dos registros.
6. **Menos memoria de programa.** Un solo código sirve para todos los elementos.

### 4.3 Diferencia clave: indirecto vs. registro indirecto
- **Indirecto**: la dirección está en una **celda de memoria** → 2 accesos.
- **Registro indirecto**: la dirección está en un **registro** → 1 acceso.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "El modo indica dónde está el operando; la dirección efectiva es el resultado de aplicarlo."
2. **Tabla:** los cuatro modos de la BLUE indexada.
3. **Ventaja:** recorrer arreglos con un solo código, reubicar y ahorrar bits.
4. **Cierre:** "El indexado deja que el código sea genérico y que el dato decida la posición."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Cuántos modos tiene la BLUE indexada? | Cuatro, según el modificador de 2 bits. |
| ¿Por qué el indexado es reubicable? | Porque la dirección se suma a un registro que se puede cambiar. |
| ¿Qué es RB? | Registro base: se suma siempre, lo carga el sistema. |
| Error común | Confundir los 7 modos teóricos con los 4 de la BLUE indexada. |

## 7. Relacionado

- [[Modos de direccionamiento]] · [[5.3.1 Los 7 modos]] · [[Registros base e índice]]
- [[P06 Ciclo de ejecución BLUE indexada y sin indexar]]
