import math as m
a, b, c = map(float, input().split())
print('{:0.2f}'.format ( a ** 5 -2 * m.sqrt(abs(b)) + a * b * c))