def solution(n):
    i = 1
    while n > 0:
        n = n // i
        i+= 1
    return i - 2

--------------------------------------

def solution(n):
    i = 0
    while n > 0:
        i += 1
        n //=  i
    return i - 1