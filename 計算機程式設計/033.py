try:
    while True:
        n = input().split(' ')
        n = list(map(int,n))
        n.sort()
        if n[0] == -1:
            break
        ans = 0
        for i in range(1,n[2] + 1):
            if n[0] % i == 0 and n[1] % i == 0 and n[2] % i == 0:
                ans = i
        print(ans)
except EOFError:
    pass