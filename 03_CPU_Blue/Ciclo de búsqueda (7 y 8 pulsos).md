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
> [!warning] El punto que hay que saber explicar
> La secuencia **conceptual** tiene 7 operaciones (MAR←PC, MEMR, MBR←dato, PC+1, IR←MBR, decodificar,
> STATE←E). El **8.º pulso** aparece cuando la memoria necesita un pulso extra de **espera** para que el
> dato esté estable en el bus (`T2` en la tabla). Por eso la bibliografía habla indistintamente de 7 u 8:
> - **7 pulsos**: memoria rápida / diseño con el incremento del PC en paralelo con `MAR ← PC`.
> - **8 pulsos**: se cuenta el pulso de espera de memoria (o el de decodificación como pulso propio).
>
> En el final conviene decir: *"la búsqueda tiene 7 pasos; el conteo en pulsos es 7 u 8 según se cuente el
> pulso de espera de memoria (o el incremento del PC solapado). Si tu apunte dice 8, la tabla es T0…T7."*
> Lo que **se evalúa** es que puedas justificar la cuenta, no el número.

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
