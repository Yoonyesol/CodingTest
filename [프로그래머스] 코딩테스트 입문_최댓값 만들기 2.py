def solution(numbers):
    numbers.sort()
    plus = numbers[-1] * numbers[-2]
    if numbers[0] < 0 and numbers[1] < 0:
        if plus < (numbers[0] * numbers[1]):    
            return numbers[0] * numbers[1]
    return plus