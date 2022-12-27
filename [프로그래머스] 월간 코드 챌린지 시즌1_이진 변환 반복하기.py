def solution(s):
    binCnt = 0
    cnt = 0
    answer = []
    while s != "1":
        cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:] 	#앞 부분 '0b' 제거
        binCnt += 1
    answer = [binCnt, cnt]
    return answer