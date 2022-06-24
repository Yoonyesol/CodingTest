# ( 가 나오면 스택에 넣기
# ) 가 나오면 스택에 (가 있는지 확인
# 스택이 비어있으면 true 리턴

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack.pop() == "(":
                continue
            else:
                return False
    return not stack    #스택이 비어있는 경우 true