def c(n,count_n):
    if n == 1:
        return count_n
    elif n % 2 == 0:
        count_n += 1
        n = n / 2
        return c(n,count_n)
    elif n % 2 == 1:
        count_n += 1
        n = (n+1) / 2
        return c(n,count_n)
while True:
    n = input()
    n = int(n,2)
    if n == 0 or n == 1:
        print('0000')
    else:
        ans = bin(c(n,0))[2:]
        if len(ans) == 3:
            print('0'+ans)
        elif len(ans) == 2:
            print('00'+ans)
        elif len(ans) == 1:
            print('000'+ans)
        else:
            print(ans)
    con = input()
    if con == '0':
        continue
    elif con == '-1':
        break 