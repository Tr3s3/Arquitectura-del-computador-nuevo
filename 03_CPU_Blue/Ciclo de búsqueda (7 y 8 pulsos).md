---
unidad: 4
tipo: concepto
examen: secundario
prioridad: maxima
---
# Ciclo de búsqueda (7 y 8 pulsos)

> [!abstract] En una frase
> El ciclo de búsqueda es la secuencia **fija** con la que la CPU trae la instrucción desde la memoria al
> IR: `PC → MAR → memoria → MBR → IR` **y el PC se incrementa**. En BLUE insume **8 pulsos** (o **7** si el
> incremento del PC se hace solapado con la carga del MAR).

## La secuencia, pulso por pulso
| Pulso | Microoperación | Señales de control que activa la UC | Comentario |
|---|---|---|---|
| **T0** | `MAR ← PC` | `PCout`, `MARin` | la dirección de la instrucción va al MAR |
| **T1** | `MEMR = 1` | `MEMR` (read) | se inicia el acceso a memoria |
| **T2** | *(espera de memoria)* | — | el bus de datos se estabiliza (tiempo de acceso) |
| **T3** | `MBR ← M[MAR]` | `MBRload` | el dato leído se guarda en el MBR |
| **T4** | `PC ← PC + 1` | `PCinc` | queda apuntando a la próxima instrucción |
| **T5** | `IR ← MBR` | `MBRout`, `IRin` | la instrucción queda en el IR |
| **T6** | decodificar el opcode | (interno de la UC) | el opcode del IR entra al decodificador |
| **T7** | `STATE ← E`, `MEMR = 0` | `STATE` | fin de la búsqueda; empieza la ejecución |

⇒ **8 pulsos** (`T0` a `T7`).

## ¿Y los 7 pulsos?
> [!important] La respuesta exacta (está en el apunte de Foster que usa la cátedra)
> El ciclo de máquina de la BLUE tiene **8 pulsos**, pero **la búsqueda se completa en 7**: en CP1 se copia el
> PC al MAR (y a Z) y se ordena la lectura; CP2 pone +1 en Y; CP3 deja estabilizar la ALU; **CP4 incrementa el
> PC**; CP5 copia el dato de memoria al MBR; **CP6 pasa el MBR al IR** y empieza la decodificación; **CP7 y CP8
> quedan libres** para ejecutar.
>
> **¿Por qué 8 y no 7, entonces?** Porque la BLUE original usaba **memoria de núcleos de ferrita**, que es
> **destructiva**: al leerla, el dato se borra, así que hay que **volver a escribirlo**. Ese pulso extra era
> para la reescritura. Con memorias de semiconductores (no destructivas) el octavo pulso ya no es necesario,
> pero **se mantiene** para no cambiar el diseño y se aprovecha para adelantar la ejecución (las 8
> instrucciones que terminan en un solo ciclo lo usan).
>
> **Frase para el final**: *"la búsqueda necesita 7 pulsos; el ciclo de máquina tiene 8 porque el octavo era
> el pulso de reescritura de la memoria de ferrita. Con semiconductores sobra, y se usa para ejecutar."*

## Diagrama de tiempos
```
         T0    T1    T2    T3    T4    T5    T6    T7
        ┌────┬────┬────┬────┬────┬────┬────┬────┐
PCout   │ ▓  │    │    │    │    │    │    │    │
MARin   │ ▓  │    │    │    │    │    │    │    │
MEMR    │    │ ▓  │ ▓  │    │    │    │    │    │
MBRload │    │    │    │ ▓  │    │    │    │    │
PCinc   │    │    │    │    │ ▓  │    │    │    │
MBRout  │    │    │    │    │    │ ▓  │    │    │
IRin    │    │    │    │    │    │ ▓  │    │    │
STATE=E │    │    │    │    │    │    │    │ ▓  │
        └────┴────┴────┴────┴────┴────┴────┴────┘
```

**Dos reglas que se ven en el diagrama:**
1. `PCout` y `MARin` van juntos (es **una** transferencia por el bus: origen habilita, destino carga).
2. `MBRload` y `MBRout` **no pueden coincidir**: el MBR no puede leer la memoria y escribir el bus en el
   mismo pulso.

## Por qué es igual para todas las instrucciones
Porque antes de decodificar no se sabe qué hay que hacer. La búsqueda es **independiente del opcode**: por
eso la UC puede tenerla "cableada" y siempre dura lo mismo. Esa es la razón por la que el ciclo de
instrucción se puede medir como `búsqueda + ejecución` (ver [[Ciclo de máquina]]).

## Detalles que suben nota
- El **incremento del PC en T4** es lo que permite ejecutar instrucciones consecutivas; si se salta, el
  valor que queda en el PC se sobrescribe (`PC ← dir`).
- La instrucción tiene `opcode (4) + dirección (12)`: el decodificador de `T6` usa sólo 4 bits, el resto se
  guarda para el campo dirección.
- Si la memoria es lenta, se agregan **pulsos de espera** (`WAIT`) informados por la señal `READY`: es el
  mismo mecanismo que usan los buses asíncronos.

## Los 6 pasos del video (versión de la cátedra, TP16)
La cátedra describe el ciclo de instrucción en **6 pasos** que engloban búsqueda + ejecución:
1. **Búsqueda de la instrucción** (`PC → MAR → memoria → MBR → IR`) y `PC ← PC + 1`.
2. **Decodificación** del opcode en la UC.
3. **Búsqueda del operando** (si la instrucción lo requiere): la dirección del IR va al MAR.
4. **Ejecución** de la operación (ALU o transferencia).
5. **Almacenamiento del resultado** (registro o memoria).
6. **Preparación de la próxima instrucción** (el PC ya apunta a la siguiente; se vuelve al paso 1).

Estos 6 pasos se ven aplicados a un programa concreto en [[TP16 Ciclo de instrucción básico]] (cargar 1,
sumarle 3, guardar el resultado). Si te piden "el ciclo de búsqueda", detallá los pulsos; si te piden "el
ciclo de instrucción básico", usá estos 6 pasos. **Son el mismo proceso con distinto nivel de detalle.**

## Cómo responderlo en el final
1. Definir: secuencia fija que trae la instrucción al IR.
2. Listar la tabla de 8 pulsos con señal(es) por pulso.
3. Aclarar explícitamente el asunto de **7 vs 8** (pulso de espera / incremento solapado).
4. Dibujar el diagrama de tiempos o al menos la cadena `PC → MAR → memoria → MBR → IR`.
5. Cerrar con que la búsqueda es idéntica para toda instrucción y que el PC queda apuntando a la siguiente.

## Errores típicos
- Olvidar el **incremento del PC** (el error más caro).
- Poner `IR ← MBR` antes de que el dato esté en el MBR.
- Activar `PCout` y `MBRout` en el mismo pulso (dos fuentes en el bus).
- Decir que en la búsqueda se lee el **operando**: se lee la **instrucción**; el operando se busca en la
  ejecución.

## Relacionado
[[Ciclo de máquina]] · [[Ciclo de ejecución — todas las operaciones]] · [[Flujo de información en BLUE (datos y direcciones)]] · [[Unidad de Control]]
