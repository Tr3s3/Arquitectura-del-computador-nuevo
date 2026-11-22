---
tipo: practica
---
# Autoevaluación

> [!abstract] Cómo usarla
> 30 preguntas cortas, en el orden del plan de estudio. **Tapá la respuesta** (los bloques están
> colapsados: hacé clic para abrirlos). Si fallás una, volvé a la nota enlazada. Objetivo: 27/30.

## Lógica digital
> [!question]- 1. ¿Cuál es la diferencia entre una compuerta NAND y una AND?
> La NAND es la AND negada: su salida es 0 sólo cuando todas las entradas son 1. Además es **universal**.
> → [[Compuertas lógicas]]

> [!question]- 2. Enunciá las dos leyes de DeMorgan.
> `(A+B)' = A'·B'` y `(A·B)' = A' + B'`. Negar cambia el operador y niega cada variable.
> → [[Leyes de DeMorgan]]

> [!question]- 3. ¿Qué es un mintérmino?
> Un producto (AND) que vale 1 para **una sola** combinación de las variables; es la base de la forma SOP.
> → [[Mintérminos y maxtérminos]]

> [!question]- 4. ¿Por qué el semisumador no sirve para todas las columnas?
> Porque no tiene entrada de **acarreo** (Cin); sólo sirve para el bit menos significativo.
> → [[Semisumador]]

> [!question]- 5. Funciones del sumador completo.
> `S = A⊕B⊕Cin`; `Cout = A·B + Cin·(A⊕B)`. Se encadenan n para sumar n bits.
> → [[Sumador completo]]

## Secuenciales y memoria
> [!question]- 6. ¿Qué es un biestable y por qué es secuencial?
> Un elemento de memoria de 1 bit; su salida depende de las entradas **y del estado anterior** (tiene
> realimentación) y cambia con el flanco de reloj.
> → [[Flip-Flops SR, D, JK y T]]

> [!question]- 7. ¿Cuál es el estado prohibido del S-R y cómo lo evita el J-K?
> `S = R = 1`. El J-K lo redefine como **conmutación (toggle)**: `Q(t+1) = JQ' + K'Q`.
> → [[Flip-Flops SR, D, JK y T]]

> [!question]- 8. ¿Cuántos flip-flops necesita un registro de 16 bits y qué señal comparten?
> 16 flip-flops D, todos con el mismo **CLK** y la misma señal **LOAD**.
> → [[Registros]]

> [!question]- 9. Diferencia entre contador asíncrono y síncrono.
> Asíncrono: los FF se disparan en cascada (retardo acumulado). Síncrono: todos con el mismo reloj y
> lógica de habilitación (todos cambian juntos).
> → [[Contadores]]

> [!question]- 10. ¿Qué contiene una celda elemental de memoria?
> Un biestable (1 bit) + línea de selección + línea de dato + buffer de tres estados + R/W'.
> → [[Celda elemental de memoria]]

> [!question]- 11. Organización y capacidad de una RAM 8×3.
> 8 palabras de 3 bits: 3 líneas de dirección (2³), 3 de datos, capacidad 24 bits.
> → [[Memoria RAM 8x3]]

> [!question]- 12. ¿Cómo se expande una memoria en vertical y en horizontal?
> Vertical: se agregan palabras, el bit de dirección más alto decodificado habilita el **CS**. Horizontal:
> mismo CS y misma dirección, los datos se reparten entre chips (palabra más ancha).
> → [[Memoria RAM 8x3]]

> [!question]- 13. Tipos de ROM.
> Máscara, PROM, EPROM (borrado con UV), EEPROM (eléctrico) y Flash (EEPROM por bloques). No volátiles.
> → [[Memoria ROM y sus tipos]]

> [!question]- 14. ¿Por qué funciona la jerarquía de memorias?
> Por la **localidad** temporal y espacial de los programas: se reutilizan las mismas instrucciones y datos.
> → [[Jerarquía de memorias]]

> [!question]- 15. Los tres mapeos de caché.
> Directo (una línea, barato y con conflictos), asociativo total (cualquier línea, caro) y asociativo por
> conjuntos (conjunto fijo, vía libre: el real).
> → [[Memoria caché]]

> [!question]- 16. Write-through vs write-back.
> Write-through escribe siempre en caché y en RAM (coherente, más tráfico); write-back escribe en caché y
> marca *dirty*, baja a RAM al desalojar.
> → [[Memoria caché]]

> [!question]- 17. ¿Qué es la TLB?
> Una memoria **asociativa** que cachea las traducciones de la tabla de páginas (dirección virtual → física).
> → [[Memoria virtual y administración de memoria]]

## CPU y BLUE
> [!question]- 18. Nombrá las cuatro unidades y los tres buses.
> CPU (UC + ALU + registros), memoria y E/S; buses de datos, de direcciones y de control.
> → [[Estructura básica de un computador]]

> [!question]- 19. Función de PC, IR, MAR, MBR y AC.
> PC: dirección de la próxima instrucción. IR: la instrucción en ejecución. MAR: dirección para memoria.
> MBR: dato que entra/sale de memoria. AC: acumulador (operando y resultado).
> → [[Registros de la CPU]]

> [!question]- 20. ¿Por qué el bus de direcciones es unidireccional?
> Porque siempre la CPU (o el maestro del bus) es quien indica la dirección; la memoria sólo responde.
> → [[Estructura básica de un computador]]

> [!question]- 21. ¿Qué pasa en cada fase del ciclo de máquina?
> Búsqueda: `PC→MAR→MEMR→MBR→IR` + `PC+1` (STATE = F). Ejecución: según el opcode (STATE = E).
> → [[Ciclo de máquina]]

> [!question]- 22. ¿Por qué el ciclo de búsqueda se dice de 7 u 8 pulsos?
> Tiene 7 pasos conceptuales; el 8.º es el pulso de espera de memoria (o el incremento del PC contado
> aparte). Lo importante es justificar la cuenta.
> → [[Ciclo de búsqueda (7 y 8 pulsos)]]

> [!question]- 23. ¿Cuál es la cuenta de pulsos de LDA y por qué?
> 8 de búsqueda + 16 de ejecución = 24, contando **2 pulsos por microoperación** (fuente al bus, destino
> carga).
> → [[Ciclo de la instrucción LDA (24 pulsos)]]

> [!question]- 24. Cuatro funciones de la UC.
> Sincronizar (reloj), decodificar (opcode), secuenciar (orden) y generar las señales de control.
> → [[Unidad de Control]]

> [!question]- 25. ¿Qué rol cumplen RUN, STATE y CLOCK en BLUE?
> RUN: marcha/parada (HLT lo apaga). STATE: F (búsqueda) o E (ejecución). CLOCK: pulsos, uno por
> microoperación.
> → [[Unidad de Control]]

> [!question]- 26. Los cuatro formatos de instrucción.
> 4, 3, 2 y 1 dirección; BLUE es de 1 dirección con acumulador implícito (`4 + 12` bits).
> → [[Formato de la instrucción (4 formatos)]]

> [!question]- 27. Modos de direccionamiento y accesos a memoria de cada uno.
> Inmediato (0), registro (0), directo (1), indirecto (2), indexado (1 + registro índice).
> → [[Modos de direccionamiento]]

> [!question]- 28. ¿Qué agrega BLUE indexada?
> RIF y RID, formato `opcode 5 / dirección 16 / modificador 2`, sumador de direcciones, decodificador del
> modificador e instrucciones `INI`/`ENI`.
> → [[BLUE indexada (RIF, RID, nuevo formato)]]

> [!question]- 29. Secuencia de una interrupción.
> Terminar la instrucción → verificar SI → guardar contexto (PC/flags) → identificar la fuente (polling o
> vector) → saltar a la ISR → atender → restaurar y `RETI`.
> → [[Interrupciones y entrada-salida]]

> [!question]- 30. CISC vs RISC en una frase cada uno.
> CISC: instrucciones complejas y variables, opera sobre memoria, UC microprogramada (x86). RISC:
> instrucciones simples de longitud fija, load/store, muchos registros, UC cableada y pipeline (ARM).
> → [[CISC y RISC]]

## Ejercicios de pizarrón (sin respuesta: para practicar en hoja)
1. Dibujar de memoria la estructura básica con los tres buses y explicarla en 2 minutos.
2. Dibujar la RAM 8×3 completa con el decodificador y describir lectura y escritura.
3. Escribir la tabla de 8 pulsos del ciclo de búsqueda con las señales de cada pulso.
4. Resolver el sumador completo (tabla + funciones + gráfico) en 10 minutos.
5. Escribir en BLUE un programa que sume 3 números y otro que recorra un arreglo con RIF.
