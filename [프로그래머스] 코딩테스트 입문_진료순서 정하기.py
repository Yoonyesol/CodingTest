def solution(emergency):
    answer = [(items, idx+1) for (idx, items) in enumerate(sorted(emergency, reverse=True))]
    arr = []
    for i in emergency:
        for j in answer:
            if i == j[0]:
                arr.append(j[1])
    return arr

-----------------------------

def solution(emergency):
    return [sorted(emergency, reverse=True).index(i)+1 for i in emergency]

------------------------------

def solution(emergency):
    arr = []
    dic = {items:idx + 1  for idx,items in enumerate(sorted(emergency, reverse=True))}
    for i in emergency:
        arr.append(dic[i])
    return arr