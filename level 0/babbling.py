def solution(babbling):
    answer = 0
    case = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for i, c in enumerate(case,start=1):       
            bab = bab.replace(c, str(i))
        if(bab.isdigit()):
            answer += 1
    return answer