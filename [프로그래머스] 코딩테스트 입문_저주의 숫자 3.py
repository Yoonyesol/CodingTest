def solution(n):
    answer = n - 1
    i = 0
    while n > 0:
        if i % 3 == 0 or '3' in str(i):
            n += 1
            answer += 1
        i += 1
        n -= 1
    return answer