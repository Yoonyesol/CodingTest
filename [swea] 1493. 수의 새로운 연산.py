def xyToNum(num):
    p_cnt = 0
    xyArr = [0, 0]
    total_p = 0
    num2 = num
    while True:
        p_cnt += 1
        total_p += p_cnt
        num2 -= p_cnt
        if num2 <= 0:
            xyArr[0] = p_cnt-(total_p-num)
            xyArr[1] = 1+(total_p-num)
            break
    return xyArr
def numToXy(x, y):
    group = (x+y)-1
    total = 0
    for i in range(1, group+1):
        total += i
    return total - (y-1)
T = int(input())
for test_case in range(1, T+1):
    p, q = map(int, input().split())
    a = xyToNum(p)
    b = xyToNum(q)
    x = a[0] + b[0]
    y = a[1] + b[1]
    print("#{} {}".format(test_case, numToXy(x, y)))