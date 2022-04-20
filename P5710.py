x = int(input())
a = 0
b = 0
c = 0
d = 0
h = 0#是偶数
k = 0#大于 4 且不大于 12

if x%2 == 0:
    h = 1
if x>4 and x<=12:
    k = 1

if h == 1 and k == 1:
    a = 1
if h == 1 or k == 1 or (h == 1 and k == 1):
    b = 1
if (h == 1 and k == 0) or (h == 0 and k == 1):
    c = 1
if h == 0 and k == 0:
    d = 1
print(a,b,c,d)