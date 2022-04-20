m,n = int(input()),int(input())
a = 0
b = 1
for i in range(m,n+1,2):
    a = a + i
print(a)
for i in range(m,n+1,3):
    b = b * i
print(b)