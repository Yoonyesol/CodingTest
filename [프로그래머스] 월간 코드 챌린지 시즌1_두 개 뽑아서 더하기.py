def solution(numbers):
    sum = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum.add(numbers[i]+numbers[j])
    sum = list(sum)
    sum.sort()
    return sum