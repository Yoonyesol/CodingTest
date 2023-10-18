def solution(myString, pat):
    answer = 0
    if pat.replace("A", "o").replace("B", "x") in myString.replace("A", "x").replace("B", "o"):
        answer = 1
    return answer