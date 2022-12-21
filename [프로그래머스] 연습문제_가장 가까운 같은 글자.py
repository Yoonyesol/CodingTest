def solution(s):
    answer = []
    for i in range(len(s)):
        arr = s[:i] #i번째 인덱스 전까지 끊어서 문자열 저장
        #arr을 뒤에서 앞으로 탐색해 arr에 현재 인덱스의 문자와 동일한 문자가 존재하는지 확인
        if arr.rfind(s[i]) != -1:   #존재한다면
            answer.append(i - arr.rfind(s[i]))  #현재 인덱스에서 찾은 문자의 인덱스를 빼서 배열에 저장
        else:   #존재하지 않는다면
            answer.append(-1)   #-1을 배열에 저장
    return answer