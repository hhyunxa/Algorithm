from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[r][c] == 0 and visited[r][c]:
                continue
            if arr[r][c] == 1:
                r = i
                c = j

    visited[r][c] = 1
    q.append((r, c))

    total_count = 0
    count = 0
    lists = []

    while q :
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if arr[nr][nc] == 0 and visited[nr][nc]:
                continue
            if arr[nr][nc] == 1:
                count += 1
            lists.append(count)

            visited[nr][nc] = 1
            q.append((nr, nc))

            total_count += 1
            print(total_count)
            new_lists = sorted(lists)
            print(new_lists, end='')
            print()

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
r = 0
c = 0
bfs(r, c)