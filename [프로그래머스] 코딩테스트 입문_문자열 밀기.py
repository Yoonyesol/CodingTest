from collections import deque
def solution(A, B):
    answer = 0
    if A == B:
        return answer
    A = deque(A)
    for i in range(len(A)):
        A.appendleft(A.pop())
        answer += 1
        if ''.join(A) == B:
            break
    if answer == len(A):
        answer = -1
    return answer