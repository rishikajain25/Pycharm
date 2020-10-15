def average(array):
    sum1 = sum(set(arr))
    len1 = len(set(arr))
    avg1 = sum1 / len1
    return avg1

n=int(input())
arr=list(map(int,input().split()))
result = average(arr)
print(result)
