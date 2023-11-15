import sys
input=sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split())) #3 2 5 5 6 4 4 5 7
left, right = 0, 0

count = [0] * (max(arr)+1)
ans = 0
while right < n:    #right포인터가 끝까지 갔을 때 종료
    if count[arr[right]] >= k:  #3의 카운트가 k보다 크거나 같다면
        count[arr[left]] -= 1   #가장 왼쪽의 카운트 줄이기
        left += 1   #left 포인터를 오른쪽으로 한 칸 이동
    else:   #3의 카운트가 k보다 작다면
        count[arr[right]] += 1  #3의 카운트를 1 증가시킴
        right += 1  #오른쪽으로 범위 증가
    ans = max(ans, right-left)  #최대 증가 부분 수열의 길이 갱신

print(ans)