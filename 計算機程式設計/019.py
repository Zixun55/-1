n = int(input())
for i in range(n,0,-1):
        o = ''
        for j in range(i,0,-1):
                o=o+str(j)
        print('#'*(n*2-i),end='')
        print(o)