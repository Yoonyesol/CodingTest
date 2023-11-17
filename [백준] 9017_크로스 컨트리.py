import sys
input=sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().split()))

    #길이가 6개가 되지 못한 팀은 삭제
    remove_set = set()
    for i in range(1, max(arr)+1):  #1번 팀부터 존재하는 가장 큰 수(팀)까지 반복
        if arr.count(i) != 6:   #달리기 주자 수가 6명이 아니라면
            remove_set.add(i)   #제외 목록에 추가

    #탈락 팀 제외한 리스트
    arr = [i for i in arr if i not in remove_set]

    #팀별 idx 저장
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic.keys():
            dic[arr[i]] = [i]
        else:
            dic[arr[i]].append(i)

    #리스트의 1~4번째 주자의 합, 동일한 등수일 시 5번째 주자의 등수로 최종 결과 구하기
    dic = sorted(dic.items(), key=lambda x:(sum(x[1][0:4]), x[1][4]))
    print(dic[0][0])