a = int(input())
b = int(input())
c = b//2
d = ((b+1)//2)-1
x = []  #'*'
y = []  #'.'
for i in range(1,b,2):
    x += str(i)

for i in range(d,0,-1):
    y += str(i)

if a == 1:
    for i in range(1,c+2,1):
        print('*'*i)
    for i in range(c,0,-1):
        print('*'*i)

elif a == 2:
    for i in range(c,0,-1):
        print('.'*i,end='')
        print('*'*((c+1)-i))
    print('*'*(c+1))
    for i in range(1,c+1,1):
        print('.'*i,end='')
        print('*'*((c+1)-i))
        
elif a == 3:
    if b != 1:
        for i in range(len(x)):
            print('.'*int(y[i])+'*'*int(x[i]))
        print('*'*b)
        for i in range((len(x)-1),-1,-1):
            print('.'*int(y[i])+'*'*int(x[i]))
    else:
        print('*')