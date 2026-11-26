---
tipo: pregunta-de-final
bloque: 1 · Preguntas principales
peso: alto
---
# P04 · Estructura básica de un computador (unidades y buses)

> [!question] Pregunta
> Describa la estructura básica de un computador: cada unidad, qué hace y cómo se conectan mediante los buses.

## 1. Teoría previa

**Computador (modelo von Neumann).** Son cinco unidades conectadas por buses:
- **CPU**: ejecuta las instrucciones. Tiene dos partes: la **UC** (controla) y la **ALU** (calcula), más los **registros** (memoria rápida interna).
- **Memoria**: guarda programa y datos en la misma memoria.
- **Entrada / salida (E/S)**: intercambian información con el mundo exterior (teclado, pantalla, disco).
- **Buses**: líneas compartidas que comunican todo.

**Los tres buses.**

| Bus | Función | Sentido | Su ancho determina |
|---|---|---|---|
| **Datos** | transporta el dato o la instrucción | bidireccional | el tamaño de palabra (16 bits en BLUE) |
| **Direcciones** | indica a quién va el dato | unidireccional, CPU → memoria/E/S | la capacidad (2ⁿ) (12 bits = 4096 celdas) |
| **Control** | dice qué hacer y cuándo | de la UC a todos | cuántas operaciones de control hay |

**Von Neumann vs. Harvard.**
- **Von Neumann**: una sola memoria para programa y datos. Simple, pero el bus atiende una cosa por vez: es el **cuello de botella**.
- **Harvard**: dos memorias y dos buses separados. Permite buscar instrucción y dato a la vez, pero cuesta más hardware. Se usa en cachés L1 y microcontroladores.

## 2. Contexto

Esta pregunta es el **mapa** de la materia. Todo lo demás se ubica dentro de estas cinco unidades. Por eso el profesor la pide primero: quiere saber si podés dibujar el computador completo y explicar qué hace cada parte y cómo se comunica. Conecta con P01 (flujo por el bus), P07 (UC) y P08 (E/S).

## 3. Gráfico

![[P04-estructura-computador.svg]]

*Lectura:* la CPU (izquierda) se conecta a la memoria (arriba derecha) y a la E/S (abajo derecha) por tres buses: datos, direcciones y control. El bus de datos es bidireccional; el de direcciones sale de la CPU.

## 4. Desarrollo detallado

### 4.1 La CPU

- **UC**: decodifica el opcode y genera las señales de control. No procesa datos. "Manda".
- **ALU**: suma, resta, AND, OR, NOT, XOR. Fija los flags Z (cero) y C (acarreo / signo).
- **Registros**: PC (12), MAR (12), MBR (16), IR (16), AC (16). Son la memoria más rápida del sistema.

### 4.2 La memoria

- Guarda programa y datos. Se direcciona por el bus de direcciones.
- En BLUE: 4096 palabras de 16 bits (12 bits de dirección).
- Usa el decodificador y las celdas que vemos en P05.

### 4.3 La E/S

- Interfaces que adaptan la velocidad y el formato del periférico a los buses.
- Tres formas de comunicarse con la CPU: **polling** (la CPU pregunta), **interrupciones** (el periférico avisa) y **DMA** (un controlador mueve bloques sin la CPU).

### 4.4 Los buses, en detalle

- **Todos escuchan, uno habla por vez**: hace falta seleccionar quién responde (dirección + chip select) y que cada dispositivo pueda desconectarse (tres estados).
- **Un dispositivo en alta impedancia** es el que no está usando el bus.

### 4.5 Cuello de botella de von Neumann

Como hay un solo bus, no se puede traer una instrucción y un dato en el mismo pulso. Las soluciones: **cachés separadas** para instrucciones y datos, **pipeline** y **DMA**.

### 4.6 Ejemplo histórico: la IAS (TP15)

- Palabra de 40 bits, instrucción de 20 bits en dos mitades de 8 (opcode) + 12 (dirección).
- Dos instrucciones por palabra. Memoria de 4096 palabras.
- Sirve para mostrar que la estructura von Neumann ya existía antes de BLUE.

## 5. Cómo se responde (3 minutos)

1. **Definición:** "Un computador de von Neumann tiene CPU, memoria, E/S y buses; una sola memoria guarda programa y datos."
2. **Dibujo:** CPU a la izquierda, memoria arriba, E/S abajo, y los tres buses.
3. **Desarrollo:** una frase por unidad, y cómo viaja la información.
4. **Cierre:** "El cuello de botella es el bus único; por eso aparecen cachés, pipeline y DMA."

## 6. Repreguntas y errores típicos

| Repregunta | Respuesta |
|---|---|
| ¿Diferencia entre bus de datos y de direcciones? | Datos: bidireccional, ancho = palabra. Direcciones: unidireccional, ancho = capacidad. |
| ¿Qué es Harvard? | Memorias y buses separados para instrucciones y datos. |
| ¿Por qué el bus de direcciones es unidireccional? | La CPU siempre indica a dónde ir; la memoria no le indica a la CPU qué direccionar. |
| Error común | Decir que la UC procesa datos. La UC sólo genera señales. |

## 7. Relacionado

- [[Estructura básica de un computador]] · [[3.1.3 Buses de datos, de direcciones y de control]] · [[4.1.1 Unidades funcionales de una computadora]]
- [[P01 Flujo de información (datos y direcciones)]] · [[P07 Unidad de Control (funciones, señales e importancia)]]
