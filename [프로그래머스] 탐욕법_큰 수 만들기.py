def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while k>0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    return ''.join(stack[:len(stack)-k])