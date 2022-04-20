def jqk(x):
    if x == 'A':
        x = 1
    if x == 'J' or x == 'Q' or x == 'K':
        x = 0.5
    a1 = float(x)

    if a1 >10.5:
        a1 = 0.0
    return a1
a = input()
b = input()
a1 = jqk(a)
b1 = jqk(b)
nn = 0
while True:
    if a1 != 0.0:
        YN = input()
        if YN == 'Y':
            a = input()
            a2 = jqk(a)
            a1 = (a1)+(a2)
            a1 = jqk(a1)
            a2 = 0
        elif YN == 'N':
            break
        if nn == 0:
            if b1<a1 and b1 != 0.0:
                b = input()
                b2 = jqk(b)
                b1 = (b1)+(b2)
                b1 = jqk(b1)
                b2 = 0
            elif b1<=8 and b1 != 0.0:
                b = input()
                b2 = jqk(b)
                b1 = (b1)+(b2)
                b1 = jqk(b1)
                b2 = 0
            elif  b1 == 0.0:
                nn = nn + 1
                continue
                
            elif b1>a1:
                nn = nn + 1
                continue
                
            elif b1>8:
                nn = nn + 1
                continue
               
        continue
    elif a1 == 0.0:
        break
while nn == 0:
    if b1<a1 and b1 != 0.0:
        b = input()
        b2 = jqk(b)
        b1 = (b1)+(b2)
        b1 = jqk(b1)
        b2 = 0
    elif b1<=8 and b1 != 0.0:
        b = input()
        b2 = jqk(b)
        b1 = (b1)+(b2)
        b1 = jqk(b1)
        b2 = 0
    elif  b1 == 0.0:
        break
    elif b1>a1:
        break
    elif b1>8:
        break

print(a1,'vs.',b1)
if a1>b1:
    print('player wins')
elif a1<b1:
    print('computer wins')
elif a1 == b1:
    print("It's a tie")