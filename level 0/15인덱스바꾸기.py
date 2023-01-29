#join, list(string)

def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s) #리스트 안에 문자 공백없이 합치기(잇기)