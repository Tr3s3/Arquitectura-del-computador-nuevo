---
unidad: 2
tipo: concepto
examen: secundaria
---
# Codificador

> [!abstract] En una frase
> Hace lo inverso del [[Decodificador]]: recibe **2ⁿ líneas** (de las cuales una está activa) y entrega
> en la salida el **código binario** de n bits que identifica a esa línea.

## Decodificador vs codificador
| | Decodificador | Codificador |
|---|---|---|
| Entradas | n | 2ⁿ |
| Salidas | 2ⁿ | n |
| Función | código → línea activa | línea activa → código |
| Uso típico | seleccionar memoria/registro | leer un teclado, priorizar pedidos |

## Codificador 8 a 3 (sin prioridad)
Entradas E0…E7, salidas A2 A1 A0. Si está activa Ei, la salida es el binario de i:

`A2 = E4 + E5 + E6 + E7`   `A1 = E2 + E3 + E6 + E7`   `A0 = E1 + E3 + E5 + E7`

| Entrada activa | A2 A1 A0 |
|---|---|
| E0 | 0 0 0 |
| E1 | 0 0 1 |
| E2 | 0 1 0 |
| E3 | 0 1 1 |
| E4 | 1 0 0 |
| E5 | 1 0 1 |
| E6 | 1 1 0 |
| E7 | 1 1 1 |

**Problema:** si se activan dos entradas a la vez, la salida es la OR de los códigos = basura.
Por eso en la práctica se usa un **codificador con prioridad**.

## Codificador con prioridad (74LS148)
Si hay varias entradas activas, la salida corresponde a la de **mayor prioridad** (la de índice más alto),
y se agregan dos salidas auxiliares:
- **GS / EO** (group select): indica que hay al menos una entrada activa (nada activo ⇒ el código no vale).
- **EI / EO** (enable in / enable out): permite **encadenar** varios codificadores (el de menor prioridad
  se habilita sólo si el anterior no tuvo pedidos).

## Aplicaciones
- **Teclado**: al presionar una tecla se activa una línea y el codificador entrega el código ASCII/posición
  y genera la interrupción (ver [[Interrupciones y entrada-salida]]).
- **Árbitro de interrupciones / de bus**: con prioridad, decide cuál de varias fuentes que piden atención
  se atiende primero.
- **Compresión de datos**: pasar de "one-hot" (una línea por valor) a binario.

> [!example] Del TP7
> El [[TP7 Codificadores y multiplexores|TP7]] pide el **4x2** y el **8x3**; resolverlos es directo: una OR
> por cada bit de salida (`X = D4+D5+D6+D7`, etc.).

## Cómo responderlo en el final
Definir (inverso del decodificador) → tabla del 8→3 → ecuaciones → decir que en la práctica se usa **con
prioridad** (GS y encadenamiento) → mencionar la aplicación al teclado y al árbitro de interrupciones.

## Errores típicos
- Suponer que funciona bien con varias entradas activas (sólo con prioridad).
- Confundir la cantidad de líneas: el codificador **reduce** líneas (2ⁿ → n).

## Relacionado
[[Decodificador]] · [[Multiplexor]] · [[Interrupciones y entrada-salida]]
