import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_len = len(str(n)) #입력받은 수의 길이
sumN = 9    #전체 수 길이: 1~9까지의 수 전체 이어쓴 길이로 초기화
if n < 10:  #입력받은 수가 10보다 작다면
    print(n)    #현재까지의 수를 바로 출력
else:   #10보다 크거나 같다면
    for i in range(2, n_len):   #n의 전체 길이보다 작은 자리수의 전체 길이수 총합 구하기(if n_len == 3: 1, 2자리 수의 모든 수를 이어쓴 개수를 구한다.)
        sumN += (int('9'*i) - int('1'+'0'*(i-1)) + 1)*i #if 2:10~99이므로, 99-10+1를 통해 구간 사이의 수의 갯수를 구하고, 자리수만큼 곱해서 총 이어쓴 자리수를 구한다.
    #n의 현재 자리수에서의 이어쓴 길이 수 구하기
    sumN += (n - int('1' + '0' * (n_len - 1)) + 1) * n_len  #if n==120: 120-100+1를 구한뒤, 자리수를 곱해서 총 이어쓴 자리수를 구한다.
    print(sumN)