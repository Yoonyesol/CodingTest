T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    code = []
    dic = {"0001101":0, "0011001":1, "0010011":2, "0111101":3,
           "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7,
           "0110111": 8, "0001011": 9}
    code_arr = []
    for _ in range(n):
        a = list(map(int, input()))
        if 1 in a:
            code = a[::-1]
    j = 0
    while j < len(code):
        arr = ''.join(map(str, code[j:j+7][::-1]))
        if arr[-1]=="1" and arr in dic.keys():
            code_arr.insert(0, dic[arr])
            j+=7
        else:
            j+=1
    a = sum(code_arr[0::2])
    b = sum(code_arr[1::2])
    if (a*3+b)%10==0:
        ans = a+b
    else:
        ans = 0
    print("#{} {}".format(test_case, ans))
