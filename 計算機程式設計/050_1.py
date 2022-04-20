a = []
b = []
c = []

if input() == 'A':
    while True:
        data = input().split()
        if data != ['B']:
            a.append(list(map(int,data)))
        else:
            break
    a = [list(i) for i in zip(*a)]
    while True:
        data = input().split()
        if data != ['0']:
            b.append(list(map(int,data)))
        else:
            break
print(a)
print(b)
for i in a:
    tem = []
    for j in b:
        tem.append(sum(list(map(lambda k:k[0] * k[1], zip(i,j)))))
    c.append(tem)

for i in c:
    for j in i:
        print(chr(j),end='')