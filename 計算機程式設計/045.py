reward1 = input()#特別獎號碼
reward2 = input()#特獎號碼
reward3 = input().split()#頭獎號碼(3組)
reward4 = input().split()#增開六獎號碼(3組)
n = int(input())
total = 0
for i in range(n):
    number = input()
    if number == reward1:
        total += 10000000
    elif number == reward2:
        total += 2000000
    elif number == reward3[0] or number == reward3[1] or number == reward3[2]:
        total += 200000
    elif number[-1:-8:-1] == reward3[0][-1:-8:-1] or number[-1:-8:-1] == reward3[1][-1:-8:-1] or number[-1:-8:-1] == reward3[2][-1:-8:-1]:
        total += 40000
    elif number[-1:-7:-1] == reward3[0][-1:-7:-1] or number[-1:-7:-1] == reward3[1][-1:-7:-1] or number[-1:-7:-1] == reward3[2][-1:-7:-1]:
        total += 10000
    elif number[-1:-6:-1] == reward3[0][-1:-6:-1] or number[-1:-6:-1] == reward3[1][-1:-6:-1] or number[-1:-6:-1] == reward3[2][-1:-6:-1]:
        total += 4000
    elif number[-1:-5:-1] == reward3[0][-1:-5:-1] or number[-1:-5:-1] == reward3[1][-1:-5:-1] or number[-1:-5:-1] == reward3[2][-1:-5:-1]:
        total += 1000
    elif number[-1:-8:-1] == reward3[0][-1:-4:-1] or number[-1:-4:-1] == reward3[1][-1:-4:-1] or number[-1:-4:-1] == reward3[2][-1:-4:-1]:
        total += 200
    elif number[5::] == reward4[0] or number[5::] == reward4[1] or number[5::] == reward4[2]:
        total += 200
print(total)