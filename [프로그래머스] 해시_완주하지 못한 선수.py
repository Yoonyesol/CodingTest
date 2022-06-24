def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]  #끝까지 비교하고도 리턴 값이 없을 때 마지막 원소 리턴