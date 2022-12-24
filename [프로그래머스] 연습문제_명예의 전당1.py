def solution(k, score):
    arr = []
    answer = []
    for i in score:
        arr.append(i)   #원소 하나씩 추가
        arr.sort(reverse = True)    #내림차순 정렬
        answer.append(min(arr[:k])) #상위 k개 pick한 뒤 최솟값을 answer에 추가
    return answer