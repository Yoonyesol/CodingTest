T = int(input())
for test_case in range(1, T + 1):
	sum = 0
	a = list(map(int, input().split()))
	for i in a:
		if i % 2 != 0:
			sum = sum + i
	print("#{} {}".format(test_case, sum))