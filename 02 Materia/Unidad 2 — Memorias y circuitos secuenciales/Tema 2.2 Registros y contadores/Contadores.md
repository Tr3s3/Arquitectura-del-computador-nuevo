---
unidad: 2
tipo: concepto
examen: secundaria
---
# Contadores

> [!abstract] En una frase
> Un contador es un registro que, con cada pulso de reloj, pasa al **estado siguiente** de una secuencia definida (normalmente 0,1,2,3… y vuelve a 0). Puede ser **asíncrono** (los FF se disparan en cadena) o **síncrono** (todos con el mismo reloj) y puede tener **carga en paralelo**.

## Contador asíncrono (de ripple)
Se encadenan flip-flops **T** (o J-K con J=K=1): el reloj del primero es el CLK del sistema, y la salida Q de cada uno es el reloj del siguiente.

- Con **4 flip-flops** se cuentan **2⁴ = 16 estados** (0000 a 1111) y vuelve a 0000 ⇒ **módulo 16**.

- La cuenta "avanza" porque cada FF conmuta cuando el anterior pasa de 1 a 0 (en la transición de bajada).

- **Ventaja:** muy simple. **Desventaja:** el retardo se acumula (los últimos bits cambian más tarde); aparecen estados intermedios falsos y el contador es lento. A alta frecuencia, los pulsos se "atrasan" y el valor leído puede no ser el real (**glitch**).

## Contador síncrono
Todos los flip-flops reciben el **mismo reloj** y las entradas J/K (o D) se calculan con compuertas combinacionales a partir de las salidas de los demás, de modo que **todos cambian en el mismo flanco**.

Con FF tipo T: `T0 = 1`, `T1 = Q0`, `T2 = Q0·Q1`, `T3 = Q0·Q1·Q2`, … (cada bit conmuta cuando todos los anteriores valen 1). Con lógica más grande se puede hacer cualquier secuencia (contador de décadas, módulo N, Gray).

| Tipo | Reloj | Retardo | Uso |
|---|---|---|---|
| Asíncrono | en cascada | alto, acumulativo | divisores de frecuencia, relojes |
| Síncrono | único, simultáneo | bajo y uniforme | contadores de programa, PC, temporizadores |

## Contador binario con carga en paralelo
Es el que combina dos cosas: **contar** o **cargar un valor** (y desde ahí seguir contando). Se arma con un registro de flip-flops D + un **sumador** + un [[Multiplexor]] en la entrada:

```
        ┌──────────────┐   +1
  LOAD →│ MUX 2:1      │→[registro]→ salida (cuenta)
  dato →│ (carga/cont) │      ↑
        └──────────────┘     CLK
```

- `LOAD = 1` ⇒ entra el dato externo (carga en paralelo).

- `LOAD = 0` ⇒ entra `valor + 1` (el sumador incrementa cada pulso).

Es exactamente el esquema del **PC (contador de programa)**: normalmente PC ← PC + 1, y si hay un salto se **carga** la dirección destino. En BLUE, el incremento del PC se hace en un pulso del [[Ciclo de búsqueda (7 y 8 pulsos)|ciclo de búsqueda]].

> [!tip] Contador módulo N
> Para contar 0…N-1 se detecta el estado N con una compuerta (NAND de los bits que deben ser 1) y se usa esa señal para **CLEAR** o para **cargar** 0 en el próximo flanco. Ejemplo: módulo 10 (década) con 4 FF se resetea al llegar a 1010.

## Aplicaciones

- Contador de programa (PC) de la CPU.

- Temporizadores y divisores de frecuencia.

- Direcciones secuenciales en memoria (DMA, refresco de la DRAM).

- Contadores de eventos en periféricos (medir pulsos de un encoder).

## Cómo responderlo en el final

1. Definición (registro + secuencia).

2. Asíncrono: FF T en cascada, módulo 2ⁿ, retardo acumulado; síncrono: reloj común y lógica de habilitación.

3. Carga en paralelo: MUX (carga / incremento) + sumador ⇒ esquema del PC.

4. Aplicación concreta: el PC de la [[Máquina BLUE — arquitectura y conjunto de instrucciones|BLUE]].

## Errores típicos

- Decir que un contador asíncrono de 4 FF cuenta hasta 15 inclusive y "se detiene": **vuelve a 0** (módulo 16).

- Confundir contador con registro: el registro mantiene; el contador cambia solo con el reloj.

- Olvidar la señal de CLEAR/carga al diseñar un módulo N.

## Relacionado
[[Registros]] · [[Flip-Flops SR, D, JK y T]] · [[Sumador completo]] · [[Registros de la CPU]]
