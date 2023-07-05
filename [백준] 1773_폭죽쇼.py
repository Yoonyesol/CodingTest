import sys
input=sys.stdin.readline
n, c = map(int, input().split())
arr = [0]*(c+1) #폭죽이 터지는 시간을 표시한 배열
ans = 0 #폭죽이 터지는 총 시간을 연산할 변수
for i in range(n):
    std = int(input())  #학생이 폭죽을 터뜨리는 시간(초)
    if std == 1:    #학생이 1초마다 폭죽을 터뜨리므로, 아래의 연산 필요없이 모든 초에 폭죽이 터진다고 표시
        print(c)
        quit()  #c를 출력하고 바로 프로그램 종료
    for j in range(std, c+1, std):  #std~c+1까지, std만큼 건너뛰며 연산
        if arr[j] == 0: #해당 인덱스에 폭죽이 터질 예정이 아직 없는 경우
            arr[j] = 1  #폭죽이 터진다고 표시
            ans += 1    #폭죽터지는 시간 +1
print(ans)