def solution(d, budget):
    d.sort()
    sum = 0
    cnt = 0
    for i in d:
        sum += i
        if budget < sum:
            break
        cnt += 1
    return cnt