import sys
input = sys.stdin.readline

n = int(input().rstrip())
length = list(map(int, input().split()))    #도로 길이
oil = list(map(int, input().split()))   #주유소 가격

left, right = 0, 1  #포인터
ans = 0 #총 지불 금액
for i in range(n-1):    #전체 도로길이 만큼 반복
    if i == 0:  #첫번째 도로는 무조건 첫번째 주유소에서 넣은 기름으로 이동
        ans += oil[0] * length[0]   #가격 업데이트
        continue    #첫번째 도로 통과
    # 두번째 도로부터 현재보다 더 가격이 저렴한 주유소가 나타날 때까지 현재 주유소에서 기름을 채운다.
    if oil[left] > oil[right]:  #현재 주유소보다 더 저렴한 주유소가 나타난다면
        left = right    #다음 주유는 그곳에서 진행
    ans += oil[left] * length[i]    #현재 시점에서 가장 저렴한 주유소와 지나는 도로길이를 순차적으로 곱해 총 지불금액을 구한다.
    right += 1  #right를 1씩 늘려가며 다음 주유소를 탐색

print(ans)