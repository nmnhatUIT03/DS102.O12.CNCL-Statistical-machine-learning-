for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            d = abs(i-2) + abs(j-2)
print(d)

