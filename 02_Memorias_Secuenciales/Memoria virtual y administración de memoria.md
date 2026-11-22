---
unidad: 2
tipo: concepto
examen: complementario
---
# Memoria virtual y administración de memoria

> [!abstract] En una frase
> La memoria virtual da a cada programa un **espacio de direcciones propio y contiguo** (las *direcciones
> virtuales*), que el hardware traduce a **direcciones físicas** reales mediante **tablas de páginas**.
> Permite programas más grandes que la RAM, aislamiento entre procesos y protección.

## Dos espacios
- **Espacio de direccionamiento (virtual):** lo que ve el programa. Puede ser enorme (2³², 2⁶⁴).
- **Espacio de memoria (físico):** la RAM realmente instalada, mucho más chica.
El mapeo virtual → físico lo hace la **MMU** (unidad de administración de memoria) en cada acceso.

## Paginación
El espacio virtual se divide en **páginas** de tamaño fijo (4 KB típico) y la memoria física en
**marcos** del mismo tamaño. Una página puede estar en cualquier marco.

La dirección virtual se parte: `nº de página virtual (VPN) | desplazamiento`.
La traducción se hace con la **tabla de páginas**: por cada página virtual guarda el **marco físico**,
más bits de control (presente, modificada/dirty, de acceso, permisos).

![cache_mapeos](assets/cache_mapeos.svg)

## Tabla de páginas asociativa (TLB)
La tabla de páginas está en memoria ⇒ cada acceso costaría dos accesos. Para evitarlo se usa la **TLB**
(translation lookaside buffer): una **memoria asociativa** pequeña y rápida (dentro de la MMU) que guarda
las últimas traducciones.
- **TLB hit** ⇒ traducción en un ciclo.
- **TLB miss** ⇒ se consulta la tabla de páginas (y se recarga la TLB).
Es exactamente la misma idea de la [[Memoria caché]], pero cachea **traducciones** en lugar de datos.

## Fallo de página y sustitución
Si la página pedida **no está en RAM** (bit *presente* = 0):
1. Se genera una **interrupción de fallo de página** (ver [[Interrupciones y entrada-salida]]).
2. El SO elige una **víctima** y la lleva a disco si está modificada.
3. Trae la página pedida del disco a un marco libre (o al de la víctima).
4. Actualiza la tabla de páginas y reintenta la instrucción.

**Algoritmos de sustitución:** FIFO, **LRU** (o su aproximación con "bits de referencia"), reloj, óptimo
(sólo teórico). Con muchas páginas activas y poca RAM aparece **thrashing**: el sistema pasa más tiempo
cambiando páginas que ejecutando.

## Segmentación y mapeo página-segmentado
- **Segmentación:** se divide por **unidades lógicas** de tamaño variable (código, datos, pila). La dirección
  es `segmento | desplazamiento` y la tabla de segmentos guarda **base + límite** (esto es lo que da
  **protección** natural).
- **Página segmentada:** cada segmento se pagina, de modo que se tienen las ventajas de los dos: protección
  lógica del segmento + eliminación de la fragmentación externa del paginado. Es el modelo de x86.

## Protección de memoria
- Bits en la entrada de la tabla: **presente**, **lectura/escritura**, **ejecutable**, **modo usuario/sistema**.
- **Base y límite** por segmento: si el desplazamiento supera el límite ⇒ trap.
- Cualquier violación (escribir una página de sólo lectura, acceder a memoria de otro proceso) genera una
  **excepción/interrupción** que atiende el SO. Así un programa no puede pisar a otro ni al sistema.

## Cómo responderlo en el final
1. Definir los dos espacios y el objetivo (tamaño, aislamiento, protección).
2. Paginación: páginas/marcos, tabla de páginas, campos de la dirección.
3. TLB (memoria asociativa) y fallo de página con el rol del SO.
4. Sustitución de páginas (LRU/FIFO) y thrashing.
5. Segmentación + paginación y protección (bits de permiso, base+límite).

## Errores típicos
- Confundir página (virtual) con marco (físico).
- Decir que la tabla de páginas está en la caché: está en memoria; la TLB es la que la cachea.
- Olvidar que la memoria virtual también **protege**, no sólo "agranda" la memoria.

## Relacionado
[[Jerarquía de memorias]] · [[Memoria caché]] · [[Memoria auxiliar y memoria asociativa]] · [[Interrupciones y entrada-salida]]
