n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
del p[0]
del q[0]
lst = list(set(p+q))
if len(lst)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

