s = input()
a = []
b = 0
for i in s:
    if i.islower():
        a += i
    elif i.isupper():
        b = b+1
if len(a) != 0:
    for i in range(len(a)):
        print(a[i],end='') 
else:
    print('No lowercase letters')
print('')
print(len(s))
print(b)