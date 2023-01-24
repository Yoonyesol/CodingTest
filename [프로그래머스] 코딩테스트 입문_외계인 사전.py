def solution(spell, dic):
    for i in dic:
        answer = 0
        for j in spell:
            if j in i:
                answer += 1
                if answer == len(spell):
                    return 1
    return 2