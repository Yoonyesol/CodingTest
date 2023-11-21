import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    setArr = list(set(arr))
    sortedArr = sorted(arr, reverse=True)

    if sortedArr[0] == 0 and sortedArr[1] == 0 and sortedArr[2] == 0:
        break

    if sortedArr[0] >= sortedArr[1]+sortedArr[2]:
        print("Invalid")
        continue

    if len(setArr) == 1:
        print("Equilateral")
    elif len(setArr) == 3:
        print("Scalene")
    elif len(setArr) == 2:
        print("Isosceles")