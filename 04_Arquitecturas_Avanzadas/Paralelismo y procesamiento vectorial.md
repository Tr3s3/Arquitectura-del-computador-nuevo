---
unidad: 8
tipo: concepto
examen: complementario
---
# Paralelismo y procesamiento vectorial

> [!abstract] En una frase
> El paralelismo es ejecutar varias operaciones a la vez. Se clasifica (Flynn) según cuántos **flujos de
> instrucciones** y de **datos** hay: **SISD** (clásico), **SIMD** (vectorial: una instrucción, muchos
> datos), **MIMD** (multinúcleo). El procesamiento vectorial es el SIMD aplicado a arreglos: sumar dos
> vectores completos con una sola instrucción.

## Clasificación de Flynn
| Clase | Instrucciones | Datos | Ejemplo |
|---|---|---|---|
| **SISD** | 1 | 1 | CPU escalar clásica (BLUE) |
| **SIMD** | 1 | muchos | procesadores vectoriales, GPU, MMX/SSE/AVX |
| **MISD** | muchas | 1 | casi no existe (tolerancia a fallas) |
| **MIMD** | muchas | muchos | multinúcleo, multiprocesadores, clústeres |

## Pipeline aritmético
Segmentar una operación larga (suma en punto flotante, multiplicación) en etapas: se pueden **encadenar**
operaciones distintas, aceptando una nueva entrada por ciclo. Es el mismo principio del
[[Pipeline|pipeline de instrucciones]] pero dentro de la ALU. Con un pipeline aritmético de 4 etapas se
calculan 4 sumas en el tiempo que antes llevaban 4 sumas en serie (una tras otra).

## Procesamiento vectorial
Una **instrucción vectorial** opera sobre arreglos completos: `V3 ← V1 + V2` significa sumar
componente por componente con un solo opcode.
```
  escalar:  for i in 0..n-1: C[i] = A[i] + B[i]     (n instrucciones + n saltos)
  vectorial: VADD C, A, B                            (1 instrucción, n operaciones)
```
- Los **registros vectoriales** son anchos (64–512 bits) y guardan varios elementos.
- Ventaja: se **amortiza** el costo de búsqueda/decodificación de la instrucción (el *overhead* del cauce).
- Es la base del cálculo científico y de los **GPU** (que son SIMD masivos).

## Multiplicación de matrices (el ejemplo típico)
`C = A · B` con matrices de n×n: cada elemento `C[i][j] = Σ A[i][k]·B[k][j]`.
- Forma escalar: n³ multiplicaciones en bucles anidados.
- Forma vectorial: el bucle interno sobre `k` se convierte en una operación de **producto punto** vectorial
  ⇒ el procesador hace varias multiplicaciones-sumas en paralelo (encadenadas en el pipeline).
- Con n grande, la ganancia es proporcional al ancho vectorial (por eso las supercomputadoras hacen
  *matrix multiply* como benchmark).

## Memoria entrelazada (para alimentar al vector)
Un procesador vectorial consume un dato por ciclo: la memoria debe entregar a ese ritmo. Se logra con:
- **bancos de memoria** que atienden en paralelo (direcciones consecutivas → bancos distintos),
- acceso **encadenado** (mientras se lee el elemento i, se procesa el i−1),
- en máquinas grandes, módulos de memoria independientes (**supercomputadoras**: Cray, etc.).

## Arreglo de procesadores SIMD / conectado
- **Arreglo SIMD**: muchos elementos de proceso (PE) idénticos, cada uno con su ALU y su memoria, que
  ejecutan **la misma instrucción sobre datos distintos** (controlado por una UC común). Ejemplo: procesar
  los píxeles de una imagen.
- **Arreglo conectado (conexión entre PE)**: los PE están interconectados (malla, hipercubo) para
  intercambiar datos: así se resuelven problemas donde cada elemento necesita a sus vecinos (autómatas
  celulares, simulación física, procesamiento de imágenes).

## Configuraciones monousuario y multiusuario
| | Monousuario (PC) | Multiusuario (servidor/mainframe) |
|---|---|---|
| Paralelismo típico | ILP + SIMD + pocos núcleos | MIMD con muchos núcleos/nodos, throughput |
| Objetivo | **latencia** (que mi programa termine ya) | **productividad** (muchas tareas por hora) |
| Memoria | jerarquía local | memoria compartida o distribuida + red |
| E/S | estándar | canales de E/S de alta capacidad |

## Cómo responderlo en el final
1. Clasificación de Flynn (SISD/SIMD/MIMD) con un ejemplo de cada uno.
2. Pipeline aritmético y su diferencia con el de instrucciones.
3. Procesamiento vectorial: idea, ventaja (amortizar el overhead), ejemplo de matrices.
4. Memoria entrelazada (cómo se alimenta el vector) y arreglos SIMD/conectados.
5. Cerrar con monousuario vs multiusuario y el objetivo de cada uno (latencia vs throughput).

## Errores típicos
- Confundir SIMD (misma instrucción, muchos datos) con MIMD (muchas instrucciones).
- Decir que un pipeline es "multiprocesamiento" (es paralelismo **temporal** dentro de una unidad).
- Olvidar que el vectorial necesita memoria que entregue datos rápido (bancos).
- Confundir arreglo SIMD con arreglo conectado (el segundo agrega comunicación entre elementos).

## Relacionado
[[Pipeline]] · [[Técnicas para aumentar la velocidad]] · [[Memoria caché]] · [[Hardware aritmético (resumen)]]
