---
unidad: 2
tipo: concepto
examen: complementario
---
# Memoria auxiliar y memoria asociativa

> [!abstract] En dos frases
> **Memoria auxiliar** = almacenamiento masivo no volátil fuera de la CPU (discos magnéticos, cinta, SSD).
> **Memoria asociativa** = memoria que se busca **por contenido** y no por dirección: se le da un dato y
> responde "sí, está en la línea k".

## Memoria auxiliar: disco magnético
Estructura física:
- **Plato** con superficie magnética; **cabezal** de lectura/escritura por superficie.
- **Pista (track):** círculo concéntrico. **Sector:** porción de pista (típico 512 B o 4 KB).
- **Cilindro:** conjunto de pistas de la misma posición en todos los platos (se accede sin mover el cabezal).
- **Tiempo de acceso** = *seek* (mover el cabezal) + *latencia rotacional* (esperar que gire) + transferencia.
  Es del orden de milisegundos: 10⁵ veces más lento que la RAM.

## Cinta magnética
- Acceso **secuencial**: para llegar a un dato hay que pasar por todos los anteriores.
- Enorme capacidad y bajo costo por bit; ideal para **respaldo** y archivo, inútil para acceso aleatorio.

## SSD (para mencionar)
Memoria **flash** (semiconductora, sin partes móviles): acceso aleatorio, sin seek, mucho más rápido que el
disco y resistente a golpes. Sigue siendo mucho más lento que la RAM y tiene desgaste por escritura
(wear leveling). Ver [[Memoria ROM y sus tipos]] (la flash es una ROM regrabable).

| Medio | Tipo de acceso | Tiempo | Uso |
|---|---|---|---|
| Disco magnético | semi-aleatorio (por cilindro) | ~5–10 ms | almacenamiento masivo |
| SSD (flash) | aleatorio | ~0,05–0,2 ms | disco de sistema |
| Cinta | secuencial | segundos | respaldo/archivo |

## Memoria asociativa (CAM)
Una RAM normal busca **por dirección**: le das la dirección y devuelve el dato.
La memoria asociativa busca **por contenido**: le das el dato (la clave) y devuelve la **dirección** (o el
número de línea donde está).

**Organización:** cada celda tiene un registro de clave + lógica de comparación + lógica de coincidencia.
- **Lógica de coincidencia:** cada línea compara su clave con la buscada (XNOR de todos los bits ⇒ 1 si
  son iguales) y activa su señal de match. Una OR de todos los match indica "hay coincidencia".
- **Operación de lectura:** se aplica la clave y la memoria devuelve el contenido de la línea que coincide
  (o el índice de esa línea).
- **Operación de escritura:** se aplica la clave y el dato; si la clave existe se actualiza, si no se
  escribe en una línea libre (o se reemplaza).

**Ventaja:** búsqueda en un solo ciclo, en paralelo, sin importar el tamaño.
**Desventaja:** mucha circuitería por celda (comparador) ⇒ carísima y de baja densidad.

## Dónde aparece en la materia
1. **TLB** de la [[Memoria virtual y administración de memoria]]: traducciones de página.
2. **Caché asociativa**: en el [[Memoria caché|mapeo asociativo]] se compara la etiqueta contra todas las
   líneas a la vez.
3. **Tablas de ruteo / buffers de periféricos**: buscar si un paquete ya fue procesado.

## Cómo responderlo en el final
1. Memoria auxiliar: disco (pistas, sectores, cilindros, tiempos), cinta (secuencial), SSD.
2. Memoria asociativa: definición (búsqueda por contenido), organización (clave + comparador + lógica de
   coincidencia), lectura y escritura.
3. Aplicación: TLB y caché asociativa.
4. Comparar: la auxiliar resuelve **capacidad**, la asociativa resuelve **velocidad de búsqueda**.

## Errores típicos
- Decir que la cinta es de acceso aleatorio.
- Confundir memoria asociativa con "memoria que se asocia a la caché".
- Olvidar que la asociativa **no** es más rápida por tecnología sino por buscar en paralelo.

## Relacionado
[[Jerarquía de memorias]] · [[Memoria caché]] · [[Memoria virtual y administración de memoria]]
