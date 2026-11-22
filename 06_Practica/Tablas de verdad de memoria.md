---
unidad: 0
tipo: practica
examen: practica
prioridad: maxima
---
# Tablas de verdad de memoria

> [!abstract] Las 10 tablas que hay que poder escribir de memoria
> Si el final práctico consiste en **dibujar y explicar tablas de verdad**, esto es el núcleo.
> Están todas juntas para el repaso de último día.

## 1. Compuertas (2 entradas)
| A | B | AND | NAND | OR | NOR | XOR | NXOR |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |

`NOT`: A = 0 ⇒ 1 · A = 1 ⇒ 0.

## 2. Semisumador
| A | B | S | C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

`S = A⊕B` · `C = A·B`

## 3. Sumador completo
| A | B | Cin | S | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

`S = A⊕B⊕Cin` · `Cout = A·B + Cin(A⊕B)`
**Truco:** S = 1 con **impar cantidad de unos**; Cout = 1 con **dos o tres unos**.

## 4. Decodificador 2→4
| A1 | A0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

Es la **matriz identidad**: una sola salida en 1 por fila.

## 5. Demultiplexor 1→4
| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|
| 0 | 0 | D | 0 | 0 | 0 |
| 0 | 1 | 0 | D | 0 | 0 |
| 1 | 0 | 0 | 0 | D | 0 |
| 1 | 1 | 0 | 0 | 0 | D |

## 6. Multiplexor 4→1
| S1 | S0 | Y |
|---|---|---|
| 0 | 0 | I0 |
| 0 | 1 | I1 |
| 1 | 0 | I2 |
| 1 | 1 | I3 |

## 7. Codificador 8→3
| Entrada activa | X | Y | Z |
|---|---|---|---|
| D0 | 0 | 0 | 0 |
| D1 | 0 | 0 | 1 |
| D2 | 0 | 1 | 0 |
| D3 | 0 | 1 | 1 |
| D4 | 1 | 0 | 0 |
| D5 | 1 | 0 | 1 |
| D6 | 1 | 1 | 0 |
| D7 | 1 | 1 | 1 |

## 8. Biestable RS (sincrónico)
| S | R | Q(t+1) |
|---|---|---|
| 0 | 0 | Q(t) mantiene |
| 1 | 0 | 1 (set) |
| 0 | 1 | 0 (reset) |
| 1 | 1 | prohibido |

## 9. Biestables D, JK y T
| D | Q(t+1) | | J | K | Q(t+1) | | T | Q(t+1) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | | 0 | 0 | Q(t) | | 0 | Q(t) |
| 1 | 1 | | 1 | 0 | 1 | | 1 | Q'(t) |
| | | | 0 | 1 | 0 | | | |
| | | | 1 | 1 | Q'(t) | | | |

## 10. RAM 8×3 — "tabla" de direcciones
| A2 A1 A0 | Palabra habilitada |
|---|---|
| 000 | palabra 0 |
| 001 | palabra 1 |
| 010 | palabra 2 |
| 011 | palabra 3 |
| 100 | palabra 4 |
| 101 | palabra 5 |
| 110 | palabra 6 |
| 111 | palabra 7 |

Capacidad = 8 × 3 = **24 bits**; 3 líneas de dirección, 3 de datos.

> [!tip] Cómo no olvidarse de ninguna
> Pensá en el recorrido de la materia: **compuertas → sumadores → decodificador/MUX → biestables →
> registros/contadores → memoria**. Si te acordás de ese orden, las diez tablas salen en ese orden.

## Enlaces
[[Cómo dibujar los circuitos (checklist de pizarrón)]] · [[Prácticas resueltas]] · [[Autoevaluación]]
