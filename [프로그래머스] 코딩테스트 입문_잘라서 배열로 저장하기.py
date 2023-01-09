def solution(my_str, n):
    answer = []
    while True:
        if len(my_str) <= n:
            answer.append(my_str[0:])
            break
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer