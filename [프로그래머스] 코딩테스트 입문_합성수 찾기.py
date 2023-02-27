def solution(n):
    answer = 0
    for i in range(4, n+1):
        j = 1
        cnt = 1
        while i >= j:
            if cnt == 3: 
                answer += 1
                break
            if i % j == 0:
                cnt += 1
            j += 1
    return answer