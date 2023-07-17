import sys
input=sys.stdin.readline
n, m = map(int, input().split())
memo = dict()   #키워드와 키워드가 사용됐는지 여부를 체크할 dict
for _ in range(n):
    memo[input().rstrip()] = 0  #초기에는 모두 사용되지 않음으로 체크
cnt = 0 #사용한 키워드의 갯수를 체크하는 변수
#이전에 이미 사용되었던 키워드 갯수를 축적하기 위해 for문 바깥에 변수를 초기화
for i in range(m):
    blog = input().rstrip().split(",")
    for i in blog:  #블로그에 사용된 모든 키워드에 대해 아래 코드 진행
        # 블로그에 사용된 코드가 memo에 존재하고, 해당 키워드가 한번도 사용되지 않은 경우
        if i in memo.keys() and memo[i] == 0:   
            memo[i] = 1 #'사용했음'으로 체크
            cnt += 1    #사용한 키워드 갯수 증가
    print(n-cnt)