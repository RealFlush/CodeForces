
n = int(input())
a = list(map(int, input().split()))

def result():
    cnt=0
    maximum=0
    z=set()
    for i in a:
        
        if i in z:
            z.remove(i)
        else:
            z.add(i)
        maximum = max(maximum,len(z))
    return maximum
print (result())


