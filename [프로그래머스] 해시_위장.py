def solution(clothes):
    dic = {}
    #의상 종류 갯수 구하기
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    #조합 구하기
    answer = 1
    for j in dic.keys():
        answer *= (dic[j]+1)
    return answer - 1   #아무것도 안 입은 경우 제외