def solution(numbers, k):
    answer = 0
    cnt = 0
    for i in range(k):
        answer = numbers[cnt % len(numbers)] 
        cnt += 2
    return answer