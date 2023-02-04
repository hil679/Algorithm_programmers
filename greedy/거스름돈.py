def solution(money):
    coin = [500,100,50,10]
    num = 0
    for co in coin:
        num += money // co
        money -= co * (money // co) # money %= co
    return num

print(solution(1260))