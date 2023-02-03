import math
def solution(balls, share):
    return math.factorial(balls) // (math.factorial(balls-share) * math.factorial(share))

--------------------------

import math
def solution(balls, share):
    return math.comb(balls, share)

