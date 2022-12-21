def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)   #인덱스를 원소//2번 반복(대칭이 되어야 하므로 원소값은 짝수가 되어야 함)
    answer += str(0)
    for j in range(len(food)-1, 0, -1): #대칭을 만들기 위해 인덱스 뒤에서부터 동일하게 반복
        answer += str(j) * (food[j] // 2)
    return answer