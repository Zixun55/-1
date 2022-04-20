def f(n,A,B,C):#(幾號圈,目前,空,目的地)
    if n == 1:
        print(str(n) + '號圈:' + A + '+' + C)
    else:
        f(n-1,A,C,B)
        print(str(n) + '號圈:' + A + '+' + C)
        f(n-1,B,A,C)

n = int(input())
f(n,'A','B','C')