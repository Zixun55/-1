n = int(input())
in1 = input().split(' ')
in2 = input().split(' ')
in3 = input().split(' ')
n1 = int(in1[0])
n2 = int(in2[0])
n3 = int(in3[0])
m1 = int(in1[1])
m2 = int(in2[1])
m3 = int(in3[1])
if n%n1 == 0:
    a = (n/n1)*m1
elif n%n1 != 0:
    a = ((n//n1)+1)*m1

if n%n2 == 0:
    b = (n/n2)*m2
elif n%n2 != 0:
    b = ((n//n2)+1)*m2

if n%n3 == 0:
    c = (n/n3)*m3
elif n%n1 != 0:
    c = ((n//n3)+1)*m3
print('%.0f'%min(a,b,c))