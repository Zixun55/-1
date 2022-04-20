import math
try:
    while True:
        x = input()
        for i in x:
            a = ord(i)
            b = a-7
            c = chr(b)
            print(c, end = '')
except EOFError:
    pass