#轉換數字
def convert(c):
    if c == 'A': 
        return 14
    elif c == 'J': 
        return 11
    elif c == 'Q': 
        return 12
    elif c == 'K': 
        return 13
    else: 
        return int(c)

def countcard(n, c, x):
    for j in n:
        if n.count(j) == x: 
            return True
    return False

def f1(n, c): 
    return countcard(n, c, 2)

def f2(n, c):
    n.sort()
    re = 0
    a = 0
    for i in n:
        if n.count(i) == 2 and i != re:
            re = i
            a += 1
    if a == 2: 
        return True
    else: 
        return False

def f3(n, c): 
    return countcard(n, c, 3)

def f4(n, c):
    result1 = True
    result2 = True
    n.sort()
    for i in range(1, len(n)):
        if n[i] - n[i - 1] != 1: 
            result1 = False
    for i in range(len(n)):
        if n[i] < 6: 
            n[i] += 13
    n.sort()
    for i in range(1, len(n)):
        if n[i] - n[i - 1] != 1: 
            result2 = False
    return result1 or result2

def f5(n, c):
    if c.count(c[0]) == 5: 
        return True
    return False

def f6(n, c): 
    return countcard(n, c, 3) and countcard(n, c, 2)

def f7(n, c): 
    return countcard(n, c, 4)

def f8(n, c): 
    return f5(n, c) and f4(n, c)

farr = [f1, f2, f3, f4, f5, f6, f7, f8]

data = input().split(' ')
n = [convert(str(i[:-1])) for i in data]
c = [i[-1] for i in data]

#無牌型
a = 0
for k in range(2):
    pass

for i in range(8):
    if farr[i](n, c): a = i + 1

#輸出牌型
print(a)