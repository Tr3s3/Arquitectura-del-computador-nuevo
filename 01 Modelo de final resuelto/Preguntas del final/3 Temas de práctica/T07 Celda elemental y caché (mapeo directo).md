---
tipo: pregunta-de-final
bloque: 3 · Temas de práctica
---
# T07 · Celda elemental y caché

> [!question] Pregunta
> Explique la celda elemental de memoria y la memoria caché: sus mapeos (directo, asociativo y por conjuntos), las políticas de escritura y la división de la dirección.

## 1. Teoría previa

**Celda elemental.** Un bit guardado en un biestable (SRAM) o un capacitor (DRAM), con selección, L/E y buffer de tres estados. Ver S01.

**Caché.** Memoria pequeña y rápida (SRAM) entre la CPU y la memoria principal. Guarda **bloques** de memoria que tienen probabilidad de usarse pronto.

**Localidad.** Temporal (lo usado se vuelve a usar) y espacial (lo vecino se usa pronto). Por eso la caché funciona.

**Acierto y fallo.** Acierto: el dato está en la caché. Fallo: no está, se trae el bloque de la memoria principal.

**Dirección partida en tres campos:**

| Campo | Para qué sirve |
|---|---|
| Etiqueta (tag) | dice si el bloque que está en la línea es el que se busca |
| Índice (línea) | dice en qué casillero de la caché mirar |
| Desplazamiento (offset) | dice qué palabra dentro del bloque |

## 2. Contexto

La caché es la aplicación más importante de la celda SRAM y de la jerarquía de memoria. Esta práctica pide los **mapeos**: cómo se decide en qué línea de la caché va un bloque. Es el punto donde se ve si entendés la relación entre la dirección y la línea.

## 3. Gráfico

![[T07-cache-mapeo.svg]]

*Lectura:* a la izquierda, 16 bloques de la memoria principal. A la derecha, 8 líneas de la caché. Cada bloque va a la línea `bloque mod 8`. Los bloques 0 y 8 compiten por la línea 0.

## 4. Desarrollo detallado

### 4.1 Mapeo directo

- Cada bloque tiene **un solo lugar** posible: `línea = bloque mod número de líneas`.
- Con 8 líneas, el bloque 13 va a la línea 13 mod 8 = 5.
- **Ventaja:** simple y barato; se compara una sola etiqueta.
- **Desventaja:** dos bloques que caen en la misma línea se expulsan mutuamente (conflicto), aunque haya otras líneas libres.

### 4.2 Totalmente asociativo

- El bloque puede ir a **cualquier** línea.
- **Ventaja:** menos conflictos.
- **Desventaja:** hay que comparar **todas** las etiquetas a la vez (hardware caro).

### 4.3 Asociativo por conjuntos (set associative)

- La caché se divide en **conjuntos** de `k` líneas (k vías). El bloque va a un conjunto fijo, pero a cualquiera de sus `k` líneas.
- Es el compromiso: menos conflictos que el directo y menos hardware que el totalmente asociativo.

### 4.4 Políticas de escritura

| Política | Cómo funciona | Ventaja | Desventaja |
|---|---|---|---|
| Write-through | escribe en la caché y en la RAM a la vez | la RAM siempre está al día | más tráfico |
| Write-back | escribe sólo en la caché y marca la línea sucia | menos tráfico | la RAM puede quedar desactualizada |

### 4.5 Celda y caché juntas
La caché usa **SRAM** (biestables), no DRAM: es más rápida y no necesita refresco. Eso la hace cara por bit, por eso es pequeña.

## 5. Cómo se responde (4 minutos)

1. **Celda:** biestable, selección, L/E, buffer.
2. **Caché:** qué es, localidad, acierto y fallo.
3. **Mapeo:** directo, asociativo y por conjuntos, con el dibujo.
4. **Políticas:** write-through y write-back.
5. **Cierre:** "La caché aprovecha la localidad; el mapeo decide dónde va cada bloque."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué es un conflicto en el mapeo directo? | Dos bloques que van a la misma línea y se expulsan. |
| ¿Por qué la caché es SRAM? | Porque es rápida y no necesita refresco. |
| ¿Qué campo dice si el dato es el correcto? | La etiqueta (tag). |
| Error común | Decir que la caché guarda datos sueltos. Guarda bloques. |

## 7. Relacionado

- [[Memoria caché]] · [[Memoria caché]] · [[Celda elemental de memoria]]
- [[S05 Jerarquía de memorias]] · [[S01 Memoria RAM (celda elemental)]]
