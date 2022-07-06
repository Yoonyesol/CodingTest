import sys
a = int(sys.stdin.readline())
answer = list(map(int, str(a)))
answer.sort(reverse = True)
print(*answer, sep="")  #unpacking