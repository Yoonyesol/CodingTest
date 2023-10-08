def solution(my_string, is_suffix):
    answer = 0
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[i:])
    if is_suffix in arr:
        answer = 1
    return answer