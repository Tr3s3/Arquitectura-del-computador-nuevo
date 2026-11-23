---
tp: 3
unidad: 1
tipo: tp
---
# TP3 — Simplificación por método analítico

> [!abstract] Consigna (cátedra)
> **Ej. 1:** dada una función booleana, reducirla a su **expresión mínima** aplicando álgebra booleana, **indicando la ley/regla/teorema** usada en cada paso. **Ej. 2:** dada una función booleana, encontrar su **tabla de verdad** y su **representación lógica** (circuito).

## Qué hay que saber para resolverlo

> [!important] Lo que corrige la cátedra
> En el método **analítico** no basta con llegar al resultado: hay que **escribir al costado de cada línea qué ley se aplicó**. Sin justificación se pierde puntaje aunque el resultado sea correcto.

## Método paso a paso (guion para el oral)

1. **Identificar la forma** de la función (suma de productos, producto de sumas, mixta).

2. **Factorizar** donde se pueda (distributiva al revés): buscar variables comunes.

3. **Aplicar complemento** (`A + A' = 1`) para eliminar variables.

4. **Aplicar absorción** (`A + A'B = A + B`).

5. **Repetir** hasta que no se pueda reducir más.

6. **Verificar** con la tabla de verdad (original y mínima tienen que coincidir).

7. **Dibujar el circuito mínimo** y contar compuertas antes y después.

## Ejemplo resuelto (tipo examen)
Simplificar `f = AB + AB' + A'B'`:

```
f = AB + AB'  +  A'B'
  = A(B + B') + A'B'      ← distributiva
  = A·1      + A'B'       ← complemento (B + B' = 1)
  = A        + A'B'       ← identidad (A·1 = A)
  = A + B'                ← absorción (A + A'X = A + X, con X = B')
```
Circuito original: 3 AND y 1 OR de 3 entradas. Circuito mínimo: **1 OR** (A + B') más un inversor. **De 4 compuertas a 2.**

## Otro ejemplo clásico
```
f = AB + A'B + AB'
  = B(A + A') + AB'   ← distributiva
  = B + AB'           ← complemento
  = B + A             ← absorción
```

> [!example] Ejercicio 2 del TP (tabla → circuito)
> Con la expresión mínima se arma la tabla evaluando cada combinación y el circuito sale directo: **una AND por producto y una OR final** (forma SOP) o **una OR por suma y una AND final** (forma POS).

## Enlaces
Desarrollo: [[Álgebra de Boole — postulados y teoremas]] · [[Mintérminos y maxtérminos]] Siguiente: [[TP4 Mintérminos, maxtérminos y Karnaugh]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| 🎬 | [Lista de reproducción del TP (simplificación analítica)](https://www.youtube.com/playlist?list=PLF0o5Yzo4mCPoBKJHQ5SiV2flYi63odyq) | — |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
