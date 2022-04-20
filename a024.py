try:
    while True:
        inarr = input().split(' ')
        x = int(inarr[0])
        y = int(inarr[1])
        def f(a,b):
            while a*b != 0:
                a = a%b
                if a == 0:
                    return b
                else:
                    b = b%a
                    if b == 0:
                        return a
        print(f(x,y))
except EOFError:
    pass