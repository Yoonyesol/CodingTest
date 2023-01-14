def solution(i, j, k):
    answer = 0
    for m in range(i, j+1):
        for n in range(len(str(m))):
            if str(k) == (str(m))[n]:
                answer += 1
    return answer