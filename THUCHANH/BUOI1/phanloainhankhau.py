age = int(input())
sex = input()

if (sex == 'M' or sex == 'm') and age >= 21:
    print("1")
elif (sex == 'M' or sex == 'm') and age < 21:
    print("3")
elif (sex == 'F' or sex == 'f') and age >= 21:
    print("2")
elif (sex == 'F' or sex == 'f') and age < 21:
    print("4")
else:
    print("I do not know why")