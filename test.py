from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(tomato_1):
    q = deque()
    visited = [[0]*M for _ in range(N)]

    for r, c in tomato_1:
        visited[r][c] = 1
        q.append((r, c))

    distance = 0

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
    
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
    
                if nr<0 or nr>=N or nc<0 or nc>=M:
                    continue
                if visited[nr][nc] or arr[nr][nc] == -1:
                    continue
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
    
                visited[nr][nc] = 1
                q.append((nr, nc))
        if q:
            distance += 1
    return distance

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tomato_1 = []

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            tomato_1.append((r, c))

answer = bfs(tomato_1)

for i in arr:
    if 0 in i:
        print(-1)
        break
else:
    print(answer)