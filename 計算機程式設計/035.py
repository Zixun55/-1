def perm(n,begin,end):
    if begin>=end:
        print(n,end='')
        print(',')
    else:
        i=begin
        
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
  
n = input().split()
n = list(map(int,n))
perm(n,0,len(n))

