def getTotHomeTree(trees, mid):
    tot = 0
    for t in trees:
        if t > mid:
            tot += (t - mid)
    return tot

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
answer=0
while start < end:
    mid = (start + end) // 2
    homeTree = getTotHomeTree(trees, mid)
    if homeTree == m:
        answer = mid
        break
    elif homeTree > m:
        start = mid + 1
        if getTotHomeTree(trees, start) < m:
            answer = mid
            break
        else:
            answer = start
    else:
        end  = mid - 1
        answer = end
print(answer)