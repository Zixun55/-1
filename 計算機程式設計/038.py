inp = input().split(' ')
n = int(inp[1])
n = bin(n-1)[2:]
c = n.count('1')
if c % 2 == 1:
    print(1)
elif c % 2 == 0:
    print(0)