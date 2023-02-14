def solution(array, n):
    array = sorted(array)
    arr = [abs(i-n) for i in array]
    return array[arr.index(min(arr))]

------------------------------------

def solution(array, n):
    array.sort(key = lambda x: (abs(x-n), x))
    answer = array[0]
    return answer