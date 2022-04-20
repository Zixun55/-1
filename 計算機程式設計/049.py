inp = input()
string = ''
for i in range(len(inp)):
    if inp[i].isupper():
        string += inp[i].lower()
    elif inp[i].islower():
        string += inp[i].upper()
n = int(input())

ans = []
for i in range(0,len(string),n):
    get  = string[i:i+n:]
    ans.append(get[::-1])
ans.reverse()
for i in range(len(ans)):
    ans[i] = ans[i][::-1]
    if i == len(ans)-1:
        print(ans[i])
    else:
        print(ans[i]+'/',end='')