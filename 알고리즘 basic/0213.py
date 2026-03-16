# 수업
# 선형 큐의 구현
n = 3
que = [0] * n
front = -1
rear = -1

def enqueue(item) :   # 삽입 .append(item)
    global rear
    if is_full() :
        print('Queue_full')
    else :
        rear += 1
        que[rear] = item

def dequeue() :       # 삭제 .pop(0)
    global front
    if is_empty() :
        print('Queue_Empty')
    else :
        front += 1
        return que[front]
    
def is_empty() :      # 공백상태 및 포화상태 검사
    return front == rear
def is_full() :
    return rear == len(que) - 1


# 원형 큐의 구현
n = 3
cq = [0] * n
front = rear = 0

def enqueue(item) :    # 삽입
    global rear
    if is_full() :
        print('Queue_Full')
    else :
        rear = (rear + 1) % len(cq)
        cq[rear] = item

def dequeue() :         # 삭제
    global front
    if is_empty() :
        print('Queue_Empty')
    else :
        front = (front + 1) % len(cq)
        return cq[front]
    
def is_empty() :        # 공백상태 및 포화상태 검사
    return front == rear
def is_full() :
    return (rear + 1) % len(cq) == front


# deque 덱
from collections import deque

q = deque()
q.append(1)      # enqueue()  # 오른쪽에 1을 추가
t = q.popleft()  # dequeue()  # 왼쪽에서 요소를 제거하고 반환. 요소가 없으면 Index Error


# BFS
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
def bfs(s, V) :      # 시작정점 s, 마지막정점 V
    visited = [0] * (V+1)       # visited 생성
    q = []                      # 큐 생성 
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 인큐 표시          
    
    while q :                                # 큐에 남은 정점이 있으면
        t = q.pop(0)                         # 디큐해서 t에 저장
        print(t)                             # 디큐한 정점 t 방문
        for w in adj_list[t] :               # t에 인접하고 아직 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0 :
                q.append(w)                  # w 인큐
                visited[w] = visited[t] + 1  # 인큐 표시

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_list = [[] for _ in range(V+1)]  # V번 헹까지 비어있는 행 준비
for i in range(E) :
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)          # 방향이 없는 경우

bfs(1, 7)


# 5105. 미로의 거리
def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = []      # 큐생성
    q.append([i,j])# 시작점 인큐
    visited[i][j] = 1# 시작점 인큐 표시
    # 탐색
    while q:
        ti, tj = q.pop(0)   # 디큐
        if maze[ti][tj] == 3:   # visit(t)
            return visited[ti][tj] - 1 - 1 # 경로의 빈칸 수, -1 추가
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로내부고, 인접이고 벽이아니면,
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])# 인큐
                visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
sti, stj = find_start(N)
ans = bfs(sti, stj, N)
print(ans)


# 실습
# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
from collections import deque

def bfs(S):   # 거리를 리턴
    q = deque()
    visited = [0]*(V+1)

    visited[S] = 1
    q.append(S)

    distance = 0

    while q:
        for _ in range(len(q)):   # 가는데 걸리는 시간 or 가는 거리정도
            node = q.popleft()
            if node == G:
                return distance
            for next_node in adj_list[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = 1
                q.append(next_node) 
        distance += 1

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


# 1979. 어디에 단어가 들어갈 수 있을까
T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    result = 0

    for r in range(N) :
        for c in range(N) :
            if puzzle[r][c] == 1 :  # 1의 갯수를 세기
                count += 1
            else :
                if count == K :     # 0을 만났을 때 1의 갯수가 K면 result를 +1 하기
                    result += 1
                count = 0           # 0을 만났으니까 1을 다시 처읍부터 count 헤야함. 즉, count 초기화
        if count == K :             # for 문을 다 돌았을 때도 count(1의 총 갯수)가 K가 되었으면 
            result += 1             # result를 +1 하기
        count = 0
                
            
    for c in range(N) :
        for r in range(N) :
            if puzzle[r][c] == 1 :
                count += 1
            else :
                if count == K :
                    result += 1
                count = 0
        if count == K :
            result += 1
        count = 0

    print(f'#{tc} {result}')


# 23795. 우주 괴물
T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == 2 :

                for d in range(4) :
                    nr = r + dr[d]
                    nc = c + dc[d]

                    while 0 <= nr < N and 0 <= nc < N :
                        if arr[nr][nc] == 1 :
                            break
                        if arr[nr][nc] == 0 :
                            arr[nr][nc] = 1
                        nr = nr + dr[d]
                        nc = nc + dc[d]
                            
    count = 0
    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == 0 :
                count += 1

    print(f'#{tc} {count}')