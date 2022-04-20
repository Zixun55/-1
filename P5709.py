inarr = input().split(' ')
m = int(inarr[0])
t = int(inarr[1])
s = int(inarr[2])
if t != 0:
    a = s//t
    if s%t == 0:
        b = m-a
        if b<=0:
            print(0)
        else:
            print(b)
    else:
        b = m-a-1
        if b<=0:
            print(0)
        else:
            print(b)
elif t == 0:
    print(0)