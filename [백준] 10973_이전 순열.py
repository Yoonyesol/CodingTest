import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
flag = False    #이중for문 탈출 플래그

for i in range(n-1, 0, -1): #뒤에서부터 확인
    if arr[i] < arr[i-1]:   #오름차순 정렬되지 않은 지점 => i-1
        for j in range(n-1, 0, -1): #뒤에서부터 확인
            if arr[i-1] > arr[j]:   #i-1 위치의 수보다 작은 수를 뒤에서부터 찾기.(i-1 위치의 수와 가장 가까운 작은 수)
                arr[i-1], arr[j] = arr[j], arr[i-1] #두 수의 위치를 바꾸어 기존 수보다 작은 수를 만든다.
                arr = arr[:i] + sorted(arr[i:], reverse=True)   #i를 기준으로 앞부분은 그대로 유지, 뒷부분은 내림차순 정렬(이전 수열을 만들기 위해서)
                print(*arr) #완성된 수열 출력
                flag = True #for문 탈출 플래그 설정
                break
    if flag: break
else:   #for문에서 중간에 break되지 않은 경우는 모든 수가 오름차순 정렬된 상태임
    print(-1)
