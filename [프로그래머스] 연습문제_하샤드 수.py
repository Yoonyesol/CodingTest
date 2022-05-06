def solution(x):
    sum = x//10000 + x%10000//1000 + x%1000//100 + x%100//10 + x%10
    return True if x%sum == 0 else False