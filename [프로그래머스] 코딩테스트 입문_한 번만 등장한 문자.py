def solution(s):
    for i in s:
        if s.count(i) >= 2:
            s = s.replace(i, "")
    return "".join(sorted(s))

--------------------------------------

def solution(s):
    return "".join(sorted([i for i in s if s.count(i) == 1]))