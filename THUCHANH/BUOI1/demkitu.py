s = input()
dem_chu, dem_so = 0, 0
for i in s:
    if i.isalpha():
        dem_chu += 1
    elif i.isnumeric():
        dem_so += 1
print(dem_chu)
print(dem_so)