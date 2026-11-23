---
tp: 15
unidad: 4
tipo: tp
prioridad: alta
---
# TP15 — Arquitectura de Von Neumann (IAS)

> [!abstract] Consigna (cátedra)
> **Ej. 1:** describir los principales componentes de la arquitectura de Von Neumann (IAS) y sus relaciones, y **graficarlos**. **Ej. 2:** describir el **formato de datos** del IAS, explicar cómo sería una **palabra instrucción**, dar un ejemplo y su **representación gráfica en la memoria principal**. **Ej. 3:** describir la **estructura ampliada** del computador IAS y cada componente, con gráfico.

## Ej. 1 — Componentes del IAS y sus relaciones

| Componente | Función |
|---|---|
| **Unidad de control (UC)** | decodifica la instrucción y gobierna todas las transferencias |
| **ALU** | operaciones aritméticas y lógicas; en el IAS incluye el registro **AC** (acumulador) y el **MQ** (cociente/multiplicador) |
| **Memoria principal** | 4096 posiciones de 40 bits, guarda **instrucciones y datos** |
| **Registros**: PC, MAR, MBR, IR, IBR | PC = próxima instrucción · MAR = dirección · MBR = dato/instrucción · IR = instrucción en curso · IBR = buffer de la instrucción de la derecha |
| **E/S** | periféricos y su control |

**Relación (la frase clave):** "Es una arquitectura de **programa almacenado**: la instrucción y el dato están en la **misma memoria**, y la UC los trae secuencialmente usando el **PC**; por eso hay **un solo bus** y el acceso es **secuencial** (cuello de botella de von Neumann)."

## Ej. 2 — Formato de datos y palabra instrucción

- **Palabra del IAS: 40 bits** (5 bytes).

- **Formato de datos**: un número entero de 40 bits, con bit de signo (complemento a 2) — en el IAS se trabaja con palabras completas.

- **Palabra instrucción del IAS: 20 bits**, en dos mitades de 10:
```
  ┌────────┬──────────┬──────────┬──────────┐
  │ opcode │ dirección│ opcode   │ dirección│
  │ (8 bits)│ (12 bits)│          │          │
  └────────┴──────────┴──────────┴──────────┘
   mitad izquierda (instrucción)  mitad derecha (opcional)
```

> [!note] La idea que hay que transmitir
> En el IAS una palabra de 40 bits puede contener **dos instrucciones de 20 bits** (una en cada mitad), y la segunda se guarda en el **IBR** mientras se ejecuta la primera. Eso es lo que después se generaliza como **palabra instrucción = opcode + dirección**.

**Ejemplo de representación en memoria** (lo que pide el TP):

| Dirección | Contenido | Interpretación |
|---|---|---|
| 000 | `00000101 000000000101` | opcode 5, dirección 5 |
| 001 | `00010100 000000000110` | opcode 20, dirección 6 |

## Ej. 3 — Estructura ampliada
Es el gráfico clásico: **memoria** arriba, **MAR/MBR** como puerta de la memoria, **PC/IR/IBR** en el camino de la instrucción, **AC y MQ** junto a la **ALU**, y la **UC** con las líneas de control a todos los bloques. Es el mismo esquema de [[Estructura básica de un computador]] con más registros.

> [!tip] Cómo cerrar la respuesta
> "Von Neumann separa **hardware** (unidades) de **software** (programa almacenado): la misma unidad de memoria guarda instrucciones y datos, y la UC los interpreta. De ahí vienen todas las ventajas (flexibilidad, programa reemplazable) y el problema (un solo bus ⇒ cuello de botella), que se resuelve con caché, pipeline y DMA."

## Enlaces
Desarrollo: [[Estructura básica de un computador]] · [[Registros de la CPU]] Siguiente: [[TP16 Ciclo de instrucción básico]]

## Videos del TP

Los videos que la cátedra dejó en la consigna del TP, con el título real de cada uno:

| | Recurso | Canal / fuente |
|---|---|---|
| ▶️ | [Arquitectura de von Neumann](https://www.youtube.com/watch?v=McA-9_qgq4Y) | FNE Profesor |

> [!tip] Cómo usarlos
> Mirá el video **después** de leer el subtema: sirve para ver el circuito moverse, no para aprenderlo desde cero. Si el video y la nota no coinciden en algo, **manda la nota** (está alineada con lo que se toma en el parcial).
