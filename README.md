# Distância entre dois pontos

## AIM:
Encontrar a distância entre dois pontos no plano cartesiano por meio de um programa em Python.

## ALGORITHM:
### Step 1: 
Importar a biblioteca `math`
```python
import math
```

### Step 2: 
Definir dois pontos no plano cartesiano.

### Step 3: 
"Traduzir" a formula para a linguagem Python.

![formula](/formula.JPG)

### Step 4: 
A distância entre dois pontos é igual a hipotenusa de delta_x e delta_y.

Usar a função `math.hypot()`

### Step 5: 
Exibir o Output 

### PROGRAM:
```python
import math

x, y = [-2,4]
x1, y1 = [-5,1]

delta_x = x1 - x
delta_y = y1 - y

distancia = math.hypot((delta_x), (delta_y))

print(f'A distância entre os pontos {x,y} e {x1,y1} é {distancia:.2f}.')
```

### OUTPUT:

A distância entre os pontos (-2, 4) e (-5, 1) é 4.24.

### RESULT:

A distância entre os dois pontos foi encontrada com sucesso.
