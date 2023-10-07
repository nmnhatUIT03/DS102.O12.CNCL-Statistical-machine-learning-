import math
a, b = map(int, input().split())
max = ((a+b)+abs(a-b))/2
min = ((a+b)-abs(a-b))/2
print("max = ",'{:.0f}'.format(max))
print("min = ",'{:.0f}'.format(min))