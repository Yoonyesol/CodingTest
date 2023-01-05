def solution(survey, choices):
    # [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    test_set = [[0, 0], [0, 0], [0, 0], [0, 0]] 
    answer = 'RCJA'
    for i, j in zip(survey, choices):
        if i == "TR" or i == "RT":
            if i == "TR":
                j = 8-j
            if j < 4:   #R형
                test_set[0][0] += 4-j
            elif j > 4: #T형
                test_set[0][1] += j%4
        if i == "CF" or i == "FC":
            if i == "FC":
                j = 8-j
            if j < 4:   
                test_set[1][0] += 4-j
            elif j > 4: 
                test_set[1][1] += j%4
        if i == "JM" or i == "MJ":
            if i == "MJ":
                j = 8-j
            if j < 4:  
                test_set[2][0] += 4-j
            elif j > 4: 
                test_set[2][1] += j%4
        if i == "AN" or i == "NA":
            if i == "NA":
                j = 8-j
            if j < 4: 
                test_set[3][0] += 4-j
            elif j > 4: 
                test_set[3][1] += j%4
    if test_set[0][0] < test_set[0][1]:
        answer = answer.replace("R", "T")
    if test_set[1][0] < test_set[1][1]:
        answer = answer.replace("C", "F")
    if test_set[2][0] < test_set[2][1]:
        answer = answer.replace("J", "M")
    if test_set[3][0] < test_set[3][1]:
        answer = answer.replace("A", "N")
    return answer