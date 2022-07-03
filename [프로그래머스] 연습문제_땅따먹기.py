def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3]) #다음 행의 0열
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[-1])

# def solution(land):
#     sum = 0
#     for i in range(len(land)):
#         idx = land[i].index(max(land[i]))   #각 행에서 가장 큰 값인 원소의 인덱스 저장
#         if(i != len(land)-1): #가장 마지막 예외처리
#             land[i+1][idx] = 0  #다음 행의 idx 인덱스 원소값을 0으로 변경
#         sum += max(land[i]) 
#     return sum