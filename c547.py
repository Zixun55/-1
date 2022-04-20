mod = 1000000007
def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (f(n-1) % mod + f(n-2) % mod) % mod
try:
    while True:
        a = int(input())
        if a == 0:
            print(0)
        else:
            print(f(a))
except EOFError:
    pass