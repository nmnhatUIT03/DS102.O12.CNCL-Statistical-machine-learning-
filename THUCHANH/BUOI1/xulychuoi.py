s = input()
s = s.lower()
s = s.replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
res = ''
for char in s:
    res += '.' + char
print(res)