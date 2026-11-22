---
unidad: 3
tipo: concepto
examen: principal
prioridad: maxima
---
# Flujo de información en BLUE (datos y direcciones)

> [!abstract] En una frase
> Toda la información de BLUE viaja por **un solo bus**: en cada pulso, **un** registro pone su contenido
> en el bus (habilitando su salida de tres estados) y **otro** lo toma (activando su `LOAD`). El flujo
> distingue dos tipos de información: **direcciones** (12 bits, van al MAR) y **datos/instrucciones**
> (16 bits, van al MBR/AC/IR).

## La regla de oro del bus único
![[blue_flujo.svg]]

1. **Nunca dos fuentes a la vez**: se cortocircuitan dos salidas. Por eso cada registro tiene salida de
   **tres estados** y sólo una está habilitada por pulso.
2. **Una transferencia por pulso**: `origen → bus → destino` en un pulso. Eso fija la duración de cada
   microoperación y de todo el [[Ciclo de máquina]].
3. **La UC habilita y deshabilita**: `PCout`, `MARin`, `MEMR`, `MBRout`, `ACin`… son las señales que
   "abren el camino" (ver [[Unidad de Control]]).

## Los dos flujos: dirección y dato
### Flujo de **direcciones** (12 bits)
```
PC ──→ MAR ──→ bus de direcciones ──→ MEMORIA
IR(campo dirección) ──→ MAR ──→ bus de direcciones ──→ MEMORIA
RIF/RID ──→ sumador de direcciones ──→ MAR   (en BLUE indexada)
```
- El PC entrega la dirección de la **instrucción** (búsqueda).
- El campo dirección del IR entrega la dirección del **operando** (ejecución: LDA, STA, ADD…).
- Es **unidireccional**: la CPU siempre manda la dirección.

### Flujo de **datos** (16 bits)
```
MEMORIA ──→ MBR ──→ IR        (la instrucción, durante la búsqueda)
MEMORIA ──→ MBR ──→ AC        (el operando, durante LDA/ADD/…)
AC ──→ MBR ──→ MEMORIA        (escritura, durante STA)
AC ──→ ALU ──→ AC             (las operaciones, sin salir a memoria)
```
- Es **bidireccional**: en lectura el dato entra a la CPU, en escritura sale.
- El MBR funciona como **buffer**: sostiene el dato mientras la memoria termina el acceso.

## Las cuatro transferencias que hay que saber de memoria
| Microoperación | Cuándo ocurre | Señales |
|---|---|---|
| `MAR ← PC` | primer pulso de la búsqueda | `PCout`, `MARin` |
| `MBR ← M[MAR]` | al terminar el acceso | `MEMR`, `MBRload` |
| `IR ← MBR` | fin de la búsqueda | `MBRout`, `IRin` |
| `AC ← MBR` | en LDA/ADD/… | `MBRout`, `ACin`, (`ALUop` si opera) |

## Ejemplo: el mismo bus, dos instrucciones distintas
```
LDA 25h        STA 25h             JMP 25h
-----------    ------------        ------------
bus ← IR(dir)  bus ← IR(dir)       bus ← IR(dir)
MAR ← bus      MAR ← bus           PC  ← bus        ← ¡la dirección es dato!
MEMR           bus ← AC
MBR ← M[MAR]   MBR ← bus           (no hay acceso a memoria)
AC  ← MBR      MEMW
```
> [!tip] Detalle que impresiona en el oral
> En `JMP`, la dirección del IR **es el dato** que se carga en el PC: no va al MAR ni a la memoria.
> Ese es el mejor ejemplo de que "dirección" o "dato" **no es el contenido, sino el uso** del registro.

## Cómo responderlo en el final (pregunta principal #1)
1. Dibujar el bus único y los registros (PC, MAR, MBR, IR, AC, ALU, UC, memoria).
2. Enunciar la regla: **una fuente y un destino por pulso**, con tres estados para no cortocircuitar.
3. Describir el **flujo de direcciones** (PC o IR → MAR → memoria, unidireccional) y el **flujo de datos**
   (MBR ↔ AC ↔ ALU, bidireccional).
4. Recorrer un `LDA` y un `STA` señal por señal sobre el dibujo.
5. Cerrar con el ejemplo del `JMP` (la dirección como dato que carga el PC).

## Errores típicos
- Dibujar dos registros escribiendo el bus en el mismo pulso.
- Decir que el bus de direcciones es parte del de datos (son distintos; se pueden multiplexar, pero en BLUE
  son separados).
- Olvidar que el IR se carga desde el MBR y no desde el bus "directo" de la memoria.
- Confundir MAR (dirección) con MBR (dato).

## Relacionado
[[Registros de la CPU]] · [[Ciclo de búsqueda (7 y 8 pulsos)]] · [[Ciclo de ejecución — todas las operaciones]] · [[Máquina BLUE — arquitectura y conjunto de instrucciones]]
