inarr = input().split(' ')
x1 = int(inarr[0])
y1 = int(inarr[1])
x2 = int(inarr[2])
y2 = int(inarr[3])
x3 = int(inarr[4])
y3 = int(inarr[5])
for i in range(1,10*10*10*10*10*10*10*10,1):
    if i % x1 == y1 and i % x2 == y2 and i % x3 == y3:
        print(i)
        break