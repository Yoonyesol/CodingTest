import sys
input=sys.stdin.readline

number = list(map(str, input().rstrip()))

i = 1   #비교할 수
pointer = 0 #number배열을 가리킬 포인터
while pointer < len(number):    #포인터가 number 배열 끝까지 갈 때까지 반복
    writing = str(i)    #비교할 수를 문자열로 변경
    for j in range(len(writing)):   #비교할 수를 한글자씩 비교
        if pointer >= len(number):  #포인터가 number 배열 끝까지 가면 종료
            break
        if writing[j] == number[pointer]:   #첫자리 수부터 비교. 동일하면 다음 자리수도 동일한지 확인하기 위해 포인터+1
            pointer += 1
    i += 1  #1씩 늘려가며 모든 가능한 수를 확인
print(i-1)  #배열의 모든 원소를 확인하면 그 결과를 출력. 마지막으로 비교수를 늘려놨기 때문에 -1의 값을 출력