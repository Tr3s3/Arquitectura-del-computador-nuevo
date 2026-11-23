---
tipo: indice
unidad: 10
---
# Unidad 10 — Entrada y Salida

> [!abstract] Qué pide la unidad
> Cómo la CPU **habla con el mundo**: E/S **programada** (*polling*), por **interrupciones** y por **DMA**; qué
> son **puertos**, **interfaces** y **handshake**; cómo se identifican y priorizan las interrupciones; y de dónde
> salen los **milisegundos** de un disco y los **GB/s** de un bus serie.

> [!important] El hilo de la unidad
> `la CPU espera` → `el periférico avisa` → `un controlador mueve`. Cada modo existe porque el anterior
> **desperdicia** algo; y el último eslabón (el dispositivo) explica **por qué** existe toda la jerarquía de
> memoria de las unidades 2 y 7.

## La estructura de la unidad (Unidad → Tema → Subtema)

```
Unidad 10 — Entrada y Salida/
├── 00 Unidad 10 — temas y subtemas
├── 00 Síntesis — Unidad 10
├── Tema 10.1 Entrada y salida programada/
│   ├── 10.1.1 Polling y sus límites
│   └── 10.1.2 Puertos, interfaces y handshake
├── Tema 10.2 Interrupciones/
│   ├── 10.2.1 Mecanismo completo
│   └── 10.2.2 Interrupciones vectorizadas y prioridad
├── Tema 10.3 DMA/
│   └── 10.3.1 Controlador, robo de ciclo y transferencia de bloques
└── Tema 10.4 Dispositivos y almacenamiento/
    ├── 10.4.1 Discos, SSD y latencias
    └── 10.4.2 Interfaces serie y paralelo
```

**4 temas y 7 subtemas.** Cada subtema es **una nota** dentro de la carpeta de su tema. La unidad está **cerrada**
y todo su contenido quedó reunido en **[[00 Síntesis — Unidad 10]]**.

| Tema | Subtemas | Estado |
|---|---|---|
| **10.1 Entrada y salida programada** | 10.1.1 Polling y sus límites · 10.1.2 Puertos, interfaces y handshake | ✅ |
| **10.2 Interrupciones** | 10.2.1 Mecanismo completo · 10.2.2 Interrupciones vectorizadas y prioridad | ✅ |
| **10.3 DMA** | 10.3.1 Controlador, robo de ciclo y transferencia de bloques | ✅ |
| **10.4 Dispositivos y almacenamiento** | 10.4.1 Discos, SSD y latencias · 10.4.2 Interfaces serie y paralelo | ✅ |

> [!note] Cómo creció el árbol
> El árbol original tenía **7 subtemas** en 4 temas. Se mantiene igual: el tema 10.1 se llama **"Entrada y salida
> programada"** (no "E/S programada") porque **una barra en el nombre de la carpeta crearía dos niveles** y el
> enlace de Obsidian no resolvería.

## Los 4 temas, de un vistazo

| Tema | Índice | La idea en una línea |
|---|---|---|
| **10.1** | [[00 Tema 10.1 — índice]] | la CPU pregunta y espera: simple, pero **quema** el procesador |
| **10.2** | [[00 Tema 10.2 — índice]] | el periférico avisa; la CPU atiende al final de la instrucción |
| **10.3** | [[00 Tema 10.3 — índice]] | un controlador mueve el bloque; la CPU sólo programa y espera el aviso |
| **10.4** | [[00 Tema 10.4 — índice]] | el disco tarda **13 ms** por posicionarse; el SSD, 0,1 ms |

## Los tres modos de E/S, en una tabla
| | **Polling** | **Interrupciones** | **DMA** |
|---|---|---|---|
| Quién inicia | CPU | CPU (avisa el periférico) | CPU programa; el DMA ejecuta |
| Quién copia | CPU | CPU | **el controlador** |
| Costo por byte | espera | ISR (≈ 20 µs) | ≈ 0 |
| Cuándo | periférico rápido y predecible | eventos esporádicos | bloques grandes |

## Material de examen ya disponible de esta unidad
| Tema | Nota | Dónde está además |
|---|---|---|
| **Interrupciones (todas)** | [[Interrupciones y entrada-salida]] | `Tanda 2/2.8` + `Apoyo a la pregunta/` |
| **Interrupciones en la BLUE** | [[5.5.1 IRQ, SI y CP8]] · [[5.5.2 Máscara, pila y RTI]] | Unidad 5 |
| **E/S de la BLUE (`INP`/`OUT`)** | [[Las 16 instrucciones de BLUE — ciclo completo pulso por pulso]] | Unidad 4 |
| **DMA y bus** | [[Técnicas para aumentar la velocidad]] · [[7.4.2 Buses internos y externos]] | Unidad 7 |
| **Jerarquía y memoria auxiliar** | [[Jerarquía de memorias]] · [[2.6.2 Memoria auxiliar y memoria asociativa]] | Unidad 2 |
| **Bus, maestro/esclavo** | [[3.1.2 Bus único y buffers de 3 estados]] · [[TP14 Buses]] | Unidad 3 · TP |

---

## Qué hay que saber hacer al terminar la unidad
1. **Comparar** polling, interrupciones y DMA (quién inicia, quién copia, costo, cuándo conviene).
2. Calcular **cuánto tiempo pierde** la CPU con polling (vueltas × duración del lazo).
3. Explicar los **10 pasos** de una interrupción y **qué guarda** el contexto.
4. Distinguir **polling de identificación** de **vectorización**, y **prioridad** de **máscara**.
5. Calcular la **dirección de la tabla de vectores** del 8086 (`vector × 4`).
6. Explicar el **DMA**: registros, `BR`/`BG`, **robo de ciclo** vs **ráfaga**, y el ahorro en µs.
7. Calcular el **tiempo de acceso** de un disco (seek + ½ vuelta + transferencia) y sus **IOPS**.
8. Pasar de **bits/s a MB/s** descontando el **codificado** (8b/10b) y explicar por qué **ganó el serie**.

## TPs de la unidad
No tiene TP propio: se estudia con [[TP14 Buses]] (líneas de control, maestros y esclavos, DMA) y
[[TP16 Ciclo de instrucción básico]] (el ciclo con `INP`/`OUT` y la espera del periférico).

## Fuente de la cátedra
Apuntes **Unidad 10** · `blue.pdf` (E/S por consulta) · `El_manual_del_Microprocesador.pdf` ·
Stallings (E/S, DMA, discos) · Tanenbaum (E/S) · Hamacher (buses y E/S) · Brey (interrupciones del 8086).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 9 — temas y subtemas]] ·
[[00 Síntesis — Unidad 10]] · [[Interrupciones y entrada-salida]]
