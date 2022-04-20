n = int(input())
data = {}
for i in range(n):
    a = input().split()
    if len(a) == 2:
        data[int(a[0])] = a[1]
    if len(a) == 3:
        if data.get(a[0]) == None:
            data[int(a[0])] = {a[1]:a[2]}
        else:
            data[int(a[0])].update(a[1],a[2])
print(data)