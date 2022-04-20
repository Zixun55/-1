try:
    while True:
        y = input()
        y1 = int(y)
        if (y1 % 4 == 0 and y1 %100 != 0) or y1 % 400 == 0:
            print('閏年')
        else:
            print('平年')
except EOFError:
    pass 