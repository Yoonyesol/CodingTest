def solution(n):
    answer = []
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            answer.append(i)
        else:
            i += 1
    for i in answer:
        if i not in result:
            result.append(i)
    return result
--------------------------------------
def solution(n):
    answer = set()
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            answer.add(i)
        else:
            i += 1
    return sorted(list(anwer))
