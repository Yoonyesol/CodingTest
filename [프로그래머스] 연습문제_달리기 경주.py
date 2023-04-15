def solution(players, callings):
    dic = {player:idx+1 for idx, player in enumerate(players)}
    dic2 = {idx+1:player for idx, player in enumerate(players)}
    for i in callings:
        a = dic[i]  #이름을 불린 선수의 현재 등수
        b = dic2[a-1]  #이름을 불린 선수의 전 등수의 선수
        
        dic[b] = a #전 등수 선수의 등수+1(밀려남)
        dic[i] = a-1 #이름을 불린 선수의 등수-1(이전 선수 추월)
        
        dic2[a] = b #이름을 불린 선수의 등수에는 전 등수의 선수를 대입
        dic2[a-1] = i    #전 선수의 등수에는 이름을 불린 선수를 대입
    return list(dic2.values())