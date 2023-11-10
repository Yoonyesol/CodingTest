import sys
input=sys.stdin.readline

n = int(input().rstrip())
house = [list(map(int, input().split())) for _ in range(n)]
house.sort()

ans = house[0][1]    #가장 긴 길이
bestLengthIdx = 0   #가장 긴 길이 인덱스
for i in range(len(house)): #가장 긴 길이와 인덱스 업데이트
    if ans < house[i][1]:
        ans = house[i][1]
        bestLengthIdx = i

#가장 긴 기둥의 왼쪽 면적 구하기(왼->오)
thisLength = house[0][1]    #현재 기둥의 길이
for i in range(bestLengthIdx):
    if thisLength < house[i+1][1]:  #다음 기둥이 더 높은 경우
        ans += thisLength * (house[i+1][0]-house[i][0]) #현재 높이 * 계산하지 않은 너비
        thisLength = house[i+1][1]  #기둥의 길이 갱신
    else:   #다음 기둥이 더 낮거나 길이가 동일한 경우
        ans += thisLength * (house[i + 1][0] - house[i][0])

#가장 긴 기둥의 오른쪽 면적 구하기(오->왼)
thisLength = house[-1][1]    #현재 기둥의 길이
for i in range(n-1, bestLengthIdx, -1): #인덱스 뒤에서부터
    if thisLength < house[i-1][1]:  #이전 인덱스의 기둥이 더 높은 경우(=다음 기둥이 더 높은 경우)
        ans += thisLength * (house[i][0] - house[i-1][0])
        thisLength = house[i-1][1]
    else:
        ans += thisLength * (house[i][0] - house[i-1][0])

print(ans)