def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, j in zip(alpha, range(10)):
        numbers = numbers.replace(i, str(j))
    return int(numbers)