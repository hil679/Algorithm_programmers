import math
def solution(a, b):
    gcd = math.gcd(a,b)
    b//=gcd
    an = []
    if(b==1):
        return 1
    while(b != 1):
        for i in range(2,b+1):
            if b % i == 0:
                an.append(i)
                b //= i
                break
    an = set(an)
    an.discard(2)#remove는 없는 거 지우려면 에러, discard는 에러 안 남
    an.discard(5)
    
    return 1 if len(an) == 0 else 2