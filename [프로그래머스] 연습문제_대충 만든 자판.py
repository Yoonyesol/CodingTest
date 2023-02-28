def solution(keymap, targets):
    answer = [0] * len(targets)
    dic = {}
    for i in keymap:
        for j in i:
            if j in dic:
                if dic[j] > i.index(j)+1:
                    dic[j] = i.index(j)+1
            else:
                dic[j] = i.index(j)+1
    for i in range(len(targets)):
        for j in targets[i]:
            if j in dic:
                answer[i] += dic[j]
            else:
                answer[i] = -1
                break
    return answer