def solution(n):
    answer = 1
    i = 1
    while i <= n:
        if (answer % 3 == 0) or('3' in str(answer)):
            i -= 1
        i+= 1
        answer += 1
    answer -= 1
    return answer

print(solution(15))

#other
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer