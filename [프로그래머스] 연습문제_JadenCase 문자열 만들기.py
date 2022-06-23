def solution(s):
    #모든 항목을 소문자로 만들고 공백 기준으로 split
    s = s.lower().split(' ')    #공백문자 연속 가능하므로 ' '를 기준으로 split
    for i in range(len(s)):
        if not s[i][:1].isdigit():  #가장 첫번째 문자가 숫자가 아닌 경우
            s[i] = s[i][:1].upper() + s[i][1:]
    return " ".join(s)