ox = [[],[],[]]
check = 0
for i in range(3):
    inp = input()
    ox[i].append(inp[0])
    ox[i].append(inp[1])
    ox[i].append(inp[2])
win = []
trans_ox = [[],[],[]]
for i in range(3):
    for j in range(3):
        trans_ox[i].append(ox[j][i])
for i in range(1,3):
    for j in range(len(ox)):
        if ox[j].count(str(i)) == 3:
            win.append(str(i))
        for k in range(len(ox[j])):
            if ox[0][k] == '1' and ox[1][k] == '1' and ox[2][k] == '1':
                win.append('1')
            if ox[0][k] == '2' and ox[1][k] == '2' and ox[2][k] == '2':
                win.append('2')
    if  (ox[0][0] == '2' and  ox[1][1] == '2' and  ox[2][2] == '2') or (ox[0][2] == '2' and  ox[1][1] == '2' and  ox[2][0] == '2'):
        win.append('2')
    if (ox[0][0] == '1' and  ox[1][1] == '1' and  ox[2][2] == '1') or (ox[0][2] == '1' and  ox[1][1] == '1' and  ox[2][0] == '1'):
            win.append('1')
    
#判斷是否能繼續
for i in range(3):
    if ox[i].count('1') == 2 and ox[i].count('0') == 1:
        pos = ox[i].index('0')
        if win.count('2') == 0:
            print(str(i)+str(pos))
            check = 1
        break
    elif trans_ox[i].count('1') == 2 and trans_ox[i].count('0') == 1:
        pos = trans_ox[i].index('0')
        if win.count('2') == 0:
            print(str(pos)+str(i))
            check = 1
        break
if (ox[0][0] == '0' and  ox[1][1] == '1' and  ox[2][2] == '1') or (ox[0][0] == '1' and  ox[1][1] == '0' and  ox[2][2] == '1') or (ox[0][0] == '1' and  ox[1][1] == '1' and  ox[2][2] == '0') or (ox[0][2] == '0' and  ox[1][1] == '1' and  ox[2][0] == '1') or (ox[0][2] == '1' and  ox[1][1] == '0' and  ox[2][0] == '1') or (ox[0][2] == '1' and  ox[1][1] == '1' and  ox[2][0] == '0'):
    if ox[0][0] == '0':print('00')
    elif ox[1][1] == '0':print('11')
    elif ox[2][2] == '0':print('22')
    elif ox[0][2] == '0':print('02')
    elif ox[2][0] == '0':print('20') 
    check = 1
        
if '1' in win and '2' in win:
    print('tie')
elif '1' in win and win.count('2') == 0:
    print('1 win')
elif '2' in win and win.count('1') == 0:
    print('2 win')
elif check == 0 and (win.count('1') == 0 and win.count('2') == 0):
    print('tie')