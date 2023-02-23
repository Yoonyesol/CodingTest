def solution(want, number, discount):
    answer = 0
    #원하는 품목이 모두 있는지 확인
    for i, j in zip(want, number):
        if j > discount.count(i):
            return 0
    for k in range(len(discount)-9):
        check = 0
        for i, j in zip(want, number):
            # k ~ k+10일 안에 원하는 품목이 존재하지 않는 경우, k+1 진행
            if j > discount[k:k+10].count(i):
                check = 0
                break
            check = 1
        answer += check
    return answer