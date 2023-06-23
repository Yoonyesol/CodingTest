import sys, itertools
input=sys.stdin.readline
n = int(input())
#input이 2 1 1 0일 때, {1:2, 2:1, 3:1, 4:0}를 저장하는 사전 생성
#각 인덱스에 input을 하나씩 대입한다. 1번 사람의 왼쪽에 두사람이 존재하고, 2번 사람의 왼쪽에는 한 사람이 존재...
dic = {idx+1:item for idx, item in enumerate(map(int, input().split()))}

#1~n번까지, 정답이 될 수 있는 모든 순열을 확인한다.
#각 조합의 원소를 모두 확인하며, 각 원소의 왼쪽에 있는 사람의 수를 모두 확인할 예정
for i in itertools.permutations([i for i in range(1, n+1)]):
    #(ex. i == [2, 1, 4, 3])
    for j in range(len(i)): #각 순열 조합 중 첫번째 인덱스의 수부터 확인한다. (ex. 2부터 시작)
        cnt = 0 #왼쪽에 있는 사람 수
        for k in i[:j]: #현재 사람(i[j])의 왼쪽에 선 사람들을 모두 살피기(ex.if i[j] == 4이라면, [2, 1]을 확인)
            if k > i[j]:   #왼쪽에 서 있는 사람(ex.2)이 i[j](ex.4)보다 더 크다면
                cnt += 1    #카운트 증가
        #왼쪽 사람 수를 모두 확인 한 후에 dic[i[j]]에 저장된 값과 실제 카운트 값이 동일한지 확인
        #ex.동일하다면 현재 순열에서 4번 사람의 왼쪽에 4보다 더 큰 수의 사람이 dic[4](=0)명 서 있다는 뜻. 정답 순열일 가능성이 높아진다.
        #ex.동일하지 않다면 4번 사람의 왼쪽에 4보다 더 큰 수의 사람 0명이 서 있지 않다는 뜻이므로 해당 순열은 답이 될 수 없다.
        if dic[i[j]] != cnt:    #동일하지 않으면 break 하고 다음 순열을 확인
            break
    #하나의 순열을 무사히 돌았다면, 모든 사람이 입력받은 조건(ex.[2 1 1 0])에 맞게 서 있다는 뜻이므로
    #정답을 출력하고 break하여 다음 순열을 생성하기를 멈춘다.
    else:
        print(' '.join(map(str, i)))
        break