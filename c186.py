try:
    while True:
        inarr = input().split(' ')
        a = len(inarr)
        for i in range(a):
            print(inarr[i])
except EOFError:
    pass