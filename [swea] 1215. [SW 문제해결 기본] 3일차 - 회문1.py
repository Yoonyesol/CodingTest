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


----------------------------------

23.05.08

import math

for test_case in range(1, 11):
    answer = 0
    hoi = int(input())
    pan = []

    for i in range(8):
        pan.append(list(input().rstrip()))
    pan2 = list(zip(*pan))

    for i in range(8):
        for j in range(9-hoi):
            p_list = pan[i][j:hoi + j]
            p_list2 = pan2[i][j:hoi + j]
            start = 0
            end = hoi - 1
            for _ in range(int(math.ceil(hoi/2))):
                if p_list[start] != p_list[end]:
                    break
                start += 1
                end -= 1
            else:
                answer += 1

            start2 = 0
            end2 = hoi - 1
            for _ in range(int(math.ceil(hoi/2))):
                if p_list2[start2] != p_list2[end2]:
                    break
                start2 += 1
                end2 -= 1
            else:
                answer += 1

    print("#{} {}".format(test_case, answer))