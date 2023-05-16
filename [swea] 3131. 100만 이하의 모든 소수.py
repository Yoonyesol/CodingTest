import math
sosu = [0 for _ in range(1000001)]
for i in range(2, int(math.sqrt(1000001))+1):
    if sosu[i] == 1:
        continue
    for j in range(i*2, 1000001, i):
        sosu[j] = 1

for i in range(2, 1000001):
    if sosu[i] == 0:
        print(i, end=" ")