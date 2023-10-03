tre_trung, xinh_dep, co_gau, giau_co = map(int, input().split())

# Kiểm tra các điều kiện
condition1 = not tre_trung or xinh_dep
condition2 = not xinh_dep or co_gau
condition3 = (xinh_dep or  not co_gau) or giau_co

if condition1 and condition2 and condition3:
    print(1)
else:
    print(0)