def solution(nums):
    pick = len(nums) / 2    #뽑기 갯수
    s = set(nums)           #중복 제거
    l = list(s)             #중복 제거한 리스트
    return min(pick, len(l)) #둘 중 더 작은 수 리턴