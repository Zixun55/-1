import math
try:
    while True:
        inarr = input().split(' ') 
        a = int(inarr[0])
        b = int(inarr[1])
        c = int(inarr[2])
        if (pow(b,2)-4*a*c) < 0:
            print("No real root")
        else:
            x1 = (-b+math.sqrt(pow(b,2)-(4*a*c)))//(2*a)
            x2 = (-b-math.sqrt(pow(b,2)-(4*a*c)))//(2*a)
            x11 = str(x1).split('.')
            x22 = str(x2).split('.')
            if x1 == x2:
                print("Two same roots x="+x11[0])
            elif x1 != x2:
                print("Two different roots x1="+x11[0],", x2="+x22[0])
except EOFError:
    pass