import sys
input=sys.stdin.readline
n = int(input())
cnt = 0 #거스름돈 갯수
while n > 0:
    if n % 5 == 0:  #n이 5의 배수라면, 거스름돈을 5의 몫만큼 거슬러준다.
        cnt += (n//5)
        break
    else:   #n이 5의 배수가 아니라면, 5의 배수가 될때까지 2로 빼준다.
        n -= 2
        cnt += 1    #빼준만큼 거스름돈 체킹
if n < 0:   #n이 음수인 경우-> 거스름돈을 2와 5로 거슬러줄 수 없는 경우
    print(-1)
else:   #거스름돈을 2와 5로 거슬러줄 수 없는 경우
    print(cnt)  #체크한 거스름돈 갯수 출력