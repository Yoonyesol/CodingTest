def solution(score):
    answer = []
    avg = []
    for i in score:
        avg.append(sum(i) / 2)
    for i in avg:
        answer.append(sorted(avg, reverse=True).index(i)+1)
    return answer