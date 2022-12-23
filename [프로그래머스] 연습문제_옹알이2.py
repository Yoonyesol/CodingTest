def solution(babbling):
    answer = 0
    bal = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in bal:
            if j + j in i:  #동일한 발음 연속 발음 불가
                break
            else:    #bal에 해당하는 단어가 i에 들어있다면 공백처리
                i = i.replace(j, " ")
        if i.strip() == '':   #공백일 때
            answer += 1
    return answer