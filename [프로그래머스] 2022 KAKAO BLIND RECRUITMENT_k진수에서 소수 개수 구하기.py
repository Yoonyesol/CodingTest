import math
def solution(n, k):
    cnt = 0
    p = ''
    while n > 0:
        p += str(n%k)
        n //= k
    p = p[::-1].split("0")
    for i in p:
        if i =="":
            continue
        i = int(i)
        if i == 1:
            continue
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0:
                break
        else:
            cnt += 1
    return cnt