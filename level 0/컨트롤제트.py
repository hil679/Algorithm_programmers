#Z먼저 시작하는 거 고려해보기
def solution(s):
    stack = []
    s = list(s.split(" "))
    for i in s:
        if(i != "Z"):
            stack.append(int(float(i)))
        else:
            stack.pop()
    return sum(stack)