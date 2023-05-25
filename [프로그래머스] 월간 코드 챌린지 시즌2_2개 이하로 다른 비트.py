def solution(numbers):
    answer = []
    for num in numbers:
        numb = list('0'+bin(num)[2:])
        idx = ''.join(numb).rfind('0')
        numb[idx] = '1'
        if num % 2 == 1:
            numb[idx+1] = '0'
        answer.append(int(''.join(numb), 2))
    return answer