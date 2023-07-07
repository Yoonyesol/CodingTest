import sys
input=sys.stdin.readline
n = int(input())
arr = []    #조건을 충족하는 수를 담는 리스트
cnt = 0 #가능한 숫자의 갯수 카운팅 변수
for i in range(n):
    guess_num, strike, ball = map(int, input().split())
    guess_num = list(str(guess_num))
    #가능한 모든 세자리 숫자를 생성
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                strike_cnt = 0  #생성한 수와 추측한 수의 스트라이크 수
                ball_cnt = 0    #생성한 수의 추측한 수의 볼 수
                if j == k or k == l or l == j:  #서로 다른 세개의 수를 생성
                    continue
                num = list(str(j)+str(k)+str(l))    #서로 다른 세 수 조합
                for a in range(3):  #스트라이크, 볼 수 맞는 수 찾아내기
                    if num[a] == guess_num[a]:  #추측한 수와 생성한 수의 위치가 같으면
                        strike_cnt += 1 #스트라이크+1
                    ball_cnt += num.count(guess_num[a]) #추측한 수가 생성한 수에 들어있다면 카운팅
                ball_cnt -= strike_cnt  #스트라이크 수가 포함되어 있으므로 빼준다
                #실제 숫자 - 추측한 수 사이의 스트라이크 수와 볼 수를 생성한 숫자 - 추측한 수 사이의 스트라이크, 볼 수와 비교
                #만약 두 수가 동일하다면 해당 수는 정답이 될 수 있는 후보군에 들어간다.
                if strike == strike_cnt and ball == ball_cnt:   
                    arr.append(num)
                    if arr.count(num) >= n: #n가지 케이스 모두 동일한 스트라이크, 볼 수라면 해당 수는 정답이 될 수 있는 수이다.
                        cnt += 1
print(cnt)