import sys
a = int(sys.stdin.readline())
arr = []
while a:
    word = sys.stdin.readline()
    arr.append(word[:-1])
    a -= 1
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)