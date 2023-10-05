def solution(l, r):
    answer = []
    for i in range(l, r+1):
        for j in list(str(i)):
            if j != '5' and j != '0':
                break
        else:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer