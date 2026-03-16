# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
def inorder(node):
    # 왼쪽 자식노드가 있을 때만
    if node*2 <= N:
        inorder(node*2)
    print(tree[node], end='')
    # 오른쪽 자식노드가 있을 때만
    if node*2+1 <= N:
        inorder(node*2+1)
    # print(tree[node], end='')  후위순위

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for idx in range(1, N+1):
        info = input().split()
        tree[idx] = info[1]

    print(f'#{tc} ', end='')

    inorder(1)
    print()


# 1226. [S/W 문제해결 기본] 7일차 - 미로1
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    visited = [[0]*16 for _ in range(16)]

    q.append((r, c))
    visited[r][c] = 1

    # 큐가 빌때까지 돌아라
    while q:
        r, c = q.popleft()   # 도달이 가능한지 아닌지

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
                continue
            if graph[nr][nc] == 1 or visited[nr][nc]:
                continue
            if graph[nr][nc] == 3:
                return 1
            
            visited[nr][nc] = 1
            q.append((nr, nc))

    # 출구를 발견하지 못했을 때
    return 0

T = 10
for tc in range(1, T+1):
    input()
    graph = [list(map(int, input())) for _ in range(16)]
    r, c, goal_r, goal_c = -1, -1, -1, -1

    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                r = i
                c = j
            elif graph[i][j] == 3:
                goal_r = i
                goal_c = j

    answer = bfs(r, c)
    print(f'#{tc} {answer}')