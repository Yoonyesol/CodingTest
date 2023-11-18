T = int(input())
for test_case in range(1, T + 1):
    card = {'S':13, 'D':13, 'H':13, 'C':13} #무늬별 카드 개수 초기화
    s = input().rstrip()    #영준이의 덱
    ans = ''    #정답 문자열을 저장할 변수
    card_dup_check = [] #중복 체크를 위한 배열

    for i in range(0, len(s), 3):   #0부터 3개씩 끊기 위해 3씩 건너뛰며 반복문 실행
        a = s[i:i+3]    #무늬+숫자 3글자씩 끊어서 a에 저장
        if a in card_dup_check: #카드가 중복이면
            ans = "ERROR"   #에러
            break
        card_dup_check.append(a)    #중복 체크 배열에 저장
        c_type = a[0]   #무늬
        card[c_type] -= 1   #무늬에 해당하는 카드 개수 -1(전체 카드 중 존재하는 카드 개수 빼기)

    if ans == '':   #'ERROR'나지 않은 경우
        ans = ' '.join(map(str, list(card.values())))   #부족한 카드를 모아서 출력
    print(f'#{test_case} {ans}')