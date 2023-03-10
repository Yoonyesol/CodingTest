def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, j in zip(alpha, range(10)):
        numbers = numbers.replace(i, str(j))
    return int(numbers)

---------------------------

def solution(numbers):
    answer = 0
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in num:
        if i in numbers:
            numbers = numbers.replace(i, str(num.index(i)))
    return int(numbers)