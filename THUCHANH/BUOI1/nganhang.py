N = int(input())
so_du = 0
for _ in range(N):
    transaction = input().split()  
    operation, amount = transaction[0], int(transaction[1])  
    if operation == 'D':
        so_du += amount  
    elif operation == 'W':
        so_du -= amount 
print(so_du)