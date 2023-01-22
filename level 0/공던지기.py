def solution(numbers, k):
    n = 1 + (k-1) * 2
    return n % len(numbers)

#other answer

from collections import deque
def solution(numbers, k):
    array = deque(numbers)  #양방향 큐 => deque

    array.rotate(-(k-1)*2)  #-(k-1)*2만큼 회전 => 음수니까 왼쪽 회전

    return array[0]