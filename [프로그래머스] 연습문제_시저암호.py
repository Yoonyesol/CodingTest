def solution(s, n):
    sList = list(s)		#sList에 입력받은 글자를 list형태로 잘라서 저장
    for i in range(len(sList)):	#sList 길이만큼 반복
        if sList[i].isupper():	#리스트에 든 글자가 대문자인 경우
            sList[i] = chr((ord(sList[i])-ord('A') +n) %26+ord('A'))
        elif sList[i].islower():	#소문자인 경우
            sList[i] = chr((ord(sList[i])-ord('a') +n) %26+ord('a'))
    return ("".join(sList))	#리스트의s 글자를 합쳐 하나의 문자열로 return