T = 10
for test_case in range(1, T+1):
    letter = int(input())
    pan = [list(map(int, input())) for _ in range(8)]
    cnt = 0
    #가로(행이동)
    for r in range(8):
        #회문 생성 횟수
        for c in range(8-letter+1):
            #회문 길이만큼 슬라이싱
            if pan[r][c:c+letter] == pan[r][c:c+letter][::-1]:
                cnt += 1
    #세로(열이동)
    for c in range(8):
        for r in range(8-letter+1):
            char = ''
            #r번째 행부터 회문의 길이에 해당하는 회문을 char에 넣기
            for r2 in range(r, r+letter):
                char += pan[r2][c]
            if char == char[::-1]:
                cnt += 1
    print("#{} {}".format(test_case, cnt))