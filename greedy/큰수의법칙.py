import sys;

n,m,k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
check_k = 0
i = 0
maxnum = max(arr)
while i < m:
    answer += maxnum
    check_k += 1
    if(check_k == k):
        arr.remove(maxnum)
        answer += max(arr)
        i += 1
        arr.append(maxnum)
        check_k = 0
    i+=1
print(answer)

