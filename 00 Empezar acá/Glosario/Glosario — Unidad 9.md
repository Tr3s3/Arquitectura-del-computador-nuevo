---
tipo: glosario
unidad: 9
---
# Glosario — Unidad 9: hardware aritmético

> [!abstract] Qué hay acá
> Las **15 fichas** de la unidad: complemento a 2 y desborde, acarreo anticipado, los tres algoritmos de
> multiplicación, los dos de división, punto flotante e IEEE 754 y la aritmética decimal. Índice alfabético en
> [[Glosario]].

### Complemento a 2
**Qué es.** Representación de enteros con signo: el negativo se obtiene **invirtiendo todos los bits y sumando 1**.
**Para qué sirve.** Restar con el **mismo sumador** que suma y tener una sola representación del cero.
**Características.** · Con `n` bits el rango es **−2ⁿ⁻¹ … +2ⁿ⁻¹−1** (4 bits: −8 a +7) · el bit más significativo
pesa negativo · `+7 + 1 = 1000` en 4 bits es **desborde**.
**Se estudia en** [[9.1.1 Complemento a 2 y desbordamiento]].

### Desbordamiento (overflow, V)
**Qué es.** El resultado **no entra** en `n` bits con signo: pasó de `+2ⁿ⁻¹−1` o bajó de `−2ⁿ⁻¹`.
**Para qué sirve.** Detectar que el resultado no sirve antes de seguir operando.
**Características.** · `V = Cin ⊕ Cout` del **bit de signo** · **no** es lo mismo que el acarreo `C` (que es
aritmética **sin** signo) · dos positivos que dan negativo (o al revés) ⇒ `V = 1`.
**Se estudia en** [[9.1.1 Complemento a 2 y desbordamiento]].

### Acarreo anticipado (carry look-ahead)
**Qué es.** Generar los acarreos **en paralelo** con lógica `G` (genera) y `P` (propaga) en vez de esperar la
cascada.
**Para qué sirve.** Que la suma no se vuelva lenta al crecer `n`: elimina la espera de la cadena.
**Características.** · `G = A·B`, `P = A ⊕ B`, `Cout = G + P·Cin` · un **CLA** de 4 bits hace la suma en 2 niveles ·
se jerarquiza (bloques de 4) · más compuertas, menos retardo.
**Se estudia en** [[9.1.2 Acarreo anticipado (G y P)]].

### Multiplicación por sumas y desplazamientos
**Qué es.** Multiplicar como en decimal: por cada bit del multiplicador, se suma el multiplicando (si el bit es 1)
y se desplaza.
**Para qué sirve.** Es el algoritmo **base**: el que se puede hacer con un sumador y dos registros.
**Características.** · `n` ciclos (una vuelta por bit) · el producto queda en `A:Q` (doble ancho: `2n` bits) ·
13 × 11: `0000/1011 → 0110/1101 → 1001/1110 → 0100/1111 → 1000/1111` = **143**.
**Se estudia en** [[9.2.1 Sumas y desplazamientos]].

### Algoritmo de Booth
**Qué es.** Multiplicación **con signo sin separar los signos**: mira el par `(Q0, Q−1)` y decide sumar, restar o
nada.
**Para qué sirve.** Multiplicar números en complemento a 2 directamente, con menos sumas cuando hay tiras de unos.
**Características.** · `01 ⇒ A + M` · `10 ⇒ A − M` · `00` y `11 ⇒ nada` · después se desplaza `(A, Q, Q−1)` a la
derecha **aritméticamente** · `(−5) × 3 = 1111 0001` = **−15**.
**Se estudia en** [[9.2.2 Algoritmo de Booth]].

### Arreglo multiplicador
**Qué es.** Multiplicador **combinacional**: `n²` celdas que suman todos los productos parciales de una vez.
**Para qué sirve.** Producto en un solo tiempo de propagación, sin reloj: el más rápido.
**Características.** · `n²` sumadores (4 bits → 16 celdas; 32 bits → 1024) · retardo ≈ `2n` niveles de compuerta ·
se puede **segmentar** para un producto por ciclo.
**Se estudia en** [[9.2.3 Arreglo multiplicador]].

### División con restauración
**Qué es.** Algoritmo de división que resta y, **si el resto da negativo, lo restaura** (vuelve a sumar el divisor)
antes de desplazar.
**Para qué sirve.** Es el más simple de entender y el más usado para explicar el proceso.
**Características.** · `n` vueltas, cada una: desplazar, restar, decidir, poner el bit del cociente ·
7 ÷ 3 ⇒ cociente `0010` = 2, resto `0001` = 1 · pierde tiempo restaurando.
**Se estudia en** [[9.3.1 Restauración y no restauración]].

### División sin restauración
**Qué es.** Variante que **no** deshace la resta: si el resto quedó negativo, en la vuelta siguiente **suma** en vez
de restar.
**Para qué sirve.** Hacer la división con **la mitad de operaciones** de suma/resta.
**Características.** · Mismo resultado, menos operaciones · el signo del resto indica qué hacer en la vuelta
siguiente · más difícil de trazar a mano (es lo que se pregunta como "por qué conviene").
**Se estudia en** [[9.3.1 Restauración y no restauración]].

### División con signo y sobreflujo
**Qué es.** Regla de signos (`cociente` = XOR de los signos; `resto` con el signo del dividendo) y el caso en que el
cociente **no entra** en `n` bits.
**Para qué sirve.** Extender la división a enteros con signo y saber cuándo la operación es imposible.
**Características.** · Sobreflujo si `|dividendo| ≥ |divisor| × 2ⁿ⁻¹` (ej.: 8 ÷ 1 en 4 bits) · división por cero ⇒
excepción de la CPU · se detecta **antes**, comparando los bits altos.
**Se estudia en** [[9.3.2 Sobreflujo y división con signo]].

### Punto flotante
**Qué es.** Formato `signo · exponente · mantisa` que representa números con coma "que se mueve": `(−1)^S × M × 2^E`.
**Para qué sirve.** Representar a la vez números **muy grandes y muy chicos** con la misma cantidad de bits.
**Características.** · Rango lo da el exponente, precisión la mantisa · operar exige **normalizar y redondear** ·
sumar requiere **alinear** exponentes.
**Se estudia en** [[9.4.1 Formato, normalización y operaciones]].

### Normalización
**Qué es.** Dejar la mantisa con forma fija (`1.xxx` en IEEE 754; `0,1xxx` con `1/2 ≤ M < 1` en la convención de la
cátedra) ajustando el exponente.
**Para qué sirve.** Que la representación sea **única** y no se pierdan bits significativos.
**Características.** · Correr la coma a la izquierda **suma** al exponente; a la derecha **resta** ·
gana un bit de precisión (el 1 implícito en IEEE) · después de operar **siempre** se normaliza.
**Se estudia en** [[9.4.1 Formato, normalización y operaciones]].

### Mantisa y exponente
**Qué es.** **Mantisa**: los dígitos significativos. **Exponente**: la escala (potencia de 2).
**Para qué sirve.** Separar precisión (mantisa) de rango (exponente).
**Características.** · La mantisa es una fracción normalizada · el exponente se guarda **con exceso** para no
necesitar signo · en IEEE 754 simple: 1 + 8 + 23; en doble: 1 + 11 + 52.
**Se estudia en** [[9.4.2 IEEE 754]].

### Exceso (bias) — exceso 64, exceso 127
**Qué es.** Forma de guardar el exponente sumándole una constante, para que todos los valores sean positivos:
`E_guardado = e + exceso`.
**Para qué sirve.** Evitar el signo en el exponente y poder **comparar** números como enteros.
**Características.** · La cátedra usa **exceso 2ⁿ⁻¹**: **64** con 7 bits y **128** con 8 bits · IEEE 754 usa
**127** en simple y **1023** en doble · multiplicar: `Ep = E1 + E2 − 64 − K`; dividir: `Ed = E1 − E2 + 64 + K`.
**Se estudia en** [[9.4.1 Formato, normalización y operaciones]].

### IEEE 754
**Qué es.** El estándar de punto flotante: simple (32 bits: **1 + 8 + 23**, exceso 127) y doble (64 bits:
**1 + 11 + 52**, exceso 1023).
**Para qué sirve.** Que los números se puedan intercambiar entre máquinas y que el redondeo sea predecible.
**Características.** · El `1` de la mantisa es **implícito** (se gana un bit) · `E = 0` ⇒ desnormalizado o cero ·
`E = 255` ⇒ infinito o `NaN` · `10,0 = 0 10000010 0100…` = `0x41200000`.
**Se estudia en** [[9.4.2 IEEE 754]].

### BCD y corrección +6
**Qué es.** Aritmética **decimal** con dígitos BCD; cuando un nible pasa de 9 o hay acarreo, se le **suma 6**.
**Para qué sirve.** Sumar en decimal exacto (calculadoras, contadores, displays) sin errores de redondeo binario.
**Características.** · `+0110` salta los 6 códigos inválidos (`1010` a `1111`) · `27 + 35`: `0101 1100` + `0110`
⇒ `0110 0010` = 62 · el 8086 lo hace con **DAA** · se desperdicia el 37,5 % de las combinaciones.
**Se estudia en** [[9.5.1 Suma decimal corregida]].
