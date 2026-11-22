---
unidad: 7
tipo: concepto
examen: secundario
---
# Técnicas para aumentar la velocidad

> [!abstract] En una frase
> Se puede acelerar un computador por **cuatro caminos**: hacer más rápido el ciclo (reloj/pipeline),
> **evitar esperas de memoria** (caché, bancos), **liberar a la CPU** de las transferencias (DMA) y
> **hacer varias cosas a la vez** (paralelismo). Casi todas las técnicas modernas son combinaciones de estos.

## 1) Pipeline (paralelismo temporal)
Solapa etapas de distintas instrucciones sin subir la frecuencia. Límite: k× con k etapas; los conflictos
lo reducen. Ver [[Pipeline]].

## 2) Memoria caché (evitar la espera de memoria)
Guarda copias de los bloques usados: si el 95 % de los accesos son aciertos, el tiempo medio cae de ~100 ns
a ~6 ns. Funciona por **localidad**. Ver [[Memoria caché]] y [[Jerarquía de memorias]].
*Variantes:* caché de instrucciones y de datos separadas (Harvard interno), multinivel (L1/L2/L3), caché de
traducciones (TLB).

## 3) Bancos de memoria (memoria entrelazada)
La memoria se divide en **bancos** que pueden atender accesos **en paralelo**. Si las direcciones
consecutivas caen en bancos distintos (**interleaving**), se puede leer una palabra por banco en el mismo
tiempo: el ancho de banda se multiplica por la cantidad de bancos.
```
  dirección 0 → banco 0      un acceso por banco
  dirección 1 → banco 1      en paralelo ⇒ 4× ancho de banda
  dirección 2 → banco 2
  dirección 3 → banco 3
```
Se usa en [[Paralelismo y procesamiento vectorial|procesadores vectoriales]] y en toda memoria moderna
(los *channels* de DRAM son bancos).

## 4) DMA / canales de datos (liberar a la CPU)
**DMA** (*Direct Memory Access*): un controlador dedicado transfiere bloques entre un periférico y la
memoria **sin pasar por la CPU**; la CPU sólo programa la operación y es avisada por interrupción al
terminar.
```
sin DMA: periférico → CPU → memoria   (la CPU pierde miles de ciclos)
con DMA: periférico ←→ memoria        (la CPU sigue trabajando)
```
- El controlador DMA pide el bus (**arbitraje**: por *cycle stealing* o por ráfagas).
- **Canal de E/S** = un DMA más complejo, capaz de ejecutar un programa de transferencias (mainframes).
- Ver [[Interrupciones y entrada-salida]].

## 5) Paralelismo (hacer varias cosas a la vez)
| Nivel | Qué se paraleliza | Ejemplo |
|---|---|---|
| **ILP / superescalar** | varias instrucciones del mismo programa en el mismo ciclo | CPU que emite 4 instrucciones por ciclo |
| **SIMD / vectorial** | la misma operación sobre muchos datos | MMX/SSE/AVX, GPU |
| **Multinúcleo (MIMD)** | varios programas/hilos en núcleos distintos | Ryzen, Core i7 |
| **Multiprocesador / clúster** | varios computadores | servidores, supercomputadoras |

Ver [[Paralelismo y procesamiento vectorial]].

## 6) Otras que conviene nombrar
- **Aumentar la frecuencia del reloj** (más ciclos por segundo): límite por consumo y temperatura.
- **Reducir los pulsos por instrucción**: ISA más simple ([[CISC y RISC|RISC]]), direccionamiento más simple.
- **Unidad de control cableada** en lugar de microprogramada (ahorra accesos a la ROM de control).
- **Registros múltiples**: menos accesos a memoria (RISC).
- **Predicción de saltos y ejecución especulativa**: mantiene lleno el pipeline.
- **Coprocesadores / aceleradores** (GPU, NPU) para tareas específicas.

## Cómo responderlo en el final
1. Enumerar los cuatro caminos (ciclo, memoria, E/S, paralelismo).
2. Desarrollar pipeline, caché, bancos y DMA con una frase de mecanismo + una de límite.
3. Agregar el nivel superescalar / SIMD / multicore.
4. Cerrar diciendo que son **complementarias**: una CPU real usa todas a la vez.

## Errores típicos
- Confundir **bancos de memoria** (ancho de banda) con **caché** (latencia).
- Decir que el DMA "hace más rápida la CPU" (le libera tiempo; la CPU no cambia).
- Pensar que subir el reloj es siempre rentable (consumo ∝ f·V²).
- Confundir multicore (varios núcleos) con pipeline (un núcleo, etapas).

## Relacionado
[[Pipeline]] · [[Memoria caché]] · [[Interrupciones y entrada-salida]] · [[Paralelismo y procesamiento vectorial]] · [[CISC y RISC]]
