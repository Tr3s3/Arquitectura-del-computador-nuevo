---
tipo: sintesis
unidad: 3
---
# 00 Síntesis — Unidad 3 (todo en un solo lugar)

> [!abstract] Qué es este archivo
> **Toda la Unidad 3 en una sola nota**: la notación de microoperaciones, el bus único con sus buffers, los tres buses, la ALU (estructura, `G`/`P`, operaciones y flags) y los nueve registros de la CPU. Sirve para **repasar antes del final** y para **imprimir**. Detalle completo de cada punto: [[00 Unidad 3 — temas y subtemas]].

## Contenido

1. [[#1. Microoperaciones (RTL)]] · 2. [[#2. El bus único]] · 3. [[#3. Los tres buses]] ·

4. [[#4. La ALU]] · 5. [[#5. Operaciones y flags]] · 6. [[#6. Los registros]] ·

7. [[#7. Recetas de examen]] · 8. [[#8. Errores que cuestan puntos]] · 9. [[#9. Autoevaluación]]

---

## 1. Microoperaciones (RTL)

| Símbolo | Significado |
|---|---|
| `←` | transferencia (**copia**, no igualdad) |
| `:` | condición (`RUN: IR ← MBR`) |
| `M[dir]` | contenido de memoria en esa dirección |
| `,` | dos microoperaciones en el mismo pulso (sólo con dos caminos) |

Ejemplos obligatorios:
```
MAR ← PC          MBR ← M[MAR]        IR ← MBR
PC  ← PC + 1      M[MAR] ← MBR        AC ← AC + MBR
```
**Una microoperación = un pulso de reloj** (con bus único).

---

## 2. El bus único

- **Una fuente por pulso**: si dos registros hablan a la vez, se pelean el bus (cortocircuito lógico).

- **Buffers de tres estados**: `EN = 1` → el registro pone su valor; `EN = 0` → **alta impedancia (Z)**.

- **Consecuencia:** `PC ← PC + 1` **no** se hace en un pulso, sino en tres:

```
CP2: PC → Y         CP3: Y + 1 → Z        CP4: Z → PC
```

| | Bus único | 2-3 buses |
|---|---|---|
| Pines / cables | pocos | muchos |
| Pulsos por instrucción | más | menos |
| Ejemplo | **BLUE** (8 pulsos de búsqueda) | CPUs modernas |

---

## 3. Los tres buses

| Bus | Dirección | De qué depende su tamaño | BLUE |
|---|---|---|---|
| **Datos** | bidireccional | ancho de la palabra | 16 bits |
| **Direcciones** | **unidireccional** | `log₂(celdas)` | 12 bits (4096) |
| **Control** | según línea | — | `Read`, `Write`, `Clock`, `IRQ`, `Reset` |

- `2^(bits de dirección)` = espacio de direccionamiento.

- **Bus interno ≠ externo**: el 8088 tiene 16 internos y 8 externos (dos ciclos por acceso de 16 bits).

- Ciclo de bus: dirección → control (`Read`/`Write`) → datos → confirmación.

---

## 4. La ALU

```
A, B  →  [ ALU ]  →  F + flags
             ↑
        S (selección) y Cin
```

**Señales de comunicación entre etapas (acarreo anticipado):**
```
G = A·B          (genera acarreo)
P = A⊕B          (propaga acarreo)
Cout = G + P·Cin
F = P ⊕ Cin
```
Con eso, `C1 = G0 + P0·C0`, `C2 = G1 + P1·G0 + P1·P0·C0`… y la suma de `n` bits no espera la cadena.

---

## 5. Operaciones y flags

| Operación | Expresión | Para qué |
|---|---|---|
| Suma | `F = A + B` | todo |
| **Resta** | `F = A + B' + 1` | restar y comparar |
| Incremento | `F = A + 1` | `PC + 1` |
| AND | `F = A·B` | enmascarar |
| OR | `F = A+B` | encender bits |
| XOR | `F = A⊕B` | invertir / comparar |
| NOT | `F = A'` | complemento a 1 |
| Desplazamiento / rotación | `<<`, `>>`, `ROL`, `ROR` | ×2, ÷2, rotar |

| Flag | Vale 1 si… | Cómo se calcula |
|---|---|---|
| **Z** | resultado = 0 | `NOR` de todos los bits |
| **C** | hubo acarreo (sin signo) | `Cout` del último bit |
| **N** | el signo es negativo | `F(n−1)` |
| **V** | desbordó en complemento a 2 | `Cin_últ ⊕ Cout_últ` |

**`C` ≠ `V`:** `6 − 3` da `C = 1` **sin** error. `C` es sin signo; `V` es con signo.

Ejemplo: `0110 − 0011` ⇒ `0110 + 1100 + 1 = (1)0011` ⇒ `F = 0011`, `Z=0`, `N=0`, `C=1`, `V=0`.

---

## 6. Los registros

| Registro | Función | Ancho (BLUE) | ¿Lo ve el programa? |
|---|---|---|---|
| **PC** | dirección de la **próxima** instrucción | 12 | indirecto (saltos) |
| **MAR** | dirección que va al bus de direcciones | 12 | no |
| **MBR** | dato que va/viene de memoria | 16 | no |
| **IR** | instrucción en curso | 16 | no |
| **AC** | acumulador (operando y resultado) | 16 | **sí** |
| **RB** | base: reubica el programa (`EA = RB + campo`) | 12 | sólo el SO |
| **RIF / RID** | índice de **fuente** / de **destino** | 12 | sí (modos indexados) |
| **SP** | puntero de pila (contexto, interrupciones) | 12 | indirecto |
| **Estado** | `Z C N V` + `SI` + `EMR` + `RUN` | — | sí (saltos y máscara) |

**`SI` vs `EMR`:** `SI` = hay pedido · `EMR` = quiero atenderlo. La interrupción entra con `IRQ · SI · EMR · CP8`.

**Fórmula de dirección con registros:**
```
EA = RB + campo [+ RIF o RID]
```

---

## 7. Recetas de examen

> [!important] Cómo se responde cada tipo de consigna
> **"Escriba las microoperaciones de X"** → una línea por pulso, con `←`, y decir qué señal habilita cada una. **"¿Por qué no se puede en un pulso?"** → un bus, una fuente; nombrar los pasos por `Y` y `Z`. **"Calcule el resultado y los flags"** → hacer la operación en binario, marcar `C` y `V` por separado. **"¿Para qué sirve cada registro?"** → tabla de 9 con una frase cada uno.

| Si te piden… | Qué mostrar sí o sí |
|---|---|
| microoperaciones de la búsqueda | `MAR←PC`, `PC←PC+1`, `MBR←M[MAR]`, `IR←MBR` |
| justificar el buffer 3 estados | que sin `Z` dos registros chocan en el bus |
| tamaños de bus | datos = palabra; direcciones = `log₂ celdas` |
| ALU con `G`/`P` | `G=A·B`, `P=A⊕B`, `Cout = G + P·Cin` |
| diferencia `C` / `V` | acarreo sin signo vs desborde con signo |

---

## 8. Errores que cuestan puntos

- Leer `←` como igualdad y "despejar" en una microoperación.

- Poner **dos transferencias** por pulso con bus único.

- Decir que el bus de direcciones es bidireccional.

- Confundir **MAR** (dirección) con **MBR** (dato).

- Decir que el **PC** apunta a la instrucción **en curso**.

- Confundir `P = A⊕B` con `P = A+B` en el acarreo anticipado.

- Decir que la ALU **guarda** el resultado (lo guarda el AC).

- Mezclar `SI` con `EMR`, o `C` con `V`.

- Decir que el **RB** cambia con cada instrucción (es fijo).

---

## 9. Autoevaluación (con respuesta)

1. ¿Cuántas transferencias por pulso con bus único? → *una*.

2. `PC ← PC + 1` con bus único: ¿cuántos pulsos? → *tres* (a `Y`, ALU, de vuelta a `PC`).

3. Buffer de 3 estados con `EN = 0` → *alta impedancia (desconectado)*.

4. Bits de dirección para 4096 celdas → *12*.

5. `G` y `P` del sumador → *`G = A·B`, `P = A⊕B`*.

6. ¿Qué flag detecta "resultado = 0"? → *`Z`*.

7. `A − B` en la ALU → *negar `B` y `Cin = 1` (`A + B' + 1`)*.

8. ¿Qué registro guarda la instrucción en curso? → *el `IR`*.

9. `RIF` y `RID`: ¿cuál es fuente y cuál destino? → *RIF = fuente, RID = destino*.

10. Interrupción: ¿qué condición la habilita? → *`IRQ · SI · EMR · CP8`*.

---

## Relacionado
[[00 Unidad 3 completa (lectura de corrido)]] · [[00 Unidad 3 — temas y subtemas]] · [[00 Tema 3.1 — índice]] · [[00 Tema 3.2 — índice]] · [[00 Tema 3.3 — índice]] · [[00 Síntesis — Unidad 2]] · [[00 Unidad 4 — temas y subtemas]] · [[00 Tanda 1 — índice]]
