def jqk(x):
    if x == 'A':
        x = 1
    if x == 'J' or x == 'Q' or x == 'K':
        x = 0.5
    a1 = float(x)
    return a1
def bang(a1):
    if a1 >21:
        a1 = 0.0
    return a1

first = input().split(' ')
x = first[0]
y = first[1]
x1 = jqk(x)
y1 = jqk(y)
xc = 1      #x的牌數
yc = 1      #y的牌數
x_au = 0    #x要牌的權限
y_au = 0    #y要牌的權限

while True:
    if x1 == 0.0 or y1 == 0.0 or xc == 5 or yc == 5 or (x_au != 0 and y_au != 0):
        break
    else:
        second = input().split(' ')
        if x_au == 0 and y_au == 0:
            if second[0] == '1':
                x2 = jqk(second[1])
                x1 = x1+x2
                x1 = bang(x1)
                xc = xc + 1

                if second[2] == '1':
                    y2 = jqk(second[3])
                    y1 = bang(y1 + y2)
                    yc = yc + 1
                elif second[2] == '0':
                    y_au = y_au + 1
            elif second[0] == '0':
                x_au = x_au + 1

                if second[1] == '1':
                    y2 = jqk(second[2])
                    y1 = bang(y1 + y2)
                    yc = yc + 1
                elif second[1] == '0':
                    y_au = 1

        elif x_au == 0 and y_au != 0:
            if second[0] == '1':
                x2 = jqk(second[1])
                x1 = x1 + x2
                x1 = bang(x1)
                xc = xc + 1
            elif second[0] == '0':
                x_au = x_au + 1

        elif y_au == 0 and x_au != 0:
            if second[1] == '1':
                y2 = jqk(second[2])
                y1 = bang(y1 + y2)
                yc = yc + 1
            elif second[1] == '0':
                y_au = y_au + 1
if x1 > y1:
    print('Player X is Winner')
elif x1 < y1:
    print('Player Y is Winner')

if x1 != 0.0:
    print('Player X $ ',end='')
    if (x1*10)%10 != 0:
        print(x1)
    else:
        print('%.0F'%x1)
elif x1 == 0.0:
    print('Player X $ Bang!')
if y1 != 0.0:
    print('Player Y $ ',end='')
    if (y1*10)%10 != 0:
        print(y1)
    else:
        print('%.0F'%y1)
elif y1 == 0.0:
    print('Player Y $ Bang!')