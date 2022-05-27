def solution(array, commands):
    a = []
    l = []
    for i in commands:
        a = array[i[0]-1:i[1]]
        a.sort()
        l.append(a[i[2]-1])
    return l