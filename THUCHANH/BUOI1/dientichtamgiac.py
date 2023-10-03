a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2

area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(format(area, ".2f"))