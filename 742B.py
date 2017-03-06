
n,x =  map(int, input().split())
a = list(map(int, input().split()))
c=[0] * (1 << 18)
summa=0
for i in a:
    summa+=c[x^i]
    c[i]+=1
#end = time.time()
print(summa)
#print(end-start)  
  


