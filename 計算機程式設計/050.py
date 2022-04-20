A = input()
a = []#A矩陣
b = []#B矩陣
a_final = []#A矩陣翻轉
c = []

while True:
    A_input = input()
    if A_input == 'B':
        break
    else:
        A_input = A_input.split()
        a.append(list(map(int,A_input)))

for i in range(len(a[0])):
    a_change = []
    for j in range(len(a)):
        a_change.append(a[j][i])
    a_final.append(a_change)

while True:
    B_input = input()
    if B_input == '0':
        break
    else:
        B_input = B_input.split()
        b.append(list(map(int,B_input)))

for i in a_final:
    tem = []
    for j in b:
        tem.append(sum(list(map(lambda k:k[0] * k[1], zip(i,j)))))
    c.append(tem)

for i in c:
    for j in i:
        print(chr(j),end='')

