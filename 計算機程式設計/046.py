n = int(input())#N筆資訊
datas = []#資訊
datas_change = []#小寫資訊
for i in range(n):
    data = input()
    datas.append(data)
    datas_change.append(data.lower())
search = input().split()#關鍵字
search_change = []#小寫關鍵字
for i in range(len(search)):
    search_change.append(search[i].lower())
ans = [[]for _ in range(n)]
for i in range(len(datas)):
    time = 0#關鍵字次數
    check = datas[i].split()
    check_change = datas_change[i].split()
    for j in range(len(search)):
        time += datas_change[i].count(search_change[j])
        for k in range(len(check)):
            for l in range(len(check_change[k])):

                pos = check_change[k].find(search_change[j])#關鍵字位置
                if pos != -1:
                    check_change[k] = check_change[k][0:pos] + check_change[k][pos:pos+len(search_change[j]):].upper() + check_change[k][pos+len(search_change[j])::]
                    check[k] = check[k].replace(check[k][pos:pos+len(search_change[j]):],search[j].upper())
    datas[i] = ' '.join(check)
    ans[i].append(0-time)
    ans[i].append(i)
    ans[i].append(datas[i])
ans.sort()
for i in range(len(ans)):
    print(ans[i][2])