n = int(input())
a = []
for i in range(n):
    a += [int(input())]
b = sorted(a)
print(int(b[-2]))
print(int(b[0])*int(b[-1]))