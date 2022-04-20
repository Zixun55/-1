def g(a,b,c):
    if a == 'A':
        a = 1
    if a == 'J' or a == 'Q' or a == 'K':
        a = 0.5
    if b == 'A':
        b = 1
    if b == 'J' or b == 'Q' or b == 'K':
        b = 0.5
    if c == 'A':
        c = 1
    if c == 'J' or c == 'Q' or c == 'K':
        c = 0.5
    a1 = float(a)
    b1 = float(b)
    c1 = float(c)
    ans = a1+b1+c1
    if ans >10.5:
        ans = 0
    return ans
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
AA = g(a,b,c)
BB = g(d,e,f)
print('%.0f'%AA)
print('%.0f'%BB)
if AA>BB:
    print('A Win')
elif AA<BB:
    print('B Win')
else:
    print('Tie')