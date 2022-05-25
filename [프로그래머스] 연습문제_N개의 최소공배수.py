def gcd(p, q): #최대공약수 
    while(q):
        p, q = q, p % q
    return p

def solution(arr):
    result = arr[0]
    for i in arr:
        result = (result * i) / gcd(result, i)
    return result