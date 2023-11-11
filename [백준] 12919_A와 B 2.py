import sys
input=sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def dfs(target):
    global ans
    if s == target: #t가 s와 동일하다면
        ans = 1 #문자열을 만들 수 있으므로 ans=1
        return  #종료
    if len(target) == 0:    #마지막까지 문자열을 만들 수 없었다면, ans값을 지정하지 않음
        return  #종료
    if target[-1] == 'A':   #A를 마지막에 추가했기 때문에
        dfs(target[:-1])    #가장 마지막 A를 삭제하고 재귀
    if target[0] == 'B':    #B를 마지막에 추가한 뒤 문자열을 뒤집었기 때문에, 가장 첫번째 글자가 B라면
        dfs(target[1:][::-1])   #B추가 문자열 역순으로 재귀

ans = 0
dfs(t)
print(ans)