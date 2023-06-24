import sys
input=sys.stdin.readline
n, w, l = map(int, input().split()) #다리를 건널 트럭 수, 다리 길이, 다리의 최대하중
arr = [i for i in map(int, input().split())]    #다리를 건널 트럭의 리스트
arr2 = []   #다리를 모두 건넌 트럭의 리스트
bridge = [0 for _ in range(w)]  #현재 다리의 상태
cnt = 1 #다리를 건너는 시간을 카운팅하는 변수. 1초부터 시작하도록 초기화
while len(arr2) < n:    #모든 트럭이 다리를 건너면 while문 종료
    if bridge[0] != 0:  #트럭이 다리의 마지막 부분에 다다랐다.
        arr2.append(bridge[0])  #현재 다리의 마지막 부분에 올라간 트럭을 arr2에 저장
        bridge[0] = 0   #트럭이 다리를 건넜으니 다리 부분을 0으로 초기화
    else:   #트럭이 아직 다리의 마지막 부분에 도달하지 못한 상태
        bridge.append(bridge.pop(0))    #맨앞 다리를 떼어 뒤로 붙이는 식으로 앞으로 나아가는 다리를 표현
        # arr에 트럭이 남아있고 arr의 맨 앞 트럭과 현재 다리의 하중을 합한 값이 최대하중보다 작거나 같다면,
        if arr and sum(bridge) + arr[0] <= l:   
            bridge[-1] = arr.pop(0)  # 다리 위에 트럭을 올린다
        cnt += 1    #모든 트럭이 다리를 건널 때까지, 매번 1초가 흐르도록 카운팅한다.
print(cnt)