import math

def solution(signals):
    answer = -1
    times = 1
    for g, y, r in signals: 
        times = math.lcm(times, g + y + r)
    
    for i in range(1, times + 1):
        is_all_yellow = True
        for j in signals: 
            moduler = (i-1) % sum(j) #j초에 몇 번째 인덱스를 가리키고 있는지
            if not j[0] <= moduler < j[0] + j[1]:
                is_all_yellow = False
                break
        if is_all_yellow:
            answer = i
            break
    return answer