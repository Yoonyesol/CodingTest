T = int(input())
for test_case in range(1, T+1):
    n = list(input())
    min_num, max_num = ''.join(n), ''.join(n)
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if i == 0 and n[j] == "0":
                continue
            n[i], n[j] = n[j], n[i]
            min_num = min(min_num, ''.join(n))
            max_num = max(max_num, ''.join(n))
            n[i], n[j] = n[j], n[i]
    print("#{} {} {}".format(test_case, min_num, max_num))