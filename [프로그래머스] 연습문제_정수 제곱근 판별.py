import math
def solution(n):
    sq = math.sqrt(n)
    if float.is_integer(sq):
        return math.pow(sq+1, 2)
    else:
        return -1