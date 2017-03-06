



dif = 0.000001
t = 0

n = int(input())
a = [int (x) for x in  input().split()]
b = [int (x) for x in  input().split()]
min1 = min(a)
max1 = max(a)
while max1 - min1 > dif:  
    t = 0
    xt = (max1 + min1)/2   
    for i in range(n):
        nt = abs(a[i] - xt) / b[i]
        if t < nt:
            t = nt
            xf = a[i]
    
    if xf >= xt:
            min1 = xt
    else:
         max1 = xt
    
print(t)
