def solution(num, total):
    answer = [0] * num
    mid = total // num
    answer[(num-1)//2] = mid
    for i in range((num-1)//2+1):
        answer[(num-1)//2-i] = mid - i
    j = 1
    for i in range((num-1)//2+1, num):
        answer[i] = mid + j
        j += 1
    return answer