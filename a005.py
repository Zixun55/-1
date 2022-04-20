try:
    while True:
        t = int(input())
        for i in range(t):
            inarr = input().split(' ')
            a = int(inarr[0])
            b = int(inarr[1])
            c = int(inarr[2])
            d = int(inarr[3])
        
            if (b-a) == (c-b) == (d-c):
                e = d+(d-c)
                print(a,b,c,d,e)
            elif (b/a) == (c/b) == (d/c):
                e = d*(d//c)
                print(a,b,c,d,e)
            else:
                print("不為等差或等比") 
except EOFError:
    pass 