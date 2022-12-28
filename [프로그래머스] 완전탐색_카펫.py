def solution(brown, yellow):
    answer = []
    for i in range(3, int((brown + yellow)**0.5)+1):
        if (brown + yellow) % i == 0 and (i-2) * (((brown+yellow) // i) - 2) == yellow:
                answer = [(brown+yellow) // i, i]
                return answer