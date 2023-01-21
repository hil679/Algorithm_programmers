import math

def solution(balls, share):
    
    answer = math.comb(balls, share) # 모든 조합 출력 대신, 조합의 개수만 반환 => itertools의 combinations와 차이임
    return answer