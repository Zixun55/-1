import json
n = int(input())
out = {}
if n == 0:
    print('menu = {')
    print('}')
else:
    for i in range(n):
        menu = input().split()
        out.setdefault(menu[0],{'hours':menu[1]+'-'+menu[2]})
        string = ''
        menus = []
        for j in range(3,len(menu)):
            if menu[j].isalpha():
                if string == '':
                    string = menu[j]
                else:
                    string = string +' '+ menu[j]
            elif menu[j].isdigit():
                menus.append(string)
                menus.append(menu[j])
                string = ''
        for j in range(len(menus)):
            if menus[j].isdigit():
                menus[j] = '$'+menus[j]
        item = {}
        for j in range(0,len(menus),2):
            item.setdefault(menus[j],menus[j+1])
        
        out[menu[0]].setdefault('items',item)
    out = json.dumps(out,indent=2)
    out = out.replace('"',"'")
    print('menu = '+out)