a = int(input())
b = int(input())
flag = []
for i in range(a, b+1):
    if i % 7 == 0 and i % 5 != 0:
        flag.append(str(i))
print(','.join(flag))