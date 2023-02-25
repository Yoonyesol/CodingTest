from itertools import permutations 
def solution(k, dungeons):
    result = []
    #던전을 방문하는 순서의 경우의 수를 나열
    for dg in permutations(dungeons, len(dungeons)):	
        nk = k	#매번 k로 피로도 리셋
        answer = 0	#방문한 던전 수 매번 리셋
        for d in dg:	#각 경우의 수마다 방문할 수 있는 던전 수 확인
            if nk >= d[0]:	#남은 피로도가 던전의 필요피로도보다 같거나 큰 경우 던전 방문
                nk -= d[1]	#남은 피로도-소모 피로도
                answer += 1 	#방문한 던전 수 + 1
        result.append(answer)
    return max(result)	#방문 가능한 최대 던전의 수