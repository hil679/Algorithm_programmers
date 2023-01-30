#simulation
def solution(polynomial):
    answer = ''
    x = []
    num = 0
    for i in polynomial.split(" + "):
        if 'x' in i:    
            i = i.replace('x','')
            if(i==''):
                x.append(1)
            else:
                x.append(int(i))
        elif i.isdigit():
            num += int(i)
    if(len(x) != 0 and num != 0):
        answer = str(sum(x) if sum(x) != 1 else '') + 'x + ' + str(num)
    elif (len(x) == 0 and num != 0):
        answer = str(num)
    elif (len(x) != 0 and num == 0):
        answer = str(sum(x) if sum(x) != 1 else '') + 'x'
    else:
        answer = '0'
        
    return answer
print(solution("3x + 7 + x"))