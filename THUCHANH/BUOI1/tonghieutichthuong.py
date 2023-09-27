a, b = map(int, input().split())
format_float = "{:.2f}".format
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)    
print(a, "x", b, "=", a * b)    
print(a, ":", b, "=", format_float(float(a / b)))