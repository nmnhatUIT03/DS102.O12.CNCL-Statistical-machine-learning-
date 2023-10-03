age = int(input())

sex = input()

if sex == 'M' or sex == 'm':
    if age >= 21:
        print("1")
    else:
        print("3")
if sex == 'F' or sex == 'f':
    if age >= 21:
        print("2")
    else:
        print("4")
if not sex == 'F' or sex == 'f' or sex == 'M' or sex == 'm':
    print("I do not know why")

    



    