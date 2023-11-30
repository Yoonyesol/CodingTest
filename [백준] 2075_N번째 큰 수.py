import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())
nNum = []   #heap 자료구조를 이용해 값을 저장할 리스트

for i in range(n):
    table = list(map(int, input().split())) #입력받은 표의 수
    for j in table: #테이블 수 하나씩 순회
        if nNum:    #리스트에 원소가 하나 이상 존재할 경우
            if nNum[0] < j: #가장 작은 원소보다 입력받은 수가 클 경우
                heapq.heappush(nNum, j) #리스트에 입력받은 수를 넣는다.(n번째로 큰 수이므로 큰 수를 넣는다)
            if len(nNum) > n:   #n번째로 큰 수의 범위를 벗어난 경우
                heapq.heappop(nNum) #가장 작은 수를 삭제한다.
        else:   #리스트에 원소가 없을 경우
            heapq.heappush(nNum, j) #새로 원소를 추가한다.(원소추가+오름차순 정렬. minHeap)
print(nNum[0])  #가장 작은 수 출력
