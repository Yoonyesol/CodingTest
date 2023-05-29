from itertools import permutations
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    aset = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            aset.add(int("".join(j)))
    for a in aset:
        if a in [0, 1]: continue
        for k in range(2, int(a**(0.5))+1):
            if a % k == 0:
                break
        else:
            answer += 1
    return answer