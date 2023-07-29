import sys
import itertools
input=sys.stdin.readline
k = int(input())
arr = input().split()
min_num = 9876543210    #0~9로 만들 수 있는 가장 큰 수로 max값을 초기화
max_num = 0 #0으로 min 값 초기화
min_num2, max_num2 = '', '' #문자열 상태의 값을 저장하기 위한 변수 초기화
#itertools의 permutation을 이용해 0~9까지의 숫자 중 k+1개를 뽑아서 각각 부등호식과 부합하는지 확인
for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k+1):
    #순열의 두 숫자와 가운데 부등호가 식에 부합한지 확인
    for j in range(len(arr)):
        if arr[j] == "<":
            if i[j] > i[j+1]:   #부합하지 않는다면 이번 순열의 다음 숫자는 확인하지 않는다.
                break
        if arr[j] == ">":
            if i[j] < i[j+1]:
                break
    else:   #모든 순열이 중간 이탈없이 식을 만족시킨다면
        a = ''.join(map(str, i))    #각 숫자를 join으로 통합
        if min_num > int(a):    #가장 작은 수 확인
            min_num = int(a)
            min_num2 = a
        if max_num < int(a):    #가장 큰 수 확인
            max_num = int(a)
            max_num2 = a
print(max_num2)
print(min_num2)