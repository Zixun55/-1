x = int(input())
y = int(input())

if x == 1:
    for i in range(y+1):
        n=''
        for j in range(1,i):
            n=n+str(j)
        for j in range(i,0,-1):
            n=n+str(j)
        print(n)

elif x == 2:
    for i in range(1,y+1):
        m=''
        print('_'*(y-i),end='')
        for j in range(1,i):
            m=m+str(j)
        for j in range(i,0,-1):
            m=m+str(j)
        print(m,end='')
        print('_'*(y-i))

elif x == 3:
    for i in range(y,0,-1):
        o=''
        print('_'*(y-i),end='')
        for j in range(1,i):
            o=o+str(j)
        for j in range(i,0,-1):
            o=o+str(j)
        print(o,end='')
        print('_'*(y-i))