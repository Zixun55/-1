try:
    while True:
        inarr = input().split(' ')
        ia = int(inarr[0])
        ib = int(inarr[1])
        print(ia+ib)
except EOFError:
    pass 