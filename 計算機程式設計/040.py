n = input().split()
time = int(input())
total = 0 #總值
for i in n:
    total += int(i)
ans = total / time #每組需得出的值
if (ans * 10) % 10 != 0:
    print("False")
else:
    for i in n:
        if int(i) > ans:
            print('False')
            time = -1
    if time != -1:
        print('True')