def number(x):
    if x == 'J':
        x = '11'
    elif x == 'Q':
        x = '12'
    elif x == 'K':
        x = '13'
    elif x == 'A':
        x = '1'
    elif x == 'T':
        x = '10'
    return x

pork_in = input().split(' ')
for i in range(5):
    if pork_in[i] == '10D':pork_in[i] = 'TD'
    elif pork_in[i] == '10S':pork_in[i] = 'TS'
    elif pork_in[i] == '10H':pork_in[i] = 'TH'
    elif pork_in[i] == '10C':pork_in[i] = 'TC'
    elif pork_in[i] == '11D':pork_in[i] = 'JD'
    elif pork_in[i] == '11S':pork_in[i] = 'JS'
    elif pork_in[i] == '11H':pork_in[i] = 'JH'
    elif pork_in[i] == '11C':pork_in[i] = 'JC'
    elif pork_in[i] == '12D':pork_in[i] = 'QD'
    elif pork_in[i] == '12S':pork_in[i] = 'QS'
    elif pork_in[i] == '12H':pork_in[i] = 'QH'
    elif pork_in[i] == '12C':pork_in[i] = 'QC'
    elif pork_in[i] == '13D':pork_in[i] = 'KD'
    elif pork_in[i] == '13S':pork_in[i] = 'KS'
    elif pork_in[i] == '13H':pork_in[i] = 'KH'
    elif pork_in[i] == '13C':pork_in[i] = 'KC'
    elif pork_in[i] == '14D':pork_in[i] = 'AD'
    elif pork_in[i] == '14S':pork_in[i] = 'AS'
    elif pork_in[i] == '14H':pork_in[i] = 'AH'
    elif pork_in[i] == '14C':pork_in[i] = 'AC'
suit = []    #花色
pork_n = []  #數字
for i in range(5):
    pork_n += pork_in[i][0]
    suit += pork_in[i][1]
for i in range(5):
    pork_n[i] = number(pork_n[i])
pork_n = list(map(int,pork_n))
pork_n.sort()
ans = 0
#1
pair = 0
for i in pork_n:
    if pork_n.count(i) == 2:
        pair += 1
        break
if pair == 1:
    ans = 1
#2
pair = 0
for i in pork_n:
    if pork_n.count(i) == 2:
        pair += 1
if pair == 4:
    ans = 2
#3
for i in pork_n:
    if pork_n.count(i) == 3:
        ans = 3
        break
#4
sf = True
for i in range(1,5):
    if pork_n[i] - pork_n[i-1] != 1 and pork_n[i] - pork_n[i-1] != 9:
        sf = False
        break
if sf == True:
    ans = 4
#5
if suit.count(suit[0]) == 5:
    ans = 5
#6
tk = 0
for i in pork_n:
    if pork_n.count(i) == 3:
        tk += 1
        break
for i in pork_n:
    if pork_n.count(i) == 2:
        tk += 1
        break
if tk == 2:
    ans = 6
#7
for i in pork_n:
    if pork_n.count(i) == 4:
        ans = 7
        break
#8
if suit.count(suit[0]) == 5: 
    sf = True
    for i in range(1,5):
        if pork_n[i] - pork_n[i-1] != 1 and pork_n[i] - pork_n[i-1] != 9:
            sf = False
            break
    if sf == True:
        ans = 8
print(ans)