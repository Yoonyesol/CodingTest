def solution(s):
    return s[(len(s)-1) // 2] if len(s) % 2 != 0 else s[(len(s)-1) // 2 : (len(s)-1) // 2 + 2]


-----------


def solution(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1: len(s) // 2 + 1]