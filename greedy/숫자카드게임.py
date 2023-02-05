import sys
def mySolution(): 
    n, m = map(int, input().split()) #row, col
    card = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] #2차원 입력 받기

    minList = []
    prevMin = 0
    for i in card:
        prevMin = min(i)
        minList.append(prevMin)
    print(max(minList))
mySolution()#한번에 입력받고 구하기

def otherSol1(): #입력 한 줄씩 받으면서 구하기
    n,m = map(int, input().split())
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        minValue = min(data)
        result = max(result, minValue)
    print(result)
otherSol1()




