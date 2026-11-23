---
unidad: 4
tipo: concepto
examen: principal
prioridad: maxima
---
# Registros de la CPU

> [!abstract] En una frase
> Los registros son las **memorias internas de la CPU** (hechas con flip-flops): guardan lo mínimo necesario para ejecutar una instrucción —dónde está el programa (**PC**), qué instrucción se ejecuta (**IR**), qué dirección se usa (**MAR**), qué dato se trae (**MBR**) y con qué se opera (**AC**).

## Tabla de registros (la que se pide)

| Registro | Ancho (BLUE) | Función | Quién lo escribe / lee |
|---|---|---|---|
| **PC** — contador de programa | 12 bits | dirección de la **próxima** instrucción | se incrementa en cada búsqueda; se **carga** si hay salto |
| **IR** — registro de instrucción | 16 bits | la instrucción **en ejecución** (opcode + dirección) | se carga al final de la búsqueda; el opcode va a la UC |
| **MAR** — registro de dirección de memoria | 12 bits | dirección que se envía al **bus de direcciones** | UC (desde PC o desde el campo dirección del IR) |
| **MBR** — registro de buffer de memoria | 16 bits | dato que entra o sale de memoria (buffer del **bus de datos**) | memoria (lectura) o bus (escritura) |
| **AC** — acumulador | 16 bits | operando principal de la ALU; guarda el resultado | ALU / MBR |

> [!tip] Por qué existen el MAR y el MBR
> La memoria es lenta y está lejos: no se conecta directo a los registros de trabajo. El **MAR** sostiene la dirección estable durante todo el acceso y el **MBR** sostiene el dato, desacoplando los tiempos. Además, si el bus es único, sin ellos no se podría mantener la dirección mientras llega el dato.

## Registros que agrega la máquina indexada (Unidad 5)

| Registro | Función |
|---|---|
| **RIF** — registro índice final | contiene un desplazamiento que **se suma** a la dirección de la instrucción |
| **RID** — registro índice de desplazamiento | segundo registro índice (permite dos arreglos/tablas a la vez) |
| **Registro de estado / flags** | bits Z (resultado cero), C (acarreo), N (negativo), V (desbordamiento), I (interrupciones habilitadas) |
| **Puntero de pila (SP)** | dirección del tope de la pila; se usa para llamadas a subrutina e interrupciones |
| **Registro base** | dirección del comienzo de un bloque/tabla (para reubicación y segmentos) |

Ver [[Modos de direccionamiento]] y [[BLUE indexada (RIF, RID, nuevo formato)]].

## Registros de control de la UC
No guardan datos, guardan **estado del ciclo**: en BLUE son **RUN** (marcha/parada), **STATE** (F = buscando, E = ejecutando) y **CLOCK** (genera los pulsos). Ver [[Unidad de Control]].

## Cómo se usan en el ciclo (resumen)
```
búsqueda:    PC → MAR → memoria → MBR → IR
ejecución:   IR(dir) → MAR → memoria → MBR → AC   (LDA)
             AC → MBR → memoria                  (STA)
             PC ← dir  (JMP)   |   PC ← PC+1 (normal)
```
El detalle pulso por pulso está en [[Ciclo de búsqueda (7 y 8 pulsos)]] y [[Ciclo de ejecución — todas las operaciones]].

## Cómo responderlo en el final

1. Definir: registros = memoria interna de la CPU, de acceso en un pulso.

2. Enumerar PC, IR, MAR, MBR, AC con **ancho y función** (y quién los carga).

3. Explicar por qué MAR/MBR existen (desacoplar la memoria del bus).

4. Mencionar los que agrega la indexada (RIF, RID) y el de estado (Z, C).

5. Cerrar mostrando el recorrido PC→MAR→MBR→IR.

## Errores típicos

- Confundir **MAR** (dirección) con **MBR** (dato): la pista es "A" de *address*.

- Decir que el PC guarda la instrucción actual (eso es el IR): el PC guarda la **dirección** de la próxima.

- Olvidar que el IR tiene el **opcode** que alimenta a la UC (sin IR no hay decodificación).

- Confundir el acumulador (dato) con el registro de estado (flags).

## Relacionado
[[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Flujo de información en BLUE (datos y direcciones)]] · [[Ciclo de máquina]] · [[Unidad de Control]]
