a, n = input().split()
a, n = float(a), int(n)
a = round(a * n) / n
print('%.10g'%a)