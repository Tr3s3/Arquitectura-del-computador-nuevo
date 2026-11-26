---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S05 · Jerarquía de memorias

> [!question] Pregunta
> Explique la jerarquía de memorias de un computador: niveles, velocidad, costo y capacidad. ¿Por qué funciona?

## 1. Teoría previa

**Jerarquía.** Es una pirámide de memorias. Cuanto más arriba, más rápida y más cara por bit, y más chica. Cuanto más abajo, más lenta, más barata y más grande.

**La pirámide.**

| Nivel | Tecnología | Tiempo típico | Quién lo administra |
|---|---|---|---|
| Registros | biestables en la CPU | < 1 ns | el compilador |
| Caché L1 | SRAM | 1–2 ns | el hardware |
| Caché L2 / L3 | SRAM | 5–20 ns | el hardware |
| RAM | DRAM | 50–100 ns | el sistema operativo |
| Disco / SSD | magnético / flash | µs–ms | el SO (memoria virtual) |
| Cinta / respaldo | magnético secuencial | segundos | el operador |

**Localidad.**
- **Temporal:** lo que se usó, se vuelve a usar pronto.
- **Espacial:** lo que está cerca de lo usado, se usa pronto.

**Acierto y fallo de caché.** Si el dato está en el nivel rápido, es un **acierto**. Si no, es un **fallo** y se trae un bloque del nivel inferior.

## 2. Contexto

La jerarquía es la razón por la que las computadoras son rápidas **y** grandes al mismo tiempo. No se puede tener memoria grande y rápida a la vez; la jerarquía combina las dos. El profesor la pregunta para ver si sabés el **por qué** (localidad) y no sólo la lista de niveles.

## 3. Gráfico

![[S05-jerarquia.svg]]

*Lectura:* arriba, los niveles rápidos y chicos (registros, L1). Abajo, los lentos y grandes (disco, cinta). El ancho de cada caja representa la capacidad.

## Figuras reales (libros y resumen de cátedra)

![[libro-stallings-f4-1.png]]

*Fig. 4.1 — Jerarquía de memoria.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 130

![[libro-stallings-f4-5.png]]

*Fig. 4.5 — Operación de lectura de caché.* · Stallings, *Organización y arquitectura de computadores*, 7ª ed., p. 135

> Las imágenes están en `assets/` de la bóveda; el gráfico propio de arriba es un resumen esquemático.

## 4. Desarrollo detallado

### 4.1 Por qué funciona: la localidad
Los programas reutilizan los mismos datos (variables de un lazo, instrucciones de un bucle) y acceden a posiciones contiguas (arreglos). Por eso, si se trae un **bloque** al nivel rápido, es probable que el programa pida el resto del bloque pronto.

### 4.2 Quién decide qué

| Salto | Qué se mueve | Quién | Tamaño |
|---|---|---|---|
| Registros ↔ L1 | palabras | el compilador | 1 palabra |
| L1 ↔ L2/L3 ↔ RAM | líneas o bloques | el hardware | 16–64 bytes |
| RAM ↔ disco | páginas | el SO | 4 KB típico |
| Disco ↔ cinta | archivos | el operador | lo que se respalde |

### 4.3 Cálculo: tiempo promedio de acceso (AMAT)
`AMAT = tiempo de acierto + tasa de fallo × penalidad de fallo`.
Ejemplo: acierto 1 ns, fallo 5 %, penalidad 100 ns → AMAT = 1 + 0,05 × 100 = 6 ns.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Una pirámide de memorias: rápida y cara arriba, lenta y barata abajo."
2. **Dibujo:** la pirámide con velocidad, costo y capacidad.
3. **Por qué:** localidad temporal y espacial.
4. **Cierre:** "La jerarquía da la ilusión de una memoria grande y rápida al mismo tiempo."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué es localidad temporal? | Reuso de un dato en poco tiempo. |
| ¿Qué pasa en un fallo de caché? | Se trae el bloque del nivel inferior y se reintenta. |
| ¿Quién administra la RAM? | El sistema operativo, con paginación. |
| Error común | Decir que la caché es más grande que la RAM. Es más chica y más rápida. |

## 7. Relacionado

- [[Jerarquía de memorias]] · [[Jerarquía de memorias]] · [[Memoria caché]]
- [[P05 Memoria RAM 8x3]] · [[T07 Celda elemental y caché (mapeo directo)]]
