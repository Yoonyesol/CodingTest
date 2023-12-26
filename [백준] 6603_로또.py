import sys
input = sys.stdin.readline

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    a = a[1:]

    #주어진 모집합에서 만들 수 있는 모든 부분집합 구하기
    subset = [[]]   #공집합
    for i in a: #모집합
        for j in range(len(subset)):    #매번 subset에 저장된 모든 원소를 모집합과 결합
            subset.append(subset[j]+[i])

    for i in sorted(subset):    #만들어진 부분집합 리스트를 사전순 정렬
        if len(i) == 6: #길이가 6인 집합만 출력
            print(*i)
    print()


-----------------

from itertools import combinations 
for lst in combinations(arr, 6) -> itertools의 combinations 사용
#[(1, 2, ..., 6), (1, 3, ..., 7), (2, 3, .., 9)]