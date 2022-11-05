for test_case in range(1, 11):
    a = int(input())
    n = list(map(int, input().split()))
    sum = 0
    for i in range(a-5):
        arr = n[i:i+5]
        middle = arr[2]
        arr.remove(middle)
        if middle - max(arr) > 0:
            sum = sum + (middle - max(arr))
    arr = n[-1:-6:-1]
    middle = arr[2]
    arr.remove(middle)
    if middle - max(arr) > 0:
    	sum = sum + (middle - max(arr))
    print("#{} {}".format(test_case, sum))