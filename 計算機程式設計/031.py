def check(x):
    for i in range(10):
        au[i] = True
    au[x] = False
    return au
n = input().split(' ')
n = list(map(int,n))
au = [True]*10  #放過就將此數之au轉成false
n_min = min(n)
c = [0]*10#0~9分別的個數
for i in n:
    c[i] = n.count(i)
total = 0
for i in c:                 #計算總數量
    total = total + i 
for i in range(len(c)):
    if c[i] == max(c) and c[i] > (total - max(c)):
        print(i,end='')
        c[i] = c[i] - 1
        au = check(i)
        total = total - 1
while total != 0:
    if c[n_min] != 0 and au[n_min] == True:
        print(n_min,end='')
        au = check(n_min)
        c[n_min] = c[n_min] - 1
        n_min = min(n)
        total = total - 1
    else:
        n_min = n_min+1