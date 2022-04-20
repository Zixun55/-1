inp = input()
time = 0
i_max = 0
string = ''

for i in range(len(inp)):
    if i == 0:
        string += inp[0]
        time += 1
        if time > i_max:
            i_max = time
    else:
        if string.count(inp[i]) == 0:
            string += inp[i]
            time = len(string)
            if time > i_max:
                i_max = time
        else:
            time = 0
            pos = string.find(inp[i])
            string = string[pos+1::] + inp[i]
            time += 1

print(i_max)