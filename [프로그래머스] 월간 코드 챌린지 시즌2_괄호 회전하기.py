def solution(s):
    answer = 0
    s_list = list(s)
    for i in range(len(s_list)-1):
        stack = []
        for j in s_list:
            if stack:
                if (j == ']' and stack[-1] == '[') or (j == '}'and stack[-1] == '{') or (j == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(j)
            else:
                stack.append(j)
        if len(stack) == 0:
            answer += 1
        s_list.append(s_list.pop(0))
    return answer