x = int(input())
if 1 <= x <= 30:
    fib0 = 1
    fib1 = 1
    if x == 1:
        fibonacci = fib0
    elif x == 2:
        fibonacci = fib1
    else:
        for i in range(2, x):
            fibonacci = fib0 + fib1
            fib0, fib1 = fib1, fibonacci
    print(fibonacci)
else:
    print(f"So {x} khong nam trong khoang [1,30].")