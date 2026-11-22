---
unidad: 3
tipo: concepto
examen: principal
prioridad: maxima
---
# Espacio de direccionamiento y cálculo de CodOp-Dirección

> [!abstract] En una frase
> El **espacio de direccionamiento** es la cantidad de posiciones que puedo direccionar, y sale de dividir
> la capacidad de memoria por el tamaño de celda. Esos bits de dirección **se los tengo que sacar de algún
> lado** en la palabra instrucción: por eso `bits de CodOp = bits de palabra − bits de dirección`.

## Las tres cuentas (la receta)
```
1) nº de celdas      = capacidad de memoria  /  tamaño de celda
2) bits de dirección = log₂ (nº de celdas)
3) bits de CodOp     = (bits de la palabra)  −  (bits de dirección)
```

Con potencias de 2 va rápido: **1 KB = 2¹⁰ B · 1 MB = 2²⁰ B · 1 GB = 2³⁰ B** y
**direcciones = exponente**. Y `log₂(nº de celdas)` = el exponente de esa potencia.

## Ejemplo completo (paso a paso)
**Memoria de 512 MB con celdas de 4 bytes**
1. `512 MB / 4 B = 128 M celdas`
2. `128 M = 2⁷ · 2²⁰ = 2²⁷` ⇒ **27 bits de dirección**
3. La palabra es de `4 B = 32 bits` ⇒ `CodOp = 32 − 27 =` **5 bits**

| CodOp | Dirección |
|---|---|
| 5 bits | 27 bits |

**Interpretación:** con 5 bits de CodOp hay **32 operaciones** posibles y con 27 bits de dirección se
direccionan 128 millones de celdas.

## Ejemplos resueltos (los del TP18 y más)
| Memoria | Celda | Nº de celdas | Bits de dirección | Palabra | **CodOp** |
|---|---|---|---|---|---|
| 512 MB | 4 B | 2²⁹/2² = 2²⁷ | 27 | 32 bits | **5** |
| 2 GB | 8 B | 2³¹/2³ = 2²⁸ | 28 | 64 bits | **36** |
| 1 GB | 4 B | 2³⁰/2² = 2²⁸ | 28 | 32 bits | **4** |
| 128 MB | 2 B | 2²⁷/2¹ = 2²⁶ | 26 | 16 bits | **no alcanza** |
| 64 MB | 1 B | 2²⁶/2⁰ = 2²⁶ | 26 | 8 bits | **no alcanza** |

> [!important] El concepto que hay que saber explicar
> Cuando la celda es **muy chica** (1 o 2 bytes) no quedan bits para el CodOp: la palabra instrucción tiene
> que contener **la dirección del operando**, y si la dirección sola ocupa más bits que la palabra, es
> **imposible**. Soluciones: **agrandar la celda** (que la palabra sea más ancha), usar **modos de
> direccionamiento** que acorten la dirección (indexado, relativo), o hacer **varios accesos** con una
> instrucción de varias palabras (es lo que pasa en TP17: instrucción de 2 bytes en celdas de 1 byte).

## Relación con el resto de la materia
- **Formato de instrucción**: en BLUE la palabra es de 16 bits y la memoria de 4096 palabras ⇒
  `12 bits de dirección` ⇒ `4 bits de CodOp` (16 instrucciones). Ver
  [[Máquina BLUE — arquitectura y conjunto de instrucciones]] y [[Formato de la instrucción (4 formatos)]].
- **Ancho del bus de direcciones**: es lo que fija el espacio direccionable (`2ⁿ × tamaño de celda`).
  Ver [[Estructura básica de un computador]].
- **Palabra vs celda**: si la celda es de 1 byte y la palabra de 4, la palabra ocupa **4 celdas
  consecutivas** y el CPU necesita **varios accesos** (o un bus más ancho) para traerla.
- **Jerarquía**: la memoria principal se direcciona así; la caché y la memoria virtual agregan otro nivel de
  traducción. Ver [[Memoria caché]] y [[Memoria virtual y administración de memoria]].

## Cómo responderlo en el final
1. Definir espacio de direccionamiento = cantidad de posiciones direccionables.
2. Hacer la cuenta **en voz alta**: dividir por el tamaño de celda, expresar en potencia de 2, sacar el
   exponente.
3. Decir que el CodOp es lo que queda: `palabra − dirección`, y **qué implica** (cuántas operaciones
   distintas puedo codificar).
4. Si el resultado es negativo: explicar por qué (la dirección no entra en la palabra) y las soluciones.
5. Cerrar con el ejemplo de BLUE (4096 palabras de 16 bits ⇒ 12 + 4).

## Errores típicos
- Dividir por el tamaño de palabra en bits en lugar de **bytes** (o mezclar MB con Mb).
- Confundir 1 GB con 1000 MB (usá 2³⁰).
- Olvidar que la cuenta es `palabra − dirección` y no al revés.
- No advertir cuando el resultado da **negativo**: eso **es** la respuesta.

## Relacionado
[[TP18 Direccionamiento de memoria]] · [[TP17 Formato básico de instrucciones]] · [[Formato de la instrucción (4 formatos)]] · [[Memoria RAM 8x3]]
