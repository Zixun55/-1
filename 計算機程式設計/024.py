try:
    while True:
        n = input()
        n_list = []
        n_list += n
        x = [[1 for _ in range(9)] for _ in range(len(n))]
        ans = 0
        down = 0
        mod = 1000000007
        start = 0

        for i in range(1,len(n)):
            for j in range(7,-1,-1):
                x[i][j] = x[i][j+1] + x[i-1][j]

        for i in range(len(n)-1):
            for j in range(9):
                ans = ((ans % mod) + (x[i][j] % mod)) % mod

        for i in range(int(n_list[0])-1):
            ans = ((ans % mod) + (x[len(n)-1][i] % mod)) % mod
            start = int(n_list[0])      

        for i in range(1,len(n_list)):
            if int(n_list[i]) > start:
                for j in range(start,int(n_list[i])):
                    ans = ((ans % mod) + (x[len(n_list)-(i+1)][j-1] % mod)) % mod
                    start = int(n_list[i])
            
            elif int(n_list[i]) < int(n_list[i-1]):
                down = 1

        if down == 0:
            ans = ans + 1
        if int(n_list[0]) == 1:
            ans = ans - 1
        print(ans)
except EOFError:
    pass