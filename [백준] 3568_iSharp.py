import sys
input=sys.stdin.readline
# 세 변수 입력받은 뒤 ";" 제외, 입력받은 문자열을 "  " 기준으로 슬라이싱
a = input().rstrip()[:-1].split(" ")
type_list = [a[0]] * (len(a) - 1)
a = a[1:]
for i in range(len(a)):
    #뒤부터 탐색
    for j in a[i][::-1]:
        if j == ",":
            a[i] = a[i][:-1]
        elif j == "&":
            type_list[i]+= "&"
            a[i] = a[i][:-1]
        elif j == "]":
            type_list[i] += "[]"
            a[i] = a[i][:-2]
        elif j == "*":
            type_list[i] += "*"
            a[i] = a[i][:-1]
        elif j.isalpha():
            break
for i, j in zip(type_list, a):
    print(str(i), str(j), end="")
    print(";")