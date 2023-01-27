def solution1(numbers):
    answer = ''
    num = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six": '6', "seven":'7', "eight":'8', "nine":'9' }
    a = ''
    for i in numbers:
        a += i
        if(a in num.keys()):
            answer += num[a]
            a = ''
        
    return int(answer)


#other
def solution2(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

