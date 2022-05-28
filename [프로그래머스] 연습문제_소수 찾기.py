import math
def solution(n):
    arr = [True for i in range(n+1)]    #n개의 배열을 True로 초기화
    #에라토스테네스의 체, 0 ~ 제곱근까지의 수 확인
    for i in range(2, int(math.sqrt(n))+1): 
        if arr[i] == True:
            j = 2
            #가장 작은 소수의 배수인 경우 소수가 아니므로, false로 업데이트
            while i*j <= n:
                arr[i*j] = False
                j+=1
    return arr[2:].count(True)  #0, 1 제외하고 true인 경우(소수) count