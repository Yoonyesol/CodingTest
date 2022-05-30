def solution(s):
    word = s.split(" ")
    print(word)
    answer = []
    for i in range(len(word)):
        st = list(word[i])
        for j in range(len(st)):
            if j%2 == 0:
                answer.append(st[j].upper())
            else:
                answer.append(st[j].lower())
        answer.append(' ')
    return "".join(answer[:-1])