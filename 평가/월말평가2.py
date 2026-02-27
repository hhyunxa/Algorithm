# 23795. 우주 괴물
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    while 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc] == 1:
                            break
                        if arr[nr][nc] == 0:
                            arr[nr][nc] = 1
                        nr = nr + dr[d]
                        nc = nc + dc[d]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1
    
    print(f'#{tc} {count}')

# 백준 2667. 단지번호붙이기
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()

    visited[r][c] = 1
    q.append((r, c))

    count = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] or arr[nr][nc] == 0:
                continue
            if arr[nr][nc] == 1:
                count += 1

            visited[nr][nc] = 1
            q.append((nr, nc))

    sums.append(count)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
sums = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            r = i
            c = j
            answer = bfs(r, c)

print(len(sums))
for a in sums:
    print(a)


# 스택의 특성과 과정 -> 후입선출 LIFO
# 큐의 특성과 과정 -> 선입선출 FIFO
# 트리 -> 전위, 중위, 후위 순회, 트리의 특성