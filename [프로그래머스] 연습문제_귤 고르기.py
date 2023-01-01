import collections
def solution(k, tangerine):
    answer = 0
    i = 0
    ls = collections.Counter(tangerine).most_common()
    for i in range(len(ls)):
        if k <= 0:
            break
        k -= ls[i][1]
        answer += 1
    return answer