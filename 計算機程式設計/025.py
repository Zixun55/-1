inp = True
while inp:
    inarr = input().split(' ')
    m = float(inarr[0])
    if m == -1:
        inp = False
        break
    elif m<0.5 or m>2.50:
        print('Input Error 0.5~2.50')
        continue
    kg = float(inarr[1])
    if kg == -1:
        inp = False
        break
    elif kg<20 or kg>300:
        print("Input Error 20~300")
        continue
    BMI = kg/(m*m)
    if BMI>24:
        print("BMI too hight")
    elif BMI<18.5:
        print("BMI too low")
    else:
        print('%.2f'%BMI)