---
tipo: pregunta-de-final
bloque: 2 · Preguntas secundarias
---
# S02 · Flip-flops (biestables)

> [!question] Pregunta
> Explique los flip-flops: qué son, tipos (SR, D, JK, T), sus ecuaciones características y la diferencia con un latch o con un registro.

## 1. Teoría previa

**Biestable.** Es un circuito secuencial de **dos estados estables** que guarda **1 bit**. Su salida depende de la entrada y **del estado anterior**: por eso es secuencial (tiene memoria).

**Sincrónico vs asincrónico.** El **síncrono** cambia sólo en el flanco de un reloj. El **asincrónico** cambia en cuanto cambia la entrada. En el final casi siempre se habla de los síncronos.

**Ecuación característica.** Es la que da la salida siguiente `Q(t+1)` en función de las entradas y del estado actual `Q(t)`.

**Cuatro tipos.**

| Biestable | Entradas | Ecuación característica | Observación |
|---|---|---|---|
| **SR** | S, R | `Q(t+1) = S + R'·Q` | S = R = 1 está prohibido |
| **D** | D | `Q(t+1) = D` | copia la entrada |
| **JK** | J, K | `Q(t+1) = J·Q' + K'·Q` | 11 invierte: no hay estado prohibido |
| **T** | T | `Q(t+1) = T ⊕ Q` | es un JK con J = K = T |

**Tablas de transición (lo que se pide).**

| Transición | RS | JK | D | T |
|---|---|---|---|---|
| 0 → 0 | S=0, R=X | J=0, K=X | D=0 | T=0 |
| 0 → 1 | S=1, R=0 | J=1, K=X | D=1 | T=1 |
| 1 → 0 | S=0, R=1 | J=X, K=1 | D=0 | T=1 |
| 1 → 1 | S=X, R=0 | J=X, K=0 | D=1 | T=0 |

## 2. Contexto

Los biestables son el **puente** entre la lógica combinacional (compuertas) y la memoria. Sin biestables no hay registros, contadores ni RAM. Por eso el profesor los pregunta junto con el resto de la unidad 2. Lo importante es que sepas la ecuación de cada uno y leer la tabla de excitación.

## 3. Gráfico

![[S02-flip-flops.svg]]

*Lectura:* cada caja muestra el nombre, sus entradas, la ecuación característica y la observación clave. Los cuatro tipos en una sola hoja.

## 4. Desarrollo detallado

### 4.1 RS
- `S = 1, R = 0` → Q = 1 (set).
- `S = 0, R = 1` → Q = 0 (reset).
- `S = R = 0` → mantiene.
- `S = R = 1` → **prohibido**: las salidas quedan indefinidas.

### 4.2 D
- Copia la entrada en cada flanco. Es el biestable de los **registros**. `Q(t+1) = D`.

### 4.3 JK
- Corrige el caso prohibido del RS: con `J = K = 1`, la salida **invierte** (toggle).
- Ecuación: `Q(t+1) = J·Q̄ + K̄·Q`.

### 4.4 T
- Si T = 1, invierte en cada flanco; si T = 0, mantiene.
- Es un JK con las dos entradas unidas. Se usa en contadores.

### 4.5 Conversión (Karnaugh)
Para implementar un JK con un RS, se hace una tabla que, para cada combinación de (J, K, Q), dé S y R. Por ejemplo, para el caso `J=1, K=1, Q=0` el JK pasa a 1, así que hay que dar `S = 1` y `R = 0`. Por Karnaugh se obtiene `S = J·Q̄` y `R = K·Q`.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Es un circuito secuencial de 1 bit que cambia en el flanco del reloj."
2. **Dibujo:** cuatro cajas (RS, D, JK, T) con su ecuación.
3. **Tabla de excitación:** para cada transición, qué entrada necesita.
4. **Cierre:** "El JK resuelve el caso prohibido del RS, y el T es un JK con J = K."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Qué pasa con S = R = 1 en el RS? | Es prohibido: la salida queda indefinida. |
| ¿Por qué el JK no tiene estado prohibido? | Con J = K = 1 invierte la salida. |
| ¿Biestable o latch? | El biestable cambia en el flanco; el latch cambia por nivel. |
| Error común | Escribir la ecuación del JK como `J·K`. La correcta es `J·Q̄ + K̄·Q`. |

## 7. Relacionado

- [[Flip-Flops SR, D, JK y T]] · [[Conversión entre biestables (RS, JK, D, T)]] · [[Mintérminos y maxtérminos]]
- Práctica relacionada: [[T01 Sumador completo (tabla de verdad, funciones y gráfico)]] (misma metodología de tabla → función → circuito).
