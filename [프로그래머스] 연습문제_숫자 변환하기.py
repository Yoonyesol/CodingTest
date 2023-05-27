def solution(x, y, n):
    answer = 0
    ans = set()
    ans.add(x)
    
    while ans:
        if y in ans:
            return answer
        temp = set()
        for i in ans:
            if i+n <= y:
                temp.add(i+n)
            if i*2 <= y:
                temp.add(i*2)
            if i*3 <= y:
                temp.add(i*3)
        ans = temp
        answer += 1
    return -1