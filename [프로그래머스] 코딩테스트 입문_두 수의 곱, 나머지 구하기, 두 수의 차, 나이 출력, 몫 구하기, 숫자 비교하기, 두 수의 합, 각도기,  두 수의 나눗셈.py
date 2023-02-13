두 수의 곱
def solution(num1, num2):
    return num1 * num2

--------------------------------

나머지 구하기
def solution(num1, num2):
    return num1 % num2

--------------------------------

두 수의 차
def solution(num1, num2):
    return num1 - num2

--------------------------------

나이 출력
def solution(age):
    return 2022 - age + 1

--------------------------------

몫 구하기
def solution(num1, num2):
    return num1 // num2

--------------------------------

숫자 비교하기
def solution(num1, num2):
    return 1 if num1 == num2 else -1

--------------------------------

두 수의 합
def solution(num1, num2):
    return num1 + num2

--------------------------------

각도기
def solution(angle):
    answer = 0
    if 0 < angle and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle and angle < 180:
        return 3
    elif angle == 180:
        return 4

--------------------------------

두 수의 나눗셈
import math
def solution(num1, num2):
    return math.floor(num1 / num2 * 1000)
