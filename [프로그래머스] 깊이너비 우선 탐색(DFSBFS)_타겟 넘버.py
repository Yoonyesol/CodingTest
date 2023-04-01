def solution(numbers, target):
    answer = [0]
    for i in numbers:
        sub = []
        for j in answer:
            sub.append(j-i)
            sub.append(j+i)
        answer = sub
    return answer.count(target)