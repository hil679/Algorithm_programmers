import sys

def mySolution():
    n = int(sys.stdin.readline())
    direction = list(map(str, sys.stdin.readline().split()))
    first = [1, 1]

    for d in direction:
        if(d == "L") and (first[1] -1 > 0):
            first[1] -= 1
        elif d == "R" and first[1] + 1 <= n:
            first[1] += 1
        elif(d == "U") and (first[0] -1 > 0):
            first[0] -= 1
        elif (d == "D") and(first[0] + 1 <= n):
            first[0] += 1
    print(first[0], first[1])

mySolution()


def otherSol():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    moveTypes = [ "L", "R", "U", "D"]
    nx, ny = 0, 0
    for plan in plans:
        for i in range(len(moveTypes)):
            if(plan == moveTypes[i]):
                nx = x + dx[i]
                ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            x = nx
            y = ny

    print(x, y)
    
otherSol()