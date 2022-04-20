def f(n):
    ans = 0
    if int(n[0]) == 0:
        return 0
    if int(n[0]) > 0:
        if len(n) == 1:
            ans += 1
        else:
            ans += f(n[1::])
    if int(n[:2:]) < 27:
        if len(n) == 2:
            ans += 1
        elif len(n) != 1:
            ans += f(n[2::])
    return ans
n = input() 
print(f(n))
