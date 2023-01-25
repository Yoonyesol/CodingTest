def solution(s):
    answer = []
    s_list = s.split()
    for i in s_list:
        if i == "Z" and answer:
            answer.pop()
        elif i != "Z":
            answer.append(int(i))
    return sum(answer)