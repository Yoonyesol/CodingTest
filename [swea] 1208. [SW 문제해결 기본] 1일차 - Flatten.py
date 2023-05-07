T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump = int(input())
    height = list(map(int, input().split()))
    for i in range(dump):
        if height[height.index(min(height))] == height[height.index(max(height))]:
            break
        height[height.index(min(height))] += 1
        height[height.index(max(height))] -= 1
    print("#{} {}".format(test_case, max(height) - min(height)))

------------------------------------------

23.05.07

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while dump:
        boxes = sorted(boxes)
        boxes[-1] = boxes[-1] - 1
        boxes[0] = boxes[0] + 1
        dump -= 1
    print("#{} {}".format(test_case, max(boxes)-min(boxes)))