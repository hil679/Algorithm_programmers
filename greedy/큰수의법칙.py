import sys;

n,m,k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

def my_solution(n,m,k, arr):
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
my_solution(n,m,k,arr)



def other_sol1(n,m,k,arr):
    arr.sort()
    first = arr[n-1]
    second = arr[n-2]

    result = 0

    while True:
        for i in range(k): # 먼저 k번 더하고
            if m == 0: #k번 더하는 과정에서 m번이 끝나면 종료
                break
            result += first
            m -= 1
        if m == 0: #연속으로 k번 더한 후 두 번째로 큰 값 더하려는데 0이 되면 종료 
            break
        result += second #아니면 second 더함
        m -= 1 
    print(result)
other_sol1(n,m,k,arr)

def other_sol2(n,m,k,arr):
    arr.sort()
    first = arr[n-1]
    second = arr[n-2]

    count = int(m/(k+1) * k)
    count += m % (k + 1)

    result = 0
    result += count * first
    result += (m - count) * second

    print(result)
other_sol2(n,m,k,arr)   