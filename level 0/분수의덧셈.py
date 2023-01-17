def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    denom = num1 * num2
    num = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    gcd_value = gcd(denom, num)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [num / gcd_value, denom / gcd_value]
    return answer