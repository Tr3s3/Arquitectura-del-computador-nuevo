---
tipo: glosario
unidad: 10
---
# Glosario — Unidad 10: entrada y salida

> [!abstract] Qué hay acá
> Las **14 fichas** de la unidad: las tres formas de hacer E/S (programada, por interrupciones y DMA), las
> interfaces y los dispositivos de almacenamiento. Índice alfabético en [[Glosario]].

### Entrada/salida (E/S)
**Qué es.** Todo intercambio de datos entre la computadora y el mundo exterior: teclado, pantalla, disco, red.
**Para qué sirve.** Que la máquina sirva para algo: es la parte que la conecta con el usuario y con el
almacenamiento.
**Características.** · Los periféricos son **mucho más lentos** que la CPU ⇒ el problema es la **sincronización** ·
se hace por **polling**, por **interrupciones** o por **DMA** · cada dispositivo tiene su **interfaz**.
**Se estudia en** [[10.1.1 Polling y sus límites]].

### Polling (E/S programada)
**Qué es.** La CPU **pregunta** una y otra vez si el periférico está listo, en un bucle.
**Para qué sirve.** Es la forma más simple de E/S, sin hardware extra.
**Características.** · **Desperdicia** la CPU entera esperando (333 vueltas para un periférico lento) ·
funciona igual (no depende de interrupciones) · sirve para dispositivos rápidos o cuando no hay nada más que hacer.
**Se estudia en** [[10.1.1 Polling y sus límites]].

### Handshake (STB y ACK)
**Qué es.** Protocolo de **acuse mutuo**: el emisor avisa `STB` (strobe: "el dato está puesto") y el receptor
contesta `ACK` ("lo tomé").
**Para qué sirve.** Transferir entre dispositivos de **velocidades distintas** sin reloj común: es la E/S
**asincrónica**.
**Características.** · No hay reloj: cada parte espera la señal de la otra · cuesta **dos líneas** más por cada
byte · se puede dar sin datos (sólo sincronizar).
**Se estudia en** [[10.1.2 Puertos, interfaces y handshake]].

### Puerto e interfaz
**Qué es.** **Puerto**: la "ventanilla" numerada por la que se lee o escribe un dispositivo. **Interfaz**: el
circuito que adapta señales, tensiones y velocidad entre el bus y el periférico.
**Para qué sirve.** Que la CPU hable con cualquier dispositivo con las pocas señales de su bus.
**Características.** · Los puertos se direccionan aparte de la memoria (E/S aislada) o en el mismo espacio
(E/S mapeada en memoria) · la interfaz tiene registros de **datos, estado y control** · ejemplo: el 8255.
**Se estudia en** [[10.1.2 Puertos, interfaces y handshake]].

### Interrupción
**Qué es.** Pedido **asincrónico** de un dispositivo para que la CPU lo atienda, dejando lo que está haciendo.
**Para qué sirve.** No desperdiciar la CPU esperando: el periférico avisa cuando tiene algo.
**Características.** · Se acepta en `IRQ · SI · CP8` (fin de instrucción) · el hardware guarda el `PC` y salta a la
**rutina de servicio** · al volver con **`RTI`** el programa sigue igual.
**Se estudia en** [[10.2.1 Mecanismo completo]].

### Interrupción vectorizada y vector de interrupciones
**Qué es.** **Vector**: la dirección de la rutina de servicio. **Vectorizada**: en lugar de preguntar quién fue, el
dispositivo entrega un **número** y la CPU salta a la dirección guardada en la **tabla de vectores**.
**Para qué sirve.** Atender la interrupción **sin sondear** a todos los dispositivos.
**Características.** · Tabla de 256 entradas × 4 bytes en el 8086 (en `00000H-003FFH`) · `IRQ5 ⇒ INT 0DH` ⇒
dirección `0DH × 4 = 34H` · es la que usan todas las PC.
**Se estudia en** [[10.2.2 Interrupciones vectorizadas y prioridad]].

### Prioridad de interrupciones
**Qué es.** Orden en que se atienden las interrupciones cuando llegan **varias** a la vez o una mientras se atiende
otra.
**Para qué sirve.** Que lo urgente no espere y que lo trivial no interrumpa.
**Características.** · **Fija por hardware**: posición en una **cadena** (el más cercano a la CPU gana) ·
**programable**: controlador (8259) con máscara y prioridad por registro · se puede **anidar** si se reactiva `SI`.
**Se estudia en** [[10.2.2 Interrupciones vectorizadas y prioridad]].

### DMA (acceso directo a memoria)
**Qué es.** Un **controlador** mueve datos entre periférico y memoria **sin** pasar por la CPU.
**Para qué sirve.** Transferencias grandes (disco, video) sin ocupar el procesador: la CPU sólo dice "moveme
este bloque" y sigue.
**Características.** · La CPU **cede el bus** y lo recupera al final (**robo de ciclo** o *cycle stealing*) ·
mueve **bloques**, no bytes · al terminar avisa con una interrupción · tasa típica: la CPU interviene ~25 % del
tiempo en vez de todo.
**Se estudia en** [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]].

### Robo de ciclo (cycle stealing)
**Qué es.** El controlador de DMA **toma prestado** un ciclo del bus para mover un dato, mientras la CPU espera.
**Para qué sirve.** Compartir el bus sin detener el programa mucho tiempo.
**Características.** · Baja el rendimiento de la CPU un pequeño porcentaje (un ciclo cada tanto) ·
alternativa: **transferencia en bloque**, que ocupa el bus hasta terminar (más rápido para el disco, peor para la
CPU).
**Se estudia en** [[10.3.1 Controlador, robo de ciclo y transferencia de bloques]].

### Disco rígido (HDD)
**Qué es.** Almacenamiento **magnético** con platos giratorios y cabezal móvil.
**Para qué sirve.** Guardar datos que deben sobrevivir al apagado, con gran capacidad y bajo costo por GB.
**Características.** · Latencia = **búsqueda** (seek) + **retardo de rotación** + transferencia ⇒ ~13,2 ms ⇒
**~76 IOPS** · es **mecánico**: los acceso aleatorios cuestan caro · no volátil.
**Se estudia en** [[10.4.1 Discos, SSD y latencias]].

### SSD
**Qué es.** Almacenamiento **en memoria flash**: no tiene partes móviles.
**Para qué sirve.** Lo mismo que el disco pero **mucho más rápido** en acceso aleatorio y más resistente.
**Características.** · ~10 000 IOPS (dos órdenes más que un HDD) y latencias de µs · **desgaste** por escritura
(se borra por bloques) · consume menos y no hace ruido.
**Se estudia en** [[10.4.1 Discos, SSD y latencias]].

### Latencia, IOPS y ancho de banda
**Qué es.** **Latencia**: tiempo de una operación. **IOPS**: operaciones por segundo. **Ancho de banda**: datos por
segundo.
**Para qué sirve.** Comparar dispositivos y calcular cuánto tarda una transferencia real.
**Características.** · Se complementan: muchas IOPS con poca latencia dan buen ancho de banda ·
`100 MB` por USB 2.0 = 1,67 s; por SATA = 0,17 s; por RS-232 ≈ **2,4 h** · el cuello puede ser el disco o el
enlace, hay que comparar los dos.
**Se estudia en** [[10.4.1 Discos, SSD y latencias]].

### Interfaces serie y paralelo
**Qué es.** **Paralelo**: varios bits a la vez por varias líneas. **Serie**: un bit por vez por una línea.
**Para qué sirve.** Conectar periféricos: la serie ganó por distancia y costo de cable, aun transfiriendo bit por
bit.
**Características.** · Paralelo: rápido en corto, caro y con **skew** (desfasaje entre líneas) en largo ·
serie: `USB 2.0 = 480 Mb/s ≈ 60 MB/s`, `SATA 6 Gb/s ≈ 600 MB/s`, `PCIe 4.0 x4 ≈ 7,9 GB/s`, `RS-232 = 115 200 bps ≈
11,5 kB/s` · al pasar de b/s a B/s se **divide por 8** (y por el overhead).
**Se estudia en** [[10.4.2 Interfaces serie y paralelo]].

### Skew (desfasaje)
**Qué es.** Diferencia de tiempo de llegada **entre líneas** de un bus paralelo.
**Para qué sirve.** Explicar por qué el paralelo no escala en distancia y por qué se pasó a la serie.
**Características.** · Cada línea tiene su retardo; si el desfasaje supera el período de bit, el receptor lee mal ·
es la razón del **skew** en memorias y en buses paralelos · se corrige con reloj de acompañamiento o con
**serdes** (serie).
**Se estudia en** [[10.4.2 Interfaces serie y paralelo]].
