import math
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    mid = math.ceil(n/2)
    dec = list(input().split())
    dec1 = dec[:mid]
    dec2 = dec[mid:]
    arr = []
    while dec1 or dec2:
        if dec1:
            arr.append(dec1.pop(0))
        if dec2:
            arr.append(dec2.pop(0))
    print("#{} {}".format(test_case, ' '.join(arr)))