def solution(price, money, count):
    sum = 0
    for i in range(count):
        sum += (i+1)*price
    return abs(sum - money) if money < sum else 0