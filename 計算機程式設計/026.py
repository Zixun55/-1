n = int(input())
a = []
b = []

for i in range(n):
    line = input().split(' ')
    a += [int(line[0]),int(line[1])]
    b += [a]
    a = []

b.sort()
length = int(b[0][1]) - int(b[0][0])
for i in range(1,n):
    if int(b[i][0]) > int(b[i-1][1]):
        length = length + (int(b[i][1]) - int(b[i][0]))
    elif int(b[i][0]) == int(b[i-1][1]):
        length = length + (int(b[i][1]) - int(b[i][0])) 
    elif (int(b[i][0]) < int(b[i-1][1])) and (int(b[i][1]) > int(b[i-1][1])):
        length = length + (int(b[i][1]) - int(b[i][0])) - (int(b[i-1][1]) - int(b[i][0]))
    elif (int(b[i][1]) < int(b[i-1][1])) and (int(b[i][0]) > int(b[i-1][0])):
        length = length
    
print(length)