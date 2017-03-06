
n,k = list(map(int, input().split()))
cnt = 0
n_n = str(n)[::-1]
if n<10**k:
    print(len(n_n)-1)
else:
    for i in  n_n:
        if i=='0':
            cnt+=1


    print(cnt)
