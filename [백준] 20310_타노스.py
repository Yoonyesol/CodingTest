import sys
input=sys.stdin.readline
n = list(input().rstrip())
one = n.count('1') // 2 #1의 개수 세기
zero = n.count('0') // 2    #0의 개수 세기
cnt = 0 #1의 개수를 셀 변수
#1의 개수의 1/2만큼만 1을 앞에서부터 제거
for i in n:
    if i == "1":    
        if cnt == one:
            break
        cnt += 1
        n.remove("1")
cnt = 0
n = n[::-1] #n을 뒤집기
#0의 개수의 1/2만큼만 0을 뒤에서부터 제거
for i in n:
    if i == "0":
        if cnt == zero:
            break
        cnt += 1
        n.remove("0")
print(''.join(n[::-1])) #n을 다시 뒤집은 결과를 join으로 출력