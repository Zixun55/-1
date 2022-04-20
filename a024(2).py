def f(a,b):
    if b == 0:
        return a
    else:
        return f(b,a%b)
try:
    while True:
        inarr = input().split(' ')
        x = int(inarr[0])
        y = int(inarr[1])
        print(f(x,y))
except EOFError:
    pass