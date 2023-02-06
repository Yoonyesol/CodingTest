def solution(before, after):
    answer = 1
    for i in before:
        if i in after:
            after = after.replace(i, "", 1)
        else:
            answer = 0
            break
    return answer

-------------------------------

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0