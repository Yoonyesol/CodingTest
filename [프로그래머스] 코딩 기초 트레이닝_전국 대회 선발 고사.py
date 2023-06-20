def solution(rank, attendance):
    dic = {idx:ranking for idx, ranking in enumerate(rank)} #인덱스번호:등수
    for i in range(len(attendance)):
        if attendance[i] == False:  #dic에서 참가하지 않은 학생의 명단 삭제
            del dic[i]
    dic = sorted(dic.items(), key = lambda x:x[1])  #참가한 학생의 명단만 가지고 value값(등수)로 오름차순 정렬
    return (10000*dic[0][0]) + (100*dic[1][0]) + dic[2][0]  #앞에서부터 1,2,3등이므로 적절하게 값을 가산해 답을 리턴

