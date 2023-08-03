import sys
input=sys.stdin.readline
n = int(input())
word = list(input().rstrip())   #첫 단어
ans = 0 #비슷한 단어의 개수를 카운팅하는 변수
for _ in range(n-1):
    compare = word.copy()   #첫 단어를 카피해서 새로운 변수에 저장
    a = list(input().rstrip())  #비교할 단어 입력받기
    cnt = 0 #두 단어의 글자 중 다른 것이 있다면 카운팅하는 변수
    for i in a: #비교할 단어의 한 글자씩 비교
        if i in compare:    #첫 단어 안에 비교할 단어의 글자가 포함되어 있다면
            compare.remove(i)   #해당 글자를 삭제
        else:   #포함되어 있지 않다면
            cnt += 1    #cnt 카운팅
    #다른 글자가 2개 미만이고, 동일한 글자를 모두 삭제하고 남은 글자가 2개 미만이라면, 비슷한 단어
    if cnt < 2 and len(compare) < 2:
        ans += 1
print(ans)