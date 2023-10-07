num = int(input())
num_str = str(num)
num_digits = len(num_str)
armstrong_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10
if num == armstrong_sum:
    print("True")
else:
    print("False")