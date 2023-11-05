import sys
input=sys.stdin.readline

r, c, n = map(int, input().split())
init_arr = [list(input().rstrip()) for _ in range(r)]
o_arr = [["O" for _ in range(c)] for _ in range(r)]
ans = []

def bomb(arr):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    #현재 배열을 폭탄이 설치된 배열로 초기화한 뒤 터뜨릴 부분만 터뜨리기
    cur_arr = o_arr
    #전체 배열을 순회
    for x in range(r):
        for y in range(c):
            if arr[x][y] == 'O':   #폭탄이 존재하는 경우
                cur_arr[x][y] = '.'    #해당 위치 폭탄 터뜨리기
                for i in range(4):  #상하좌우 살피기
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= r or nx < 0 or ny >= c or ny < 0:
                        continue
                    cur_arr[nx][ny] = '.'   #폭탄이 터짐
    return cur_arr

if n == 1:  #1초 후
    ans = init_arr  #초기 상태
elif n % 2 == 0:
   ans = o_arr  #폭탄이 설치되지 않은 모든 칸에 폭탄 설치(모든 칸에 폭탄)
elif n % 4 == 3:    #3초 전(초기 상태 폭탄) 폭탄 터짐
    ans = bomb(init_arr)
elif n % 4 == 1:    #5,9,13...은 폭탄이 두 번 터져야 한다
    ans = bomb(init_arr)    #초기 상태에서 3초가 지난 후의 상태
    ans = bomb(ans) #그 상태에서 다시 3초가 지난 후의 상태

for i in ans:
    print("".join(i))