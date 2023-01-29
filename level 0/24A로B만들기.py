def solution(before, after):
    before, after = list(before),list(after)
    for b in before:
        if(b in after):
            after.remove(b)
    return 1 if after==[] else 0
print(solution("allpe", "apple"))