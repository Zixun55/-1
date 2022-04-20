a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x = a*0.08+b*0.1393+c*0.1349+d*1.1287+e*1.4803
y = a*0.07+b*0.1304+c*0.1217+d*1.1127+e*1.2458
z = a*0.06+b*0.1087+c*0.1018+d*0.9572+e*1.1243
if x < 183:
    x = x+183
if y < 383:
    y = y+383
if z < 983:
    z = z+983
if x<y and x<z:
    print('Type 183')
elif y<x and y<z:
    print('Type 383')
elif z<y and z<x:
    print('Type 983')