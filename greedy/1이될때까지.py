n ,k = map(int, input().split())
result = 0

def mySolution(n,k,result):
    while True:
        if(n % k == 0): #최대한 많이 나누기
            n //= k
        else:
            n -= 1
        result += 1

        if n == 1:
            break
    print(result)
mySolution(n,k,result)

def otherSolution(n,k,result): # N이 매우 큰 경우 효율적인 sol
    #n = 19, k = 5 가정
    #1 단계 이후: target, n = 15, result = 19 -15 = 4 => if (n >= k): result = 5, n = 3
    #2 단계 : target, n = 0, result += 3 - 0 -> result = 8, if (n < k): break 더 이상 나누지 않음
    #      : result += (n - 1)로 간다. => result += -1 => result = 7
    while True:
        target = (n // k) * k
        result += n - target
        n = target

        if n < k:
            break
        result += 1
        n //= k
    result += (n - 1) # 1이 될 때 까지여서, 나눈 나머지 만큼 1씩 빼줘야하는데 n만큼 빼면 0이 됨, 따라서 n-1번 빼줌
    print(result)
otherSolution(n,k,result)
