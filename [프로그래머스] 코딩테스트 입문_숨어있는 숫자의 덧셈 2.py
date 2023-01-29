def solution(my_string):
    answer = []
    temp = ''
    for i in range(len(my_string)):
        if not my_string[i].isalpha():
            temp += my_string[i]
        else:
            if temp:
                answer.append(int(temp))
                temp = ''
    if temp:
        answer.append(int(temp))
    return sum(answer)