# 5656. [모의 SW 역량테스트] 벽돌 깨기
import copy
from collections import deque

def dfs(count):
    if count == N:
        arr2 = copy.deepcopy(arr)
        cnt = update(arr2)
        result.append(cnt)
        
        return
    else:
        for i in range(W):
            pick.append(i)
            dfs(count+1)
            pick.pop()

def update(ar):
    for c in pick:
        for r in range(H):
            if ar[r][c] != 0:
                if ar[r][c] > 1:
                    ar = bfs(r, c, ar)
                else:
                    ar[r][c] = 0
                break
        for r in range(1, H):
            for c in range(W):
                if ar[r][c] == 0 and ar[r-1][c] != 0:
                    
                    for r2 in range(r, 0, -1):
                        ar[r2][c] = copy.deepcopy(ar[r2-1][c])
                    ar[0][c] = 0
                
    cnt = 0
    for r in ar:
        cnt = cnt + (W - r.count(0))
    return cnt
        
def bfs(rr, cc, ar):
    q = deque()
    visited = [[0]*W for _ in range(H)]

    visited[rr][cc] = 1
    q.append((rr, cc))

    while q:
        r, c = q.popleft()
        num = ar[r][c]
        ar[r][c] = 0

        for d in range(4):
            for n in range(1, num):
                nr = r + dr[d]*n
                nc = c + dc[d]*n

                if 0<=nr<H and 0<=nc<W and visited[nr][nc] == 0:
                    if ar[nr][nc] == 1:
                        ar[nr][nc] = 0
                    elif ar[nr][nc] > 1:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        
    ar[rr][cc] = 0
    return ar

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    
    pick = []
    result = []
    dfs(0)
    print(f'#{tc} {min(result)}')

