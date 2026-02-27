# 백준 2573. 빙산
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start):
    q = deque()
    visited = [[0]*M for _ in range(N)]

    for r, c in start:
        visited[r][c] = 1
        q.append((r, c))
    
    count = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if arr[nr][nc] != 0:
                q.append((nr, nc))
            if arr[nr][nc] == 0:
                count += 1   # 빙산 주위의 0의 수 세기
                visited[nr][nc] = 1
                q.append((nr, nc))
            
        if arr[r][c] <= count:   # 빙산 녹기
            arr[r][c] = 0
        else:
            arr[r][c] -= count
        count = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

start = []
year = 0
while True:
    cnt = 0   # 덩어리
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 0 :
                start.append((r, c))
                answer = bfs(start)   # 한 덩어리를 돌기
                cnt += 1
    year += 1
    
    if cnt >= 2:
        print(year)
        break
    if cnt == 0:
        print(0)
        break
