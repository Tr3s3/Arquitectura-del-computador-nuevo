---
tipo: recursos
---
# Videos de apoyo (análisis)

> [!abstract] Estado del análisis
> De los **30 enlaces** de la lista (16 videos sueltos y 14 listas de reproducción), se pudo leer el contenido de **5 videos**. Los demás no se pudieron analizar: YouTube bloqueó el acceso (error 401 o verificación de "no sos un bot") o son listas de reproducción de decenas de videos que no se recorrieron. Dos enlaces de listas están cortados en el texto original (`PLXHYADKEpvEw` y `PLJDUYntOvyB4`) y no se pueden abrir.

## Qué se pudo analizar

| Video | Tema | Estado | Dónde se usa en la bóveda |
|---|---|---|---|
| Sumadores, semi-sumadores (`pZfp3wuIirY`) | Semisumador, sumador completo, 3 bits | **Transcripción completa** | [[1.5.1 Semisumador y sumador completo]] |
| Direccionamiento de memoria (`HMr9y-Nfj0A`) | Bits de dirección = log₂(celdas) | **Transcripción completa** | [[2.7.1 Bits de dirección igual a log2 de celdas]] |
| Lenguaje máquina, ejemplo (`Fju6DhqzL9w`) | Formato de 16 bits, RISC vs. CISC, clases de instrucciones | **Transcripción parcial** (solo la primera mitad) | [[5.1.1 Instrucción, opcode y operandos]] · [[5.1.2 Clasificación de las instrucciones]] |
| Cómo funciona una computadora (`bwrG6Sdow14`) | Programa, compilación, carga, caché | **Transcripción completa** | [[4.1.1 Unidades funcionales de una computadora]] |
| CPU - procesador (`aCUHp1KLX7E`) | 32/64 bits, GHz, caché L1/L2/L3, multinúcleo | **Transcripción completa** | [[4.1.1 Unidades funcionales de una computadora]] |

## Qué no se pudo analizar

| Video | Motivo |
|---|---|
| Memoria principal (`VPvVvy5ahAU`) · RAM, ROM, caché (`YMR5IdezPv4`) · ROM y RAM (`swOCvouHeAg`) · Componentes de una computadora (`6fz1Mjv_VHc`) · Von Neumann (`McA-9_qgq4Y`) · Motherboard (`PCMpxIzqEO4`) · Almacenamiento secundario (`e27trfKcuBA`) · Periféricos (`unyZ8yNpBV8`) · Formato básico de instrucciones (`FtzdL81PgrQ`) · Modos de direccionamiento (`HNUodUAQTbU`) · Introducción a ensamblador (`5AaDqy1UiFU`) | YouTube devolvió error 401 o la página de verificación de bot; no hay transcripción accesible. |
| Compuertas, álgebra de Boole, funciones booleanas, simplificación (3 listas) · decodificadores y multiplexores (2 listas) · biestables y registros (2 listas) · buses (1 lista) · ciclo de instrucción básico (1 lista) | Son **listas de reproducción** con muchos videos cada una. No se recorrieron. |

## Contenido útil de los videos analizados

### 1. Sumadores (semisumador y sumador completo)
- **Semisumador**: suma dos bits A y B. El bit de suma es **S = A ⊕ B** (XOR) y el acarreo es **C = A · B** (AND). Usa una compuerta AND y una XOR con las mismas entradas.
- **Sumador completo**: suma tres bits (A, B y el acarreo de entrada C_in). Un semisumador no alcanza porque no recibe el acarreo de la columna anterior.
- **Actividad propuesta en el video**: dibujar el sumador completo y completar las sumas 0+0+0, 0+0+1, 1+1+0 y 1+1+1 (ver la tabla de verdad).
- El video muestra que la suma de varios bits es una cadena de sumadores completos, con el acarreo de salida de cada uno como entrada del siguiente.

### 2. Direccionamiento de memoria
- Ejemplo de la cátedra: memoria de **512 MB** con celdas de **4 bytes**. Cantidad de celdas = 512 MB ÷ 4 B = 2²⁹ ÷ 2² = **2²⁷ = 128 M celdas**.
- Cada celda tiene una dirección, así que hacen falta **27 bits de dirección** (log₂(2²⁷) = 27).
- Si la instrucción tiene 32 bits, quedan **32 − 27 = 5 bits** para el código de operación. Con 5 bits se pueden codificar 2⁵ = 32 operaciones distintas.

### 3. Lenguaje máquina (primera mitad)
- Las instrucciones son patrones de bits que el procesador reconoce. El conjunto de instrucciones y su codificación es el **lenguaje máquina**.
- **RISC**: pocas instrucciones, simples, más eficientes y más baratas de fabricar.
- **CISC**: muchas instrucciones y formatos, más complejas y con decodificación más difícil.
- Clasificación de las instrucciones en tres grupos: **transferencia de datos** (load, store), **aritmética y lógica** (add, sub, and, or, rotate) y **control** (branch, salto).
- Ejemplo de la cátedra: máquina de **16 bits**, con instrucciones de 4 dígitos hexadecimales. El primer dígito (4 bits) es el código de operación y los 12 bits restantes son el operando. Memoria direccionable con 2 dígitos hexadecimales (de 00 a FF).
- Ciclo de máquina en tres fases: **búsqueda** (el PC indica la dirección), **decodificación** y **ejecución**. El ciclo se repite hasta que la máquina se detiene.

### 4. Cómo funciona una computadora
- El hardware no ejecuta nada por sí solo: necesita programas. Un programa es un conjunto de instrucciones escritas en un lenguaje de programación.
- El video describe: código fuente en disco → compilación → archivo ejecutable en disco → carga en memoria principal → la CPU copia las instrucciones a sus registros y las ejecuta.
- **Caché**: memoria intermedia y muy rápida entre el procesador y la memoria principal, con niveles L1, L2 y L3.

> [!warning] Imprecisiones del video
> - Dice que la compilación genera "un objeto ejecutable". En la práctica, después de compilar hay un paso de **enlazado** (linking) que arma el ejecutable. Esto hay que contarlo en el final.
> - Dice que el procesador puede tardar "10 millones de veces más" en leer un disco que la memoria. Ese orden de magnitud es exagerado: la diferencia suele ser de algunos miles a cien mil veces, según la tecnología. No lo uses como dato de examen sin verificarlo.

### 5. CPU - procesador
- La CPU busca, decodifica y ejecuta instrucciones. Es el componente que controla a los demás.
- Arquitectura de **32 o 64 bits**: el tamaño de los registros de datos y de los buses de direcciones y datos.
- Velocidad en **Hz**: ciclos por segundo. Un procesador actual está en el orden de los GHz.
- **Caché**: L1 (la más pequeña y rápida, dentro del chip), L2 y L3 (la más grande, fuera del procesador).
- Ejemplo de configuración de la cátedra: L1 de 64 KB (32 KB de datos y 32 KB de instrucciones), L2 de 256 KB y L3 de 12 MB.
- **Multinúcleo**: a partir de 2004 los fabricantes pusieron varios núcleos en un chip en lugar de subir el reloj. Eso permite ejecutar varios programas en paralelo.

## Preguntas de final que salen de estos videos

| Pregunta posible | Respuesta corta | Dónde estudiar |
|---|---|---|
| ¿Por qué el semisumador no alcanza para sumar varios bits? | No recibe el acarreo de entrada de la columna anterior. | [[1.5.1 Semisumador y sumador completo]] |
| Memoria de 512 MB con celdas de 4 bytes: ¿cuántos bits de dirección? ¿Cuántos quedan para el código de operación en una instrucción de 32 bits? | 27 bits de dirección; 5 bits para el código de operación. | [[2.7.1 Bits de dirección igual a log2 de celdas]] · [[2.7.2 CodOp vs campo de dirección]] |
| ¿Qué diferencia hay entre RISC y CISC? | RISC: pocas instrucciones simples. CISC: muchas instrucciones complejas y formatos variados. | [[5.1.2 Clasificación de las instrucciones]] |
| En una instrucción de 16 bits con código de operación de 4 bits, ¿cuántas instrucciones distintas hay? | 2⁴ = 16 códigos de operación. El operando tiene 12 bits. | [[5.2.1 Los 4 formatos y el campo único de dirección]] |
| ¿Cuáles son las fases del ciclo de instrucción? | Búsqueda, decodificación y ejecución, controladas por el PC. | [[4.3.2 Búsqueda, los 8 pulsos]] |
| ¿Para qué sirve la caché? ¿Qué diferencia hay entre L1, L2 y L3? | Guarda datos e instrucciones que la CPU probablemente va a usar; L1 es la más rápida y la más chica, L3 la más grande. | [[2.5.2 Caché, mapeos y políticas]] |
