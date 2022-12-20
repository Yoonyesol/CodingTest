def solution(k, m, score):
    answer = 0
    arr = []
    score.sort(reverse = True)
    for i in range(0, len(score), m):
        arr = score[i:i+m]
        if len(arr) == m:
            answer += min(arr) * m
    return answer