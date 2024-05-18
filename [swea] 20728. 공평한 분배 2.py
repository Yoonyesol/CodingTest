tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()  #오름차순 정렬

    min_gap = 1e9   #차이의 최솟값
    for i in range(n-k+1):  #0~k...번째까지의 인덱스값만 모아서 부분 배열 생성
        gap = arr[i+k-1] - arr[i]   #부분 배열 내 최댓값-최솟값
        min_gap = min(gap, min_gap)

    print("#{} {}".format(t+1, min_gap))