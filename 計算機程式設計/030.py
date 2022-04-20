string = input().split(' ')
n = [int(i) for i in input().split(' ')]
dic = {}

for i in range(len(n)):
    dic[n[i]] = string[i]

n.sort()

for i in n:
    print(dic[i], end='')