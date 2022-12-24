def solution(X, Y):
    arr = []
    for i in set(X)&set(Y): #x와 y의 중복만큼 i 반복
        for j in range(min(X.count(i), Y.count(i))):    #중복된 수 중 x, y에 여러번 들어있는 수 카운트
            arr.append(i)
    if len(arr) == 0:
        return "-1"
    arr.sort(reverse = True)
    if arr[0] == '0':
        return "0"
    return ''.join(str(s) for s in arr)