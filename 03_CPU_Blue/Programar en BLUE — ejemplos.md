---
unidad: 4
tipo: practica
examen: practica
---
# Programar en BLUE — ejemplos

> [!abstract] En una frase
> Programar en BLUE es escribir **una instrucción por línea**, con `opcode` + `dirección`, y recordar que
> **todo pasa por el AC**: no hay registros de propósito general. Alcanza con `LDA`, `STA`, `ADD`/`SUB`,
> los saltos `JZ`/`JC`/`JMP` y `HLT`.

## Modelo de programación
| Elemento | Uso |
|---|---|
| `AC` | único registro de trabajo (acumulador) |
| Memoria | programa **y** datos (von Neumann) |
| `JZ`, `JC` | únicos saltos condicionales: se usan **después** de una operación que fije Z o C |
| Etiquetas | direcciones simbólicas (el ensamblador las traduce) |

## Ejemplo 1 — suma de dos números
```
        LDA  x        ; AC ← M[x]      (carga el primer sumando)
        ADD  y        ; AC ← AC + M[y] (suma el segundo)
        STA  z        ; M[z] ← AC      (guarda el resultado)
        HLT
x:      5
y:      7
z:      0
```

## Ejemplo 2 — máximo de dos números (usa `SUB` y `JC`/`JZ`)
```
        LDA  a        ; AC ← a
        SUB  b        ; AC ← a - b   (si a < b, el resultado es negativo ⇒ hubo borrow ⇒ C = 1)
        JC   bmayor   ; si hubo acarreo/borrow, b > a
        LDA  a        ; AC ← a
        JMP  fin
bmayor: LDA  b        ; AC ← b
fin:    STA  max
        HLT
a:      12
b:      30
max:    0
```
> [!tip] Cómo se compara en una máquina de un solo acumulador
> No hay instrucción de comparación: **se compara restando**. El resultado de `SUB` actualiza Z (resultado
> cero ⇒ son iguales) y C (borrow ⇒ el primero era menor). Después se salta según el flag.

## Ejemplo 3 — lazo: sumar los primeros 5 números
```
        LDA  cero     ; AC ← 0        (acumulador de la suma)
        STA  suma
        LDA  uno
        STA  cont     ; cont ← 1
lazo:   LDA  suma
        ADD  cont     ; suma ← suma + cont
        STA  suma
        LDA  cont
        ADD  uno      ; cont ← cont + 1
        STA  cont
        SUB  cinco    ; ¿cont = 5?  (cont - 5 = 0 ⇒ Z = 1)
        JZ   fin
        JMP  lazo
fin:    HLT
cero:   0
uno:    1
cinco:  5
suma:   0
cont:   0
```

## Ejemplo 4 — operaciones lógicas (máscaras)
```
        LDA  dato
        AND  mascara   ; aísla los bits que están en 1 en la máscara
        STA  resultado
        LDA  dato
        XOR  todos1    ; complemento a 1 (XOR con todo 1)
        STA  invertido
        HLT
```
- `AND` con una máscara = **enmascarar** (poner en 0 los bits que no interesan).
- `OR` con una máscara = **encender** bits.
- `XOR` con todo 1 = **complementar**; `XOR` con una máscara = **invertir sólo esos bits**.

## Ejemplo 5 — entrada/salida
```
        IN   5        ; AC ← dato del puerto 5 (por ejemplo, un teclado)
        OUT  6        ; puerto 6 ← AC (por ejemplo, un display)
        HLT
```

## Cómo se arma la instrucción en binario
Instrucción `LDA 25h` con `opcode LDA = 0000` y dirección `25h = 0000 0010 0101`:
```
 0000 | 0000 0010 0101
 opcode   dirección (12 bits)
```
`SUB 30h` con `opcode SUB = 0011` y `30h = 0000 0011 0000`:
```
 0011 | 0000 0011 0000
```
> [!warning] Números de opcode
> Verificá la tabla binaria en tu apunte ([[Máquina BLUE — arquitectura y conjunto de instrucciones]]).
> La estructura `4 + 12` bits sí es la de la cátedra y eso es lo que se corrige.

## Cómo responderlo en el final
1. Aclarar el modelo: un AC, memoria con programa y datos, saltos por flags.
2. Escribir un programa corto (suma, lazo o máximo) **comentado línea por línea**.
3. Explicar cómo se compara (restando) y por qué `JZ`/`JC` funcionan.
4. Mostrar el ensamblado en binario de una instrucción (opcode + dirección).

## Errores típicos
- Usar un registro que no existe (`R1`, `R2`): en BLUE sólo hay AC.
- Hacer `SUB` y saltar sin pensar qué flag corresponde (Z = iguales, C = borrow).
- Olvidar recargar el AC antes de cada operación (las operaciones **destruyen** el AC anterior).
- Confundir la etiqueta con una instrucción (es una dirección).

## Relacionado
[[Máquina BLUE — arquitectura y conjunto de instrucciones]] · [[Ciclo de ejecución — todas las operaciones]] · [[BLUE indexada (RIF, RID, nuevo formato)]]
