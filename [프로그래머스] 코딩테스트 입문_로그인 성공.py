def solution(id_pw, db):
    answer = ''
    for i in db:    #로그인 성공
        if id_pw[0] != i[0]:
            answer = "fail"
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return answer

--------------------------------------
def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"