def solution(arr1, arr2):
    answer = 0
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1
    else:
        if len(arr1) > len(arr2):
            answer = 1
        elif len(arr1) < len(arr2):
            answer = -1 
    return answer