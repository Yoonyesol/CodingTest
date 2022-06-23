def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))] #arr1의 길이만큼 answer = [[],[],[]...]
    for i in range(len(arr1)):  #arr1의 행
        tmp = [0] * len(arr2[0])    #arr2의 열 길이만큼 tmp = [0],[0],[0]...
        for j in range(len(arr1[0])):   #arr1의 열, arr2의 행
            for k in range(len(arr2[0])):   #arr2의 열
                tmp[k] += arr1[i][j] * arr2[j][k]
        answer[i] = tmp
    return answer