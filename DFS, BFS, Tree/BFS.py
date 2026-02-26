# 백준 7576. 토마토
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


# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
from collections import deque
def bfs(S):
    q = deque()
    visited = [0] * 100

    visited[S] = 1
    q.append(S)

    while q:
        for _ in range(len(q)):
            node = q.popleft()

            if node == 99:
                return 1
            for next_node in adj_list[node]:
                if visited[next_node]:
                    continue

                visited[next_node] = 1
                q.append(next_node)

    return 0

T = 10
for tc in range(1, T+1):
    _, N = map(int, input().split())
    numbers = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]

    for i in range(0, len(numbers), 2):
        a, b = numbers[i], numbers[i+1]
        adj_list[a].append(b)

    answer = bfs(0)
    print(f'#{tc} {answer}')


# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
from collections import deque

def bfs(S):   # 거리를 리턴
    q = deque()
    visited = [0]*(V+1)

    visited[S] = 1
    q.append(S)

    distance = 0

    while q:
        for _ in range(len(q)):   # 현재 같은 층에 있는 얘들을 다 처리할 때까지
            node = q.popleft()

            if node == G:
                return distance
            
            for next_node in adj_list[node]:
                if visited[next_node]:
                    continue

                visited[next_node] = 1
                q.append(next_node) 
                
        distance += 1   # 한 층을 다 돌았으니 거리를 1 늘림

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    S, G = map(int, input().split())

    answer = bfs(S)
    print(f'#{tc} {answer}')


# 1226. [S/W 문제해결 기본] 7일차 - 미로1
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    visited = [[0]*16 for _ in range(16)]

    visited[r][c] = 1
    q.append((r, c))

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0>nr or nr>=16 or 0>nc or nc>=16:
                continue
            if visited[nr][nc] or arr[nr][nc] == 1:
                continue
            if arr[nr][nc] == 3:
                return 1
            
            visited[nr][nc] = 1
            q.append((nr, nc))

    return 0

T = 10
for tc in range(1, T+1):
    input()
    arr = [list(map(int, input())) for _ in range(16)]

    r, c, goal_r, goal_c = -1, -1, -1, -1

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                r = i
                c = j
            elif arr[i][j] == 3:
                goal_r = i
                goal_c = j

    answer = bfs(r, c)
    print(f'#{tc} {answer}')


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