import math
inarr = input().split(' ')
a = float(inarr[0])
b = float(inarr[1])
c = float(inarr[2])
if (a+b)>c and (b+c)>a and (a+c)>b:
    p = (a+b+c)/2
    A = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('%.1f'%A)
else:
    print('不為三角形')