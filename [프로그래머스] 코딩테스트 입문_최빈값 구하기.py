def solution(array):
    arr = []
    s_arr = list(set(array))
    for i in s_arr:
        arr.append(array.count(i))
    if arr.count(max(arr)) >= 2:
        return -1
    else: 
        return s_arr[arr.index(max(arr))]