n = int(input())
a = list(map(int, input().split()))
res = []
count=0
if int(a[0])>=n:
    print (n-1)
    for i in range(1,n):
        print(1,i+1)
else:
    print(sum(x for x in a[1:]))
    while a[0]>0:
        print(0,a.index(max(a)))
        a[0]-=1
        maximum = max(a)
        a.remove(a.index(max(a)))
        
              
        
        
        
    
