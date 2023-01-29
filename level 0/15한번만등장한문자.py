def solution(s):
    print([i for i in s if s.count(i) == 1]) # ['d']
    print(i for i in s if s.count(i) == 1) # <generator object solution.<locals>.<genexpr> at 0x103242820>
    print(type(sorted(i for i in s if s.count(i) == 1))) # type: <class 'list'>, 결과: ['d']
    return ''.join(sorted(i for i in s if s.count(i) == 1))
print(solution("abcabcabcd"))