from collections import Counter 
def solution(topping):
    answer = 0
    toppingDic = Counter(topping)
    toppingSet = set()
    for i in topping:
        toppingDic[i] -= 1
        toppingSet.add(i)
        if toppingDic[i] == 0:
            toppingDic.pop(i)
        if len(toppingDic) == len(toppingSet):
               answer += 1
    return answer