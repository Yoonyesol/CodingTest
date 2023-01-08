def solution(age):
    #97 ~ 122 / a ~ z
    age_list = []
    answer = ''
    age_list = list(map(int, str(age)))
    for i in age_list:
        answer += chr(i+97)
    return answer