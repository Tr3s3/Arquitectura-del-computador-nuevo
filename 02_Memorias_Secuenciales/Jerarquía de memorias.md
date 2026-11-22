---
unidad: 2
tipo: concepto
examen: secundario
prioridad: alta
---
# Jerarquía de memorias

> [!note] Si es la primera vez que ves esto
> Hay un triángulo imposible: queremos memorias **grandes** (para guardar mucho), **rápidas** (para no
> esperar) y **baratas**. No existe una que sea las tres. La solución es usar **varias a la vez**, ordenadas
> en pisos: arriba, poquita y carísima pero instantánea; abajo, enorme y baratísima pero lenta. El sistema
> funciona porque los programas **repiten** (localidad): si el dato que necesito está arriba casi siempre, el
> promedio se parece a la velocidad de arriba con el costo de abajo. Es el mismo truco que tener heladera
> chica en la cocina y depósito grande en el fondo.

> [!abstract] En una frase
> Como no existe una memoria que sea a la vez **grande, rápida y barata**, el computador usa **varios
> niveles**: chicos y rápidos cerca de la CPU (registros, caché) y grandes y lentos lejos (RAM, disco,
> cinta), y funciona porque los programas tienen **localidad**.

## El problema que resuelve
- Los registros son rapidísimos pero guardan bytes.
- La RAM es grande pero tarda ~100 ns; el disco, milisegundos.
- La CPU puede ejecutar una instrucción por ns: si esperara al disco, perdería millones de ciclos.
La jerarquía explota el hecho de que **la CPU no accede a todo por igual**.

## Los principios de localidad
1. **Localidad temporal**: si se accedió a una dirección, es muy probable que se vuelva a acceder pronto
   (los **bucles**: la misma instrucción una y otra vez).
2. **Localidad espacial**: si se accedió a una dirección, es probable que se acceda a las **vecinas**
   (los programas son secuenciales; los arreglos se recorren en orden).

De ahí que convenga traer **bloques** de instrucciones/datos, no palabras sueltas: eso es exactamente lo
que hace la [[Memoria caché]].

## Los niveles
![jerarquia_memorias](../assets/jerarquia_memorias.svg)

| Nivel | Tecnología | Tiempo típico | Capacidad | Administrado por |
|---|---|---|---|---|
| Registros | flip-flops | ~1 ns | decenas–cientos de bytes | el compilador/programador |
| Caché L1 | SRAM | 1–2 ns | 16–64 KB | hardware |
| Caché L2/L3 | SRAM | 5–15 ns | MB | hardware |
| Memoria principal | DRAM | 50–100 ns | GB | SO + hardware |
| Secundaria | SSD / disco | 0,1 ms / 10 ms | TB | SO |
| Terciaria | cinta, respaldo | segundos | TB | operador |

**Regla de la pirámide:** al bajar un nivel, el tiempo de acceso y el costo por bit suben/bajan en
órdenes de magnitud, y la capacidad crece. Hacia arriba: más rápida, más cara por bit, más chica.

## Quién administra cada salto
- Registros ↔ caché ↔ RAM: **hardware** (la caché es transparente al programa).
- RAM ↔ disco: **sistema operativo**, con [[Memoria virtual y administración de memoria|memoria virtual]]
  y paginación.
- Disco ↔ cinta: el operador o el sistema de respaldo.

## Por qué funciona (lo que hay que decir)
Porque el **costo medio de acceso** se acerca al del nivel rápido: si el 95 % de los accesos los resuelve
la caché, el tiempo medio es ≈ 0,95·(1 ns) + 0,05·(100 ns) ≈ 6 ns, mucho mejor que 100 ns. Se paga el
precio de un sistema de control (comparadores, etiquetas, políticas de reemplazo) a cambio de una mejora
grande.

> [!example] Cálculo típico
> T caché = 2 ns, T RAM = 80 ns, acierto = 90 % ⇒ T medio = 0,9·2 + 0,1·80 = **9,8 ns**.
> Con acierto del 99 % ⇒ 0,99·2 + 0,01·80 = **2,78 ns**. Se ve por qué se pelea por cada punto de acierto.

## Cómo responderlo en el final
1. Definir jerarquía y el objetivo (combinar velocidad, capacidad y costo).
2. Dibujar la pirámide con los niveles y sus tiempos.
3. Explicar los dos principios de localidad (son la justificación física).
4. Decir quién administra cada nivel (hardware / SO) y dar un número: registros ~1 ns, DRAM ~100 ns,
   disco ~10 ms.
5. Cerrar con el cálculo del tiempo medio y la idea de que la caché es **transparente**.

## Errores típicos
- Decir "toda la memoria es igual para la CPU" (los tiempos difieren en 10⁶).
- Confundir jerarquía con "tipos de memoria" (es una organización por niveles).
- Olvidar la localidad: sin ella la jerarquía no mejora nada.

## Relacionado
[[Memoria caché]] · [[Memoria virtual y administración de memoria]] · [[Celda elemental de memoria]] · [[Técnicas para aumentar la velocidad]]
