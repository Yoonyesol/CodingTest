def solution(str1, str2):
    str1Arr = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2Arr = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    str1Dic = {i:str1Arr.count(i) for i in str1Arr}
    str2Dic = {i:str2Arr.count(i) for i in str2Arr}
    kyo, hap = 0, 0
    for i in str1Dic.keys():
        if i in str2Dic.keys():
            kyo += min(str1Dic[i], str2Dic[i])
            hap += max(str1Dic[i], str2Dic[i])
        if i not in str2Dic.keys():
            hap += str1Dic[i]
    for j in str2Dic.keys():
        if j not in str1Dic.keys():
            hap += str2Dic[j]
    return 65536 if hap == 0 else int(65536 * (kyo / hap))

--------------------------------

def solution(str1, str2):
    # 두글자씩 쌍 만들기. 알파벳이 아닌 글자가 포함된 경우 pass
    str1Arr = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2Arr = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    # str1Arr, str1Arr 각 원소의 갯수 카운트
    str1Set = set(str1Arr)
    str2Set = set(str2Arr)
    kyo, hap = 0, 0
    for i in str1Set:
        if i in str2Arr:
            kyo += min(str1Arr.count(i), str2Arr.count(i))  # 동일원소 존재 시 교집합
            hap += max(str1Arr.count(i), str2Arr.count(i))  # 동일원소 존재 시 합집합
        else: #str1 단독
            hap += str1Arr.count(i)
    for j in str2Set:
        if j not in str1Arr: #str2 단독
            hap += str2Arr.count(j)
    # zero divide 에러 피하기 위해 hap == 0일 경우 예외 처리
    return 65536 if hap == 0 else int(65536 * (kyo / hap))