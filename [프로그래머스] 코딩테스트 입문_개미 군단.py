def solution(hp):
    answer = 0
    answer += hp // 5
    hp %= 5
    answer += hp // 3
    hp %= 3
    answer += hp
    return answer

------------------------------

def solution(hp):
    return hp // 5 + (hp % 5 // 3) + (hp % 5 % 3)   #장군 + 병정 + 일

------------------------------

def solution(hp):
    answer = 0
    for i in [5, 3, 1]:
        div, hp = divmod(hp, i)
        answer += div
    return answer