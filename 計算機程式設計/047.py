string = input()
repeat = []#放過的
for i in range(len(string)):
    if string[i].isdigit():
        print(string[i],end='')
    elif string[i].isalpha():
        if repeat.count(string[i]) == 0 and string.count(string[i]) > 0 and string.count(string[i]) < 10:
            print(string.count(string[i]),end='')
            repeat.append(string[i])
    
