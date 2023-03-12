def solution(lines):
    answer = 0
    setArr = [0 for _ in range(200)]
    for i in lines:
        for j in range(i[0] ,i[1]):
            setArr[j + 100] += 1
    return setArr.count(2) + setArr.count(3)