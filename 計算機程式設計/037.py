def f(n,l,a):
    if n == 0:
        print(0)
    elif n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    else:
        l.append(int(l[a-1]) + int(l[a-2]) + int(l[a-3]))
        if a == n:
            print(l[a])
        else:
            a += 1
            f(n,l,a)
l = [0,0,1,1]
n = int(input())
n = n-1
f(n,l,4)