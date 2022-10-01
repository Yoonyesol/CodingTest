import sys
n = int(sys.stdin.readline())
#set: 자료가 정렬되어 들어간다.
arr1 = set(map(int, input().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in arr1:
        print(1)
    else:
        print(0)