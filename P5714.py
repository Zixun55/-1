inarr = input().split(' ')
k = float(inarr[0])
m = float(inarr[1])
b = k/(m*m)
if b<18.5:
    print('Underweight')
elif b>24:
    print('%g'%b)
    print('Overweight')
else:
    print('Normal')