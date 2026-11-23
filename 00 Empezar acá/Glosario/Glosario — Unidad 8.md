---
tipo: glosario
unidad: 8
---
# Glosario — Unidad 8: paralelismo

> [!abstract] Qué hay acá
> Las **16 fichas** de la unidad: pipeline de datos, procesamiento vectorial y SIMD, bancos de memoria y
> multiprocesadores. Índice alfabético en [[Glosario]].

### Paralelismo
**Qué es.** Hacer **varias** operaciones a la vez, en lugar de una tras otra.
**Para qué sirve.** Superar el techo que impone la frecuencia del reloj.
**Características.** · Niveles: **bit** (ancho de palabra), **instrucción** (pipeline/superscalar), **dato**
(SIMD/vectorial), **tarea** (multicore/cluster) · exige dependencias resueltas y sincronización ·
el límite lo pone la ley de **Amdahl**.
**Se estudia en** [[8.1.1 Etapas segmentadas y suma de vectores]].

### Segmentación de operaciones (pipelining de datos)
**Qué es.** Aplicar la idea del pipeline a un **cálculo repetitivo** sobre un vector: una suma entra a la etapa 1
mientras la anterior está en la 2.
**Para qué sirve.** Sumar vectores en tiempo casi constante: `T = k + (n − 1)`.
**Características.** · Necesita **muchos datos independientes** · las etapas son de suma/resta/multiplicación ·
un conflicto entre etapas se llama **riesgo de datos** y se resuelve con encadenamiento.
**Se estudia en** [[8.1.1 Etapas segmentadas y suma de vectores]].

### Encadenamiento (chaining)
**Qué es.** Permitir que la salida de una operación entre a otra **sin pasar por los registros**, apenas está
disponible.
**Para qué sirve.** Encadenar operaciones dependientes (producto y suma) sin esperar el ciclo completo: es el
`FMA` de las GPU.
**Características.** · Reduce el tiempo de un cálculo dependiente a casi el de una sola operación · requiere
hardware que detecte el encadenamiento · sin encadenamiento hay que esperar `k` ciclos entre operaciones.
**Se estudia en** [[8.1.2 Encadenamiento y speedup]].

### Procesamiento vectorial y registro vectorial
**Qué es.** Instrucciones que operan sobre **muchos** elementos con un solo código de operación, usando registros
anchos (por ejemplo 128, 256 o 512 bits).
**Para qué sirve.** Procesar arreglos con **una** instrucción por grupo de datos: imagen, video, ciencia.
**Características.** · Un registro de 256 bits con datos de 32 bits = **8 lanes** (8 operaciones a la vez) ·
el compilador debe **vectorizar** el bucle · es la base de SSE/AVX y de las GPU.
**Se estudia en** [[8.2.1 SIMD, registros vectoriales y GPU]].

### SIMD
**Qué es.** *Single Instruction, Multiple Data*: **una** instrucción, **muchos** datos en paralelo.
**Para qué sirve.** Multiplicar el rendimiento sin multiplicar las instrucciones: 4 sumas en el tiempo de 1.
**Características.** · Es **paralelismo de datos** · lo usan las GPU, los procesadores vectoriales y los
DSP · necesita datos contiguos y de la misma operación.
**Se estudia en** [[8.2.1 SIMD, registros vectoriales y GPU]].

### Clasificación de Flynn
**Qué es.** Las cuatro clases de máquinas según cuántas **instrucciones** y cuántos **datos** procesan por vez:
**SISD**, **SIMD**, **MISD** y **MIMD**.
**Para qué sirve.** Clasificar cualquier máquina en una pregunta de examen con sólo contar instrucciones y datos.
**Características.** · **SISD**: la BLUE · **SIMD**: GPU/vectorial · **MISD**: casi inexistente (redundancia) ·
**MIMD**: multicore y clusters.
**Se estudia en** [[8.2.2 Flynn, arreglos SIMD y conectados]].

### Arreglo conectado (network)
**Qué es.** Red de procesadores conectados entre vecinos (malla, hipercubo, árbol) que intercambian datos.
**Para qué sirve.** Escalar a cientos de procesadores con un costo de comunicación conocido.
**Características.** · El costo depende de la **distancia** (número de saltos) · malla 2D: cada nodo con 4
vecinos · más conexiones = más rápido y más caro.
**Se estudia en** [[8.2.2 Flynn, arreglos SIMD y conectados]].

### Multiplicación de matrices y paralelismo
**Qué es.** El cálculo clásico `C = A × B` (cada elemento es un producto escalar) usado para medir paralelismo.
**Para qué sirve.** Mostrar las tres formas: por **filas** (paralelismo de datos), por **bloques** (localidad) y
distribuida (por nodos).
**Características.** · `n³` multiplicaciones: es `O(n³)`, ideal para repartir · se acelera con SIMD, con bancos y
con caché (bloques) · el cuello es el acceso a memoria, no la ALU.
**Se estudia en** [[8.2.3 Multiplicación de matrices]].

### Banco de memoria y entrelazado
**Qué es.** Dividir la memoria en **bancos** que se pueden acceder **en paralelo**; el **entrelazado** asigna
direcciones consecutivas a bancos distintos.
**Para qué sirve.** Aumentar el **ancho de banda**: con `B` bancos, hasta `B` accesos simultáneos.
**Características.** · `Ancho de banda = (bancos × ancho) / tiempo de acceso` · ejemplo: 4 bancos de 8 B cada
10 ns ⇒ **3,2 GB/s** · el entrelazado es la forma de aprovecharlo.
**Se estudia en** [[8.3.1 Bancos de memoria y ancho de banda]].

### Conflicto de banco
**Qué es.** Situación en la que dos accesos simultáneos caen en el **mismo** banco y hay que serializarlos.
**Para qué sirve.** Explica por qué un arreglo mal recorrido pierde todo el paralelismo.
**Características.** · Aparece cuando el **stride** (salto) es múltiplo de la cantidad de bancos (por ejemplo
stride 4 con 4 bancos) · se evita cambiando el patrón de acceso o rellenando el arreglo (*padding*).
**Se estudia en** [[8.3.2 Patrón de entrelazado y conflictos de banco]].

### Coherencia de caché
**Qué es.** Protocolo que garantiza que, si un núcleo escribe una dirección, los demás **no** sigan usando una copia
vieja.
**Para qué sirve.** Que el paralelismo no dé resultados incorrectos: es la condición de que el multicore funcione.
**Características.** · Se resuelve por **snooping** (cada caché escucha el bus) o por **directorio** ·
protocolos **MESI/MOESI** con estados modificado, exclusivo, compartido, inválido · genera tráfico extra.
**Se estudia en** [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]].

### Ley de Amdahl
**Qué es.** `S = 1 / ((1 − p) + p/N)`: la mejora total está limitada por la parte **no paralelizable**.
**Para qué sirve.** Calcular cuánto se gana **de verdad** al agregar núcleos, y mostrar por qué no es lineal.
**Características.** · Con `p = 0,9`: `N = 4 ⇒ 3,08`, `N = 16 ⇒ 5,93`, techo **10** · el techo es `1/(1−p)` ·
es la respuesta obligada cuando preguntan "¿por qué 16 núcleos no van 16 veces más rápido?".
**Se estudia en** [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]].

### Escalabilidad
**Qué es.** Capacidad del sistema de mantener el rendimiento cuando **crecen** la carga o los recursos.
**Para qué sirve.** Decidir si conviene agregar núcleos, memoria o nodos.
**Características.** · **Vertical**: más potencia en la misma máquina · **horizontal**: más máquinas (cluster) ·
está limitada por los recursos compartidos y por la sincronización (Amdahl).
**Se estudia en** [[8.4.2 Monousuario vs multiusuario]].

### Monousuario contra multiusuario
**Qué es.** Dos escenarios de uso: un solo usuario con todos los recursos, o muchos usuarios compitiendo por
ellos.
**Para qué sirve.** Cambiar el criterio de rendimiento: con un usuario importa la **latencia**; con muchos, el
**throughput** y la equidad.
**Características.** · Multiusuario exige planificación del SO y protección entre procesos · el límite pasa a ser
el ancho de banda de memoria y la coherencia de caché · el rendimiento por usuario cae aunque el total suba.
**Se estudia en** [[8.4.2 Monousuario vs multiusuario]].

### NUMA y cluster
**Qué es.** **NUMA**: varios procesadores con memorias **locales**, con tiempos de acceso distintos según dónde
esté el dato. **Cluster**: computadoras completas unidas por red.
**Para qué sirve.** Escalar fuera del chip sin que todos peleen por un único bus.
**Características.** · NUMA acoplado **fuertemente**, cluster **débilmente** · en NUMA importa **dónde** está el
dato · en un cluster la comunicación es por red (más lenta).
**Se estudia en** [[8.4.2 Monousuario vs multiusuario]].

### Acoplamiento (fuerte y débil)
**Qué es.** Grado de dependencia entre procesadores: fuerte si comparten memoria y reloj; débil si se comunican por
mensajes.
**Para qué sirve.** Clasificar multiprocesadores y entender qué se puede compartir.
**Características.** · Fuerte: memoria compartida (SMP, NUMA) · débil: cada nodo con su memoria (cluster,
distribuida) · más acoplamiento = más rápido para comunicar y más difícil de escalar.
**Se estudia en** [[8.4.2 Monousuario vs multiusuario]].
