import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = list(map(int, input().split()))

arr = sorted(arr)   #오름차순 정렬
left, right = 0, n-1    #더해야 할 두 수를 가리키는 인덱스
cnt = 0 #제조 가능한 갑옷 개수
while left < right: #더해야 할 두 수가 같아지면 종료
    if arr[left] + arr[right] > m:  #가장 큰 수+가장 작은 수가 m보다 크다면,
        right -= 1  #가장 큰 수를 하나 줄여서 다시 확인해본다.
    elif arr[left] + arr[right] < m:  #가장 큰 수+가장 작은 수가 m보다 작다면,
        left += 1  #가장 작은 수 대신 그 다음 작은 수를 더해서 다시 확인해본다.
    else:  #가장 큰 수+가장 작은 수가 m과 동일하다면,
        cnt += 1    #갑옷 재조 개수 +1
        left += 1   #체크한 가장 작은 수 다음 수를 체크
        right -= 1  #체크한 가장 큰 수 이전 수를 체크
print(cnt)