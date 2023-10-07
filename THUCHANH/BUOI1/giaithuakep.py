n = int(input())
tich_chan = 1
tich_le = 1
for i in range(2, n+1, 2):
    tich_chan *= i
for i in range(1, n+1, 2):
    tich_le *= i
if n % 2 == 0:
    print(tich_chan)
else:
    print(tich_le)