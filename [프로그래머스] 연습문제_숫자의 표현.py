def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1): #i부터 연속된 값의 합을 구함
            sum += j
            if sum > n: #합계가 input보다 큰 경우
                break
            elif sum == n: #합계가 input과 같은 경우
                answer += 1
                break
    return answer