def solution(s):
    answer = True
    for i in s:
        answer = False
        if len(s)==4 or len(s)==6:
            if s.isdigit():
                answer = True
    return answer

-------------------------

def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isalpha():
                break
        else:
            answer = True        
    return answer