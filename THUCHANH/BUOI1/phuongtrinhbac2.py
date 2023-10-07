import math
a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c
def format_number(num):
    if num % 1 == 0:
        return str(int(num))
    return str(num)
if a != 0:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a) 
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("PT co hai nghiem phan biet:")
        print("x1 = ",format_number(x1))
        print("x2 = ",format_number(x2))
    elif delta == 0:
        x = -b/(2*a)
        print("PT co nghiem kep: ", "x1 = x2 = ",format_number(x))
    else:
        print("PTVN")