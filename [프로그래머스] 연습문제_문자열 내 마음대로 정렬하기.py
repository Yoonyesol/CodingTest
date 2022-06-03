def solution(strings, n):
    answer = []
    answer2 = []
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    for j in answer:
        answer2.append(j[1:])
    return answer2