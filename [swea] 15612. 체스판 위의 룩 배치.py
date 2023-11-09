T = int(input())
for test_case in range(1, T + 1):
    ans = "yes"
    c_cnt = 0
    arr = [list(input()) for _ in range(8)]

    for i in range(8):
        cnt = arr[i].count("O") #한 행에서 록의 개수
        if cnt > 1:     #한 행에 여러개의 록이 위치한 경우
            ans = 'no'  #ans값을 no로 지정 후 for문 종료
            break
        c_cnt += cnt    #한 행에서 록의 개수를 c_cnt에 저장해 최종 8개의 록이 판 위에 있는지 확인할 예정
        arr2 = []   #세로 검증을 위한 배열 생성
        for j in range(8):
            arr2.append(arr[j][i])  #말판의 세로를 검증
        if arr2.count("O") > 1: #세로값만 입력한 배열에서 록의 개수가 1개 이상이라면
            ans = "no"  #실패
            break

    if c_cnt != 8:  #최종적으로 록의 개수가 8개가 아니라면 ans="no"
        ans = "no"
    print(f'#{test_case} {ans}')
