def solution(number, limit, power):
    answer = 0
    cnt = 0
    #약수 리스트
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i**0.5)+1):   #제곱근까지만 계산
            if i % j == 0:  #제곱근인 경우
                if i // j == j :
                    cnt += 1
                else:
                    cnt += 2
        if limit < cnt:
            answer += power
        else: answer += cnt
    return answer