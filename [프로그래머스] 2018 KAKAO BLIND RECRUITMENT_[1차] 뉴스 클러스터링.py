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