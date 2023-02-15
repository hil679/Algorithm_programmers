import sys
n = int(input())
c = 100
s = 100
for i in range(n):
    c_dice, s_dice = list(map(int, input().split()))
    if s_dice > c_dice:
        c -= s_dice  
    elif s_dice < c_dice: 
        s -= c_dice
print(c, s)