t = [[0 for _ in range(9)] for _ in range(5)]
con = []
id1 = input()
h1 = int(input())
for i in range(h1):
    c = int(input())
    a = c//10 - 1
    b = c%10 - 1
    t[a][b] = id1

id2 = input()
h2 = int(input())
for i in range(h2):
    c = int(input())
    a = c//10 - 1
    b = c%10 - 1
    if t[a][b] != 0:
        con += (t[a][b],id2,str(c))
    else:
        t[a][b] = id2

id3 = input()
h3 = int(input())
for i in range(h3):
    c = int(input())
    a = c//10 - 1
    b = c%10 - 1
    if t[a][b] != 0:
        con += (t[a][b],id3,str(c))
    else:
        t[a][b] = id3

for i in range(0,len(con),3):
    print(con[i],'and',con[i+1],'confict on',con[i+2])