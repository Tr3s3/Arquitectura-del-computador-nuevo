---
tipo: recursos
---
# Videos de apoyo (análisis)

> [!abstract] Estado del análisis
> De los **30 enlaces** de la lista (16 videos sueltos y 14 listas de reproducción), se pudo leer el contenido de **5 videos**. Los demás no se pudieron analizar: YouTube bloqueó el acceso (error 401 o verificación de "no sos un bot") o son listas de reproducción que no se recorrieron.

## Qué se pudo analizar

| ID del video | Tema | Estado de la lectura |
|---|---|---|
| `pZfp3wuIirY` | Sumadores | Leído |
| `bwrG6Sdow14` | Cómo funciona la computadora | Leído |
| `aCUHp1KLX7E` | CPU | Leído |
| `HMr9y-Nfj0A` | Direccionamiento de memoria | Leído |
| `Fju6DhqzL9w` | Lenguaje de máquina | Leído solo hasta el ciclo de búsqueda (parcial) |

## Qué no se pudo analizar

- **Bloqueados por YouTube (401 o verificación de bot):** `VPvVvy5ahAU`, `YMR5IdezPv4`, `swOCvouHeAg`, `6fz1Mjv_VHc`, `McA-9_qgq4Y`, `PCMpxIzqEO4`, `e27trfKcuBA`, `unyZ8yNpBV8`, `FtzdL81PgrQ`, `HNUodUAQTbU`, `5AaDqy1UiFU`.
- **Listas de reproducción sin recorrer:** 14 enlaces.

> [!warning] Pendiente
> Para completar el análisis hace falta pasar las transcripciones de los videos bloqueados o las URLs de los videos individuales.

## Contenido útil de los videos leídos

### Sumadores
- **Semisumador:** suma dos bits A y B. Suma S = A ⊕ B (XOR) y acarreo C = A · B (AND).
- **Sumador completo:** suma tres bits (A, B y el acarreo de entrada). El semisumador no alcanza porque no recibe el acarreo de la columna anterior.
- Varios sumadores completos en cadena forman un sumador de n bits.

### Direccionamiento de memoria
- Ejemplo: memoria de **512 MB** con celdas de **4 bytes**. Son 2²⁹ ÷ 2² = 2²⁷ celdas, así que hacen falta **27 bits de dirección**.
- Con una instrucción de **32 bits**, quedan **5 bits** para el código de operación (2⁵ = 32 operaciones posibles).

### Lenguaje máquina
- El lenguaje máquina son los patrones de bits que el procesador reconoce.
- Comparación **RISC** (pocas instrucciones simples) y **CISC** (muchas instrucciones y formatos).
- Clasificación de instrucciones en transferencia de datos, aritmético-lógicas y de control.
- Ejemplo de instrucción de **16 bits** con código de operación de 4 bits.
- Ciclo: búsqueda, decodificación y ejecución.

### Cómo funciona la computadora
- El hardware necesita programas. El programa se compila, se carga en memoria principal y la CPU ejecuta sus instrucciones.
- La caché es una memoria intermedia más rápida que la memoria principal, con niveles L1, L2 y L3.

### CPU
- La CPU busca, decodifica y ejecuta instrucciones.
- Arquitectura de 32 o 64 bits. Velocidad medida en GHz.
- Caché en niveles L1, L2 y L3 (L1 es la más rápida).
- Procesadores multinúcleo: varios núcleos en un chip para ejecutar en paralelo.

## Preguntas de final que salen de estos videos

| Pregunta posible | Respuesta corta | Dónde estudiar |
|---|---|---|
| ¿Por qué el semisumador no alcanza para sumar varios bits? | No recibe el acarreo de entrada de la columna anterior. | [[1.5.1 Semisumador y sumador completo]] |
| Memoria de 512 MB con celdas de 4 bytes: ¿cuántos bits de dirección? ¿Cuántos quedan para el código de operación en una instrucción de 32 bits? | 27 bits de dirección; 5 bits para el código de operación. | [[2.7.1 Bits de dirección igual a log2 de celdas]] · [[2.7.2 CodOp vs campo de dirección]] |
| ¿Qué diferencia hay entre RISC y CISC? | RISC: pocas instrucciones simples. CISC: muchas instrucciones complejas y formatos variados. | [[5.1.2 Clasificación de las instrucciones]] |
| ¿Cuáles son las fases del ciclo de instrucción? | Búsqueda, decodificación y ejecución. | [[4.3.2 Búsqueda, los 8 pulsos]] |
| ¿Para qué sirve la caché? | Guarda datos e instrucciones que la CPU probablemente va a usar, para reducir el tiempo de acceso a memoria. | [[2.5.2 Caché, mapeos y políticas]] |
