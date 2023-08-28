import sys
input = sys.stdin.readline
change = input().rstrip()
a = change.count('a')   #문자열 전체에서 'a'의 갯수
left = 0    #시작 인덱스
min_b = float('inf')    #무한대로 초기화

# 이어진 문자열: 'a'가 연달아 있는 문자열
# 위에서 구한 a개의 부분 문자열 중, 'a'가 연달아 있을 수 있도록 'b'를 'a'로 교체해 주는 경우의 수를 구한다.
# 모든 경우의 수 중 가장 적은 교체횟수가 정답

while left < len(change):   #시작인덱스가 문자열의 길이를 넘어서지 않도록 한다.(넘어서면 인덱스 에러 발생)
    right = left + a    #검사해야 할 a개의 문자열 중 마지막 인덱스
    if right > len(change): #마지막 인덱스가 문자열의 길이를 넘어선 경우, 문자열이 원형이므로 문자열 시작부분으로 인덱스가 넘어간다.
        part = change[left:len(change)]+change[:right-len(change)]
    else:   #마지막 인덱스가 문자열의 길이를 넘어가지 않는 경우
        part = change[left:right]   #평범하게 시작-끝 인덱스를 지정해 문자열 추출
    min_b = min(min_b, part.count('b')) #추출한 문자열에 b가 있다면, b 개수만큼 교환해야 한다. 가장 교환개수가 적은 경우를 찾기위해 min사용
    left += 1   #시작인덱스를 한칸 늘려가며 다음 a개 검사
print(min_b)