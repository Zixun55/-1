def check(chess,n,win):
    for i in range(10):
        for j in range(6):
            if chess[i][j] == str(n) and chess[i][j+1] == str(n) and chess[i][j+2] == str(n) and chess[i][j+3] == str(n) and chess[i][j+4] == str(n):#五子連續
                if chess[i][j+5] != str(n):#第六子不連續
                    win.append(n)
                else:
                    break     
    for i in range(6):
        for j in range(6):
            if chess[i][j] == str(n) and chess[i+1][j+1] == str(n) and chess[i+2][j+2] == str(n) and chess[i+3][j+3] == str(n) and chess[i+4][j+4] == str(n):#右斜五子連續 
                if i != 1 or j != 1 or i != 5 or j != 5:
                    if chess[i+5][j+5] != str(n) and chess[i-1][j-1] != str(n):#第六子不連續
                        win.append(n)
                elif i == 5 or j == 5:
                    if chess[i-1][j-1] != str(n):
                        win.append(n)
                else:
                    if chess[i+5][j+5] != str(n):#第六子不連續
                        win.append(n)
def reverse_check(chess,n,win):
    for i in range(6):
        for j in range(6):
            if chess[i][j] == str(n) and chess[i+1][j+1] == str(n) and chess[i+2][j+2] == str(n) and chess[i+3][j+3] == str(n) and chess[i+4][j+4] == str(n):#左斜五子連續 
                if i != 1 or j != 1:
                    if chess[i+5][j+5] != str(n) and chess[i-1][j-1] != str(n):#第六子不連續
                        win.append(n)
                elif i == 5 or j == 5:
                    if chess[i-1][j-1] != str(n):
                        win.append(n)
                else:
                    if chess[i+5][j+5] != str(n):#第六子不連續
                        win.append(n) 
def end(chess):
    for i in range(10):
        for j in range(6):
            if chess[i][j] == '0' and chess[i][j+1] == '1' and chess[i][j+2] == '1' and chess[i][j+3] == '1' and chess[i][j+4] == '1':
                print(str(i)+str(j))
                return
            elif chess[i][j] == '1' and chess[i][j+1] == '0' and chess[i][j+2] == '1' and chess[i][j+3] == '1' and chess[i][j+4] == '1':
                print(str(i)+str(j+1))
                return
            elif chess[i][j] == '1' and chess[i][j+1] == '1' and chess[i][j+2] == '0' and chess[i][j+3] == '1' and chess[i][j+4] == '1':
                print(str(i)+str(j+2))
                return
            elif chess[i][j] == '1' and chess[i][j+1] == '1' and chess[i][j+2] == '1' and chess[i][j+3] == '0' and chess[i][j+4] == '1':
                print(str(i)+str(j+3))
                return
            elif chess[i][j] == '1' and chess[i][j+1] == '1' and chess[i][j+2] == '1' and chess[i][j+3] == '1' and chess[i][j+4] == '0':
                print(str(i)+str(j+4))
                return    
def ends(chess):
    for i in range(6):
        for j in range(6):
            if chess[i][j] == '0' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '1':
                print(str(i)+str(j))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '0' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '1':
                print(str(i+1)+str(j+1))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '0' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '1':
                print(str(i+2)+str(j+2))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '0' and chess[i+4][j+4] == '1':
                print(str(i+3)+str(j+3))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '0':
                print(str(i+4)+str(j+4))
                return
def reverse_ends(chess):
    for i in range(6):
        for j in range(6):
            if chess[i][j] == '0' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '1':
                print(str(9-i)+str(j))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '0' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '1':
                print(str(8-i+1)+str(j+1))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '0' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '1':
                print(str(7-i)+str(j+2))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '0' and chess[i+4][j+4] == '1':
                print(str(6-i)+str(j+3))
                return
            elif chess[i][j] == '1' and chess[i+1][j+1] == '1' and chess[i+2][j+2] == '1' and chess[i+3][j+3] == '1' and chess[i+4][j+4] == '0':
                print(str(5-i)+str(j+4))
                return

chess = [[],[],[],[],[],[],[],[],[],[]]
win = []
reverse_chess = [[],[],[],[],[],[],[],[],[],[]]
for i in range(10):
    inp = input()
    for j in range(10):
        chess[i].append(inp[j])
        reverse_chess[i].append(inp[j])
reverse_chess.reverse()
trans_chess = [[],[],[],[],[],[],[],[],[],[]]
#翻轉矩陣
for i in range(10):
    for j in range(10):
        trans_chess[i].append(chess[j][i])

check(chess,1,win)
check(chess,2,win)
check(trans_chess,1,win)
check(trans_chess,2,win)
reverse_check(reverse_chess,1,win)
reverse_check(reverse_chess,2,win)

if 1 in win and 2 in win:
    print('tie')
elif 1 in win and win.count(2) == 0:
    print('1 win')
elif 2 in win and win.count(1) == 0:
    print('2 win')
elif win.count(2) == 0 and win.count(1) == 0:
    end(chess)
    end(trans_chess)
    ends(chess)
    reverse_ends(reverse_chess)