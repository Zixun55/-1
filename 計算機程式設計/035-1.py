from itertools import permutations
inp = input().split()
ans = list(permutations(inp,len(inp)))
ans = list(map(str,ans))
out = []
if len(ans) == 1:
    print('[0]')
else:
    for i in range(len(ans)):
        out.append(ans[i][1:-1])


    for i in range(len(out)):
        out[i] = out[i].replace("'","")
        

        print('['+out[i]+']',end='')
        if i != (len(out)-1):
            print(',')
