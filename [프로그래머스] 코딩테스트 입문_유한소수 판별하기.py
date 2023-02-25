def solution(a, b):
    a_arr = []
    b_arr = []
    # 1. 기약분수로 나타내기-분자, 분모의 소인수 확인, 동일한 소인수는 제거
    i = 2
    while a >= i:
        if a % i == 0:
            a //= i
            a_arr.append(i)
        else: 
            i += 1
    i = 2
    while b >= i:
        if b % i == 0:
            b //= i
            if i in a_arr:
                a_arr.remove(i)
            else:
                b_arr.append(i)
        else: 
            i += 1
    #2. 분모의 소인수가 2와 5인지 확인하기
    for i in b_arr:
        if not i in [2, 5]:
            return 2
    return 1