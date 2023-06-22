import sys
input=sys.stdin.readline
n = int(input())    #골 들어간 횟수
arr = []    #[골 넣은 팀, 골 들어간 시간] 저장할 리스트
for _ in range(n):
    arr.append(list(input().split()))   #[골 넣은 팀, 골 들어간 시간] 저장
arr.append(["0", "48:00"])  #마지막 48분까지의 시간동안의 시간도 체크해야 하므로 48분 배열 추가."0"부분은 아무거나 지정해도 상관없다.
dic = {"1":"00:00", "2":"00:00"}    #각 팀의 승리시간을 저장할 dic. 배열로 해도 됨
goal = [0, 0, 0]    #각 팀이 골을 넣은 횟수를 체크할 리스트. goal[0]은 패딩이다.
for i in range(len(arr)-1): #현재 인덱스 시간, 다음 인덱스 시간을 비교할 것이므로 인덱스에러를 방지하기 위해 len(arr)-1
    goal[int(arr[i][0])] += 1   #현재 팀의 골 넣은 횟수 체크
    c_m, c_s = map(int, arr[i][1].split(":"))    #현재 시간
    a_m, a_s = map(int, arr[i+1][1].split(":"))    #다음 시간
    #(다음 시간-현재 시간)
    if c_s > a_s:   #다음 초보다 현재 초가 더 큰 경우 뺄셈 음수 예외처리
        a_m -= 1    #1분 깎고
        a_s += 60   #60초 늘리기
    m = a_m - c_m   #다음 시간-현재 시간(분)
    s = a_s - c_s   #다음 시간-현재 시간(초)

    if goal[1] > goal[2]:   #1팀이 승리 중
        d_m, d_s = map(int, dic["1"].split(":"))  # 1팀의 총 승리시간
        d_m += m    #1팀의 승리시간을 다음 골이 들어간 지점까지 연장
        d_s += s
        while d_s >= 60:    #60초 넘으면 1분으로 처리
            d_s -= 60
            d_m += 1
        dic["1"] = str(d_m).zfill(2)+":"+str(d_s).zfill(2)  #"MM:SS" 형태로 만들어 dic에 저장
    elif goal[1] < goal[2]: #2팀이 승리 중
        d_m, d_s = map(int, dic["2"].split(":"))  # 2팀의 총 승리시간
        d_m += m
        d_s += s
        while d_s >= 60:
            d_s -= 60
            d_m += 1
        dic["2"] = str(d_m).zfill(2) + ":" + str(d_s).zfill(2)

for i in dic.values():
    print(i)