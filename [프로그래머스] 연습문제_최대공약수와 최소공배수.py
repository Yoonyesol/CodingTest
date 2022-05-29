def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a
def solution(n, m):
    arr = []
    arr.append(gcd(n, m))
    arr.append(n * (m / gcd(n, m)))
    return arr