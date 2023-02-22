def solution(s, skip, index):
    answer = ''
    for alp in s:
        loop = index
        while loop:
            alp = chr(ord(alp)+1)
            if ord(alp) > ord("z"):
                alp = "a"
            if alp in skip:
                loop += 1
            loop -= 1
        answer += alp
    return answer