try:
    while True:
        a = input()
        l = (int(len(a)))//2
        b = a[::-1]
        c = a[0:l:1]
        d = b[0:l:1]
        if c == d:
            print('yes')
        else:
            print('no')
except EOFError:
    pass