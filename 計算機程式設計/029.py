inarr = input().split(' ')
odd = []
even = []
out = []
for i in range(len(inarr)):    
    if int(inarr[i]) % 2 == 0:
        even += [inarr[i]]
    elif int(inarr[i]) % 2 != 0:
        odd += [inarr[i]]
odd = list(map(int,odd))
even = list(map(int,even))
odd = sorted(odd)
even = sorted(even)
even.reverse()
out = odd + even
print(out)