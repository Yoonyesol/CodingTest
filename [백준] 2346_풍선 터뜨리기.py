import sys
from collections import deque
N = int(sys.stdin.readline())
poong = deque(enumerate(map(int, sys.stdin.readline().split())))
stack = []

while poong:
    idx, item = poong.popleft()
    stack.append(idx + 1)
    if item > 0:
        poong.rotate(-(item-1))
    elif item < 0:
        poong.rotate(-item)

print(' '.join(map(str, stack)))