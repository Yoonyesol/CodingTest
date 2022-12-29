def solution(progresses, speeds):
    answer = []
    stack = []
    for i, j in zip(progresses, speeds):
        if (100 - i) % j == 0:
            stack.append((100 - i) // j)
        else:
            stack.append((100 - i) // j + 1)
    idx = 0
    for i in range(len(stack)):
        if stack[idx] < stack[i]:
            answer.append(i - idx)  #앞 원소때문에 대기했던 원소들
            idx = i #다음 원소 가리키기
    answer.append(len(stack) - idx) #마지막 남은 원소값
    return answer