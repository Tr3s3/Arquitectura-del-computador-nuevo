---
tipo: indice
unidad: 10
---
# Unidad 10 — Entrada y Salida

> [!abstract] Qué pide la unidad
> Cómo la CPU **habla con el mundo**: E/S **programada** (polling), por **interrupciones** y por **DMA**; puertos,
> interfaces y dispositivos. Cierra la materia con el mecanismo que ya usaste en la 1.ª tanda (INP/OUT de BLUE) y
> en la 2.ª (interrupciones, peso 9).

| Tema | Subtemas | Dónde está el desarrollo |
|---|---|---|
| **10.1 E/S programada (polling)** | la CPU pregunta en un lazo · desperdicia tiempo · INP/OUT de la BLUE | [[Interrupciones y entrada-salida]] · carpeta `Tanda 2/2.8` |
| **10.2 E/S por interrupciones** | `IRQ·SI·CP8` · polling del flag · máscara (EMR) · pila y RTI · vectorizadas | [[Interrupciones y entrada-salida]] · carpeta `Tanda 2/2.8` |
| **10.3 DMA** | el controlador mueve bloques sin la CPU · robo de ciclo · handshake | [[Interrupciones y entrada-salida]] (sección comparativa) · [[Técnicas para aumentar la velocidad]] |
| **10.4 Puertos e interfaces** | puerto paralelo vs serie · handshake · buffers · memorias auxiliares | [[Memoria auxiliar y memoria asociativa]] · [[TP12 Memoria principal]] |
| **10.5 Dispositivos y jerarquía** | discos, SSD, cintas · latencias · por qué el disco es el último nivel | [[Jerarquía de memorias]] · carpeta `Tanda 2/2.4` |

---

## Qué hay que saber hacer
1. **Comparar** polling, interrupciones y DMA en una tabla (quién inicia, quién ocupa la CPU, para qué sirve).
2. Explicar **el problema de las interrupciones anidadas** y cómo lo resuelve la máscara.
3. Decir **qué guarda la pila** al entrar a una interrupción y qué restaura `RTI`.
4. Justificar **para qué está el DMA** (bloques grandes, sin gastar la CPU).

## TPs de la unidad
No hay TP propio: se estudia con [[TP16 Ciclo de instrucción básico]] (ciclo de E/S) y la parte de E/S de
[[TP17 Formato básico de instrucciones]].

## Fuente de la cátedra
Apuntes **Unidad 10** · `blue.pdf` (E/S de la máquina elemental) · Stallings (E/S) · Tanenbaum (E/S).

---

## Relacionado
[[00 Índice de la materia (las 10 unidades)]] · [[00 Unidad 9 — temas y subtemas]] ·
[[00 Índice — el final resuelto]]
