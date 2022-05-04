def solution(absolutes, signs):
    arr = []
    for i in range(len(absolutes)):
        if signs[i]:
            arr.append(absolutes[i])
        else: 
            arr.append(absolutes[i]*(-1))
    return sum(arr)