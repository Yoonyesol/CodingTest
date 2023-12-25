import sys
input=sys.stdin.readline
arr = []
a, b = 0, 0
for _ in range(9):
    arr.append(int(input().rstrip()))
search = sum(arr) - 100
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == search:
            a = arr[i]
            b = arr[j]
            break
    if len(arr) == 7:
        break
for i in sorted(arr):
    if i == a or i == b:
        continue
    print(i)

----------------

2차 

import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input().strip()))

num = sum(arr) - 100
for i in arr:
    if i > num or i*2 == num:
        continue
    temp = num - i
    if temp in arr:
        arr.remove(temp)
        arr.remove(i)
        break

for i in sorted(arr):
    print(i)

--------------------

import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input().strip()))

num = sum(arr) - 100
a, b = 0, 0
for i in arr:
    if i > num or i*2 == num:
        continue
    if num - i in arr:
        a, b = num - i, i
        break

for i in sorted(arr):
    if i != a and i != b:
        print(i)
