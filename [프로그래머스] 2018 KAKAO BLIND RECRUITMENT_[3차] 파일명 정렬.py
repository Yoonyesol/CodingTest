def solution(files):
    answer = []
    head = ''
    number = ''
    tail = ''
    for i in files:
        for j in range(len(i)):
            if i[j].isdigit():
                head = i[:j]
                number = i[j:]
                for k in range(len(number)):
                    if number[k] in [" ", ".", "-"]:
                        tail = number[k:]
                        number = number[:k]
                        break
                answer.append([head, number, tail])
                head = ''
                number = ''
                tail = ''
                break
    answer = sorted(answer, key = lambda x:(x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]