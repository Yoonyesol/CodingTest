import sys
import collections

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    number = int(sys.stdin.readline())
    arr.append(number)

print(round(sum(arr)/len(arr))) #산술평균
arr.sort()
print(arr[int(len(arr)/2)])  #중앙값

cntList = collections.Counter(arr).most_common(3)
answer = 0
for _ in range(len(cntList)):
    if len(cntList) > 1 and cntList[0][1] == cntList[1][1]:
        answer = cntList[1][0]  #최빈값
    else:
        answer = cntList[0][0]
print(answer)

print(max(arr)-min(arr))  #최대-최소