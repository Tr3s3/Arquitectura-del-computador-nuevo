---
tipo: glosario
unidad: 7
---
# Glosario — Unidad 7: CPU y arquitecturas

> [!abstract] Qué hay acá
> Las **15 fichas** de la unidad: pipeline y sus problemas, las formas de ir más rápido, CISC contra RISC y dónde están los buses en la placa. Índice alfabético en [[Glosario]].

### Pipeline (cauce)
**Qué es.** Técnica de solapar etapas: mientras una instrucción se ejecuta, la siguiente se decodifica y la de más allá se busca. **Para qué sirve.** Aumentar el **ritmo** (instrucciones por unidad de tiempo), no la latencia de una sola. **Características.** · `k` etapas ⇒ hasta `k` instrucciones a la vez · tiempo total para `n` instrucciones: `k + (n − 1)` ciclos · ideal: una instrucción por ciclo · exige etapas **parejas** y reloj común. **Se estudia en** [[7.1.1 Etapas y diagrama en escalera]].

### Riesgo (hazard)
**Qué es.** Situación que impide que la próxima instrucción entre al pipeline en el ciclo previsto. **Para qué sirve.** Explica por qué el pipeline **no** llega al ideal y obliga a agregar hardware o instrucciones. **Características.** · **Estructural**: falta un recurso (un solo bus) · **de datos**: falta el valor (dependencia RAW) · **de control**: no se sabe qué instrucción sigue (salto) · se resuelven con más hardware, adelantamiento o deteniendo el cauce. **Se estudia en** [[7.1.2 Hazards y sus soluciones]].

### Adelantamiento (forwarding)
**Qué es.** Llevar el resultado de una etapa **posterior** directamente a la entrada de la etapa que lo necesita, sin esperar a que se escriba en el registro. **Para qué sirve.** Eliminar la mayoría de los riesgos de datos **sin perder ciclos**. **Características.** · Necesita cables y comparadores extra · funciona ALU → ALU · **no** resuelve el caso `LOAD` seguido de uso (el dato recién llega del memoria al final). **Se estudia en** [[7.1.2 Hazards y sus soluciones]].

### Detención (stall) y NOP
**Qué es.** **Stall**: congelar el cauce uno o más ciclos. **NOP**: instrucción vacía que ocupa el ciclo. **Para qué sirve.** Resolver lo que el adelantamiento no puede: es la solución que **siempre** funciona. **Características.** · Cada stall/NOP = **un ciclo perdido** · NOP explícito = lo que inserta el compilador · se suman al cálculo del speedup como penalidad. **Se estudia en** [[7.1.2 Hazards y sus soluciones]].

### Speedup y techo `k`
**Qué es.** `S = T_sin / T_con`, y en un pipeline con `k` etapas: `S = k·n / (k + n − 1)`. **Para qué sirve.** Calcular la mejora real y su **límite**: con `n → ∞`, `S → k`. **Características.** · Con `k = 5`: `S(3) = 2,14`, `S(100) = 4,81`, `S(1000) = 4,98` · el techo **nunca** se alcanza · los stalls y los saltos bajan el `S` real. **Se estudia en** [[7.1.3 Cálculo de speedup y límites]].

### Superscalar
**Qué es.** Pipeline que emite **más de una** instrucción por ciclo, con varias vías en paralelo. **Para qué sirve.** Superar el límite de 1 instrucción/ciclo: con 2 vías, hasta 2. **Características.** · Necesita detectar dependencias y despachar en orden · `w` vías × `f` GHz ⇒ `w·f·10⁹` instrucciones/s teóricas · el código tiene que tener paralelismo suficiente. **Se estudia en** [[7.2.1 Superscalar, superpipeline, SMT y multicore]].

### Superpipeline
**Qué es.** Pipeline con **más etapas** (más finas) para poder subir la frecuencia. **Para qué sirve.** Ir más rápido sin ensanchar el cauce (más GHz con el mismo trabajo por ciclo). **Características.** · Más etapas ⇒ más penalidad por salto y más consumo · límite práctico alrededor de 20-30 etapas · el Pentium 4 llegó a ~20 y volvió atrás. **Se estudia en** [[7.2.1 Superscalar, superpipeline, SMT y multicore]].

### SMT (multihilo simultáneo)
**Qué es.** Un núcleo que mantiene **dos o más hilos** y toma instrucciones de cualquiera de ellos en cada ciclo. **Para qué sirve.** Aprovechar los ciclos que un hilo pierde por fallos de caché o dependencias. **Características.** · Comparte la unidad de ejecución; **duplica** los registros y el `PC` · no es lo mismo que multicore (no hay núcleos físicos nuevos) · mejora el rendimiento con cargas mezcladas. **Se estudia en** [[7.2.1 Superscalar, superpipeline, SMT y multicore]].

### Multicore
**Qué es.** Varios **núcleos completos** en el mismo chip, cada uno con su pipeline. **Para qué sirve.** Escalar en paralelo cuando la frecuencia ya no sube (límite de potencia). **Características.** · Cada núcleo tiene sus cachés L1/L2 y comparten L3 · necesita **coherencia de caché** · el límite es la ley de Amdahl y el ancho de banda de memoria. **Se estudia en** [[8.4.1 Multicore, coherencia de caché y ley de Amdahl]].

### Predicción de saltos
**Qué es.** Adivinar si un salto se toma (y a dónde) para no detener el cauce. **Para qué sirve.** Reducir el costo del **riesgo de control**, que es el más caro: un salto mal predicho vacía el pipeline. **Características.** · Predictor de **2 bits**: 4 estados (fuerte/débil tomado, fuerte/débil no tomado) ⇒ acierta en bucles · predictores modernos usan historia y `BTB` · el costo de fallar = `k − 1` ciclos. **Se estudia en** [[7.2.2 Caché y predicción de saltos]].

### CISC
**Qué es.** Arquitectura de **instrucciones complejas**, de tamaño variable, que pueden operar sobre memoria (x86). **Para qué sirve.** Programar con **pocas** instrucciones y código compacto; ahorrar memoria (cuando era caro). **Características.** · Muchos formatos y modos de direccionamiento · `CPI` alto · el hardware es más complejo pero el compilador tiene menos trabajo · hoy ejecuta microcódigo internamente. **Se estudia en** [[7.3.1 Tabla comparativa y ejemplos]].

### RISC
**Qué es.** Arquitectura de **instrucciones simples y de tamaño fijo**, con **load/store** y muchos registros (ARM, MIPS). **Para qué sirve.** Que el pipeline sea simple y rápido: decodificar es trivial y todas las instrucciones tardan parecido. **Características.** · 1 ciclo por instrucción (ideal) · sólo `LOAD` y `STORE` tocan memoria · 3 direcciones · el compilador hace el trabajo (más instrucciones, menos ciclos). **Se estudia en** [[7.3.1 Tabla comparativa y ejemplos]].

### Load/store
**Qué es.** Regla de RISC: el acceso a memoria sólo ocurre en instrucciones `LOAD` y `STORE`; el resto opera registro a registro. **Para qué sirve.** Hacer predecible el tiempo de las instrucciones y simplificar el pipeline. **Características.** · Consecuencia de instrucciones de tamaño fijo y de 1 ciclo · compara con CISC, donde `ADD` puede leer memoria · obliga a tener **muchos registros**. **Se estudia en** [[7.3.2 UC cableada vs microprogramada y load-store]].

### von Neumann contra Harvard
**Qué es.** **von Neumann**: una memoria y un bus para instrucciones y datos. **Harvard**: memorias y buses **separados**. **Para qué sirve.** Entender el **cuello de botella** de von Neumann y por qué existen las cachés separadas. **Características.** · von Neumann: simple, pero no puede traer instrucción y dato a la vez · Harvard: menos conflicto, más cables y dos espacios de direcciones · las PC actuales son Harvard **en la caché** (L1I y L1D). **Se estudia en** [[7.4.1 von Neumann vs Harvard]].

### Bus interno y externo (FSB)
**Qué es.** **Interno**: dentro del chip, une registros y ALU. **Externo**: en la placa, une CPU con memoria y periféricos; el clásico es el **FSB** (a través del **puente norte**). **Para qué sirve.** Distinguir a quién pertenece cada transferencia y qué limita el rendimiento. **Características.** · El FSB transporta direcciones y datos hacia la memoria · en las PC actuales el controlador de memoria está **dentro** de la CPU (DMI/QPI reemplazan al FSB) · el bus externo es el cuello histórico del sistema. **Se estudia en** [[7.4.2 Buses internos y externos]].
