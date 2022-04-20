try:
    while True:
        inarr = input().split(' ')
        a = int(inarr[0])
        b = inarr[1]
        c = int(inarr[2])
        if b == '+':
            print(a+c)
        elif b == '-':
            print(a-c)
        elif b == '*':
            print(a*c)
        elif b == '/':
            print(a//c)
except EOFError:
    pass