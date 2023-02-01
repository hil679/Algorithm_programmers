from collections import deque
def solution(A, B):
    c_A , c_B= deque(A), deque(B)
    n = 0
    while(n<len(c_A)):
        if  c_A == c_B:
            return n
        c_A.rotate(1)
        n += 1
    return -1
print(solution("hello", "ohell"))

#solution=lambda a,b:(b*2).find(a)