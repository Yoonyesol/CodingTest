def solution(dartResult):
    temp = []
    for i in range(len(dartResult)):
        if dartResult[i] == '1':
            if dartResult[i+1] == "0":
                temp.append(10)
            else:
                temp.append(1)
        if dartResult[i] == '0':
            if dartResult[i-1] != "1":
                temp.append(0)
        if dartResult[i] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            temp.append(int(dartResult[i]))
        if dartResult[i] == "D":
            temp[-1] **= 2
        if dartResult[i] == "T":
            temp[-1] **= 3
        if dartResult[i] == "*":
            temp[-1] *= 2
            if len(temp) >= 2:
                temp[-2] *= 2
        if dartResult[i] == "#":
            temp[-1] *= (-1)
    return sum(temp)