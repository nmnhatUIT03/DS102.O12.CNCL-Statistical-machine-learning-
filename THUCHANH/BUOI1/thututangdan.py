arr = []

a = arr.append(float(input()))
b = arr.append(float(input()))
c = arr.append(float(input()))

arr.sort()

for num in arr:
    if(num) == int(num):
        num = int(num)
    print(num, end=" ")