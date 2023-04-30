import sys
input=sys.stdin.readline
n = int(input())
people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w,h))
arr = [1] * n   #등수
for i in range(len(people)):
    for j in range(len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            arr[i] += 1
    print(arr[i], end=" ")