from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = Counter(a)
cb = Counter(b)

def solve():
    ans = 0
    balance = {}
    
    for mark in range(1, 6):
        c1 = ca.get(mark, 0)
        c2 = cb.get(mark, 0)
        s = c1 + c2
        if s % 2 != 0:
            return -1
        balance[mark] = c1 - (s / 2)
        
    if sum(balance.values()) != 0:
        return -1
        
    return int(sum(map(abs, balance.values())) / 2)
    
    
print (solve())
