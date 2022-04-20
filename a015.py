try:
    while True:
        inarr = input().split(' ')
        r = int(inarr[0])
        c = int(inarr[1])
        a = []
        for i in range(r):
            a += [input().split(' ')]
        print(a)
        for i in range(c):
            for j in range(r):
                print(a[j][i],end = ' ')
            print('')
except EOFError:
    pass