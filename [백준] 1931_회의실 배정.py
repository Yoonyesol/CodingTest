import sys
input = sys.stdin.readline
n = int(input())
x = []
for i in range(n):
    a, b = map(int, input().split())
    x.append([a, b])
x = sorted(x, key=lambda x:(x[1], x[0]))    #끝나는 시간->동차시 시작시간 오름차순 정렬
cnt = 1 #회의배정확정 카운트 변수, 첫번째 회의는 무조건 확정이므로 1로 초기화
end_time = x[0][1]  #가장 빨리 끝나는 회의의 끝나는 시간
for i in range(1, n):   #가장 빨리 끝나는 회의 이후부터 인덱스 n-1까지의 회의 모두 확인
    if x[i][0] >= end_time: #이전 회의의 끝나는 시간보다 시작 시간이 뒤인 회의
        cnt += 1    #회의배정 확정    
        end_time = x[i][1]  #확정된 회의의 끝나는 시간으로 ent_time교체. 이를 기반으로 다음 회의를 잡는다.
print(cnt)

# 정렬기준이 끝나는 시간 -> 시작 시간인 이유: 
# 빨리 끝나는 회의일수록 뒷부분 남는 시간에 다른 회의를 많이 잡을 수 있으므로,
# 언제 회의가 끝나는지부터 확인한다.
# 시작 시간이 오름차순인 이유는, 오름차순 정렬하지 않았을 때 (4,4/3,4)인 경우는 회의를 잡을 수 없다고 표시되어 cnt+0이다.
# 하지만 오름차순 정렬하면(3,4 / 4,4) 이전 회의 끝나는 시간보다 뒤의 회의 시작 시간이 더 크므로 회의배정횟수는 cnt+1이 된다.