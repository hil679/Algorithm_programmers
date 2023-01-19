def solution(num_list):
    answer = []
    #num_list.reverse() => return 값이 없음
    #sort(return 없음), sorted(return있음)도 마찬가지
    answer = list(reversed(num_list))
    return answer