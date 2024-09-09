N, K = map(int, input().split())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
B.sort(reverse=True)
A.sort(reverse=True)
print(A)
print(B)
ans = 0
a = 0
b = 0
change = 0
for i in range(N):
    if A[a] < B[b] and change < K: 
        ans += B[b]
        b += 1
        change += 1
    else:
        ans += A[a]
        a += 1
print(ans)