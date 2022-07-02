import math
def solution(n):
    answer = []
    while True: #10진수 -> 3진수
        a = int(n/3)
        b = int(n%3)
        answer.insert(0,b)
        if a != 0:
            n = a
        else: break
    sum = 0
    #배열을 뒤집었다 가정하고 끝자리수부터 계산
    for i in range(len(answer)):    
        sum += answer[i] * math.pow(3,i)
    return sum