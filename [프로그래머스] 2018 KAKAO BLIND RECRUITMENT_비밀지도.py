def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b').zfill(n)
        arr2[i] = format(arr2[i], 'b').zfill(n)
    for i in range(n):
        hap = ''
        for j in range(n):
            if arr1[i][j] == arr2[i][j] and arr1[i][j] == '0':
                hap += " "
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                hap += "#"
        answer.append(hap)
    return answer