def solution(s):
    answer = []
    s = s[2:-2].split("},{")    #['1,2,3', '2,1', '1,2,4,3', '2']
    s.sort(key=len) #['2', '2,1', '1,2,3', '1,2,4,3']
    for i in s:
        s_list = i.split(",")
        for j in s_list:    #원소가 한 개인 집합부터 중복을 피해 리스트에 넣는다.
            if int(j) not in answer:
                answer.append(int(j))
    return answer