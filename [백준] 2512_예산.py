import sys
input=sys.stdin.readline

n = int(input().rstrip())   #지방 개수
arr = list(map(int, input().split()))   #지방 요청 예산
budget = int(input().rstrip())  #정해진 예산 총액
start, end = 0, max(arr)    #시작 포인트, 끝 포인트

while start <= end: #start가 end보다 크면 while문 종료
    total = 0   #총 예산
    mid = (start + end) // 2    #평균
    for i in arr:   #전체 예산을 돌면서
        total += min(i, mid)    #평균값과 요청 예산 중 더 적은 금액을 total에 추가
    if total <= budget: #총 금액이 정해신 예산보다 작다면
        start = mid + 1 #예산을 늘리기
    else:
        end = mid - 1   #예산을 줄이기
print(end)  #가능한 최대 예산 출력