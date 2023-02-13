import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    denom = lcm(denom1, denom2)
    numer = (numer1 * (denom / denom1)) + (numer2 * (denom / denom2))
    return [numer/math.gcd(int(numer),denom), denom/math.gcd(int(numer),denom)]

---------------------------------

import math
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)
    return [numer/math.gcd(numer,denom), denom/math.gcd(numer,denom)]