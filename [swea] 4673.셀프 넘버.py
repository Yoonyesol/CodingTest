temp = [i for i in range(1, 10000)]
arr = set()
for i in temp:
    num = i
    for j in str(i):
        num += int(j)
    arr.add(num)
for i in sorted(set(temp)-arr):
    print(i)


---------------------------------


temp = [i for i in range(1, 10000)]
arr = set()
for i in temp:
    num = i
    num2 = i
    while num2 > 0:
        num2, n = divmod(num2, 10)
        num += n
    arr.add(num)
for i in sorted(set(temp)-arr):
    print(i)