def solution(sides):
    return len([i for i in range(max(sides) - min(sides) + 1, max(sides) + 1)]) + len([i for i in range(max(sides) + 1, sum(sides))])
