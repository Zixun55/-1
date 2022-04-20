s = input().split(' ')
p = input()
q = input()
s1 = s.copy()
s2 = s.copy()
s3 = s.copy()
for i in range(len(s)):
    if s1[i] == p:
        s1[i] = q
    if i != -1:
        print(s1[i]+' ',end = '')
    else:
        print(s1[i])
print('')
for i in range(len(s)):
    if s2[i] == p:
        s2[i] = q+' '+p
    if i != -1:
        print(s2[i]+' ',end = '')
    else:
        print(s1[i])
print('')
for i in range(len(s)):
    if s3[i] == p:
        s3[i] = ''
    if i != -1:
        if s3[i] != '':
            print(s3[i]+' ',end = '')
    else:
        print(s1[i])
#print(s.replace(' '+p,' '+q))
#print(s.replace(' '+p,' '+q+' '+p))
#print(s.replace(' '+p,''))