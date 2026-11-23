---
unidad: 9
tipo: concepto
examen: complementario
---
# Hardware aritmético (resumen)

> [!abstract] En una frase
> Todo el hardware aritmético se construye con **sumadores** (un [[Sumador completo]] encadenado) más lógica de control: la resta es una suma en complemento a 2, la multiplicación es una serie de sumas y desplazamientos (o el algoritmo de Booth), la división es una serie de restas y desplazamientos, y la punto flotante agrega alineación de exponentes y redondeo.

## Representación de números

| Representación | Rango (n bits) | Cómo se obtiene el negativo |
|---|---|---|
| **Magnitud y signo** | −(2ⁿ⁻¹−1) … +(2ⁿ⁻¹−1) | se cambia sólo el bit de signo |
| **Complemento a 1** | −(2ⁿ⁻¹−1) … +(2ⁿ⁻¹−1) | se niegan todos los bits |
| **Complemento a 2** | −2ⁿ⁻¹ … +(2ⁿ⁻¹−1) | se niegan todos los bits y se suma 1 |
| Sin signo | 0 … 2ⁿ−1 | — |

El complemento a 2 se usa porque **el mismo sumador suma y resta** y no hay dos ceros.

## Suma y resta

- **Con magnitud y signo:** hay que comparar magnitudes y signos y decidir si suma o resta ⇒ hardware con más lógica de control.

- **Con complemento a 2:** `A − B = A + (−B) = A + B' + 1`. Se implementa con XOR en las entradas de B y `SUB` como acarreo de entrada (ver [[ALU]]). **Un solo circuito para las dos operaciones.**

- **Desbordamiento (overflow):** ocurre cuando el resultado no cabe. En complemento a 2 se detecta si los acarreos de entrada y salida del bit de signo **difieren** (`V = Cin ⊕ Cout` del MSB). En sin signo, es el acarreo de salida (C).

## Multiplicación

| Algoritmo | Idea | Hardware |
|---|---|---|
| **Magnitud y signo** | multiplicar magnitudes y aplicar el signo aparte (`signo = sA ⊕ sB`) | sumador + registro de doble ancho con desplazamiento |
| **Productos parciales** | sumar el multiplicando desplazado por cada bit del multiplicador en 1 | sumador + desplazador |
| **Booth** | recodifica el multiplicador en dígitos −1, 0, +1 ⇒ **menos sumas** | sumador-restador + lógica de recodificación + desplazamiento |
| **Arreglo multiplicador** | matriz de sumadores, todos los productos parciales en paralelo (combinacional) | n² celdas: rápido pero caro |

**Booth:** se mira el par (Q0, Q−1). Si es `01` ⇒ sumar el multiplicando; `10` ⇒ restar; `00`/`11` ⇒ sólo desplazar. Sirve para operandos **con signo en complemento a 2** sin separar el signo, y es más rápido cuando en el multiplicador hay rachas de 1s.

## División

- **Restaurativa:** se intenta restar el divisor; si el resultado es negativo se **restaura** (se vuelve a sumar) y se pone 0 en el cociente; si es positivo, se pone 1. Es la versión directa del algoritmo manual.

- **No restaurativa:** no restaura; usa el signo del resto para decidir la próxima operación (menos pasos).

- **Hardware:** registro de doble ancho (dividendo/resto), sumador-restador, desplazamiento a la izquierda.

- **Sobreflujo (overflow) al dividir:** ocurre si el divisor es 0, o si el cociente no cabe en el registro (dividendo ≥ divisor × 2ⁿ). Hay que detectarlo y generar interrupción/trap.

## Punto flotante
Formato (IEEE 754, simplificado): `signo | exponente (con exceso) | mantisa normalizada`.
```
  valor = (−1)^S × 1.M × 2^(E − exceso)
```

| Operación | Pasos |
|---|---|
| **Suma/resta** | 1) comparar exponentes; 2) **alinear** (desplazar la mantisa del menor); 3) sumar/restar mantisas; 4) **normalizar**; 5) redondear |
| **Multiplicación** | 1) sumar exponentes (y restar el exceso); 2) multiplicar mantisas; 3) normalizar y redondear; 4) signo = XOR |
| **División** | 1) restar exponentes; 2) dividir mantisas; 3) normalizar y redondear |

**Registro de configuración:** signo, exponente, mantisa (más bits de guarda, redondeo y *sticky* para no perder precisión). Hardware: ALU de punto flotante (**FPU**), normalmente segmentada (pipeline aritmético: ver [[Pipeline]]).

## Aritmética decimal (BCD)

- Cada dígito decimal ocupa 4 bits (0000–1001). Se usa en aplicaciones financieras.

- **Sumador BCD:** suma binaria de 4 bits; si el resultado es **> 9** o hubo acarreo, se **suma 6** (0110) para saltar los seis códigos inválidos y se propaga acarreo. Ejemplo: `8 + 5 = 1101` (13, inválido) ⇒ `+ 0110` = `1 0011` ⇒ dígito 3 con acarreo. ✔

- **Resta BCD:** se hace en complemento a 10 (o a 9) y se corrige de manera análoga.

- **Multiplicación/división decimal:** por sumas/restas repetidas o por tablas, con corrección BCD.

## Cómo responderlo en el final

1. Representaciones y por qué complemento a 2 (un solo sumador, sin doble cero).

2. Suma/resta con el mismo sumador + detección de overflow.

3. Multiplicación: productos parciales, Booth, arreglo multiplicador.

4. División: restaurativa vs no restaurativa, sobreflujo.

5. Punto flotante: formato y los pasos de cada operación (alinear, normalizar, redondear).

6. BCD: sumar 6 cuando el resultado > 9.

## Errores típicos

- Detectar overflow por el acarreo de salida en complemento a 2 (hay que mirar **los dos** acarreos del MSB).

- Decir que Booth sirve sólo para números sin signo.

- Olvidar la **normalización** y el **redondeo** en punto flotante.

- En BCD, sumar 6 también cuando el resultado es válido.

## Relacionado
[[Sumador completo]] · [[ALU]] · [[CISC y RISC]] · [[Pipeline]]
