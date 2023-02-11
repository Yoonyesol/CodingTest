def solution(money):
    i = 0
    while money >= 5500:
        i += 1 
        money -= 5500
    return [i, money]

------------------------------

def solution(money):
    return [money//5500, money%5500]

------------------------------

def solution(money):
    return divmod(money, 5500)