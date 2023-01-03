def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    answer = [cnt+lottos.count(0), cnt]
    for i in range(len(answer)):
        if answer[i] >= 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    return answer