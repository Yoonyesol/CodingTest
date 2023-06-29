def solution(arr):
    if not 2 in arr:
        return [-1]
    idx = []
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    return arr[idx[0]:idx[-1]+1]