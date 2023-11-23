import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
x = list(map(int, input().split()))

ans = 0
if m == 1:  #가로등 개수가 1개인 경우
    ans = max(x[0]-0, n-x[0])
else:   #가로등 개수가 2개 이상인 경우
    for i in range(m):  #모든 가로등에 대해 반복
        if i == 0:  #첫번째 인덱스라면
            height = x[i]-0 #첫번째 가로등에서부터 길의 시작부분까지의 거리를 저장
        elif i == m-1:  #마지막 인덱스라면
            height = n-x[i] #마지막 가로등에서부터 길의 마지막부분까지의 거리를 저장
        else:   #시작 인덱스, 마지막 인덱스가 아니라면
            temp = x[i]-x[i-1]  #두 가로등 사이의 거리를 저장
            if temp % 2 == 0:   #두 가로등 사이 거리가 짝수라면
                height = temp // 2  #2로 나눈값을 최소 높이로
            else:   #두 가로등 사이 거리가 홀수라면
                height = temp // 2 + 1  #2로 나눈 값으로 커버 안 되는 지점이 생기므로 +1 해주기
        ans = max(height, ans)  #매번 가장 큰 수를 ans에 저장해 모든 지점을 커버하는 가로등의 높이 구하기
print(ans)