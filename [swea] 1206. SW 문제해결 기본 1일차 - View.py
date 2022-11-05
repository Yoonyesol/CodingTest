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


-----------------------------------------------


for test_case in range(1, 11):
    a = int(input())
    n = list(map(int, input().split()))
    sum = 0
    for i in range(2, a-2):
        view1 = n[i]-n[i-2]
        view2 = n[i]-n[i-1]
        view3 = n[i]-n[i+1]
        view4 = n[i]-n[i+2]
        if view1 > 0 and view2 > 0 and view3 > 0 and view4 > 0 :
            sum = sum + min(view1, view2, view3, view4)
    print("#{} {}".format(test_case, sum))