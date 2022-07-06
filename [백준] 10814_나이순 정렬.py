import sys
input = int(sys.stdin.readline())
arr = []
while input > 0:
    age, name = sys.stdin.readline().split()
    arr.append((int(age), name))
    input-=1
arr.sort(key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])