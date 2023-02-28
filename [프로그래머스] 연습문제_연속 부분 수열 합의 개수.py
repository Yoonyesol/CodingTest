def solution(elements):
    arr = [i for i in elements] #길이1
    arr.append(sum(elements))   #길이n
    for i in range(2, len(elements)):  #길이 2 ~ n-1개의 부분수열
        for j in range(len(elements)):
            hap = 0
            if i + j > len(elements):	#배열의 인덱스를 벗어날 경우
                hap += sum(elements[j:len(elements)])
                hap += sum(elements[0:(i + j)%len(elements)])
            else:
                hap += sum(elements[j:i+j])
            arr.append(hap)	#구한 합을 arr에 추가
    return len(set(arr))	#중복제거 후 출력