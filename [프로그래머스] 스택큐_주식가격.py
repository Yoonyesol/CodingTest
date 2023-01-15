from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        first = q.popleft()
        cnt = 0
        for i in q:
            cnt += 1
            if first > i:
                break
        answer.append(cnt)
    return answer