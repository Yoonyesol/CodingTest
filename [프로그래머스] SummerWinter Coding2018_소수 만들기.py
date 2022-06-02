import itertools #하나의 리스트에서 모든 조합을 구하기, product: 여러개의 리스트에서 모든 조합 구하기
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    comb_arr = list(itertools.combinations(nums, 3))
    for i in comb_arr:
        if is_prime(sum(i)):
            cnt += 1
    return cnt