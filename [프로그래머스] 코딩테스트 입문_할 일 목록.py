def solution(todo_list, finished):
    answer = []
    for i, j in zip(todo_list, finished):
        if not j:
            answer.append(i)
    return answer