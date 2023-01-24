def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n)) # key 값을 기준으로 정렬
    #(abs(x-n), x-n) => abs(x-n)로 먼저 정렬, 같을 경우 두 번째 인자인 x-n 기준으로 정렬
    answer = array[0]
    return answer
