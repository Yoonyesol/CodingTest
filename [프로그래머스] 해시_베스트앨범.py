def solution(genres, plays):
    answer = []
    dic = {g:[] for g in set(genres)}
    for index, (genre, play) in enumerate(zip(genres, plays)):
        dic[genre].append([index, play])
    genre_sort = sorted(dic.keys(), key=lambda x:sum(map(lambda y:y[1], dic[x])), reverse=True)
    for g in genre_sort:
        temp = [i[0] for i in sorted(dic[g], key=lambda x:(x[1], -x[0]), reverse=True)]
        answer += temp[:min(2, len(temp))]
    return answer

----------------------

def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {genre:0 for genre in set(genres)}
    for idx, (i, j) in enumerate(zip(genres, plays)):
        dic1[idx] = (i, j)
        dic2[i] += j
    dic1 = sorted(dic1.items(), key = lambda x:-x[1][1])
    dic2 = sorted(dic2.items(), key = lambda x:-x[1])
    for i in dic2:
        cnt = 0
        for j in dic1:
            if j[1][0] == i[0]:
                answer.append(j[0])
                cnt += 1
            if cnt == 2:
                break
    return answer