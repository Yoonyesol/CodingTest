def solution(id_list, report, k): 
    answer = []
    singo = {i:0 for i in id_list}
    report = list(set(report))  #중복 제거
    stop = []
    #신고된 유저 카운트
    for i in range(len(report)):
        report[i] = report[i].split()   
        singo[report[i][1]] += 1
    #정지된 유저
    for j in singo.keys():
        if singo[j] >= k:
            stop.append(j)
    #정지된 유저를 신고한 유저
    singo = {i:0 for i in id_list}
    for k in report:
        if k[1] in stop:
            singo[k[0]] += 1
    return list(singo.values())