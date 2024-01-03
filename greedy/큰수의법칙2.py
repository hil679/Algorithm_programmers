import sys
arrNum, n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse = True)

def sol1(): #mine   
    sum = 0
    a = 0
    i = 0

    while i < n:
        j = 0
        while j < k and i < n:
            sum += arr[0]
            i += 1
            j += 1
        sum += arr[1]
        i += 1
        a += 1

    print(sum)

def sol2(): #책 참고 -> 규칙 찾아내기
    cnt = n / (k + 1)
    first = arr[0]
    second = arr[1]

    result = second * cnt
    result += first * (n - cnt) 

    print(result)


sol1() #mine
sol2() # 책 참고