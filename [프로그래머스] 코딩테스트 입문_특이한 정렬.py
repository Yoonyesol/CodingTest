def solution(numlist, n):
    answer = [(abs(n-i), i) for (a, i) in enumerate(numlist)]
    answer.sort(key = lambda x: (x[0], -x[1]))
    numlist = []
    for i in answer:
        numlist.append(i[1])
    return numlist

-------------------------------------------------

def solution(numlist, n):
    answer = sorted(numlist, key = lambda x: (abs(x-n), n-x))
    return answer