T = int(input())
for test_case in range(1, T+1):
    _, k = input().split()
    arr = list(input().split())
    stack = [[] for _ in range(10)]
    dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6,
           "SVN":7, "EGT":8, "NIN":9}
    for i in arr:
        stack[dic[i]].append(i)

    print("#{}".format(test_case))
    for i in stack:
        for j in i:
            print(j, end=" ")