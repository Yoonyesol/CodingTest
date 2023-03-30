def solution(name, yearning, photo):
    answer = []
    dic = {name:yearning for name, yearning in zip(name, yearning)}
    for i in range(len(photo)):
        answer.append(0)
        for j in photo[i]:
            if j in dic.keys():
                answer[i] += dic[j]
    return answer