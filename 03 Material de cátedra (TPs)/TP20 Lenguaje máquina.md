---
tp: 20
unidad: 5
tipo: tp
prioridad: alta
---
# TP20 — Lenguaje máquina

> [!abstract] Consigna (cátedra)
> **Ej. 1:** ¿qué es el lenguaje máquina y cómo son sus instrucciones? · **Ej. 2:** RISC y CISC, características, ventajas y desventajas · **Ej. 3:** clasificación de las instrucciones de máquina (3 ejemplos de cada grupo) · **Ej. 4:** gráfico de una máquina de 16 bits con sus componentes y organización interna · **Ej. 5:** formato de instrucción de 16 bits de esa máquina · **Ej. 6:** programa ejemplo de al menos 5 instrucciones y explicación de su ejecución.

## Ej. 1 — Qué es el lenguaje máquina
> "Es el sistema de códigos **interpretable directamente por el circuito** del procesador. Se compone de un conjunto de **instrucciones** que determinan las acciones que realiza la máquina; un programa es una **cadena de esas instrucciones** más los datos. Las instrucciones son **exclusivamente ceros y unos** y son **específicas de cada arquitectura** (aunque los conjuntos se parezcan entre sí)."

Se ejecutan **en secuencia**, con cambios de flujo por el propio programa (saltos) o por **eventos externos** (interrupciones). Es el **último nivel** de la jerarquía: lenguaje de alto nivel → ensamblador → **máquina**.

## Ej. 2 — RISC vs CISC (versión del TP, con ventajas y desventajas)

| | **RISC** (reduced) | **CISC** (complex) |
|---|---|---|
| Conjunto | reducido, instrucciones simples | amplio, instrucciones complejas y poderosas |
| **Ventajas** | ejecución más rápida; diseño y fabricación más fáciles y baratos; escalable; buena compatibilidad con compiladores modernos | poco esfuerzo del compilador; **código corto** (menos memoria); menos instrucciones para la misma tarea; gestión de energía/reloj |
| **Desventajas** | el rendimiento depende del código (dependencias entre instrucciones); mucho software usa instrucciones complejas; necesita memorias muy rápidas y **caché grande** | varios **ciclos de reloj** por instrucción; el **pipeline se complica**; muchos más transistores; mayor consumo, temperatura y tamaño; se usa sólo ~20 % de las instrucciones |

## Ej. 3 — Clasificación de las instrucciones (con 3 ejemplos cada grupo)

| Grupo | Qué hace | Ejemplos |
|---|---|---|
| **Transferencia de datos** | mueven datos entre memoria, registros y E/S | `LOAD` · `STORE` · `MOV` |
| **Aritméticas / lógicas** | operan con la ALU | `ADD` · `SUB` · `AND` (también `OR`, `XOR`, `NOT`, desplazamientos) |
| **De control** | cambian el flujo del programa | `BRANCH` · `JUMP` · `CALL`/`RET` (y las condicionales `JZ`, `JC`) |

(Se pueden agregar: **de E/S** (`IN`/`OUT`) y **de control del sistema** (`HLT`, `NOP`, instrucciones de interrupciones y de manejo de pila `PUSH`/`POP`).)

## Ej. 4 y 5 — Máquina de 16 bits y su formato
Componentes a graficar: **UC, ALU, registros (PC, IR, MAR, MBR, y los registros de trabajo), memoria y buses**, cada uno con su organización interna (por ejemplo, el registro formado por flip-flops D y la memoria como matriz con decodificador).

**Formato de instrucción de 16 bits** (como en el TP17): `opcode + dirección`, y si la máquina tiene registros, `opcode + registro + dirección`:
```
 ┌────────┬───────────┬─────────────────┐
 │ opcode │  registro │    dirección    │
 └────────┴───────────┴─────────────────┘
```

## Ej. 6 — Programa ejemplo
El TP propone (con su propia máquina de 16 bits) algo equivalente a:
```
 156C   ; cargar el registro 5 con el contenido de la celda 6C
 166D   ; cargar el registro 6 con el contenido de la celda 6D
 5056   ; sumar los registros 5 y 6 y dejar el resultado en el registro 0
 306E   ; almacenar el registro 0 en la celda 6E
 C000   ; parar
```
**Cómo explicar la ejecución:** "el **PC** contiene la dirección de la primera instrucción; la UC la busca (PC→MAR→memoria→MBR→**IR**), la decodifica (los primeros bits son el opcode, los siguientes el registro y los últimos la dirección) y la ejecuta; el **PC se incrementa** y se repite. En este programa actúan: PC, MAR, MBR, IR, la UC (señales), los **registros de trabajo** y la **ALU** en la suma. Al final, el resultado queda en la celda 6E."

> [!tip] Cómo adaptar este ejercicio a BLUE
> Es el mismo ejercicio que [[TP16 Ciclo de instrucción básico|el programa del TP16]] (cargar, sumar, almacenar), pero con registros. En el final, si te dan un programa, **describí siempre el ciclo completo de cada instrucción** y terminá diciendo en qué registro/celda queda el resultado. Eso es lo que se evalúa.

## Enlaces
Desarrollo: [[Lenguaje máquina y clasificación de instrucciones]] · [[CISC y RISC]] · [[Programar en BLUE — ejemplos]] Anterior: [[TP19 Modos de direccionamiento]]
