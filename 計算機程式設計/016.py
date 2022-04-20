n = input()
cm = int(input())
k = int(input())
m = cm/100
b = k/(m*m)
if b>24:
    print('Hi',n+', Your BMI: '+"%f"%b+' too HIGH.')
elif b<18.5:
    print('Hi',n+', Your BMI: '+"%f"%b+' too LOW.')
else:
    print('Hi '+n+', Your BMI: '+"%f"%b+ '.')