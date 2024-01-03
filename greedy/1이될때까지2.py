import sys

def sol1():
    n, k = map(int, sys.stdin.readline().split())
    divide = 0
    rest = n % k

    n -= rest
    while(n > 1):
        n //= k
        divide += 1

    print(rest + divide)
sol1()