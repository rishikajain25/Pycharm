m=int(input())
rm=set(map(int,input().split()))
n=int(input())
rn=set(map(int,input().split()))
s=sorted(rm.symmetric_difference(rn))
for i in s:
    print(i)