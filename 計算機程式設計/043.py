BC = []
NC = []
CT = []
NS = []
NM = []
HL = []
NL = []
n_school = int(input())#學校數量
name_school = []#學校名字
for i in range(n_school):
    school = input().split()#學校名字及屬性
    name_school.append(school[0])
    for j in range(1,len(school)):
        if school[j] == 'BC':BC.append(school[0])
        elif school[j] == 'NC':NC.append(school[0])
        elif school[j] == 'CT':CT.append(school[0])
        elif school[j] == 'NS':NS.append(school[0])
        elif school[j] == 'NM':NM.append(school[0])
        elif school[j] == 'HL':HL.append(school[0])
        elif school[j] == 'NL':NL.append(school[0])

n_search = int(input())#搜尋數量
ans = [[]for _ in range(n_search)]
for h in range(n_search):
    n_c = 0#條件數量
    search = input().split()
    c = [[] for _ in range(search.count('+') + 1)]#條件
    for j in range(len(search)):
        if search[j] == '+':
            n_c += 1
        else:
            c[n_c].append(search[j])

    for i in range(len(c)):
        for k in name_school:
            time = 0#符合幾項條件
            for j in range(len(c[i])):
                if c[i][j] == 'BC':
                    if BC.count(k) != 0:
                        time = time + 1
                if c[i][j] == 'NC':
                    if NC.count(k) != 0:
                        time = time + 1
                if c[i][j] == 'CT':
                    if CT.count(k) != 0:
                        time = time + 1
                if c[i][j] == 'NS':
                    if NS.count(k) != 0:
                        time = time + 1
                if c[i][j] == 'NM':
                    if NM.count(k) != 0:
                        time = time + 1
                if c[i][j] == 'HL':
                    if HL.count(k) != 0:
                        time = time + 1
                if c[i][j] == 'NL':
                    if NL.count(k) != 0:
                        time = time + 1
                if time == len(c[i]):
                    ans[h].append(k)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end=' ')
    print('')