import math

calcular_delta = lambda p, p1: p1 - p
distancia = lambda x, y, x1, y1: math.hypot(calcular_delta(x,x1), calcular_delta(y, y1))

print(f'{distancia(-2,4,-5,1):.2f}')
