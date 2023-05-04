import sys
input=sys.stdin.readline

answer = 0
h, w = map(int, input().split())    #2차원 세로 h, 2차원 가로 w
arr = list(map(int, input().split()))   #블록이 쌓인 높이
for i in range(1, len(arr)-1):
    left_max = max(arr[:i+1])
    right_max = max(arr[i+1:])
    total_min = min(left_max, right_max)
    
    if total_min > arr[i]:
        answer += total_min - arr[i]
        
print(answer)



