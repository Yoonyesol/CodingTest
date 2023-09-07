import sys
input = sys.stdin.readline
_= input()
arr = list(map(int, input().split()))
a = []
min_val = 1e9   #이전 리스트 값 중 가장 작은 값
max_minus = 0   #현재값과 최소값의 차이(Ai-Aj의 최댓값)
for i in arr:
    if min_val <= i:    #현재 값 i가 i이전의 리스트 값 중 최소값보다 크거나 같다면
        max_minus = max(max_minus, i-min_val)   #현재값-최소값, 기존 최댓값 중 더 큰 값을 저장
    else:    #현재 값이 i이전의 리스트 값 중 최소값보다 작다면
        min_val = i #현재 값을 최소값으로 설정
    a.append(max_minus) #빈배열에 위의 메커니즘으로 구한 최댓값을 차례대로 저장
print(' '.join(map(str, a)))    #a의 값을 공백 기준으로 출력