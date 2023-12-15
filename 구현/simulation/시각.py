import sys
def sol():
    n = int(sys.stdin.readline())
    result = 0
    if(n < 3):
        result = 105 * 15 * (n + 1)
    elif(n<13):
        result = pow(60, 2) + 105 * 15 * n
    elif(n<23):
        result = pow(60, 2) * 2 + 105 * 15 * (n-1)
    else:
        result = pow(60, 2) * 3 + 105 * 15 * (n-2)
    print(result)
sol()