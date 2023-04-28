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