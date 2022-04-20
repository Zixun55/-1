code = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
inp = input().split()
inp_split = []
for i in range(len(inp)):
    inp_split.append([])
    for j in range(len(inp[i])):
        inp_split[i].append(inp[i][j])
ans = []

for i in range(len(inp)):
    string = ''
    for j in range(len(inp[i])):
        string += code[inp_split[i][j]]
    if ans.count(string) == 0:
        ans.append(string)
print(len(ans))