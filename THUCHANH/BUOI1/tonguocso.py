# Nhập một số nguyên từ bàn phím
num = int(input("Nhập một số nguyên: "))

# Khởi tạo biến sum_of_divisors để tính tổng các ước số
sum_of_divisors = 0

# Tìm ước số của số vừa nhập và cộng vào tổng
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

# In tổng các ước số
print(f"Tổng các ước số của {num} là: {sum_of_divisors}")
