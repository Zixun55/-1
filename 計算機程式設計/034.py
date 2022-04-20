def f(n,l,a):
    if n < 0 or (n*10%10 != 0):
        print('Error')
    elif n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        l.append(2*int(l[a-1])+3*int(l[a-2]))
        if a == n:
            print(l[a])
        else:
            a += 1
            f(n,l,a)
l = [0,1]
n = float(input())
f(n,l,2)