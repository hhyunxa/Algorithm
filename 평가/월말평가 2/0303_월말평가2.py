# 1
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
                            arr[nr][nc] = 3
                        nr = nr + dr[d]
                        nc = nc + dc[d]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1
    
    print(f'#{tc} {count}')


# 2
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    visited[r][c] = 1
    q.append((r, c))

    size = 1   # 칸의 개수
    gold = arr[r][c]   # 금의 총량

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] or arr[nr][nc] == 0:
                continue
            if arr[nr][nc] != 0 :
                size += 1
                gold += arr[nr][nc]
            visited[nr][nc] = 1
            q.append((nr, nc))

    sums.append((gold, size))

T = int(input())
for tc in range(1, T=1):
    N = int(input())
    arr = [list(map(int, input().split()))]
    visited = [[0]*N for _ in range(N)]

    sums = []   

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                r = i
                c = j
                bfs(r, c)

    ans_gold = sums[0][0]
    ans_size = sums[0][1]

    for i in range(1, len(sums)):
        curr_gold = sums[i][0]
        curr_size = sums[i][1]

        if curr_gold > ans_gold:
            ans_gold = curr_gold
            ans_size = curr_size
        elif curr_gold == ans_gold:
            if curr_size < ans_size:
                ans_size = curr_size

    print(f"#{tc} {ans_gold} {ans_size}")
