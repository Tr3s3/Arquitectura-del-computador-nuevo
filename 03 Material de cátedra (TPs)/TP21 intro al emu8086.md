---
tp: 21
unidad: 4
tipo: tp
prioridad: media
---
# TP21 — Introducción al EMU8086

> [!abstract] Consigna (cátedra)
> "Ejecutar el programa emulador **EMU8086** y relacionarlo con los elementos básicos que conforman el **modelo de programación del microprocesador 8086**." El TP guía la instalación, la compilación de un archivo `.COM`, la ejecución **paso a paso** y el análisis del primer programa (`guia01.asm`), y termina con **6 preguntas** (a–f) sobre lo observado.

> [!note] Unidad y encuadre
> El TP está enmarcado en **"Procesadores / Unidad 4"** y su bibliografía es **Brey, *Los microprocesadores Intel***. No es un tema de la matriz del final, pero sirve para **ver con los ojos** lo que en la BLUE se explica con pulsos: registros, flags, pila, memoria y lenguaje de máquina.

## Qué hay que saber para resolverlo

1. **Qué es un emulador**: un programa que *simula* el microprocesador y muestra **registros, memoria, flags y pila** mientras ejecuta. Permite ejecutar **instrucción por instrucción (single step)**.

2. **El modelo de programación del 8086**: 14 registros de 16 bits (`AX BX CX DX`, `SP BP SI DI`, `CS DS SS ES`, `IP`, `FLAGS`); los cuatro primeros se pueden usar como dos registros de 8 bits (`AH/AL`).

3. **Segmento : offset**: la dirección física se calcula `CS × 10h + IP` (20 bits). En un `.COM`, `CS = DS = SS` y el programa arranca en el offset **100h**.

4. **Ensamblador vs lenguaje de máquina**: `mov AH, 7Ah` (legible) se ensambla como `B4 7A` (bytes).

5. **Bases numéricas en el código**: `7Ah` hexadecimal, `11001111b` binario, `99` decimal, `'A'` carácter.

## El programa del TP, anotado
```asm
#MAKE_COM#        ; le dice al ensamblador que genere un .COM
ORG 100h          ; el programa se carga desde el offset 100h (después del PSP)

mov AH, 7Ah       ; AH = 7A hexadecimal (122 decimal)
mov BL, 99        ; BL = 99 decimal (= 63h)
mov CL, 11001111b ; CL = CFh (binario)
mov AX, 100       ; AX = 100 decimal (64h)  ← pisa AH y AL juntos
mov BX, 'A'       ; BX = 0041h  (código ASCII de 'A')
mov CX, 0ABCDh    ; CX = ABCD hexadecimal
mov DX, 6540      ; DX = 6540 decimal (= 198Ch)
ret               ; termina: vuelve al sistema (que ejecuta INT 20h)
```

> [!warning] Ojo con el orden
> `mov AX, 100` **borra** lo que se había cargado en `AH` dos instrucciones antes: `AX` es el registro de 16 bits que **contiene** a `AH` (bits altos) y `AL` (bajos). Lo mismo con `BX`, `CX` y `DX`. Ese es el detalle que hace que el ejercicio "no dé lo que uno esperaba".

## Las respuestas a las 6 preguntas del TP

| # | Pregunta | Respuesta |
|---|---|---|
| **a** | ¿Por qué se incluye `org 100h`? | Porque un programa **`.COM`** se carga en el **Program Segment Prefix**, que ocupa los primeros **256 bytes (100h)**. `ORG 100h` le dice al ensamblador que **las direcciones del programa empiezan en 100h**, para que las etiquetas y los saltos apunten bien. |
| **b** | ¿Cuántos y cuáles formatos de numeración se usan? | **Cuatro**: **decimal** (`99`, `100`, `6540`), **hexadecimal** (sufijo `h`: `7Ah`, `0ABCDh`), **binario** (sufijo `b`: `11001111b`) y **carácter ASCII** (entre comillas: `'A'` → 41h). |
| **c** | En `MOV` hay tres campos: instrucción, dato1 y dato2. ¿Cuál es fuente y cuál destino? | La sintaxis es `MOV destino, fuente`: **dato1 = destino**, **dato2 = fuente**. El dato se **copia** de la fuente al destino (la fuente **no** se modifica). El destino no puede ser un valor inmediato. |
| **d** | ¿Por qué la misma instrucción `MOV` tiene distintos códigos hexadecimales? | Porque el **opcode depende del registro y del tamaño del dato**: `mov AH, imm8` se codifica `B4 7A` (2 bytes), `mov AX, imm16` es `B8` + 2 bytes (3 bytes), `mov CL, imm8` es `B1`, etc. El **primer byte** identifica instrucción + registro + tamaño; el o los siguientes, el dato. |
| **e** | ¿Qué función cumple el registro `IP`? | Es el **contador de programa** del 8086: contiene el **offset** de la **próxima instrucción** dentro del segmento `CS`. La dirección física es `CS:IP`. Después de cada instrucción se incrementa en su tamaño. |
| **f** | ¿Por qué los `OFFSET` no se incrementan en una cantidad constante? | Porque las instrucciones **no ocupan lo mismo**: `mov AH,7Ah` = **2 bytes**, `mov AX,100` = **3 bytes**, `mov CX,0ABCDh` = **3 bytes**. El offset avanza **el largo de cada instrucción**, que es variable. |

## Tabla 1 del TP (lo que hay que completar)

| SEGM (CS) | OFFSET | Lenguaje de máquina | Ensamblador |
|---|---|---|---|
| 0B56 | 0100 | `B4 7A` | `mov AH, 7A` |
| 0B56 | 0102 | `B3 63` | `mov BL, 99` |
| 0B56 | 0104 | `B1 CF` | `mov CL, 11001111b` |
| 0B56 | 0106 | `B8 64 00` | `mov AX, 100` |
| 0B56 | 0109 | `BB 41 00` | `mov BX, 'A'` |
| 0B56 | 010C | `B9 CD AB` | `mov CX, 0ABCDh` |
| 0B56 | 010F | `BA 8C 19` | `mov DX, 6540` |
| 0B56 | 0112 | `C3` | `ret` |
| 0B56 | 0000 | `INT 20H` | (lo ejecuta el sistema al volver del `ret`) |

> [!tip] Cómo verificar en el emulador
> Después de **compilar** (`compile`) y abrir el emulador, usá **`single step`** y mirá cómo cambian **solo algunos bytes de los registros** en cada paso (por ejemplo, `AH` cambia sin tocar `AL`). Al final, `IP` salta a `0000` del segmento `CS` y se ejecuta `INT 20H`: el programa termina y vuelve al sistema.

## Cómo se conecta con la materia

- Los **registros índice** `SI`/`DI` del 8086 son los `RIF`/`RID` de la BLUE indexada ([[Registros base e índice]]).

- Los **registros de segmento** cumplen el papel del **registro base** ([[Registros base e índice]]).

- El **flag IF** de `FLAGS` es el `SI` de las interrupciones de la BLUE ([[Interrupciones y entrada-salida]]).

- `IP` es el **PC** de la BLUE; `CS:IP` es la dirección efectiva ([[Flujo de información en BLUE (datos y direcciones)]]).

- Todo esto en un chip real: [[El 8086 como CPU convencional (TP21)]].

## Errores típicos

- Cargar `AH` y después `AX` y esperar que `AH` conserve su valor (se pisa).

- Decir que `MOV` "mueve": en realidad **copia**.

- Confundir **offset** (posición dentro del segmento, 16 bits) con **dirección física** (20 bits).

- Pensar que `ret` termina el programa: **retorna**; quien termina es `INT 20h`.

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Introducción al uso del Emu8086](https://www.youtube.com/watch?v=6Dv2RVFH-vM) | Delgado Miguel Ángel |
| 📁 | [Material del TP en Google Drive](https://drive.google.com/file/d/1WJBJFrOIoJn9GwHm3EtbM2gDHFS-ANtZ/view) | — |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).

## Relacionado
[[El 8086 como CPU convencional (TP21)]] · [[00 Índice de TPs y qué aporta cada uno]] · [[Registros de la CPU]] · [[Lenguaje máquina y clasificación de instrucciones]] · [[Espacio de direccionamiento y cálculo de CodOp-Dirección]]
