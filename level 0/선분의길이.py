def solution(lines):
    answer = [0 for _ in range(201)]
    for line in lines:
        for i in range(line[0], line[1]):
            answer[i+100] += 1
    return answer.count(2) + answer.count(3)
print(solution([[0, 1], [2, 5], [3, 9]]))