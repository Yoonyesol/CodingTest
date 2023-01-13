def solution(my_string):
    answer = ''
    for i in my_string:
        if not answer: 
            answer += i
        else:
            if i in answer:
                continue
            else:
                answer += i
    return answer