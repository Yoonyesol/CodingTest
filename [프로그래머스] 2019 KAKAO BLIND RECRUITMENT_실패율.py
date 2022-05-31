def solution(N, stages):
    d = dict()
    stg_pass = len(stages)
    for i in range(1, N+1):
        if stg_pass > 0: #스테이지에 도달한 사람이 한 명 이상이면
            not_pass = stages.count(i)   #해당 스테이지를 통과하지 못한 사람의 수 카운트
            d[i] = not_pass / stg_pass #stage 값: 실패율 - dict에 저장
            stg_pass -= not_pass    #스테이지 통과 못한 사람 수 빼기
        else:   #스테이지에 도달한 사람이 한 명도 없을 경우
            d[i] = 0
    return sorted(d, key=lambda x:d[x], reverse=True) #sorted key lambda 매개변수: 결과