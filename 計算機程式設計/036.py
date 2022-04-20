def f(n):
    if n == 1:
        return 2
    else:
        ans = n+f(n-1)
    return ans
n = int(input())
print(f(n))