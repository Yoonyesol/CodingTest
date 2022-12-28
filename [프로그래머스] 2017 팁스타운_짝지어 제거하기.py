def solution(s):
    answer = []
    for i in s:
        if len(answer) == 0:    #비어있을 때
            answer.append(i)
        elif answer[-1] == i:   #top과 s의 문자가 동일할 때
            answer.pop()    #answer top 제거
        else:
            answer.append(i)
    if len(answer) == 0:    #answer이 비어 있으면 정상 수행 완료
        return 1
    else:
        return 0