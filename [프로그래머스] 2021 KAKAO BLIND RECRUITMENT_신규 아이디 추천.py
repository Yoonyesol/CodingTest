def solution(new_id):
    answer = ''
    new_id = new_id.lower()  #1단계
    for two in new_id:  #2단계
        if two.isdecimal() or two.isalpha() or two in ['-', '_', '.']:
            answer += two
    while '..' in answer:   #3단계
        answer = answer.replace("..", ".")
    if answer[0] == ".":    #4단계
        if len(answer) >= 2:
            answer = answer[1:]
        else: 
            answer = "."
    if answer[-1] == ".":
        answer = answer[:-1]
    if answer == "":    #5단계
        answer += "a"
    if len(answer) >= 16:   #6단계
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    while len(answer) <= 2:   #7단계
        answer += answer[-1]
    return answer