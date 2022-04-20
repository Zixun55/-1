inarr = input().split(' ')
a = int(inarr[0])
b = int(inarr[1])
c = int(inarr[2])
d = int(inarr[3])
s = (c-a)*60+(d-b)
f = s%60
e = (s-f)//60
print(e,f)