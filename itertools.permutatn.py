from itertools import permutations
s,n=input().split()
x=permutations(sorted(s),int(n))
for i in x:
    print(''.join(i))
