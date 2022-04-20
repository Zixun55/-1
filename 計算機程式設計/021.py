a = int(input())
b = int(input())
if a%2 != 0:
    a = a+1
if b%2 != 0:
    b = b+1
x = 0
for i in range(a,b+1,2):
    x = x+i
print(x)