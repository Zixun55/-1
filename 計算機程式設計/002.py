import math
a = int(input())
b = int(input())
c = int(input())
if (pow(b,2)-4*a*c) < 0:
    print("No real root")
else:
    x1 = (-b+math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
    x2 = (-b-math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
    print("%.1f" %x1)
    print("%.1f" %x2)