def solution(a, b, c, d):
    arr = [a, b, c, d]
    dic = {i: 0 for i in set(arr)}
    for i in arr:
        dic[i] += 1 
    dic = sorted(dic.items(), key=lambda x:(-x[1],x[0]))
    if len(dic) == 1:
        return dic[0][0]*1111
    elif len(dic) == 2:
        if dic[0][1] == 3 and dic[1][1] == 1:
            return (10*dic[0][0]+dic[1][0])**2
        if dic[0][1] == 2 and dic[1][1] == 2:
            return ((dic[0][0]+dic[1][0])*abs(dic[0][0]-dic[1][0]))
    elif len(dic) == 3:
        return (dic[1][0]*dic[2][0])
    elif len(dic) == 4:
        return dic[0][0]