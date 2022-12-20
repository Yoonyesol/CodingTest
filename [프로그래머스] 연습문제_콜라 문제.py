def solution(a, b, n):
    answer = 0
    while a <= n:
        answer += b
        n = n - a + b   #남은 병 n: a개 주고 b개 받아서 마심
    return answer