x = int(input())
y = int(input())
z = int(input())
def f(n,a,b,c,d):
    if n>10 and n<16:
        nn = n*a*b
    elif n>15 and n<21:
        nn = n*a*c
    elif n>20:
        nn = n*a*d
    elif  n>-1 and n<11:
        nn = n*a
    return nn
xn = f(x,30,0.95,0.9,0.8)
yn = f(y,70,0.9,0.85,0.75)
zn = f(z,40,0.85,0.8,0.8)
if x+y+z >= 30:
    print('%.0f'%((xn+yn+zn)*0.87))
else:
    print('%.0f'%(xn+yn+zn))

