import sys

n = int(sys.stdin.readline())
num_list = [0]*10001

#입력받을 때마다 리스트의 해당 인덱스 원소값 1씩 추가
for _ in range(n):
  num = int(input())
  num_list[num] += 1 

#리스트를 돌며 리스트의 원소값만큼 인덱스 값을 출력
for i in range(1, len(num_list)):
  if num_list[i] != 0:
    for j in range(num_list[i]):
      print(i)

