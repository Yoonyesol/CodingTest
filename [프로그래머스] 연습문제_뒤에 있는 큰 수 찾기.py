def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    for idx, num in enumerate(numbers):
        while stack and num > numbers[stack[-1]]:
            answer[stack.pop()] = num
        stack.append(idx)
    return answer